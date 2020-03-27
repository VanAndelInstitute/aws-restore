import boto3
import sys


s3 = boto3.resource('s3')
bucket = s3.Bucket('motuz')

#get folder name of the folder you would like to restore from glacier (input on command line)
folderName = sys.argv[1]

#get all bucket objects
allBucketObjects = bucket.objects.all()

#loop through bucket objects to restore
for obj_sum in allBucketObjects:
    #if the folder name is in the object key continue to restore
    if folderName in obj_sum.key: 
        #variable for current object
        obj = s3.Object(obj_sum.bucket_name, obj_sum.key) 
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

