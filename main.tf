variable "project" {}
variable "region" {}

provider "google" {
}

resource "google_project_service" "container_registry" {
  project = var.project
  service = "storage-component.googleapis.com"
  disable_dependent_services=true
}

resource "google_project_service" "cloud_run" {
  project = var.project
  service = "run.googleapis.com"
  disable_dependent_services=true
}
