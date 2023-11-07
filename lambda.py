import json
import boto3
client = boto3.client('sns')
def lambda_handler(event, context):
    answer = json.loads(event['Records'][0]['body'])
    region = answer['Records'][0]['awsRegion']
    eventName = answer['Records'][0]['eventName']
    bucketName = answer['Records'][0]['s3']['bucket']['name']
    objectName = answer['Records'][0]['s3']['object']['key']
   
   
    if(eventName == 'ObjectRemoved:Delete'):
        eventName = 'deleted'
    elif(eventName == 'ObjectCreated:Put'):
        eventName = 'uploaded'
       
    bucketName = bucketName.replace('+', ' ')
    
    
    response = client.publish(
    TopicArn='Your-SNS-ARN',
    Message='The file '+objectName.replace('+', ' ')+' is '+eventName+' in  the bucket '+bucketName+' at region {}.'.format(region),
    Subject='message-notification',
 
    MessageStructure='string',
    MessageAttributes={
        'String': {
            'DataType': 'String',
            'StringValue': 'String'
        }
            
    },
)
