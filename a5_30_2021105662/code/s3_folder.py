import os
import boto3
import time
import sys

session = boto3.Session(profile_name='default')
s3 = session.client('s3')
my_bucket = '2024-bigdata-project-yenny'


def download(s3, bucket, obj, local_file_path):
    s3.download_file(bucket, obj, local_file_path)

def upload(s3, local_file_path, bucket, obj):
    s3.upload_file(local_file_path, bucket, obj)

def make_public_read(s3, bucket, key):
    s3.put_object_acl(ACL='public-read', Bucket=bucket, Key=key)


if __name__ == "__main__":
    file_path = sys.argv[1]
    make_public = bool(int(sys.argv[2]))
    file_download = bool(int(sys.argv[3]))

    today = time.localtime()
    today_year = today.tm_year
    today_date = time.strftime('%m-%d', today)
    s3_folder = f'{today_year}/{today_date}'
    

    for root, dirs, files in os.walk(file_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_key = os.path.join(s3_folder, os.path.relpath(local_file_path, file_path))
            upload(s3, local_file_path, my_bucket, s3_key)
            if make_public:
                make_public_read(s3, my_bucket, s3_key)
            if file_download:
                download(s3, my_bucket, s3_key, file)