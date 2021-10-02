import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games[games['type']=='play']
plays.columns =['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']


hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'),['inning','event'] ]

#converts inning from object type to numeric
hits.loc[:,'inning'] = pd.to_numeric(hits.loc[:,'inning'])

#dict for replacing values
replacements = {r'^S(.*)': 'single', r'^D(.*)': 'double', r'^T(.*)': 'triple', r'^HR(.*)': 'hr'}

#other attempts at replace
#hit_type = hits.replace(replacements, regex=True) #works probably replaces matching vals in any of the 2 cols
#hit_type = hits.replace(hits['event'],replacements, regex=True) #doesn't work, 2 cols but no replacement
#hit_type = hits.replace({"event": replacements}) #doesn't work, 2 cols but no replacement

#works returns single 'event' column with values replaced, not sure if this is what course requires?
hit_type = hits['event'].replace(replacements, regex=True) 


#creates new column from df hit_type (they have the same index)
hits = hits.assign(hit_type=hit_type)
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')


#convert 'hit_type' column to a category data type to save memory as only few values
hits['hit_type'] = pd.Categorical(hits['hit_type'],['single', 'double', 'triple', 'hr']) #WORKS
#hits.loc[:,'hit_type'] = pd.Categorical(hits.loc[:,'hit_type'],['single', 'double', 'triple', 'hr']) #WORKS with .loc








