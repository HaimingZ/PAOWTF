import pandas as pd
import os

# original data
datapath = os.path.dirname(__file__)
df = pd.read_csv(datapath + '/data/patent-export-0602.csv')

# processed data

df_ = pd.DataFrame()
df_['Title'] = df['Title']
df_['Publication Number'] = df['Publication Number']
df_['Status'] = df['Status (Active/Expired)']
df_['Country'] = df['Publication Country']
df_['File Year'] = df['File Date'].str.slice(stop=4).astype(float)
df_['Grant Year'] = df['Grant Date'].str.slice(stop=4).astype(float)
df_['Priority Year'] = df['Priority Date'].str.slice(stop=4).astype(float)
df_['Publication Year'] = df['Publication Date'].str.slice(stop=4).astype(float)
df_['Expiration Year'] = df['Est. Expiration Date'].str.slice(stop=4).astype(float)
df_['Ultimate Parent'] = df['Ultimate Parent']
df_['Normalized Assignee'] = df['Normalized Assignee']


# assign labels
labels = ['origin', 'fixed', 'floating', 'gravity-based', 'jacket', 'monopile',
          'tripod', 'tripile', 'suction bucket', 'tlp', 'spar', 'semi-submersible']
for _ in labels:
    df_[_] = df['Project: Labels'].apply(
        lambda x: True if _ in str(x) else False)

# assign regions
df_['Region'] = ''
for i in range(df_.shape[0]):
    if df_.loc[i, 'Country'] in ['CN', 'HK', 'JP', 'TW', 'KR']:
        df_.loc[i, 'Region'] = 'East Asia'

    elif df_.loc[i, 'Country'] in ['US', 'CA', 'MX']:
        df_.loc[i, 'Region'] = 'North America'

    elif df_.loc[i, 'Country'] in ['EP', 'AL', 'AT', 'BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI',
                                   'FR', 'GB', 'GR', 'HR', 'HU', 'IE', 'IS', 'IT', 'LI', 'LT', 'LU', 'LV', 'MC',
                                   'MK', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SE', 'SI', 'SK', 'SM', 'TR']:
        df_.loc[i, 'Region'] = 'Europe'

    elif df_.loc[i, 'Country'] in ['EA', 'RU', 'BY', 'AM', 'TM']:
        df_.loc[i, 'Region'] = 'EAPO'

    elif df_.loc[i, 'Country'] in ['AU', 'NZ']:
        df_.loc[i, 'Region'] = 'Oceanic'

    elif df_.loc[i, 'Country'] in ['MY', 'SG', 'IN', 'PH']:
        df_.loc[i, 'Region'] = 'South and South-east Asia'

    elif df_.loc[i, 'Country'] in ['AR', 'BR', 'UY', 'CO', 'CL']:
        df_.loc[i, 'Region'] = 'South America'

    else:
        df_.loc[i, 'Region'] = 'Other'

df_.to_csv(datapath + '/data/data_processed.csv', index=False)
