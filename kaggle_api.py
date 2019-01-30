''' 
This code will help you to download the dataset from kaggle using kaggle CLI
In order to use CLI use below steps:
-------------------------------------
1. Install kaggle using command :-  pip install kaggle
2. Login to kaggle and download the kaggle.json file from API token sectionselfself.
3. Create a folder with name kaggle in home directroy if using Linux or in case windows c:/users/your_account  with name .kaggle
4. Put download kaggle.json file having your cerdentials to newly created folderself.

CLI commands:
-------------
 1. To list the data sets
 >>  kaggle datasets list --sort-by votes

 2. To download the data set
 >> kaggle datasets download <dataset ref name>
'''

import subprocess # to run command on CMD propmpt
import zipfile # to unzip the file
import os
import pandas as pd

dataset_name = 'uciml/iris' # data set name
kaggle_download_command =  "kaggle datasets download " + str(dataset_name)

# subprocess.run("kaggle datasets list --sort-by votes") # will the you the list of dataset availble on kaggle.com
subprocess.run(kaggle_download_command) # will donwload the zip file having a csv and sqllite file having the data

# unzipping  file
dirname, filename = os.path.split(os.path.abspath(__file__))  # extracting the directory name where dataset is dwonloaded
download_name_temp =  dataset_name.split("/")
downloaded_file =   str(download_name_temp[-1]) + ".zip"
path =  str(dirname) + '/'  + str(downloaded_file)

# unzipping the downloaded file
unzip_it = zipfile.ZipFile(path, 'r')
unzip_it.extractall(dirname)
unzip_it.close()

# reading the dataset in pandas
dataset = str(download_name_temp[-1]) + ".csv"
df = pd.DataFrame.from_csv(dataset)
print(df)
