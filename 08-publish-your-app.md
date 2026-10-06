---
title: Publish Your Streamlit App
teaching: 20
exercises: 30
---

::::::::::::::::::::::::::::::::::::::: objectives

- Learn how to deploy a Streamlit app

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How do I deploy my app so other people can see it?
- How do I create a `requirements.txt` file?

::::::::::::::::::::::::::::::::::::::::::::::::::

Now that we have our final app, it's time to publish (a.k.a deploy) it so that other people can see and interact with the visualizations.

## Create a GitHub repo

The first step is to create a new GitHub repository that will contain the code, data, and environment files.

:::::::::::::::::::::::::::::::::::::::::  callout

## Refresher on creating GitHub repos

If you have not created a GitHub repository before or need a refresher, please refer to [this episode on Remotes in GitHub](https://swcarpentry.github.io/git-novice/07-github.html) from the Software Carpentries lesson [Version Control with Git](https://swcarpentry.github.io/git-novice/)


::::::::::::::::::::::::::::::::::::::::::::::::::

Give your repo a descriptive name, like `interact-with-gapminder-data-app`. Make sure that the repo is "Public" (not Private) and check the box to initialize the repo with a README.md.

Once your repo is created, clone a copy of it to your local computer. You can use the application GitHub Desktop to more easily accomplish this. You can download GitHub Desktop [here](https://desktop.github.com).

Now that you have a copy of your repo on your computer, you can copy over your code and data files.

## Copy over the code and data files

During this workshop, we have created some Jupyter Notebooks files and an `app.py` file. We don't need the Jupyter Notebooks to be a part of the app's repo, only the `app.py` file.

Remember that at the start of the `app.py` file, we import our data with the line:

```python
df = pd.read_csv("Data/gapminder_tidy.csv")
```

So, we also need to make sure to include the `Data` folder and the `gapminder_tidy.csv` file inside of it.

You can copy these files using a GUI (Finder on Macs or Explorer on PCs) or the command line, whatever you are comfortable with.

Let's suppose that your repo is named `interact-with-gapminder-data-app`, and it has been cloned to the `GitHub` folder in your `Documents`. So, the location of your local repo is `~/Documents/GitHub/interact-with-gapminder-data-app`. So far, we have been working from the `Desktop`, in a folder called `data_viz_workshop`. Using the command line, we can copy the relevant files with:

```bash
cp ~/Desktop/data_viz_workshop/app.py ~/Documents/GitHub/interact-with-gapminder-data-app/app.py
mkdir ~/Documents/GitHub/interact-with-gapminder-data-app/Data
cp ~/Desktop/data_viz_workshop/Data/gapminder_tidy.csv ~/Documents/GitHub/interact-with-gapminder-data-app/Data/gapminder_tidy.csv
```

Your interact-with-gapminder-data-app folder should now look like:

```output
interact-with-gapminder-data-app
│   README.md
│   app.py    
│
└───Data
    │   gapminder_tidy.csv
```

We're almost done! But we need to do one more thing... specify an environment for the app to run in.

## Add a requirements.txt file

In order for our app to run on Streamlit's servers, we need to tell it what the environment should look like - or what packages need to be installed. While there are many standards for describing a python environment (such as the `environment.yml` file we used to create our conda environment at the beginning of this workshop), Streamlit tends to work best with a `requirements.txt` file.

The `requirements.txt` file is just a list of package names and version numbers, with each line looking like `packagename==version.number.here`. And there is no need to list out all of the packages, just the top-level ones. The dependencies will get installed for each listed package as well.

The `requirements.txt` file should be kept in the root of your repository. So, after creating a requirements file your repo should look like:

```output
interact-with-gapminder-data-app
│   README.md
│   requirements.txt    
│   app.py    
│
└───Data
    │   gapminder_tidy.csv
```

For our app, we only need to specify two packages: Streamlit and Plotly. Note that you may have different version numbers. Here is an example of our `requirements.txt` file:

```source
streamlit==1.1.0
plotly==5.1.0
```

## Push the updated repo

Now that we have our code, data, and environment files added to our local copy of the repository, it's time to push our repo to GitHub. You can use GitHub Desktop or use git from the command line to accomplish this. If you have unwanted extra files (like `.DS_Store`) added to the directory, make sure to add them to a `.gitignore` file!

Once you have added, committed, and pushed your changes (with a descriptive commit message!) go to your GitHub repo online to double check that it is up to date.

Now we are ready to deploy the app!

## Sign up for Streamlit Cloud (Community Tier)

Follow the steps detailed on Streamlit's Documentation to sign up for a free Streamlit Cloud account and connect it to your GitHub account. The documentation is located [here](https://docs.streamlit.io/streamlit-cloud/get-started).

You can sign up for a Streamlit Cloud account at [share.streamlit.io/](https://share.streamlit.io/).

On the free Community tier, you can deploy up to 3 apps at once. If you later decide to build more Streamlit apps, you can remove this one.

## Deploy your app

When you have signed in to your Streamlit account, click "New app". Copy and paste your GitHub repo URL, for example `https://github.com/username/interact-with-gapminder-data-app`, specify the correct branch name (which is most likely `main`), and specify the filename of your app (`app.py`). Then click "Deploy", and wait for the balloons!

You can read the documentation about this process for deploying an app [here](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app).

## Exercises

:::::::::::::::::::::::::::::::::::::::  challenge

## Add your own twist

Now that you have successfully deployed the app we created together, it's time for you to add your own twist.

You can add more visualizations, more widgets, or make use of Streamlit's other capabilities to add to and enhance the app. Make it your own!


::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::  discussion

## Share \& Present Your Apps

After everyone has had time to work on adding their own twist to their Streamlit apps, take some time to share your apps with each other and present what was added to the base app.

What did you find challenging?

What feature that you added did you most like?

What is something else you would like to add in the future?


::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::: keypoints

- All Streamlit apps must have a GitHub repo with the code, data, and environment files
- You can deploy up to 3 apps for free with Streamlit Cloud

::::::::::::::::::::::::::::::::::::::::::::::::::


