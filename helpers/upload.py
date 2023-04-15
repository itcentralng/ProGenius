import boto3
import os
import random
import string

session = boto3.session.Session()
client = session.client(
    's3',
    region_name=os.environ.get('SPACE_REGION'),
    endpoint_url=os.environ.get('SPACE_ENDPOINT'),
    aws_access_key_id=os.environ.get('SPACE_KEY'),
    aws_secret_access_key=os.environ.get('SPACE_SECRET'))

import base64
from io import BytesIO

def add(base64_string):
    try:
        # decode base64 string to bytes
        file_data = base64.b64decode(base64_string)
        # create file-like object
        file = BytesIO(file_data)
        # create file name
        name = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.png'
        # upload file
        client.upload_fileobj(file, os.environ.get('SPACE_NAME'), name, ExtraArgs={'ACL': 'public-read'})
        return f"{os.environ.get('SPACE_EDGE_ENDPOINT')}/{os.environ.get('SPACE_NAME')}/{name}"
    except Exception as e:
        print(e)
        return None


def remove(filename):
    try:
        client.delete_object(Bucket=os.environ.get('SPACE_NAME'), Key=filename)
        return True
    except Exception as e:
        print(e)
        return None