
import pandas as pd

# df = pd.read_csv('athlete_events.csv')
# region_df=pd.read_csv('noc_regions.csv')

# print(df.columns.tolist())


def preprocess(df,region_df):
    # global df,region_df
    df=df[df['Season']=='Summer']
    #merging
    df=df.merge(region_df,on='NOC',how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    # One hot Encoding
    df=pd.concat([df,pd.get_dummies(df['Medal'],dtype=int)],axis=1)
    # df=df[(df['Year']!=1906)&(df['Sport']!='Art Competitions')]
    df = df[(df['Year'] != 1906) ]

    return df
# print(pd.concat([df,pd.get_dummies(df['Medal'],dtype=int)],axis=1))



