#Importing stuff
import numpy as np
import pandas as pd

def converting_to_csv():
    #needed in order to make it work on Andre's PC
    logins = pd.read_parquet('logins.parquet5')
    logins.to_csv('logins.csv')

def reading_dataset(type):
    #Reading the dataset
    if(type == 'csv'):
        logins = pd.read_csv('logins.csv')
        print(logins.head())
    else:
        logins = pd.read_parquet('logins.parquet5')
        print(logins.head())
    return logins

def dropping_nas(logins):
    #Deleting every row that has missing strings 
    logins2 = logins[logins['id'].notna() &
                logins['account_id'].notna() &
                logins['device_id'].notna() &
                logins['installation_id'].notna()]
    
    #Deleting every row that has missing booleans
    logins2 = logins2[logins2['is_from_official_store'].notna() &
                    logins2['is_emulator'].notna() &
                    logins2['has_fake_location_app'].notna() &
                    logins2['has_fake_location_enabled'].notna() &
                    logins2['probable_root'].notna() &
                    logins2['never_permitted_location_on_account'].notna() &
                    logins2['ato'].notna()]
    
    #Deleting every row that has a missing timestamp
    logins2 = logins2[logins2['timestamp'].notna()]
    return logins2

if __name__ == "__main__":
    logins = reading_dataset('csv')
    print(logins.head())