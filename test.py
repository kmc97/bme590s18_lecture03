i# Katie Carroll
# Massive Mini Project #1
# fun facts this code only works if the everyone.csv file is already created...because everyone knows that is super useful


def main():
    combine_all_files()
    check_camel_case()
    check_spaces()
    jason_reader()

def number_of_csvs():
    from glob import glob
    file_list = glob("*.csv")
    file_list.remove('mlp6.csv')
    file_list.remove( 'everyone.csv') #used for iteration (needs to be uncommented if file exists prior)
    number_files = len(file_list)
    return number_files

def list_of_csvs():
    from glob import glob
    file_list = glob("*.csv")
    file_list.remove('mlp6.csv')
    file_list.remove('everyone.csv')
    return file_list

def combine_all_files():
    import numpy as np
    import pandas as pd
    file_list = list_of_csvs()
    number_files = number_of_csvs()
    summation_df = pd.DataFrame(dtype = 'str')

    for i in file_list:
        df_loop = pd.read_csv(i, delimiter= ',',index_col = False, names = ["first name", "last name", "dukeID", "git name", "Team name"]) 
        summation_df = pd.concat([summation_df,df_loop])
        final_df = summation_df.drop_duplicates()
    final_df = final_df.set_index(np.arange(number_files+1)) 
    final_df.to_csv('everyone.csv')
    return final_df

def check_camel_case():
    final_df = combine_all_files()
    camel_case = 0
    team_names = final_df['Team name']

    for i in team_names:
        x=i.islower()
        y=i.isupper()
        if x == False and y == False:
            camel_case = camel_case+1
        else:
            camel_case = camel_case+0

    print('There are',camel_case,'teams who use CamelCase')


def check_spaces():    
    final_df = combine_all_files()
    team_name_vector = final_df['Team name']
    for i in team_name_vector:
        if " " in team_name_vector:
            space_status = False
            print('WARNING: An unhelpful message alerting you a team name has a space in it')
        else:
            space_status = True
       # print(space_status)
    return space_status

def jason_reader():
    import csv
    import json
   
    file_list = list_of_csvs()

    for i in file_list:
        csvfile = open(i, 'r')
        replace_end = i
        updated_ending = replace_end.replace('.csv', '.json')
        jsonfile = open(updated_ending, 'w')
        fieldnames = ("First name", "last name", "duke ID", "git ID", "team name")
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            json.dump(row, jsonfile)
            jsonfile.write('\n')

main()
