# this is a python script to test if the lambda function is working correctly using boto3 > python tutorial_print.py
# We have hard coded the bucket name, object lambda access point arn and the 'Key' which is the file in the bucket (tutorial.txt)
import boto3
from botocore.config import Config

s3 = boto3.client('s3', config=Config(signature_version='s3v4'))

def getObject(bucket, key):
    objectBody = s3.get_object(Bucket = bucket, Key = key)
    print(objectBody["Body"].read().decode("utf-8"))
    print("\n")

print('Original object from the S3 bucket:')
# substitute s3-bucket-name with bucket name upon resource creation from (s3-access-point.yml) stack, (tutorial.txt) is the file to be uploaded into the bucket
getObject("s3-bucket-name", 
          "tutorial.txt")

print('Object transformed by S3 Object Lambda:')

# substitute object-lambda-access-point-arn with the Object Lambda Access Point Arn upon resource creation from (object-lambda.yml) stack
getObject("object-lambda-access-point-arn",
          "tutorial.txt")   