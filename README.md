# This is my centralized Django API for all my side projects 
Documented with swagger ui and link to schema is in Repo description 

Purpose of repo = Reference for any future projects and for anyone looking for an easy way to get going with DRF and Heroku
This is not a quickstart intro for Django. This will take some time, but you will thank yourself later for a much easier experience. 

## Get Started locally 
### Do these things before running 
- make a directory named whatever you want. Then cd into that directory
- Run the following command: <b> django-admin startproject config . </b> 
- Yes keep the period at the end of the command, otherwise the project will be setup in a way that doesn't go along with these instructions 
- Create necassary files by running: <b> touch Procfile requirments.txt .env .gitignore </b> 
- Initialize virtual environment by running: <b> python3 -m venv env </b>
- Then activate the venv by running: <b> source env/bin/activate </b> 
- Copy  text from requirements.txt in this repo and paste that text in your requirements.txt
- Setup your virtual environment by running: <b> pip3 install -r requirements.txt </b> 
- Then finalize setting up your environment by running: <b> pip3 freeze > requirements.txt </b> 
- Then copy the text from the procfile in the repo and paste it into your Procfile
- put the following text in your .env file on different lines: 
    - <b> env </b> 
    - <b> .env </b>
    - <b> .DS_STORE </b>
- cd into the config folder
- make a components folder inside the config folder you're currently in  and create all the files that are shown in the same folder in the repo
- Do the same thing for the local settings folder within the config foler in the repo and copy it into your folder. This will take time and is tedious. It would probably be easier for you just to copy from my repo considering the project names are the same. 
- Then copy and paste the content in the settings.py file and paste it into your file
- To finally get ready to run the app, cd back into the root folder
- To make the migrations, run the command: <b> python3 manage.py makemigrations --settings=config.local.settings </b> 
- Then to migrate the app, run the command: <b> python3 manage.py migrate --setting=config.local.settings </b> 
- Finally, run: <b> python3 manage.py runserver --settings=config.local.settings </b> 

## Develop Away 
