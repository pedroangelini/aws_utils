import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None, bucket_folder_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :param bucket_folder_name: the folder name of where to put the file in the bucket
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    if bucket_folder_name is None or len(bucket_folder_name) == 0:
        bucket_folder_name = ""
    elif bucket_folder_name[-1] != "/":
        bucket_folder_name = bucket_folder_name + "/"

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, bucket_folder_name + object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True