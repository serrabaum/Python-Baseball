import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games[games['type']=='play']
plays.columns =['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

#print(plays.columns)

hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'),['inning','event'] ]


#hits['inning'] = hits['inning'].apply(pd.to_numeric) WORKS
#hits['inning'] = pd.to_numeric(hits['inning']) WORKS

hits = hits.loc[:,['inning']].apply(pd.to_numeric) #WORKS



