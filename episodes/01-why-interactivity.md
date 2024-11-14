---
title: Why make interactive visualizations?
teaching: 10
exercises: 0
---

::::::::::::::::::::::::::::::::::::::: objectives

- To understand the difference between static and interactive plots
- To understand why we may want to make plots interactive
- To introduce what we will be doing in this workshop lesson

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- Why are visual representations of data useful when trying to see patterns?
- Why do we want to make visualizations interactive?
- Consider the message you want to convey or story you want to tell. Is it clearer with some interactivity?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Why do we like visualizations?

Visualization is often one of the first and most vital steps of exploratory data analysis.
People benefit from visual representation of data to see patterns, and plotting data is also an important part of a researcher's communication toolbox.
Interactive visualizations can be used both during the initial exploratory phase and the final publication and communication phase of a research project.

::::::::::::::::::::::::::::::::::::::  discussion

## Discuss: visualizations in research publications

When was the last time you saw a research paper without figures?

When reading research do you start with the figures?

How would the recent publications you have studied have made sense if you couldn't see the figures?


::::::::::::::::::::::::::::::::::::::::::::::::::

## Choices in analysis and presentation

Producing a figure will often depend on the story you want to tell, or the pattern you wish to highlight in your data.

Any one visualization is limited in how many attributes can (and should) be represented. For example, if you have a scatterplot and assign one attribute to x-axis, one attribute to the y-axis (maybe even one to the z-axis!), another attribute to the color, yet another attribute to the shape, and even another attribute to the size... you may be able to cram a lot of information into the plot, but the resulting visualization will probably not tell a clear story.

Any one visualization is limited in how many different attributes can be reasonably included. Modern data sets are often too dense to visualize without making a lot of these choices.

But with an interactive plot, we can include all of this information - just not at the same time. Rather than being forced to choose which few attributes to represent and communicate, you can allow the audience to choose the information they are interested in seeing, with the possibility they will choose to explore all of the possible visualizations.

The magic of interactivity is that you don't have to limit yourself and your plots - you can visualize it all! However, you should carefully consider the options for your interactive visualizations so that they are still telling a cohesive story about the data.

Interactivity gives the audience a chance to explore the data in ways a static (non-interactive) plot does not.  It can also help you and your collaborators understand your data better.

:::::::::::::::::::::::::::::::::::::::::  callout

## There are many options for making figures with Python

This tutorial makes use of Plotly and Streamlit, but a range of options now exist for visualizing data in the Python ecosystem.

These are summarized at [PyViz.org](https://pyviz.org/tools.html).

Many of the tools described are developed with specific users in mind, whereas others are intentionally more basic and adaptable. Some are focused on particular issues, such as choices of color or the aggregation of data. There is a lot here to explore!


::::::::::::::::::::::::::::::::::::::::::::::::::

## How will we build our interactive visualization app?

1. Create a new and squeaky clean python environment that has only the packages we need
2. Use pandas to wrangle our data into a tidy format
3. Create some initial visualizations and learn how to use Plotly Express
4. Create a basic streamlit app (no interactivity yet!) with one of those initial visualizations
5. Go back through our code to refactor (reorganize) some hardcoded information into more flexible variables
6. Add widgets! These are what allow our app to be truly interactive and allow users to adjust the displayed plots
7. Deploy the app - so everyone can see what you created.
8. (Optionally) Put your own creative spin on it - add some of your own widgets and visualizations to make your app unique



:::::::::::::::::::::::::::::::::::::::: keypoints

- Visualization is an important part of both exploratory data analysis and communicating results
- Interactivity allows us to visualize more information without overcomplicating a single plot

::::::::::::::::::::::::::::::::::::::::::::::::::


