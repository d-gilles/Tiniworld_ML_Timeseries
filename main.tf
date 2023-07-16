variable "project" {}
variable "region" {}

provider "google" {
}

resource "google_project_service" "container_registry" {
  project = var.project
  service = "storage-component.googleapis.com"
}

resource "google_project_service" "cloud_run" {
  project = var.project
  service = "run.googleapis.com"
}
