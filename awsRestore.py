import boto3
from botocore.exceptions import ClientError
import sys

try:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('motuz')
    #get folder name of the folder you would like to restore from glacier (input on command line)
    folderName = sys.argv[1]
except ClientError as e:
    print(e.response)
    sys.exit()

try:
    s3Client = boto3.client('s3')
    paginator = s3Client.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket='motuz', PaginationConfig={'PageSize':1000})
except ClientError as e:
    print(e.response)
    sys.exit()

try:
    for page in page_iterator:
            #loop through bucket objects to restore
            for obj in page['Contents']:
                    #if the folder name is in the object key continue to restore
                    if folderName in obj['Key']:
                        #variable for current object
                        obj = s3.Object('motuz', obj['Key']) 
                        #check to see if object is in glacier deep archive
                        if obj.storage_class == 'DEEP_ARCHIVE': 
                            #if restore status is blank continue to request restore
                            if obj.restore is None: 
                                    print('Submitting restoration request: %s' % obj.key)
                                    #restore object
                                    obj.restore_object(RestoreRequest={'Days': 1}) 
                            #if object is being restored print status
                            elif 'ongoing-request="true"' in obj.restore: 
                                print('Restoration in-progress: %s' % obj.key)
                            #if object is done being restored print status    
                            elif 'ongoing-request="false"' in obj.restore: 
                                print('Restoration complete: %s' % obj.key)
except ClientError as e:
    print(e.response)
    sys.exit()