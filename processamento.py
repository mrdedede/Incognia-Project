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

#pre-processing
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
#add new columnns

def transform_data(logins):
    # 1) timestamp (int) -> weekday (string)
    day_divider = 86400000 # one day has 86400000 ms
    logins['weekday'] = (logins['timestamp']/day_divider).values.astype(dtype='datetime64[D]')
    logins['weekday'] = logins['weekday'].dt.day_name()
    # 2) Aparelhos por conta (int)

    # 3) Wallpaper por contas no dispositivo (float)
    logins['wallpaper_per_accounts'] = logins['wallpaper_count']/logins['n_accounts']
    # 4) Download Externo (bool) = root (true) + loja oficial (false)

    #gambiarra -> logins['download_extern'] = logins.apply(lambda x: x['probable_root']*(1.0 - x['is_from_official_store']) , axis=1) 
    logins['probable_root'] = logins['probable_root'].astype(int)
    logins['is_from_official_store'] = logins['is_from_official_store'].astype(int)
    logins['download_extern'] = logins['probable_root'] & (~logins['is_from_official_store']) #converting to int, its possible to make bool operations
    
    # 5) Instalação em dispositivo diferente? (bool) (count_installation_on_different_devices)
    
    return logins
if __name__ == "__main__":
    #converting_to_csv()
    logins = reading_dataset('parquet')
    #print(logins.head())
    logins_dropna = dropping_nas(logins)
    logins_updated = transform_data(logins_dropna)
    print(logins_updated)