---
title: Instructor Notes
---

### If you have limited time

If this lesson should last for strictly less than 2 hours, it is highly recommended that you have learners complete Episode 2 (Create a New Environment) before the lesson begins, as a part of Setup. You could even include it as part of an "Installation Office Hour" where learners get all set up and prepared before the workshop starts.

If you are teaching Episode 2 (Create a New Environment) during the workshop, be advised that this is the part where you most likely to need helpers to resolve any difficulties or technical problems learners may have. It also may eat up extra time as the learners try to get their environments set up.

### This lesson assumes familiarity with python and pandas

It is important to note that this lesson was designed to follow the [Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/index.html) lesson.

### See all of the code

If you want to see all of the finished code as it should be after the lesson is completed (.ipynb and .py files), they are available [in the code folder](https://github.com/carpentries-incubator/python-interactive-data-visualizations/tree/gh-pages/code).

### Reset environment before teaching

If you have practiced the lesson prior to teaching and want to reset your environment for teaching you need to:

- Remove the jupyter kernel `jupyter kernelspec uninstall dataviz`.  You may want to list your kernels first with `jupyter kernelspec list`.
- Remove the conda environment `conda remove --name dataviz --all`.  Reminder you can use `conda env list` to list all your current environments.
- Delete or rename your streamlit app.
- Move, rename, or delete your local `data_viz_workshop` and `interact-with-gapminder-data-app` folders.
- Move, rename, or delete your github repo.




