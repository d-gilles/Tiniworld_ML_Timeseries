start:
	mkdir -p model
	pip install -r requirements.txt
	export PYTHONPATH=$PWD


train:
	python tiniworld_core/main.py

docker_build:
	docker build -t tiniworld_webapp .

docker_run:
	docker run -it --rm \
		-p  8501:8501 \
		tiniworld_webapp

streamlit:
	streamlit run webapp/0_🏠_Home.py
