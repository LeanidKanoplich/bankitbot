from google.cloud import storage
import os
import config

# Создаем клиента для работы с Google Cloud Storage
storage_client = storage.Client()

def upload_file_to_gcs(local_file_path, destination_blob_name):
    try:
        bucket = storage_client.bucket(config.GCP_CLOUD_STORAGE_BUCKET_NAME)
        blob = bucket.blob(destination_blob_name)
        # Загружаем файл в Google Cloud Storage и устанавливаем публичный доступ к нему
        blob.upload_from_filename(local_file_path)
        blob.make_public()
        public_url = blob.public_url
        # Удаляем локальный файл после успешной загрузки
        os.unlink(local_file_path)
        return public_url
    except Exception as e:
        print(e)
