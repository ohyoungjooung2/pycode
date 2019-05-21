import json
import boto3


def lambda_handler(event, context):
    a=get_users()
    return(a)
    # TODO implement
    #return {
    #    
     #   'statusCode': 200,
      #  'body': json.dumps('Hello from Lambda!')
    #}
  

def get_users():
    iam=boto3.client('iam')
    iam.generate_credential_report()
    res=iam.get_credential_report()
    GC=res['Content']
    print(GC)
