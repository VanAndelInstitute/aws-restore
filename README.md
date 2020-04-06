# aws-restore

awsRestore is a python script that runs on the command line for restoring entire folders and subfolders stored in AWS Glacier Deep Archive.

# Description
All files that are in Deep Archive storage within the folder and all subfolders will be restored. If a file is already restored or is in progress of being restored, it will be noted in the output.

The user enters the bucket name, folder name (top level folder - all subfolders will be included in the restore), and days (how long it will be available for download). 

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
Run the program in the terminal with the following command line arguments:

    --bucket         Name of the bucket with items to be restored
    --foldername     Name of the folder to be restored
    --days           Number of days the restored items will be available for download

example:

    python3 awsRestore.py --bucket <<bucket name>> --foldername <<folder name>> --days <<number of days>>
