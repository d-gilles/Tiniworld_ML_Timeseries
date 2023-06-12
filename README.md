## Final project of the Data Science Bootcamp (Le Wagon) October – December 2022 in Cologne.

The aim of this project is to analyze the ticket sales of an indoor playground operator and to make a prediction about the expected future ticket sales. The data was provided to us by the company Tiniworld, an operator of indoor playgrounds with 64 locations in Vietnam.

### The project includes the following steps:
-	Reading the raw data from a CSV file.
-	The splitting of the data, according to the different locations.
-	Train machine learning models based on these data sets.
-	Provision of the graphical evaluation of the data in a web app

### To run this project ...
- Download the repo, it includes all the data needed.
- run `make setup` to set up a folder for the ML models and install requirements.
- run `make train` to crossvalidate und fit models all location with ticke sales > `THRESHOLD` .


By default there are just the 2 best selling locations and the overall sales for the whole company. So there are 3 models to play with.
You can add more model by changing the `THRESHOLD` variable in `tiniworld/logic/params.py`

### Start frontend
After setting up and training the models, you can now see the results.
This project includes a streamlit http frontend to interact with the data.
You can choose from 2 options to run the frontend.

1.  Run streamlit direct by `make app`
2.  Use Docker. For this you need a docker Daemon running on your machine. To build a docker image, just run `make docker_build` and to run it in a container - guess what - run `make docker_run`.

In both cases streamlit should automatically start your browser and go to `localhost:8501` if not click [here](http://localhost:8501)
