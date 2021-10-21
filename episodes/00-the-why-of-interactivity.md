---
title: "The value of data visualization and interactivity"
teaching: 10
exercises: 0
questions:
- "Why do we need visual repesentation of data to see patterns?"
- "How will interacting with data change this understanding?"
objectives:
- "To understand the difference between static and interactive figures"
- "To consider which aspects of your data would work with some user interaction"
keypoints:
- "Consider the message you want to convey or story you want to tell. Is it clearer with some interactivity?"
- "Data types are often best suited to certain certain dimensions (for example timeseries as a continuous x-axis, rather than coloured groups)"
- "A plot or figure should make sense without needing to use the interactivity"
- "If a plot changes then titles and labels need to change too, or they will be inaccurate or misleading"
---

## Why plot?
The goal of research is to improve our understanding of the world, but that overall increase in knowledge is small if that understanding doesn't spread.  

Humans benefit from visual representation of data to see patterns and plotting data has become an essential part of the researcher's toolbox for communication.

> ## Our reliance on the visual?
> When was the last time you saw a research paper without figures?
>
> When reading research do you start with the figures?
>
> How would the recent publications you have studied have made sense if you couldn't see the figures?
{: .discussion}

## Choices in analysis and presentation
Producing a figure will often depend on the story you want to tell, or the pattern you wish to highlight in your data. 
You have to decide which variables in your data (group, treatment, location, time, amount)to map to the available visual dimensions (x-y-z position / colour / symbols / etc).

Modern sources of data often present additional problems, those of density and complexity, that require further choices relating to aggregation and ommission. All of these aspects require choices and this can force a certain interpretation on your audience, a limit what you can show.

Interactivity gives the reader/user a chance to explore the data in ways a static (non-interactive) plot does not.  It can also help you and your collaborators understand your data better.
![Plotting can be used to enlighten, interactivity can allow exploration](../fig/plotting_power.png)

> ## A wealth of choices for making figures in Python
> This tutorial makes us of Plotly and Streamlit, but a range of options now exist for visualizing data in the Python ecosystem.  
>
> These are summariazed at [PyViz.org](https://pyviz.org/tools.html).
>
> Many of the tools described are developed with specific users in mind, whereas others are intentionally more basic and adaptable. Some are focused on particular issues, such as choices of colour or the aggregation of data. There is a lot here to explore...
{: .callout}

### The steps for constructing our interactive data visualization
  1. Building your environment for analysis and plotting (in a way that can be repeated)
  2. Data processing and cleaning. 
  3. Separating out variables of interest
  4. Identifying variables you may want to explore (and how best to map these to visual differences/dimensions).
  5. Visualizing the central data (choosing your plot types)
  6. Converting addtional choices in the visualization to widgets.
  7. Hosting a plot as an app (so it can be seen ad explored)

{% include links.md %}
