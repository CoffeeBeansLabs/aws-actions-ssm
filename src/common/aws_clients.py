import os

import boto3


def get_client(service_name: str, region_name: str, aws_access_key: str, aws_secret_key: str):
    return boto3.client(service_name=service_name, region_name=region_name,
                        aws_access_key_id=aws_access_key,
                        aws_secret_access_key=aws_secret_key)
