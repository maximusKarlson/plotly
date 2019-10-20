# Dashboard with Dash & Heroku

Dash is a powerful tool to generate beautiful dashboards and gain insights. But at a certain point it gets important that these dashboards become available to not just one local user, but everyone with a internet connection.

**Check out my Dashboard for some visualizations of the famous *tips* dataset provided by `plotly`:**

[https://maximuskarlson.herokuapp.com](https://maximuskarlson.herokuapp.com)

To fullfill this task `heroku` offers an easy solution. You simply install the `heroku CLI` and watch how easy and fast your python application gets transformed into a flask application.

This repository consists of four files and one virtual environment.
* **tips-dashboard.py**: The `dash` application (Dashboard)
* **requirements.txt**: Contains all used libraries within the app. The easly create and maintain this file (after updates, code changes etc.) My advice would be to use the `pip virtualenv`. A detailed explanation can be found underneath.
* **Procfile**: Used to generate the webapplication. Entry point must be entered here.
* **venv**: `Virtualenv` folder with all the libraries etc.

## How to deploy the app
1. First you need to sign up for [Heroku](www.heroku.com) and download the CLI.
2. Install `virtualenv`. I'm a big anaconda fan and use it every day, but for this task `venv` suits better. The reason why we use virtual environments in general is, that the *requirements.txt* file needs to contain all the used libraries within the main program. `Venv` offers an easy solution:
    ```python
    pip freeze > requirements.txt
    ```
    creates exactly this file. Whenever the code gets changed or new libraries will be used you simply run this command again.
3. Create a project folder:
   ```python
   mkdir my_cool_folder && cd
   ```
4. Initialize an empty git repository:
   ```python
   git init
   ```

**NOTE: I'M USING MAC! IF YOU USE WINDOWS THESE COMMANDS CAN VARY**

5. Create a virtual environment using `virtualenv` and activate this env. To leave the env just type `deactivate`.
   ```bash
    python3 -m venv your-fancy-name
    source venv/bin/activate
   ```
6. Install all the required packages within this environment:
   ```bash
    $ python3 -m pip install dash
    $ ​python3 -m pip install dash-auth
    $ ​python3 -m pip install dash-renderer
    $ ​python3 -m pip install dash-core-components
    $ ​python3 -m pip install dash-html-components
    $ ​python3 -m pip install plotly​
    $ python3 -m pip install plotly.express
    $ python3 -m pip install requests
   ```
7. Install a new dependency gunicorn for deploying the app: (VERY IMPORTANT!!)
   ```bash
    $ python3 -m pip install gunicorn
   ```
8. Prepare the `.gitignore` and the `Procfile` file.  
   
   **.gitignore**: Just a file which prevents git from including the virtualenv folder to the commit files.

    ```python
    venv
    *.pyc
    .DS_Store
    .env
    ```

   **Procfile**: A file used by [`gunicorn`](https://gunicorn.org)

   ```python
    web: gunicorn tips-dashboard:server
   ```
   `tips-dashboard` ​refers to the filename of our application (tips-dashboard.py) and​ server ​refers to the variable ​server​ inside that file.
9. Create the current *requirements.txt* file:
    ```python
    pip freeze > requirements.txt
    ```
10. Log into your heroku account and deploy your app
    ```python
    heroku login

    heroku create a-new-fancy-name

    gitt add .

    git commit -m 'Initial Commit'

    git push heroku master

    heroku ps:scale web=1
    ```

Congratulations - your app should be online now.

## Update your app

If installing a new package:
```python
$ ​pip install ​newdependency
$ ​pip freeze > requirements.txt
```
If updating an existing package:
```python
$ ​pip install ​dependency​ --upgrade $ ​pip freeze > requirements.txt
```
In all cases:
```python
$ ​git status​ ​# view the changes (optional)
$ ​git add .​ ​# add all the changes
$ ​git commit -m ​"​a description of the changes​" $ ​git push heroku master
```

## Lessons learned / Troubleshooting

The first time i tried to deploy the app I had massive issues with including all the needed libraries within the *requirements.txt* file. `Virtualenv` definetly makes your life easier! A good test if all your dependencies are met is to activate your `venv` and start your program local. If you can access it in your browser (localhost:8050) everything should be fine.

Depending on what you want to visualize authentication is not needed. 

The name you configure during step 10 (`heroku create a-new-fancy-name`) will be your subdomain. Therefore *test2* is maybe not the best choice. Of course this subdomain needs to be unique.

To publish an application to different heroku-apps simply add the specific remote name of the created application.  
For example: You already have a application calles *app1.heroku.com*. Now you want to create a new app calles *app2.heroku.com*.
Simply use this code to add thge specific remote: `heroku git:remote -a app2`.