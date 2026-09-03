import numpy as np
import pandas as pd


def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        flag=2
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

    if flag == 1:
        # Z= temp_df.groupby(['Year', 'region', 'Games', 'City']).sum()[['Gold', 'Silver', 'Bronze']].reset_index()
        # Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']

          X= temp_df.groupby(['Year', 'region', 'Games', 'City']).sum()[['Gold', 'Silver', 'Bronze']].sort_values(
            by='Year', ascending=True).reset_index()
          X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']

          Y=temp_df.groupby('region')[['Gold','Silver','Bronze']].sum()
          Y['region']=country
          Y['Year']='ALL'
          Y['Games']='ALL'
          Y['City']='ALL'
          Y['Total'] = X['Total'].sum()
          Z=pd.concat([X,Y],axis=0,ignore_index=True)
          Z.index=Z.index+1
          Z.index.name='S.r'


    elif flag==2 :
        X = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
        X = temp_df[
            ['region','Games', 'City', 'Sport', 'Gold', 'Silver', 'Bronze']].groupby(
            [ 'region','Games','City','Sport' ])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
        X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']
        X=X.sort_values(by='Total',ascending=False).reset_index(drop=True)
        X.index=X.index+1
        X.index.name='Rank'
        # Overall total medals
        Y = X.groupby(
            ['region', 'Games', 'City']
        )[
            ['Gold', 'Silver', 'Bronze']
        ].sum().reset_index()

        Y['Total'] = Y['Gold'] + Y['Silver'] + Y['Bronze']
        Y['Sport']='ALL'

        Y = Y.sort_values(by='Total', ascending=False)
        Y.index = Y.index + 1


        Z=pd.concat([X,Y],axis=0,ignore_index=True)
        Z.index=Z.index+1
        Z.rename(index={32: 'Total'}, inplace=True)
        Z.index.name='Rank'




    else:

        Z = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Gold',
                                                                                      ascending=False).reset_index()
        Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
        Z.index=Z.index+1

    return Z

def over_over(df,year,country):

   if year != 'Overall' and country != 'Overall':
        medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
        temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]

        X = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Gold',
                                                                                  ascending=False).reset_index()
        X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']
        X.index=X.index+1
        X.index.name='Total'

        return X




