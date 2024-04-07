import os
import boto3
import time

session = boto3.Session(profile_name='default')
s3 = session.client('s3')

def download(s3, bucket, obj, local_file_path):
    s3.download_file(bucket, obj, local_file_path)

def upload(s3, local_file_path, bucket, obj):
    s3.upload_file(local_file_path, bucket, obj)

def make_public_read(s3, bucket, key):
    s3.put_object_acl(ACL='public-read', Bucket=bucket, Key=key)

if __name__ == "__main__":
    #download(s3,'2024-bigdata-project-yenny', '2024/sea.jpg', 'download.jpg')
    #upload(s3, 'upload.jpg', '2024-bigdata-project-yenny', '2024/upload.jpg')
    make_public_read(s3, '2024-bigdata-project-yenny', '2024/upload.jpg')