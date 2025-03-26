from google.cloud import storage

# Replace with your bucket name and file path
BUCKET_NAME = "your-gcs-bucket-name"
LOCAL_FILE_PATH = "yellow_tripdata_2025-01.parquet"
GCS_FILE_PATH = "folder_name/yellow_tripdata_2025-01.parquet"  # Optional: Organize in a folder

def upload_to_gcs(bucket_name, local_file, gcs_path):
    """Uploads a Parquet file to Google Cloud Storage."""
    client = storage.Client()  # Authenticated client
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)

    # Upload the file
    blob.upload_from_filename(local_file)
    print(f"✅ File uploaded to gs://{bucket_name}/{gcs_path}")

# Call the function to upload
upload_to_gcs(BUCKET_NAME, LOCAL_FILE_PATH, GCS_FILE_PATH)

