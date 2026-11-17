---
title: Data Wrangling
teaching: 15
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Learn useful pandas functions for wrangling data into a tidy format

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- What format should my data be in for Plotly Express?
- Why can't I use the data in its current format?
- What is tidy data?
- How can I use pandas to wrangle my data?

::::::::::::::::::::::::::::::::::::::::::::::::::

Data visualization libraries often expect data to be in a certain format so that the functions can correctly interpret and present the data. We will be using the Plotly Express library for visualizing data, which works best when data is in a tidy, or "long" format.

We want to visualize the data in `gapminder_all.csv`. However, this dataset is in a "wide" format - it has many columns, with each year + metric value in it's own column. The unit of observation is the "country" - each country has its own single row.

:::::::::::::::::::::::::::::::::::::::::  callout

## Open the CSV file within Jupyter Lab

Click on the `Data` folder in the left-hand navigation pane and then double click on `gapminder_all.csv` to view this file within Jupyter Lab.

Explore the dataset visually. What does each row represent? What does each column represent? About how many rows and columns are there?


::::::::::::::::::::::::::::::::::::::::::::::::::

We are going take this wide dataset and make it long, so the unit of observation will be each country + year + metric combination, rather than just the country. This process is made much simpler by a couple of functions in the `pandas` library.

## Tidy Data

The term "tidy data" may be most popular in the R ecosystem (the "tidyverse" is a collection of R packages designed around the tidy data philosophy), but it is applicable to all tabular datasets, not matter what programming language you are using to wrangle your data.

You can ready more about the tidy data philosophy in Hadley Wickham's 2014 paper, "Tidy Data", available [here](https://vita.had.co.nz/papers/tidy-data.pdf).

