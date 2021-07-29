---
title: "Add Widgets to the Streamlit App"
teaching: 20
exercises: 0
questions:
- "Why do I want to have widgets in my app?"
- "What kinds of widgets are there?"
- "How can I use widgets to alter my plot?"
objectives:
- "Learn how to add a Select Box widget"
- "Learn how to modify a plot based on widget values"
keypoints:
- "In order to add widgets, we need to refactor our code to make it more flexible. Make good use of variables and f-Strings when refactoring."
- "Add a widget to select the continent or metric from a list with `st.selectbox()`"
- "There are two ways to add a widget to the sidebar: `st.sidebar.widget()` and `with st.sidebar:`"
---

We now have a working Streamlit app. However, it is only displaying one plot, and we can't currently change what that plot is showing. 
And we know that there is a lot more information to visualize in our dataset!
So we are going to add in even more interactivity with some widgets.

However, the `app.py` file is not a great place to experiment and iterate with our code. For that, let's go back to our `data_visualizations.ipynb` notebook.

## Refactoring code for added flexibility

First, let's decide what attributes we want to be able to change in the plot. Right now, the plot is showing the GDP for countries in Oceania - that right there is two different attributes: the metric (GDP) and the continent (Oceania).

These are also the two attributes that we are filtering for using `df.query()`:

~~~
df_gdp_o = df.query("continent=='Oceania' & metric=='gdpPercap'")
~~~
{: .language-python}

Notice that what is passed to `df.query()` is simply a string. Right now, the specific values of "Oceania" and "gdpPercap" are specified in the string. However, we can easily make these values variable using f-Strings.

> ## f-Strings
> f-Strings are the modern way of formatting strings in Python. 
> You may have used the "old-school" methods of %-formatting or `str.format()` to accomplish the same goal, but the syntax for f-Strings is much nicer. 
> You can learn more about f-Strings [here](https://realpython.com/python-f-strings/).
{: .callout}

To incorporate f-Strings into our query, let's tweak a few things. Try out this code in a cell in your Jupyter Notebook.

~~~
continent = "Oceania"
metric = "gdpPercap"

old_query = "continent=='Oceania' & metric=='gdpPercap'"
new_query = f"continent=='{continent}' & metric=='{metric}'"

print(old_query)
print(new_query)
~~~
{: .language-python}

Notice how the two strings are identical?

The `new_query` variable is more flexible, because we can redefine the `continent` and `metric` variables. Go ahead and try it!

~~~
continent = "Europe"
metric = "pop"

query = f"continent=='{continent}' & metric=='{metric}'"

print(query)
~~~
{: .language-python}

It's important to isolate these `continent` and `metric` values because we can adjust them with our widgets.

Let's go ahead and try incorporating this into our plot (still in the Jupyter Notebook)

~~~
continent = "Europe"
metric = "pop"

query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)

title = "GDP for countries in Oceania"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": "GDP Percap"})
fig.show()
~~~
{: .language-python}

Do you notice any other places that we need to incorporate f-Strings? The title and axis lables!

~~~
continent = "Europe"
metric = "pop"

title = f"{metric} for countries in {continent}"
labels = {"value": f"{metric}"}
~~~
{: .language-python}

Let's show that plot again, with our updated code:

~~~
continent = "Europe"
metric = "pop"

query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)

title = f"{metric} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric}"})
fig.show()
~~~
{: .language-python}

There's just one more thing to tweak. "gdpPercap", "lifeExp", and "pop" aren't the prettiest labels. Let's map them to more display-friendly labels with a dictionary.

~~~
metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}
~~~
{: .language-python}

Now, here's our final code:

~~~
continent = "Europe"
metric = "pop"

query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)

metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric_labels[metric]}"})
fig.show()
~~~
{: .language-python}

There is one last step before we can be ready to create our widgets. We need a list of all continents and all metrics. To do this, we will use pandas' `unique()` function.

~~~
df['continents'].unique()
~~~
{: .language-python}

See how we get every possible value in the `continents` column exactly once? Let's define this as a list, assign it to a variable, and do the same thing for `metric`.

~~~
continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())
~~~
{: .language-python}

Now, we are ready to define our widgets. Let's copy this final code over to our `app.py` file, so that it is like this:

~~~
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

df = pd.read_csv("data/gapminder_tidy.csv")

continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

continent = "Europe"
metric = "pop"

query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)

metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric_labels[metric]}"})
st.plotly_chart(fig, use_container_width=True)
~~~
{: .language-python}

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

The `st.selectbox()` function requires you to define a label (what will display in the app next to the widget) and the options (a list of possible values to select from).

Let's go ahead and add the metric widget as well.

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

df = pd.read_csv("data/gapminder_tidy.csv")

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

Go ahead and save the `app.py` file, click "Rerun" in the Streamlit app, and have fun playing with those widgets!

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

The second option let's us also add some other things to the sidebar, and clearly organize it, like this:

~~~
with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list)
~~~
{: .language-python}

There is one last thing we should do to before we have our final app. Notice how the widget options for "Choose a metric" aren't our nicely formatted options? We can fix this with the format_func argument:

~~~
metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

def format_metric(metric_raw):
    return metric_labels[metric_raw]

metric = st.selectbox(label = "Choose a metric", options = metric_list, format_func=format_metric)
~~~
{: .language-python}

## The final app

Finally, here is our finished `app.py` file:

~~~
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Interact with Gapminder Data")

df = pd.read_csv("data/gapminder_tidy.csv")

continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())
metric_labels = {"gdpPercap": "GDP Per Capita", "lifeExp": "Average Life Expectancy", "pop": "Population"}

def format_metric(metric_raw):
    return metric_labels[metric_raw]

with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list, format_func=format_metric)

query = f"continent=='{continent}' & metric=='{metric}'"
df_filtered = df.query(query)


title = f"{metric_labels[metric]} for countries in {continent}"
fig = px.line(df_filtered, x = "year", y = "value", color = "country", title = title, labels={"value": f"{metric_labels[metric]}"})
st.plotly_chart(fig, use_container_width=True)
~~~
{: .language-python}

Save, Rerun, and... Share!

{% include links.md %}

