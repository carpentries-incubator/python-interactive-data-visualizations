---
title: "Add Widgets to the Streamlit App"
teaching: 10
exercises: 0
questions:
- "Why do I want to have widgets in my app?"
- "What kinds of widgets are there?"
- "How can I use widgets to alter my plot?"
objectives:
- "Learn how to add a Select Box widget"
- "Learn how to modify a plot based on widget values"
keypoints:
- "Add a widget to select the continent or metric from a list with `st.selectbox()`"
- "There are two ways to add a widget to the sidebar: `st.sidebar.<widget>()` and `with st.sidebar: st.<widget>()`"
---

We are now ready to add in the actual widgets. Remember all of that work we did to refactor the code so that we substituted in the `continent` and `metric` variables instead of having hardcoded values... and then we just assigned those variables to strings so the result was the same anyways? Well, now we are going to actually change the value of `continent` and `metric` - and widgets allow the users to select the value! 

## Adding the Select widgets

We are going to add two widgets to our app. One widget will let us select the continent, and one widget will let us select the metric. For both, the user should select one option out of a list of strings. What comes to mind as the best type of widget?

You may have said "Dropdown box". In Streamlit, this is called a "Select box", and is created with `st.selectbox()`.

> ## Look through the documentation for widget options
> Streamlit has many types of widgets available. You can see the documentation for them [here](https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets)
{: .callout}

Let's create our `continent` widget. Before, we had assigned `continent` to a string. Now we will assign it to a widget.

~~~
continent = st.selectbox(label = "Choose a continent", options = continent_list)
~~~
{: .language-python}

The `st.selectbox()` function requires you to define a label (what will display in the app next to the widget) and the options (a list of possible values to select from). Remember how we created a list of all possible continent values, `continent_list`? This is the list we pass to the `options` argument.

Let's go ahead and add the metric widget as well, this time using the list of all possible metric values.

~~~
metric = st.selectbox(label = "Choose a metric", options = metric_list)
~~~
{: .language-python}

Your app should now look like this:

~~~
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

df = pd.read_csv("Data/gapminder_tidy.csv")

continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

continent = st.selectbox(label = "Choose a continent", options = continent_list)
metric = st.selectbox(label = "Choose a metric", options = metric_list)

query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)

metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric_labels[metric]}"})
st.plotly_chart(fig, use_container_width=True)
~~~
{: .language-python}

Go ahead and save the `app.py` file, click "Rerun" in the Streamlit app, and experiment with how the widgets can affect your plot.

![Streamlit app after adding widgets](../fig/streamlit_app_lesson6_1.png)

## Move the widgets to the sidebar

Streamlit also lets us have a sidebar that can be closed and opened. This is a good place to stash our widgets. There are two ways to add something to the sidebar. One is by adding `sidebar` to the widget definition, like this:

~~~
continent = st.sidebar.selectbox(label = "Choose a continent", options = continent_list)
metric = st.sidebar.selectbox(label = "Choose a metric", options = metric_list)
~~~
{: .language-python}

The other way is to place the variables within a `with st.sidebar:` statement, like this:

~~~
with st.sidebar:
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list)
~~~
{: .language-python}

The second option lets us also add some other things to the sidebar, and clearly organize it, like this:

~~~
with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list)
~~~
{: .language-python}

![Streamlit app after adding sidebar](../fig/streamlit_app_lesson6_2.png)

There is one last thing we should do to before we have our final app. Notice how the widget options for "Choose a metric" aren't our nicely formatted options? We can fix this with the `format_func` parameter. 
In order to pass a function to the `format_func` parameter, we first need to define a function. The function input should be the value being selected from the list. The function output should be how we want that value to be displayed. We can use a dictionary to map these "raw" values to their "pretty" equivalents.

~~~
metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

def format_metric(metric_raw):
    return metric_labels[metric_raw]

metric = st.selectbox(label = "Choose a metric", options = metric_list, format_func=format_metric)
~~~
{: .language-python}

## The final app

Finally, we have our finished `app.py` file. In order to make this app easier to read and understand, we should also comment our code. Commenting our code not only helps others... but also us 2 months later when we want to pick up the project again!

~~~
import streamlit as st
import pandas as pd
import plotly.express as px

# set up the app with wide view preset and a title
st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

# import our data as a pandas dataframe
df = pd.read_csv("Data/gapminder_tidy.csv")

# get a list of all possible continents and metrics, for the widgets
continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

# map the actual data values to more readable strings
metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

# function to be used in widget argument format_func that maps metric values to readable labels, using dict above
def format_metric(metric_raw):
    return metric_labels[metric_raw]

# put all widgets in sidebar and have a subtitle
with st.sidebar:
    st.subheader("Configure the plot")
    # widget to choose which continent to display
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    # widget to choose which metric to display
    metric = st.selectbox(label = "Choose a metric", options = metric_list, format_func=format_metric)

# use selected values from widgets to filter dataset down to only the rows we need
query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)

# create the plot
title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric_labels[metric]}"})

# display the plot
st.plotly_chart(fig, use_container_width=True)
~~~
{: .language-python}

Save, Rerun, and... Share!

![Final Streamlit app](../fig/streamlit_app_lesson6_3.png)

{% include links.md %}

