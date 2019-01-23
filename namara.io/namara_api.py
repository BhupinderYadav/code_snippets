import requests
import json
import pandas as pd

class Namara:
    def __init__(self, api_key, debug=False, host='api.namara.io', api_version='v0'):
        self.api_key = api_key
        self.debug = debug
        self.host = host
        self.api_version = api_version
        self.path = ''
        self.headers = {'Content-Type': 'application/json', 'X-API-Key': api_key}

    def get(self, data_set_id, version, options=None):
        #api request path builder
        api_url = r'https://' + str(self.host) + r'/' + str(self.api_version) +   r'/data_sets/' + \
                                str(data_set_id) + r'/data/'+ version + r'?api_key=' + str(self.api_key)

        # making request to namara.io
        response = requests.get(api_url, options, headers=self.headers)
        results = response.json()
        response.close()
        return results


    def export(self, data_set_id, version, options=None):
        #https://api.namara.io/v0/data_sets/:data_set_id/data/:version/export
        export_url = r'https://' + str(self.host) + r'/' + str(self.api_version) +   r'/data_sets/' + \
                                str(data_set_id) + r'/data/'+ version + 'export'


        # making request to namara.io
        response = requests.get(export_url, options, headers=self.headers)
        pass
        # print('File is succesfully downloaded')


if __name__ == '__main__':

    # generate the project api_key from namara.io
    api_key = '4d8e47aad063f9457b3a68c60af01e91a2cf7de40babb3fe9ef3434af9f61538'

    # data set id available on the namara.io to extract the data set
    data_set_id = 'f6dbb3b8-d6bd-484e-997d-50c922e89550'

    # data_set_version available on namara.io
    data_set_version = 'en-19'

    # option/query  you want to perfome on dataset on namara.io
    options = {
  # 'select': 'acres',
  # 'where': 'style = 'Bungalow'',
  # 'operation': 'count(*)', #agregate options
  'offset': '0',
  'limit': '200'
  }

    # intiating the namara class with your project key
    namara = Namara(api_key)

    # accessing get method from namara class to extract the data set by passing data_set_id , version and query options available
    #on namara.io
    Data = namara.get( data_set_id, data_set_version, options)

    # accessing data in data frame
    data_frame =  pd.DataFrame(Data)
    print(data_frame)

    # saving the data in csv File
    # file_name = 'output.csv'
    # file_path = r'C:\Users\bhupi\Desktop\Resume' + file_name
    # data_frame.to_csv('output.csv')
