# aws-restore

awsRestore is a collection of python scripts that runs on the command line for restoring entire folders and subfolders stored in AWS Glacier Deep Archive or deleted using S3 versioning.

# Description

## awsRestore.py
All files that are in Deep Archive storage within the folder and all subfolders will be restored. If a file is already restored or is in progress of being restored, it will be noted in the output.

The user enters the bucket name, folder name (top level folder - all subfolders will be included in the restore), and days (how long it will be available for download). 

## awsUndelete.py
All files that are deleted have a new version of the file called a delete marker. Restoring a file is as simple as deleting the delete marker, but this script will do it in batch.

The user enters the bucket name, folder name (top level folder - all subfolders will be included in the undelete).

# Installation
Mac OS X: A version of Python is already installed.

Windows: You will need to install python3 which is available at python.org.

Prior to using this script you must log-in to the aws account through the terminal using "aws configure".

example:

    aws configure
    AWS Access Key ID [****************TDNW]: <<your aws access key>>
    AWS Secret Access Key [****************qUQl]: <<your aws secret access key>>
    Default region name [us-east-2]: <<your aws region>>
    Default output format [json]: <<your default output>>


# Usage

## awsRestore.py
Run the program in the terminal with the following command line arguments:

    --bucket         Name of the bucket with items to be restored
    --prefix         S3 prefix of the path (folder) to be restored
    --days           Number of days the restored items will be available for download
    --dryrun         (Optional) Shows what files would have been restored without restoring

example:

    python3 awsRestore.py --bucket <<bucket name>> --prefix <<prefix>> --days <<number of days>> --dryrun
    py awsRestore.py --bucket <<bucket name>> --prefix <<prefix>> --days <<number of days>> --dryrun

    python3 awsRestore.py --bucket <<bucket name>> --prefix <<prefix>> --days <<number of days>>
    py awsRestore.py --bucket <<bucket name>> --prefix <<prefix>> --days <<number of days>>
    
## awsUndelete.py
Run the program in the terminal with the following command line arguments:

    --bucket         Name of the bucket with items to be restored
    --prefix         S3 prefix of the path (folder) to be restored
    --dryrun         (Optional) Shows what files would have been undeleted

example:

    python3 awsUndelete.py --bucket <<bucket name>> --prefix <<prefix>> --dryrun
    py awsUndelete.py --bucket <<bucket name>> --prefix <<prefix>> --dryrun

    python3 awsUndelete.py --bucket <<bucket name>> --prefix <<prefix>>
    py awsUndelete.py --bucket <<bucket name>> --prefix <<prefix>>