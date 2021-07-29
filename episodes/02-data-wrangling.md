---
title: "Data Wrangling"
teaching: 15
exercises: 0
questions:
- "What format should my data be in for Plotly Express?"
- "Why can't I use the data in its current format?"
- "What is tidy data?"
- "How can I use pandas to wrangle my data?"
objectives:
- "Learn useful pandas functions for wrangling data into a tidy format"
keypoints:
- "Import your CSV using `pd.read_csv('<FILEPATH>')"
- "Transform your dataframe from wide to long with `pd.melt()`"
- "Split column values with `df['<COLUMN>'].str.split('<DELIM>')`"
- "Sort rows using `df.sort_values()`"
- "Export your dataframe to CSV using `df.to_csv('<FILEPATH>')`"
---

Data visualization libraries often expect data to be in a certain format so that the functions can correctly interpret and present the data. We will be using the Plotly Express library for visualizing data, which works best when data is in a tidy, or "long" format.

We want to visualize the data in `gapminder_all.csv`. However, this dataset is in a "wide" format - it has many columns, with each year + metric value in it's own column. The unit of observation is the "country" - each country has its own single row.

You can click on the `Data` folder and double click on `gapminder_all.csv` to view this file within Jupyter Lab.

We are going take this very wide dataset and make it very long, so the unit of observation will be each country + year + metric combination, rather than just the country. This process is made much simpler by a couple of functions in the `pandas` library.

## Getting Started

Let's go ahead and get started by opening a Jupyter Notebook with the `dataviz` kernel. If you navigated to the `Data` folder to look at the CSV file, navigate back to the root before opening the new notebook. 
We are also going to rename this new notebook to `data_wrangling.ipynb`.

Jupyter Notebooks are very handy because we can combine documentation (markdown cells) with our program (code cells) in a reader-friendly way.
Let's make our first cell into a markdown cell, and give this notebook a title:

~~~
# Data Wrangling
~~~
{: .source}

You can then add basic metadata like your name, the current date, and the purpose of this notebook.

## Read in the data

We will start by importing pandas and reading in our data file. We can call the `df` variable to display it.

~~~
import pandas as pd
df = pd.read_csv("data/gapminder_all.csv")
df
~~~
{: .language-python}

## Melting the dataframe from wide to long

The first function we are going to use to wrangle this dataset is `pd.melt()`. This function's entire purpose to to make wide dataframes into long dataframes.

> ## Check out the documentation
> To learn more about `pd.melt()`, you can look at the function's [documentation](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
> To see this documentation within Jupyter Lab, you can type `pd.melt()` in a cell and then hold down the shift + tab keys.
> You can also open a "Show Contextual Help" window from the Launcher.
{: .callout}

Let's take a look at all of the columns with:

~~~
df.columns
~~~
{: .language-python}

`pd.melt()` requires us to specify at least 3 arguments: the dataframe (`frame`), the "id" columns (`id_vars`) - that is, the columns that won't be "melted" - and the "value" columns (`value_vars`) - the columns that will be melted.

Our "id" columns are `country` and `continent`. Our "value" columns are all of the rest. That's a lot of columns! But no worries - we can programmatically make a list of all of these columns.


~~~
cols = list(df.columns)
cols.remove('continent')
cols.remove('country')
cols
~~~
{: .language-python}

Now, we can call `pd.melt()` and pass `cols` rather than typing out the whole list.

~~~
df_melted = pd.melt(df, id_vars=['country', 'continent'], value_vars = cols
df_melted
~~~
{: .language-python}

> ## New dataframe variable names
> When wrangling a dataframe in a Jupyter notebook, it's a good idea to assign transformed dataframes to a new variable name.
> You don't have to do this with every transformation, but do try to do this with every substantial transformation.
> This way, we don't have to re-run the entire notebook when we are experimenting with transformations on a dataframe.
{: .callout}

Just look at that beautiful, long dataframe! Take a closer look to understand exactly what `pd.melt()` did. The `variable` column has all of our former column names, and the `value` column has all of the values that used to belong in those columns.

## Splitting a column

But we're not done yet! Take a closer look at the `variable` column. This column contains two pieces of information - the metric and the year. Thankfully, these former column names have a consistent naming scheme, so we can easily split these two pieces of information into two different columns.

~~~
df_melted[['metric', 'year']] = df_melted['variable'].str.split("_", expand=True)
df_melted
~~~
{: .language-python}

## Saving the final dataframe

Now that all of our columns contain the appropriate information, in a tidy/long format, it's time to save our dataframe back to a CSV file. But first, we're going to re-order our columns (and remove the now extra `variable` column) and sort the rows.

~~~
df_final = df_melted[['country', 'continent', 'year', 'metric', 'value']]
df_final = df_final.sort_values(by=["continent", "country", "year", "metric"])
df_final
~~~
{: .language-python}

Finally, we will export the dataframe to a CSV file.

~~~
df_final.to_csv("data/gapminder_tidy.csv", index=False)
~~~
{: .language-python}


{% include links.md %}

