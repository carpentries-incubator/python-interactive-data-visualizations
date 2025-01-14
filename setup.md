---
title: Setup
---

## Getting the Files

:::::::::::::::::::::::::::::::::::::::::  callout

## Click the link to download the file

[data\_viz\_workshop.zip](files/data_viz_workshop.zip)


::::::::::::::::::::::::::::::::::::::::::::::::::

The dataset we will be using is taken from the [gapminder] dataset,
just like the [Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/) workshop.
We will also be using a special environment, which can be recreated on your machine using [Anaconda][anaconda].

To obtain the dataset and environment, download the file [data\_viz\_workshop.zip](files/data_viz_workshop.zip).
If given the option, choose to Save File in your Desktop folder. If you are not given the option to choose where to save the file, then
move this zipped file to your Desktop. Finally, double click the zipped file to unzip it.
You should now have a folder called `data_viz_workshop`. If you open this folder, you will see a file called `environment.yml` and a folder called `Data`.

## Optional: Create the virtual environment

Creating the environment can be done as a part of setup if learners already have experience in working with virtual environments. This will save time during the workshop itself to focus on other activities.

If your instructor tells you to create the `dataviz` environment in advance, follow the directions in Episode 2, [Create a new environment](episodes/02-create-new-environment.md)). Then, you can open Jupyter Lab in the project root directory (e.g. `Desktop/data_viz_workshop`)

## Create a GitHub account (if you don't already have one)

You can sign up for a GitHub account at [github.com/signup](https://github.com/signup)

Make sure to choose a general purpose email that you are likely to still have access to in 5 years - that is, not an email tied to a specific workplace, university, or Internet Service Provider.

Make sure to also choose an appropriate username that you are comfortable putting on your resume or sharing with colleagues - some variation of your name is a good idea.

After you have a GitHub account, you should also download GitHub Desktop, so that you can clone, pull, and push without having to use the command line. You can download GitHub Desktop [here](https://desktop.github.com).

## Installing Python Using Anaconda

[Python](https://python.org/) is a popular language for research computing, and great for general-purpose programming as well. Installing all of its research packages individually can be a bit difficult, so we recommend [Anaconda](https://www.anaconda.com/products/individual), an all-in-one installer.

Regardless of how you choose to install it, **please make sure you install Python version 3.x** (e.g., 3.6 is fine).

We will teach Python using the [Jupyter Notebook](https://jupyter.org/), a programming environment that runs in a web browser (Jupyter Notebook will be installed by Anaconda). For this to work you will need a reasonably up-to-date browser. The current versions of the Chrome, Safari and Firefox browsers are all [supported](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#browser-compatibility) (some older browsers, including Internet Explorer version 9 and below, are not).

::: tab

### Windows

1. Open https://www.anaconda.com/products/individual#download-section with your web browser.
1. Download the Anaconda for Windows installer with Python 3. (If you are not sure which version to choose, you probably want the 64-bit Graphical Installer Anaconda3-...-Windows-x86_64.exe)
1. Install Python 3 by running the Anaconda Installer, using all of the defaults for installation except make sure to check **Add Anaconda to my PATH environment variable.**

### macOS

1. Open https://www.anaconda.com/products/individual#download-section with your web browser.
1. Download the Anaconda Installer with Python 3 for macOS (you can either use the Graphical or the Command Line Installer).
1. Install Python 3 by running the Anaconda Installer using all of the defaults for installation.

### Linux

1. Open https://www.anaconda.com/products/individual#download-section with your web browser.
1. Download the Anaconda Installer with Python 3 for Linux. (The installation requires using the shell. If you aren't comfortable doing the installation yourself stop here and request help at the workshop.)
1. Open a terminal window and navigate to the directory where the executable is downloaded (e.g., `cd ~/Downloads`).
1. Type `bash Anaconda3-` and then press <kbd>Tab</kbd> to autocomplete the full file name. The name of file you just downloaded should appear.
1. Press <kbd>Enter</kbd> (or <kbd>Return</kbd> depending on your keyboard). You will follow the text-only prompts. To move through the text, press <kbd>Spacebar</kbd>. Type `yes` and press enter to approve the license. Press <kbd>Enter</kbd> (or <kbd>Return</kbd>) to approve the default location for the files. Type `yes` and press <kbd>Enter</kbd> (or <kbd>Return</kbd>) to prepend Anaconda to your `PATH` (this makes the Anaconda distribution the default Python).
1. Close the terminal window.
:::

[gapminder]: https://en.wikipedia.org/wiki/Gapminder_Foundation
[anaconda]: https://www.anaconda.com/

