start:
	mkdir model
	pip install -r requirements.txt

train:
	python tiniworld_core/main.py

docker_build:
	docker build -t tiniworld_webapp .

docker_run:
	docker run -it --rm \
		-p  8501:8501 \
		tiniworld_webapp
