# if year == 'Overall' and country == 'Overall':
    #     temp_df = medal_df
    # elif year == 'Overall' and country != 'Overall':
    #     flag = 1
    #     temp_df = medal_df[medal_df['region'] == country]
    # elif year != 'Overall' and country == 'Overall':
    #     temp_df = medal_df[medal_df['Year'] == int(year)]
    # elif year != 'Overall' and country != 'Overall':
    #     temp_df = medal_df[(medal_df['Year'] == int(year)) & (medal_df['region'] == country)]
    #
    # if flag == 1:
    #     X = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Year',
    #                                                                                 ascending=True).reset_index()
    #     X['region'] = country
    #     X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']
    #     Y = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by='Gold',
    #                                                                                   ascending=False).reset_index()
    #     Y['Year'] = 'ALL'
    #     Y['Total'] = X['Total'].sum()
    #     Z = pd.concat([X, Y], axis=0, ignore_index=True)
    # else:
    #     # X = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    #     X = temp_df[
    #         ['Sport', 'region', 'City', 'Games', 'Gold', 'Silver', 'Bronze']].groupby(
    #         [ 'region' ])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    #     X['Total'] = X['Gold'] + X['Silver'] + X['Bronze']
    #     # X=X.sort_values(by='Total',ascending=False)
    #     Y = temp_df[(temp_df['Year'] == year) & (temp_df['region'] == country)][
    #         ['Sport', 'region', 'City', 'Games', 'Gold', 'Silver', 'Bronze']].groupby(['region', 'City', 'Games', ])[
    #         ['Gold', 'Silver', 'Bronze']].sum().reset_index()
    #     Y['Total'] = Y['Gold'] + Y['Silver'] + Y['Bronze']
    #     Y['Sport'] = 'ALL'
    #     # # Y['Games']=X['Games']
    #     # # Y['City']=X['City']
    #     Z = pd.concat([Y, X], axis=0, ignore_index=True)
    #     # return Z
    #
    # return Z