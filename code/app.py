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
