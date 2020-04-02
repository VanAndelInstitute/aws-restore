# aws-restore

awsRestore is a python script that runs on the command line for restoring entire folders and subfolders stored in AWS Glacier Deep Archive.

# Description
All files that are in Deep Archive storage within the folder and all subfolders will be restored. If a file is already restored or is in progress of being restored, it will be noted in the output.

The user enters the bucket name, folder name (top level folder - all subfolders will be included in the restore), and days (how long it will be available for download). 

# Installation
Mac OS X: A version of Python is already installed.

Windows: You will need to installpython3 which is available at python.org.

# Usage
Run the program in the terminal with the following command line arguments:

--bucket        -Name of the bucket with items to be restored\
--foldername    -Name of the folder to be restored\
--days          -Number of days the restored items will be available for download\
