#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError
import sys
import argparse

try:
    #add parser for command line arguments. User adds prefix/folder-name, and bucket name undelete file
    parser = argparse.ArgumentParser(description = 'add parameters to undelete')
    parser.add_argument('--prefix', action = 'store', help="the object/file path prefix or folders to undelete")
    parser.add_argument('--bucket', action = 'store', help="bucket to undelete from")
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()
    bucketname = args.bucket
    #get prefix of the folder you would like to undelete
    prefix = args.prefix
    dryrun = args.dryrun
except Exception as e:
    print(e)
    sys.exit()

try:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucketname)
except ClientError as e:
    print(e.response)
    sys.exit()

try:
    s3Client = boto3.client('s3')
    #add paginator to allow for larger than 1000 objects to undelete
    paginator = s3Client.get_paginator('list_object_versions')
    page_iterator = paginator.paginate(Bucket=bucketname, Prefix=prefix, PaginationConfig={'PageSize':1000})
except ClientError as e:
    print(e.response)
    sys.exit()

try:
    #loop through pages to undelete
    for page in page_iterator:
        for obj in page['DeleteMarkers']:
            if prefix in obj['Key']:
                if dryrun:
                    print("Dryrun: would have undeleted: %s" % obj['Key'])
                else:
                    s3.ObjectVersion(bucketname, obj['Key'], obj['VersionId']).delete()
                    print("Undeleting: %s" % obj['Key'])
except ClientError as e:
    print(e.response)
    sys.exit()
