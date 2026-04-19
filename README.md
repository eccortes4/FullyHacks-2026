# Flask-Vercel Hackpack

> A premade Flask template!

- [Flask-Vercel Hackpack](#flask-vercel-hackpack)
  - [About FullyPacks 🐘🎁](#about-fullypacks-)
  - [About Flask](#about-flask)
  - [How to Deploy](#how-to-deploy)
    - [Automatic](#automatic)
    - [Manual](#manual)
  - [How to Run Locally](#how-to-run-locally)

## About FullyPacks 🐘🎁

Welcome to `fullypack_flask_vercel`, one of a [_curated collection of Github templates_](https://github.com/orgs/acmcsufoss/repositories?q=fullypack_&type=all&sort=stargazers) designed to kickstart your project and help you get up and running in no time!

## About Flask

Flask is a web framework that allows you to create web applications using the Python programming language. In simple terms, Flask provides you with tools and features that make it easier to build web applications.

A web application is a software program that runs in a web browser. For example, when you use Facebook or Instagram, you're using a web application.

Flask makes it easy to create a web application by providing a set of functions and tools that help you:

- Define the structure of your application, such as the different pages or URLs users can access.
- Define the behavior of your application, such as what happens when a user clicks a button or fills out a form.
- Store and retrieve data, such as user information or images.

## How to Deploy

### Automatic

- Click [here](https://vercel.com/new/clone?repository-url=https://github.com/acmcsufoss/hackpack_flask_vercel/)

### Manual

1. Use this template by clicking "Use this template" button above or [click here](https://github.com/acmcsufoss/hackpack_flask_vercel/generate)
2. Deploy your new project to [Vercel](https://vercel.com/new)

## How to Run Locally

1. Install Python 3.7 or later
2. Use this template by clicking "Use this template" button above or [click here](https://github.com/acmcsufoss/hackpack_flask_vercel/generate) and download the zip folder or clone it using Git
3. Open the folder in VSCode
4. Create a virtual environment:

   ```terminal
   python3 -m venv venv
   ```

5. Activate the virtual environment:

   Linux

   ```terminal
   source venv/bin/activate
   ```

   Windows

   ```terminal
   .\venv\Scripts\activate
   ```

6. Install dependencies:

   ```terminal
   pip install -r requirements.txt
   ```

7. Run the app:

   ```terminal
   flask --app api/index.py run --debug
   ```
