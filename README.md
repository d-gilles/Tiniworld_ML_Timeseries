## Final project of the Data Science Bootcamp (Le Wagon) October – December 2022 in Cologne.

The aim of this project is to analyze the ticket sales of an indoor playground operator and to make a prediction about the expected future ticket sales. The data was provided to us by the company Tiniworld, an operator of indoor playgrounds with 64 locations in Vietnam.

### The project includes the following steps:
-	Reading the raw data from a CSV file.
-	The splitting of the data, according to the different locations.
-	Train machine learning models based on these data sets.
-	Provision of the graphical evaluation of the data in a web app
- run this app locally or in the cloud

### LIVE DEMO
Have a look at the app [here](https://tiniworld-yknatb6hna-ey.a.run.app/)

### tech and tools
... used in this project:
- python
- pandas
- prophet
- plotly
- streamlit
- docker
- terraform
- google cloud platform

### To run this project yourself...
- Download the repo, it includes all the data needed.

This project uses direnv, to load environment variables from the .env file. By default the repo comes with a .env.example file. Just rename this to .env (`mv .env.example .env`) and add your custom values. Make shure you have direnv installed and run `direnv allow` when entreing the folder for the first time. After changing the content of the .env file you always have to `direnv reload` to commit this changes.

- run `make setup` to set up a folder for the ML models and install requirements.
- run `make train` to crossvalidate und fit models all location with ticke sales > `THRESHOLD` .


By default there are just the 2 best selling locations and the overall sales for the whole company. So there are 3 models to play with.
You can add more model by changing the `THRESHOLD` variable in `tiniworld/logic/params.py`

### Start frontend localy
After setting up and training the models, you can now see the results.
This project includes a streamlit http frontend to interact with the data.
You can choose from 3 options to run the frontend.

1.  Run streamlit direct by `make app`
2.  Use Docker. For this you need a docker Daemon running on your machine. To build a docker image, just run `make docker_build` and to run it in a container - guess what - run `make docker_run`.

    In both cases streamlit should automatically start your browser and go to `localhost:8501` if not click [here](http://localhost:8501)

3. Host the frontend online on Google Cloud Platform

### Deploy online
This repo includes a configuration to setup a gcp environment and deploy the app online. If you would like to do that you will need a few things.

**Install Terraform:**</br> If you haven't already, you'll need to install Terraform on your machine. Instructions can be found on [the official HashiCorp website](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

**Set Up Google Cloud Platform (GCP) Project:** </br>
- Login to gcp or create a account.
- Create a new project on GCP.
- Provide the project ID and project region in the .env file as `TF_VAR_PROJECT_ID` and `TF_VAR_REGION`


**Set Up GCP Authentication:**
- Create a new Service Account for Terraform in the GCP Console, ensuring that it has sufficient permissions for the resources you'll be managing (usually Project or Owner level).
- Create and download a JSON key for this Service Account.
- Set an environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the downloaded JSON key file. You can also do this in the .env file, so it will be set just inside this folder.
- Activate the [**Cloud Resource Manager API**](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com) for your project

**Run the app online:**</br>
After doing the steps above, just run `make online` to deploy the app on gcp.
The command will give you back the url of the website.
