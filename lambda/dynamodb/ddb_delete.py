import boto3
import collections
import datetime
import sys
from boto3.dynamodb.conditions import Key, Attr

#session = boto3.session.Session(profile_name='admints', region_name='us-east-1')
#boto3.setup_default_session(profile_name='admints')

# --------------------------------------
# AWS Lambda Handler
# --------------------------------------
def lambda_handler(event, context):
    # Default variables

    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")
    try:
        if env == 'local':
            print('BEGIN - LAMBDA - dynabodb')
            print('BEGIN - START TIME - {0}'.format(start_time))
            print('Running locally')
            boto3.setup_default_session(profile_name='pacheco')
    except NameError:
        print('BEGIN - LAMBDA - dynabodb')
        print('BEGIN - START TIME - {0}'.format(start_time))
        print('Running AWS')

    # Create the resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    # Get the client from the resource
    #dynamodb = dynamodb_resource.meta.client

    table = dynamodb.Table('myapps')

    try:
        table.delete_item(
            Key=event
        )
    except:
        error={'ErrorID': '-1', 'Error':'Key Delete Failed'}
        print(error)
        exit(error)
    #botocore.exceptions.ClientError: An error occurred (ValidationException)

    #response = table.query(
    #KeyConditionExpression=Key('id').eq('01')
    #)

    #items = response['Items']
    #print(items)

    # Log the end of the Lambda function
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")
    print('END - END TIME - {0}'.format(end_time))
    print('END - LAMBDA - dynabodb')

    print(event)
    return event
# Used to dbug


# --------------------------------------
# Main
# --------------------------------------
# Allow you to run on local sandbox for testing
if __name__ == "__main__":
    #print("running __mina__")
    # Connection settings.  Win NOT be used with lambda function
    global env
    env = 'local'

    event={
        'id': '03',
        'name': 'Mary Ferry'
    }

    lambda_handler(event, "test")
else:
    print("Not running __mina__")
