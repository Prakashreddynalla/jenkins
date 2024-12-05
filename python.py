import boto3
client=boto3.client('ec2')
response=client.run_instances(
    ImageId='ami-038bba9a164eb3dc1',
    InstanceType ='t2.micro',
    KeyName ='west',
    SubnetId='subnet-0cfa79ac3472e8561',
    MaxCount =1,
    MinCount =1
)
