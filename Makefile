docker_build:
	docker build -t tiniworld_webapp .

docker_run:
	docker run -it -p  8501:8501  tiniworld_webapp
