setup:
	@mkdir -p model
	@python -m pip install --upgrade pip
	@pip install .

train:
	@python tiniworld_core/main.py

app:
	@streamlit run webapp/0_🏠_Home.py

docker_build:
	@docker build -t tiniworld:latest .

docker_run:
	@docker run -it --rm \
		-p  8080:8080 \
		tiniworld:latest

tf_init:
	@terraform init
	@terraform apply -auto-approve

docker_push:
	@docker push $(CONTAINER_REGISTRY)/$(TF_VAR_PROJECT)/$(IMAGE_NAME):latest

docker_deploy:
	@gcloud config set project $(TF_VAR_PROJECT)
	@gcloud run deploy tiniworld --image $(CONTAINER_REGISTRY)/$(TF_VAR_PROJECT)/$(IMAGE_NAME):latest --platform managed --region $(TF_VAR_REGION) --allow-unauthenticated

get_URL:
	@echo "The URL of your app is: $$(gcloud run services describe $(IMAGE_NAME) --region $(TF_VAR_REGION) --platform managed --format "value(status.url)")"

prepare:
	setup
	train

local:
	app

online:
	@docker build -t $(CONTAINER_REGISTRY)/$(TF_VAR_PROJECT)/$(IMAGE_NAME):latest .
	make tf_init
	make docker_push
	make docker_deploy
	make get_URL

kill:
	@terraform destroy -auto-approve
	@gcloud projects delete $(TF_VAR_PROJECT) --quiet
