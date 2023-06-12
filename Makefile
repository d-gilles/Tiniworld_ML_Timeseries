setup:
	@mkdir -p model
	@python -m pip install --upgrade pip
	@pip install .

train:
	@python tiniworld_core/main.py

app:
	@streamlit run webapp/0_🏠_Home.py

docker_build:
	@docker build -t tiniworld_webapp .

docker_run:
	@docker run -it --rm \
		-p  8501:8501 \
		tiniworld_webapp
