import pandas as pd
import matplotlib.pyplot as plt
from data import games

#filter only plays to new df 
plays = games[games['type']=='play']

#create new strike_outs df 
strike_outs = plays[plays['event'].str.contains('K')]

#create groupby object (panda series)
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

#reset index, converts strike_outs to df and names the new column 
#containing the no. of strike outs om the game
strike_outs= strike_outs.reset_index(name='strike_outs')
print(strike_outs.dtypes)

strike_outs = strike_outs.loc[:,['year','strike_outs']].apply(pd.to_numeric)
print(strike_outs.dtypes)

strike_outs.plot(x='year', y='strike_outs', kind='scatter').legend(['Strike Outs'])
plt.show()








