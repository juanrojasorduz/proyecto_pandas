import pandas as pd
import os
from especial_functions import conditions_function,input_validation

print('')

file_types = ['csv','json','xlsx']
options_index = [1,2,3,4]
source_files = os.listdir('source')
data_types = ['object','int64','float64','bool','datetime64']
execution = ['Y','N']


messages = {
    0: 'Select a file type between csv,json or xlsx to import the file',
    1: 'Select a file from the following options:',
    2: 'Please select an option',
    3: 'Enter the name of the field you want to set as the index',
    4: 'Here you have a previous visualization of the first 3 raws:',
    5: '¡Welcome to the data cleanse process!',
    6: 'Do you want to send the file with the modifications Y/N?',
    7: 'Type the name of the destination file <file_name>.<ext>',
    8: 'Enter the file type you want to export'
}


error_messages = {
    0: 'Value error! You must select an argument between the following values',
    1: 'Source file error! You must have at least one file with the extension previously entered',
    2: 'Source file error! You must select a file between the following options',
    3: 'Value error! Please verify the file extension'
}


index_menu = """
Options to set index:
1- Default index
2- Drop default index and reset index
3- Keep default index as a filed and reset index
4- Drop default index and set an index between the available columns 
"""


def file_import():
    file_type = input_validation('options_list','string',file_types,[],[],messages[0],error_messages[0],False)
    source_options = list(filter(lambda x: os.path.splitext(x)[1].lstrip('.') == file_type,source_files))
    if not source_options:
        print(error_messages[1])
        exit()
    source_file_route = 'source/'+input_validation('options_list','string',source_options,[],[],messages[1],error_messages[2],False)
    if file_type == 'csv':
        df = pd.read_csv(source_file_route)
    elif file_type == 'json':
        df = pd.read_json(source_file_route)
    elif file_type == 'xlsx':
        df = pd.read_excel(source_file_route)
    return df


def previous_visualization(df):
    print(messages[4])
    print(df.head(3))


def index_fixed(df):
    columns = list(df.columns)
    previous_visualization(df)
    print(index_menu)
    response = input_validation('options_list','int',options_index,[],[],messages[1],error_messages[2],True)
    if response == 2:
        df = df.reset_index(drop=True,inplace=False)
    elif response == 3:
        df = df.reset_index(drop=False,inplace=False)
    elif response == 4:
        index_set = input_validation('options_list','string',columns,[],[],messages[3],error_messages[0],False)
        df = df.set_index(index_set, drop=True, inplace=False)
    return df


def file_export(df):
    previous_visualization(df)
    request = input_validation('options_list','string',execution,[],[],messages[6],error_messages[0],False)
    if request == 'N':
        print('Execution not done!')
        exit()
    destination_file_type = input_validation('options_list','string',file_types,[],[],messages[8],error_messages[0],False)
    destination_file_route = 'destination/'+input_validation('condition','string',[],'file_name_extension',destination_file_type,messages[7],error_messages[3],False)
    print(destination_file_route)
    if destination_file_type == 'csv':
        df.to_csv(destination_file_route)
    elif destination_file_type == 'json':
        df.to_json(destination_file_route)
    elif destination_file_type == 'xlsx':
        df.to_excel(destination_file_route)
    print('File saved!')


def run():    
    print(messages[5])
    df = file_import()
    df = index_fixed(df)
    file_export(df)


if __name__ == '__main__':
    run()
