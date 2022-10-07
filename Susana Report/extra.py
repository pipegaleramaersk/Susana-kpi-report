# Filter to teams that are more than 5 people 
teams_more_five = processed_data.groupby(['Organisational Unit Title'])['Headcount'].sum() > 5
teams_more_five = pd.DataFrame(teams_more_five).reset_index()
teams_more_five = teams_more_five.rename({'Headcount': 'More_than_5'})

teams_more_five[teams_more_five['Headcount'] == False].shape[0]