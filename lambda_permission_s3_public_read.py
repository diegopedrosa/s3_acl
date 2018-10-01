import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    for e in event['Records']:
        object_acl = s3.ObjectAcl(str(e['s3']['bucket']['name']),str(e['s3']['object']['key']))
        response = object_acl.put(ACL='public-read')
    return {
        "statusCode": 200,
        "body": response
    }
