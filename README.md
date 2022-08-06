# Flight_fare_Prediction
Main goal is to predict the fares based on given factors in the dataset

# Software and Accout Requirement.
Github Account
Heroku Account
VS Code
GIT CLI

# Steps
git status
git add
git commit -m "message" Git commit create the version and push will push this changes to github
git push origin main This origin actually is the repo link
git remote -v To check repo link

# Virtual environment and requirements.txt
Creating conda virtual env conda create -p <env_name> python==3.7 -y -p to create venv in project folder itself
Activate venv conda activate <env_name>/ or conda activate <env_name>
Creating requirement.txt file pip freeze > requirements.txt
To install requirements.txt pip install -r requirements.txt

# To setpup CI/CD pipeline in heroku we need following information
HEROKU_EMAIL: singhmohan1998july@gmail.com
HEROKU_API_KEY: <API_KEY>
HEROKU_APP_NAME: ML-Fare-Prediction-app-MO

# BUILD DOCKER IMAGE
docker build -t <image_name>:<tag_name> .
image_name should be in lower case and tag_name generally use 'latest'

docker images To list Docker Image and get IMAGE_ID
Run Docker Image docker run -p 5000:5000 -e PORT=5000 <IMAGE_ID>
docker ps To check running container in docker
docker stop <container_id> to stop docker container

# Notes
If adding '-e .' then we must have setup.py file in root directory. This will create <custom_pkg_name>-egg.info file for every package which contains "init.py" file. Where "-e ." executed inside "requirements.txt". Its actually lunching the "setup.py" hence the egg.info file will get created for all custom packages.