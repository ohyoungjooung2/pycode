#This simple python script tested on python3.
#Requires boto3.
#Simply generate aws iam group,user,password(using ohsgpgn).
#This cloud be used for multiple user and groups using loops. Have fun.
import boto3
from ohsgpgn import ohsgpgn
newpass=ohsgpgn.genGoodpass(20)
username='tester3'
groupname='testgrp'
tag_key='Dept'
tag_val='Entertainment'

client=boto3.client('iam')

#create group
res = client.create_group(
    GroupName=groupname
)

#Create user
res = client.create_user(
    UserName=username,
    Tags = [
        {
        'Key': tag_key,
        'Value': tag_val 
        }
    ]
)

res = client.create_login_profile(
    UserName=username,
    Password=newpass,
    #PasswordResetRequired=True|False
    PasswordResetRequired=True
)

res = client.attach_user_policy(
    UserName='tester3',
    PolicyArn='arn:aws:iam::aws:policy/IAMUserChangePassword'
)

#Add user to group
res = client.add_user_to_group(
    GroupName=groupname,
    UserName=username
)
print(f'{username} created with password: {newpass} to group {groupname}')