Wickham later refined and revised the tidy data philosophy, and published it in the 12th chapter of his open access textbook "R for Data Science" - available [here](https://r4ds.had.co.nz/tidy-data.html).

The revised rules are:

1. Each variable must have its own column
2. Each observation must have its own row
3. Each value must have its own cell

It might be difficult at first to identify what makes a dataset "untidy", and therefore what you will need to change in order to wrangle the dataset into a tidy shape.

Here are the five most common problems with untidy datasets (Identified in ["Tidy Data"](https://vita.had.co.nz/papers/tidy-data.pdf)):

1. Column headers are values, not variable names
2. Multiple variables are stored in one column
3. Variables are stored in both rows and columns
4. Multiple types of observational units are stored in the same table
5. A single observational unit is stored in multiple tables

::::::::::::::::::::::::::::::::::::::  discussion

## Discuss: how is our dataset untidy?

Look again at the file `gapminder_all.csv` you opened in Jupyter Lab.
Which of the 5 most common problems with untidy datasets applies to this dataset?


::::::::::::::::::::::::::::::::::::::::::::::::::

## Getting Started

Let's go ahead and get started by opening a Jupyter Notebook with the `dataviz` kernel. If you navigated to the `Data` folder to look at the CSV file, navigate back to the root before opening the new notebook.
We are also going to rename this new notebook to `data_wrangling.ipynb`.

![](fig/jupyter_lab_dataviz_notebook.png){alt='Jupyter Lab - Notebooks - dataviz kernel'}

Jupyter Notebooks are very handy because we can combine documentation (markdown cells) with our program (code cells) in a reader-friendly way.
Let's make our first cell into a markdown cell, and give this notebook a title:

```source
# Data Wrangling
```

You can then add basic metadata like your name, the current date, and the purpose of this notebook.

## Read in the data

We will start by importing pandas and reading in our data file. We can call the `df` variable to display it.

```python
import pandas as pd
df = pd.read_csv("Data/gapminder_all.csv")
df
```

## Melting the dataframe from wide to long

One problem with our dataset is that "column headers are values, not variable names". The type of metric and the year are stuck in our column headers, and we want that information to be stored in rows.

The first function we are going to use to wrangle this dataset is `pd.melt()`. This function's entire purpose to to make wide dataframes into long dataframes.

:::::::::::::::::::::::::::::::::::::::::  callout

## Check out the documentation

To learn more about `pd.melt()`, you can look at the function's [documentation](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
To see this documentation within Jupyter Lab, you can type `pd.melt()` in a cell and then hold down the shift + tab keys.
You can also open a "Show Contextual Help" window from the Launcher.


::::::::::::::::::::::::::::::::::::::::::::::::::

Let's take a look at all of the columns with:

```python
df.columns
```

`pd.melt()` requires us to specify at least 3 arguments: the dataframe (`frame`), the "id" columns (`id_vars`) - that is, the columns that won't be "melted" - and the "value" columns (`value_vars`) - the columns that will be melted.

Our "id" columns are `country` and `continent`. Our "value" columns are all of the rest. That's a lot of columns! But no worries - we can programmatically make a list of all of these columns.

```python
cols = list(df.columns)
cols.remove("continent")
cols.remove("country")
cols
```

Now, we can call `pd.melt()` and pass `cols` rather than typing out the whole list.

```python
df_melted = pd.melt(df, id_vars=["country", "continent"], value_vars = cols)
df_melted
```

:::::::::::::::::::::::::::::::::::::::::  callout

## New dataframe variable names

When wrangling a dataframe in a Jupyter notebook, it's a good idea to assign transformed dataframes to a new variable name.
You don't have to do this with every transformation, but do try to do this with every substantial transformation.
This way, we don't have to re-run the entire notebook when we are experimenting with transformations on a dataframe.


::::::::::::::::::::::::::::::::::::::::::::::::::

Just look at that beautiful, long dataframe! Take a closer look to understand exactly what `pd.melt()` did. The `variable` column has all of our former column names, and the `value` column has all of the values that used to belong in those columns.

## Splitting a column

Now that we have melted our datset, we can address another untidy problem: "Multiple variables are stored in one column".

Take a closer look at the `variable` column. This column contains two pieces of information - the metric and the year. Thankfully, these former column names have a consistent naming scheme, so we can easily split these two pieces of information into two different columns.

```python
df_melted[["metric", "year"]] = df_melted["variable"].str.split("_", expand=True)
df_melted
```

::::::::::::::::::::::::::::::::::::::  discussion

## Wide vs long data

Take a moment to compare this dataframe to the one we started with.

What are some advantages to having the data in this format?


::::::::::::::::::::::::::::::::::::::::::::::::::

## Saving the final dataframe

Now that all of our columns contain the appropriate information, in a tidy/long format, it's time to save our dataframe back to a CSV file. But first, let's clean up our datset: we're going to re-order our columns (and remove the now extra `variable` column) and sort the rows.

```python
df_final = df_melted[["country", "continent", "year", "metric", "value"]]
df_final = df_final.sort_values(by=["continent", "country", "year", "metric"])
df_final
```

Finally, we will export the dataframe to a CSV file.

```python
df_final.to_csv("Data/gapminder_tidy.csv", index=False)
```

We set the index to False so that the index column does not get saved to the CSV file.

## Exercises

::::::::::::::::::::::::::::::::::::::  discussion

## Imagining other tidy ways to wrangle

We wrangled our data into a tidy form. However, there is no single "true tidy" form for any given dataset.

What are some other ways you may wish to organize this dataset that are also tidy?

:::::::::::::::  solution

## For Example

Instead of having a `metric` and `value` column, given that `metric` only has 3 values,
you could have a column each for `gdpPercap`, `lifeExp`, and `pop`.

The values in each of those three columns would reflect the value of that metric for a given country in a given year.
The columns in this dataset would be: `country`, `continent`, `year`, `gdpPercap`, `lifeExp`, and `pop`.

How would you wrangle the original dataset into this other tidy form using pandas?


:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::: keypoints

- Import your CSV using `pd.read_csv('<FILEPATH>')`
- Transform your dataframe from wide to long with `pd.melt()`
- Split column values with `df['<COLUMN>'].str.split('<DELIM>')`
- Sort rows using `df.sort_values()`
- Export your dataframe to CSV using `df.to_csv('<FILEPATH>')`

::::::::::::::::::::::::::::::::::::::::::::::::::


