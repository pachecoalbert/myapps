import boto3
import collections
import datetime
import sys
from boto3.dynamodb.conditions import Key, Attr
import ddb_write
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

    try:
        ddb_write.lambda_handler(event,'test')
    except:
        error={'ErrorID': '-1', 'Error':'Update Call Failed'}
        print(error)
        exit(error)

    # Log the end of the Lambda function
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")
    print('END - END TIME - {0}'.format(end_time))
    print('END - LAMBDA - dynabodb')

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
        'name': 'Mary Ferry',
        'dept': 'Finance',
    }

    lambda_handler(event, "test")
else:
    print("Not running __mina__")
