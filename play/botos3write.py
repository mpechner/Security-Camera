import boto3
import os

camera='1'
bucket='mikey.com-security'
path='/mnt/cameraimages/images'

s3 = boto3.resource('s3')
for dirName, subdirList, fileList in os.walk(path):
    for fname in fileList:
        if len(path) == len(dirName):
            finame=fname
        else:
            finame = '%s/%s'%(dirName[len(path)+1:], fname)
        print(finame)
        res=s3.meta.client.upload_file(dirName + '/' + fname, bucket, finame)
        print res
        os.unlink(dirName + '/' + fname)
