import pandas as pd

df = pd.read_csv('data/zestawienie.csv')
df.drop_duplicates(subset='Nazwa instytucji', keep=False, inplace=True)
df.drop_duplicates(subset='Adres - miasto', keep=False, inplace=True)


def find_all_by_city(city_name):
    return df.loc[df['Adres - miasto'] == city_name]


def find_by_uni_name(uni_name):
    return df.loc[df['Nazwa instytucji'] == uni_name]


def find_all_by_city_and_subject(city_name, subject):
    return df.loc[(df['Adres - miasto'] == city_name) and (subject in df['Subjects'])]