def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                                ascending=False).reset_index()

    medal_tally['total_medals'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']

    return medal_tally


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    Country = np.unique(df['region'].dropna().values).tolist()
    Country.sort()
    Country.insert(0, 'Overall')
    return years, Country


def data_over_time(df):
    nations_over_time = pd.DataFrame(df[['region','Year']].drop_duplicates().dropna()['Year'].value_counts()).reset_index().rename(columns={'count':'No. of countries participated'}).sort_values(by='Year')

    # events_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values(
    #     by='Year').reset_index(drop=True).rename(columns={'count': 'No. of events'})

    # nations_over_time.index = nations_over_time .index.values + 1
    return nations_over_time


def events_over_time(df):
    # nations_over_time = pd.DataFrame(df.drop_duplicates(['Year', col])['Year'].value_counts()).rename(
    #     columns={'count': 'No. of Countries Participated'}).sort_values(by='Year').reset_index()

    events_over_time = df.drop_duplicates(['Year', 'Event'])['Year'].value_counts().reset_index().sort_values(
        by='Year').reset_index(drop=True).rename(columns={'count': 'No. of events'})

    # nations_over_time.index = nations_over_time .index.values + 1
    return events_over_time


def athletes_over_time(df):
    athletes_over_time = df[['Name', 'Year']].drop_duplicates().groupby('Year').count().rename(
        columns={'Name': 'No. of Athletes'}).reset_index().sort_values(by='Year')

    return athletes_over_time


def most_successful(df, sport):
    temp_df = df.dropna(subset=['Medal'])
    if sport != 'Overall':
        X = pd.DataFrame(
            temp_df[temp_df['Sport'] == sport][['Name', 'Sport', 'region', 'Gold', 'Silver', 'Bronze']].groupby(
                ['Name', 'Sport', 'region'])[['Gold', 'Silver', 'Bronze']].sum()).sort_values(by='Gold',
                                                                                              ascending=False)

        X['Total_Medals'] = X['Gold'] + X['Silver'] + X['Bronze']
        X = X.sort_values(by='Total_Medals', ascending=False).reset_index().head(10)
        X.index = (X.index) + 1
        X.index.name = 'Rank'

    # return X
    else:
        X = temp_df[['Name', 'Sport', 'region', 'Gold', 'Silver', 'Bronze']].groupby(['Name', 'Sport', 'region'])[
            ['Gold', 'Silver', 'Bronze']].sum()
        X['Total_Medals'] = X['Gold'] + X['Silver'] + X['Bronze']
        X = X.sort_values(by='Total_Medals', ascending=False).reset_index().head(15)
        X.index = (X.index) + 1
        X.index.name = 'Rank'
    return X


# Most successfull counties in a sport

def most_successful_country(df, sport):
    if sport != 'Overall':
           medal1 = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

           Z = medal1[medal1['Sport'] == sport].groupby(['Sport', 'region'])[['Gold', 'Silver', 'Bronze']].sum().sort_values(by='Gold', ascending=False)
           Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
           Z = Z.sort_values(by='Total', ascending=False).head(10)

    else:
           medal1 = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

           Z = medal1.groupby(['Sport', 'region'])[['Gold', 'Silver', 'Bronze']].sum()

           Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']



           Z = Z.loc[Z.groupby('Sport')['Total'].idxmax()]



           Z=pd.DataFrame(Z).sort_values(by='Total', ascending=False)
           Z = Z.sort_values('Sport').reset_index()
           Z.index=(Z.index)+1
           Z.index.name='S.r'
           # print('Leading Countries in every sport')
    return Z


def yearwise_medal_tally(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index().rename(columns={'Medal': 'No. of Medals'})
    return final_df


def country_event_heatmap(df, country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0).astype('int')
    return pt


def most_successful_countrywise(df, country):
    temp_df = df.dropna(subset=['Medal'])

    X = pd.DataFrame(
        temp_df[temp_df['region'] == country][['Name', 'Sport', 'region', 'Gold', 'Silver', 'Bronze']].groupby(
            ['Name', 'Sport', 'region'])[['Gold', 'Silver', 'Bronze']].sum()).sort_values(by='Gold', ascending=False)

    X['Total_Medals'] = X['Gold'] + X['Silver'] + X['Bronze']
    X = X.sort_values(by='Total_Medals', ascending=False).reset_index().head(20)
    X.index = (X.index) + 1
    X.index.name = 'Rank'
    return X


def craze_of_sport(df, country):
    medal1 = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    Z= medal1[medal1['region'] == country].groupby(['Sport'])[['Gold', 'Silver', 'Bronze']].sum().sort_values(
        by='Gold', ascending=False).head(30)
    Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
    Z = Z.sort_values(by='Total', ascending=False).head(20)
    A=Z[Z['Total']!=0].reset_index().head(10)
    A.index = (A.index) + 1
    A.index.name = 'Rank'
    return A


def weight_v_height(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region']).copy()
    athlete_df['Medal'] = athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
    else:
        temp_df = athlete_df
    return temp_df

########It is producing wrong results in graph
def men_vs_women(df):
    Z = df.drop_duplicates(subset=['ID', 'Year', 'region']).groupby(['Year', 'Sex']).count()[
        'ID'].reset_index().pivot_table(index='Year', columns='Sex', values='ID').reset_index().fillna(0).astype(
        'int')
    Z['total'] = Z['F'] + Z['M']
    return Z



def name_event_wise(df, name):
    df['Total'] = df['Gold'] + df['Silver'] + df['Bronze']
    idx = df[df['Total'] != 0].index
    df = df.loc[idx]
    df.drop(columns=['Total', 'Gold', 'Silver', 'Bronze'], inplace=True)
    z = df[df['Name'] == name][
        ['Name', 'region', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal']].reset_index(drop=True).dropna()
    return z


def name_year_wise(df, name):
    Z = df.groupby(['Name', 'Games', 'Year', 'City', 'Sport'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
    Z = Z[Z['Name'] == name].reset_index(drop=True)
    return Z


def overall_name_wise(df, name):
    p = df[df['Name'] == name].groupby(['Name'])[['Gold', 'Silver', 'Bronze']].sum()
    p['Total'] = p['Gold'] + p['Silver'] + p['Bronze']
    return p


# select year and event and gate top3 medalist:-
def choose(df, year, event):
    df.dropna(subset=['Medal'], inplace=True)
    Z = df[(df['Year'] == year) & (df['Event'].str.strip() == event)].drop(
        columns=['notes', 'Bronze', 'Gold', 'Silver', 'Age', 'Height', 'Weight', 'NOC', 'ID', 'Team']).reset_index(
        drop=True)
    medal_order = {'Gold': 1, 'Silver': 2, 'Bronze': 3}

    Z['Medal_Order'] = Z['Medal'].map(medal_order)

    Z= Z.sort_values('Medal_Order').drop(columns=['Medal_Order','Total']).reset_index(drop=True)
    return Z

#CODE FRO YEAR WISE ANALYSIS

#top 10 athlete of a year
def top10_year(df,year,sex):
    if sex=='M' or sex=='F':
           Z = df[(df['Year'] == year)&(df['Sex']== sex)].groupby(['Name', 'Sex', 'Games', 'Year'])[
                ['Gold', 'Silver', 'Bronze']].sum().reset_index()
           Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
           Z=Z.sort_values(by='Total', ascending=False).head(10).reset_index(drop=True)


    else:
        Z = df[(df['Year'] == year) ].groupby(['Name', 'Sex', 'Games', 'Year'])[
            ['Gold', 'Silver', 'Bronze']].sum().reset_index()
        Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
        Z = Z.sort_values(by='Total', ascending=False).head(10).reset_index(drop=True)

    return Z



def top10_year_sport(df,year,sport,sex):

    if sex=='M' or sex=='F':

          Z = df[(df['Year'] == year) & (df['Sport'] == sport)&(df['Sex']==sex)].groupby(['Name', 'Sex', 'Games', 'Year', 'Sport'])[
              ['Gold', 'Silver', 'Bronze']].sum().reset_index()
          Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
          Z=Z.sort_values(by='Total', ascending=False).head(10).reset_index(drop=True)
    else:
        Z = df[(df['Year'] == year) & (df['Sport'] == sport)].groupby(['Name', 'Sex', 'Games', 'Year', 'Sport'])[
            ['Gold', 'Silver', 'Bronze']].sum().reset_index()
        Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
        Z=Z.sort_values(by='Total', ascending=False).head(10).reset_index(drop=True)
    return Z

# for country-wise analysis
def top10_country_sport(df,region,sport):
      Z = df[(df['region'] == region) & (df['Sport'] == sport)].groupby(['Name', 'Sex', 'Sport'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
      Z['Total'] = Z['Gold'] + Z['Silver'] + Z['Bronze']
      Z=Z.sort_values(by='Total', ascending=False).head(10).reset_index(drop=True)
      return Z


def parti(df, region):
    X = df[df['region'] == region].drop_duplicates(subset=['Year', 'Name', 'Sport']).groupby(['Year', 'Sex']).count()
    Z = X.pivot_table(index='Year', columns='Sex', values='Name').fillna(0).astype('int')
    Z['Total'] = Z['F'] + Z['M']
    Z = Z.reset_index()
    return Z

def men_medal_women(df,region):
      medal_df=df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
      Z=medal_df[medal_df['region']==region].groupby(['region','Sex','Year'])[['Gold','Silver','Bronze']].sum()
      Z['Total_medals']=Z['Gold']+Z['Silver']+Z['Bronze']
      Z=Z.pivot_table(index='Year',columns='Sex',values='Total_medals').fillna(0).astype('int').reset_index()
      Z['total']=Z['F']+Z['M']
      return Z
#___________________ compare two athletes _____________________________________________________________

# def compare(df, n1, n2):
#     a = df[df['Name'] == n1].groupby(['Name', 'region', 'Sport'])[['Gold', 'Bronze', 'Silver']].sum().reset_index()
#     a['Total_medals'] = a['Gold'] + a['Silver'] + a['Bronze']
#
#     a['First_time_participated'] = df[df['Name'] == n1]['Year'].min()
#     a['won_first_medal_in'] = df[df['Name'] == n1].dropna(subset=['Medal'])['Year'].min()
#
#     b = df[df['Name'] == n2].groupby(['Name', 'region', 'Sport'])[['Gold', 'Bronze', 'Silver']].sum().reset_index()
#     b['Total_medals'] = b['Gold'] + b['Silver'] + b['Bronze']
#     b['First_time_participated'] = df[df['Name'] == n2]['Year'].min()
#     b['won_first_medal_in'] = df[df['Name'] == n2].dropna(subset=['Medal'])['Year'].min()
#
#     # c=df[df['Name']==n3].groupby(['Name','region','Sport'])[['Gold','Bronze','Silver']].sum()
#     # c['Total_medals']=c['Gold']+c['Silver']+c['Bronze']
#     # c['First_time_participated']=df[df['Name']==n3]['Year'].min()
#     # c['won_first_medal_in'] =df[df['Name']==n3].dropna(subset=['Medal'])['Year'].min()
#     return pd.concat([a, b], axis=0)



