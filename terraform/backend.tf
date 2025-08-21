terraform {
  backend "gcs" {
    bucket = "anik-tf-state-bucket-1"
    prefix = "terraform/state"
  }
}
