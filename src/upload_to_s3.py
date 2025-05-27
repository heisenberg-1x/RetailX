import boto3
import os
from datetime import datetime

bucket_name = 'retailx-data'  
date_str = datetime.today().strftime('%Y-%m-%d') 
s3_folder = f'raw/{date_str}/' 

s3 = boto3.client('s3')

local_folder = '../data_samples'
for filename in os.listdir(local_folder):
    if filename.endswith('.json'):  
        local_path = os.path.join(local_folder, filename)  
        s3_key = s3_folder + filename  

        print(f" Uploading {filename} to s3://{bucket_name}/{s3_key}")

        s3.upload_file(local_path, bucket_name, s3_key)  

        print(f" Uploaded: {filename}")