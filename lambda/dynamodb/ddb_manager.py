import boto3
import collections
import datetime
import ddb_write
import ddb_read
import ddb_update
import ddb_delete


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

    if event['event_id'] == 'write':
        print('Write event')
        ddb_write.lambda_handler(event['event'],'test')
    elif event['event_id'] == 'read':
        print('Read event')
        ddb_read.lambda_handler(event['event'],'test')
    elif event['event_id'] == 'update':
        print('Update event')
        ddb_update.lambda_handler(event['event'],'test')
    elif event['event_id'] == 'delete':
        print('Delete event')
        ddb_delete.lambda_handler(event['event'],'test')
    else:
        error={'ErrorID': '-1', 'Error':'Unknown Event Action: {}'.format(event['event_id'])}
        print(error)
        exit(error)



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

    event={'event_id': 'delete',
           'event': {
                'id': '03',
                'name': 'Mary Ferry',
           }
    }

    lambda_handler(event, "test")
else:
    print("Not running __mina__")
