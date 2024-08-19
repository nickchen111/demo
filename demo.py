import sys
print(sys.path)

from datetime import datetime
from google.cloud import storage

def generate_gcs_url(bucket_name, object_name, expiration=3600):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    url = blob.generate_signed_url(expiration, method='GET')
    return url

bucket_name = "statics-dev.mirrordaily.news"
object_name = "shortpage_creativity01.json"

url = generate_gcs_url(bucket_name, object_name)
print(url)