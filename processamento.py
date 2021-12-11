#Importing stuff
import numpy as np
import pandas as pd

def converting_to_csv():
    #needed in order to make it work on Andre's PC
    logins = pd.read_parquet('logins.parquet5')
    logins.to_csv('logins.csv')

def reading_loginsset(type):
    #Reading the loginsset
    if(type == 'csv'):
        logins = pd.read_csv('logins.csv')
        print(logins.head())
    else:
        logins = pd.read_parquet('logins.parquet5')
        print(logins.head())
    return logins

#pre-processing
def transform_bool(logins):
    #Transformando float em inteiro
    logins['is_from_official_store'] = logins['is_from_official_store'].astype(int)
    logins['is_emulator'] = logins['is_emulator'].astype(int)
    logins['has_fake_location_app'] = logins['has_fake_location_app'].astype(int)
    logins['has_fake_location_enabled'] = logins['has_fake_location_enabled'].astype(int)
    logins['probable_root'] = logins['probable_root'].astype(int)
    logins['never_permitted_location_on_account'] = logins['never_permitted_location_on_account'].astype(int)
    logins['ato'] = logins['ato'].astype(int)
    return logins
def dropping_nas(logins):
    # Tratando todas as linhas com inteiros ausentes
    logins['max_installations_on_related_devices'] = logins['max_installations_on_related_devices'].fillna(logins['max_installations_on_related_devices'].mean()) 
    logins['boot_count'] = logins['boot_count'].fillna(logins['boot_count'].mean())
    logins['wallpaper_count'] = logins['wallpaper_count'].fillna(logins['wallpaper_count'].mean())
    logins['n_accounts'] = logins['n_accounts'].fillna(logins['n_accounts'].mean())
    
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

def transform_logins(logins):
    # 1) timestamp (int) -> weekday (string)
    day_divider = 86400000 # one day has 86400000 ms
    logins['weekday'] = (logins['timestamp']/day_divider).values.astype(dtype='datetime64[D]')
    logins['weekday'] = logins['weekday'].dt.day_name()
    # 2) Frequencia de reinicialização (float) = boot_count / device_age_ms
    logins['boot_frequency_per_day'] = (logins['boot_count'] / logins['device_age_ms'])/day_divider

    # 3) Wallpaper por contas no dispositivo (float)
    logins['wallpaper_per_accounts'] = logins['wallpaper_count']/logins['n_accounts']

    # 4) Download Externo (bool) = root (true) + loja oficial (false)

    #gambiarra -> logins['download_extern'] = logins.apply(lambda x: x['probable_root']*(1.0 - x['is_from_official_store']) , axis=1) 
    logins['download_extern'] = logins['probable_root'] & (~logins['is_from_official_store']) #converting to int, its possible to make bool operations
    
    # 5) localização suspeita (bool) = has_fake_location_app  and has_fake_location_enabled and never_permitted_location_on_account

    logins['suspicious location'] = logins['has_fake_location_app'] & logins['has_fake_location_enabled'] & logins['never_permitted_location_on_account']
    
    return logins
if __name__ == "__main__":
    #converting_to_csv()
    logins = reading_loginsset('parquet')
    #print(logins.head())
    
    logins_dropna = dropping_nas(logins)
    logins_transformed = transform_bool(logins_dropna)
    logins_updated = transform_logins(logins_transformed)
    print(logins_updated)