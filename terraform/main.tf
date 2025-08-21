provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "gcs_bucket" {
    name = "anik-gcs-bucket-1"
    location = "US"
    force_destroy = true
}

resource "google_bigquery_dataset" "etl_dataset" {
    dataset_id = "etl_demo_dataset"
    location = "US"
}