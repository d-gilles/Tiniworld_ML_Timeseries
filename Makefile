setup:
	@mkdir -p model
	@python -m pip install --upgrade pip
	@pip install .

train:
	@python tiniworld_core/main.py

app:
	@streamlit run webapp/0_🏠_Home.py

docker_build:
	@docker build -t $(CONTAINER_REGISTRY)/$(PROJECT_ID)/$(IMAGE_NAME):latest .

docker_run:
	@docker run -it --rm \
		-p  8080:8080 \
		$(CONTAINER_REGISTRY)/$(PROJECT_ID)/$(IMAGE_NAME):latest
