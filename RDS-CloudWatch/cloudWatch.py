#!/usr/bin/python

## Parameters:
# MetricName. Eg: CurrConnections
# Function. Can be one of the following: Average, Sum, SampleCount, Maximum, or Minimum.
# Dimension. Eg: rds-hostname
# Region. Eg: eu-west-1
# AWS_Access_Key
# AWS_Secret_Access_Key


import boto.ec2.cloudwatch
import sys
import datetime

accessKey = "XXXXXXXXXXXXXXXXXXX"
secretKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

try:
    metName = sys.argv[1]
    funcName = sys.argv[2]
    dimSpace = sys.argv[3]
    region = sys.argv[4]

except:
    print "Usage: cloudWatch.py MetricName Function rds-instance-name Region"
    print "Example: cloudWatch.py CurrConnections Average rds-instnace01 eu-west-1"
    sys.exit(1)

dim = {}
dim["DBInstanceIdentifier"] = dimSpace

regions = boto.ec2.cloudwatch.regions()
reg = ''
for r in regions:
    if region == r.name:
        reg = r
c = boto.ec2.cloudwatch.CloudWatchConnection(aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region=reg)
metrics = c.list_metrics(dimensions=dim)

end = datetime.datetime.utcnow()
start = end - datetime.timedelta(minutes=20)

dataPoints = [];

for met in metrics:
    if met.name == metName:
        dataPoints = met.query(start, end, funcName)

if len(dataPoints) > 0:
    max = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    index = 0
    for i in range(0,len(dataPoints)):
        if max < dataPoints[i][u'Timestamp']:
            max = dataPoints[i][u'Timestamp']
            index = i
    for key in dataPoints[index].keys():
        if funcName in key:
            value = dataPoints[index][key]
    print value
else:
    print 'Error! No response from Amazon.'
    sys.exit(2)

