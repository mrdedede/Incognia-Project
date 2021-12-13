#Importando bibliotecas
import pandas as pd
import numpy as np

# Lendo Arquivos

def converting_to_csv():
    """Cria um arquivo logins.csv baseado no logins.parquet5
    """
    #Necessário para funcionar no PC de Andre
    logins = pd.read_parquet('logins.parquet5')
    logins.to_csv('logins.csv')

def reading_loginsset(type):
    """Lê o arquivo de logins com o qual vamos trabalhar

    Parameters:
    type (str): Indica se o arquivo lido é CSV ou Parquet

    Returns:
    pd.DataFrame: O DataFrame equivalente ao do nosso Dataset de Logins
    """
    #Lendo o Dataset de Logins
    if(type == 'csv'):
        logins = pd.read_csv('logins.csv')
        print(logins.head())
    else:
        logins = pd.read_parquet('logins.parquet5')
        print(logins.head())
    return logins

#Pre-Processamento

def transform_bool(logins):
    """Lê o arquivo de logins e transforma as linhas onde deveriam-se haver dados bool
    mas há floats em int para assim, facilitar-se as operações com eles. Ademais, deletam-se
    as linhas onde os valores são diferentes de 0 e 1, como manda a regra de bool.

    Parameters:
    logins (pd.DataFrame): Estado atual do DataFrame onde estamos trabalhando

    Returns:
    pd.DataFrame: DataFrame após conversões
    """
    # Transformando float em inteiro
    bool_columns = ['is_from_official_store', 'is_emulator', 'has_fake_location_app',
                    'has_fake_location_enabled', 'probable_root',
                    'never_permitted_location_on_account', 'ato']
    logins[bool_columns] = logins[bool_columns].astype(int)

    # Removendo linhas onde o valor é diferente de 0 e 1
    logins = logins[((logins['is_from_official_store'] == 1) | (logins['is_from_official_store'] == 0)) &
                    ((logins['is_emulator'] == 1) | (logins['is_emulator'] == 0)) &
                    ((logins['has_fake_location_app'] == 1) | (logins['has_fake_location_app'] == 0)) &
                    ((logins['has_fake_location_enabled'] == 1) | (logins['has_fake_location_enabled'] == 0)) &
                    ((logins['probable_root'] == 1) | (logins['probable_root'] == 0)) &
                    ((logins['never_permitted_location_on_account'] == 1) | (logins['never_permitted_location_on_account'] == 0)) &
                    ((logins['ato'] == 1) | (logins['ato'] == 0))]

    return logins

def dropping_nas(logins):
    """Retira todas as linhas onde ocorrem dados inexistentes onde nosso approach
    ideal é remover

    Parameters:
    logins (pd.DataFrame): Estado atual do DataFrame no qual trabalhamos

    Returns:
    pd.DataFrame: DataFrame após conversões
    """
    # Deletando todas as linhas onde as colunas de string estejam vazias
    logins2 = logins[logins['id'].notna() &
                logins['account_id'].notna() &
                logins['device_id'].notna() &
                logins['installation_id'].notna()]
    
    # Deletando todas as linhas com booleanos faltantes
    logins2 = logins2[logins2['is_from_official_store'].notna() &
                    logins2['is_emulator'].notna() &
                    logins2['has_fake_location_app'].notna() &
                    logins2['has_fake_location_enabled'].notna() &
                    logins2['probable_root'].notna() &
                    logins2['never_permitted_location_on_account'].notna() &
                    logins2['ato'].notna()]
    
    # Deletando todas as linhas sem timestamp
    logins2 = logins2[logins2['timestamp'].notna()]
    return logins2

def filling_with_mean(logins):
    """Coloca a média em todas as linhas onde ocorrem dados inexistentes
    onde nosso approach ideal é imputar algum valor

    Parameters:
    logins (pd.DataFrame): Estado atual do DataFrame no qual trabalhamos

    Returns:
    pd.DataFrame: DataFrame após conversões
    """
    # Tratando todas as linhas com inteiros ausentes
    logins['max_installations_on_related_devices'] = logins['max_installations_on_related_devices'].fillna(logins['max_installations_on_related_devices'].mean()) 
    logins['boot_count'] = logins['boot_count'].fillna(logins['boot_count'].mean())
    logins['wallpaper_count'] = logins['wallpaper_count'].fillna(logins['wallpaper_count'].mean())
    logins['n_accounts'] = logins['n_accounts'].fillna(logins['n_accounts'].mean())

    return logins

def create_new_columns(logins):
    """Cria novas colunas baseadas no nosso approach, são elas:
    weekday (uma data), boot_frequency_per_day (um float), wallpaper_per_accounts(float),
    external_download (bool), suspicious_location (bool)

    Parameters:
    logins (pd.DataFrame): Estado atual do DataFrame no qual trabalhamos

    Returns:
    pd.DataFrame: DataFrame após conversões
    """

    # 1) timestamp (int) -> weekday (string)
    day_divider = 86400000 # one day has 86400000 ms
    logins['weekday'] = (logins['timestamp']/day_divider).values.astype(dtype='datetime64[D]')
    logins['weekday'] = logins['weekday'].dt.day_name()
    # 2) Frequencia de reinicialização (float) = boot_count / device_age_ms
    logins['boot_frequency_per_day'] = (logins['boot_count'] / (logins['device_age_ms']/day_divider))
    
    # 3) Wallpaper por contas no dispositivo (float)
    logins['wallpaper_per_accounts'] = logins['wallpaper_count']/logins['n_accounts']

    # 4) Download Externo (bool) = root (true) + loja oficial (false)

    #gambiarra -> logins['external_download'] = logins.apply(lambda x: x['probable_root']*(1.0 - x['is_from_official_store']) , axis=1) 
    logins['external_download'] = logins['probable_root'] & (~logins['is_from_official_store']) #converting to int, its possible to make bool operations
    
    # 5) localização suspeita (bool) = has_fake_location_app  and has_fake_location_enabled and never_permitted_location_on_account

    logins['suspicious_location'] = logins['has_fake_location_app'] & logins['has_fake_location_enabled'] & logins['never_permitted_location_on_account']
    
    # Limpando erros que foram percebido num estágio posterior
    logins = logins[logins['boot_frequency_per_day'].notna()]
    logins = logins[logins['timestamp'].notna()]
    
    
    return logins

#Tudo abaixo dessa linha DEVE ser comentado após os commits, usar apenas para testes!!

# if __name__ == "__main__":
#     logins = reading_loginsset('csv')
#     #logins = reading_loginsset('parquet')
#     #print(logins.head())
#     logins = dropping_nas(logins)
#     logins = transform_bool(logins)
#     logins = create_new_columns(logins)
#     print(logins)