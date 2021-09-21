import os
import glob

import pandas as pd

#Get list of CSV data files
game_files=glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))

#sort list in place
game_files.sort()

#list of column names for use in pd.read_csv
game_columns=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6','event']

#Empty list to hold 
game_frames = []

for game_file in game_files:
    game_frame=pd.read_csv(game_file, names=game_columns)
    game_frames.append(game_frame)

#Concat all df in game_frames (list of df's)
games=pd.concat(game_frames)

#retrieves values based on condition
games.loc[games['multi5']=='??']

#create boolean df for conditional update of games df - not used in below update
    #mytest = games.loc[games['multi5']=='??']

#updating values in 'multi5' column
games.loc[(games.multi5 == '??'),'multi5']=''

#create new df identifiers with a new column extracted from 'multi2' using regex
identifiers = games['multi2'].str.extract((r'(.LS(\d{4})\d{5})'))

#use fillna to populate NaN values using ffill method
identifiers = identifiers.fillna(method='ffill')

#rename columns
identifiers.columns = ['game_id','year']

#concat games and identifiers on column basis (axis = 1)
games = pd.concat([games, identifiers],axis=1,sort=False)

games=games.fillna('')

#convert 'type' column to a category data type to save memory
#as only few3values
games.loc[:,'type'] = pd.Categorical(games.loc[:,'type'])

#Show number of rows with each value in 'type' column
games['type'].value_counts()

#shows df column data types
games.dtypes

#print df to check
print(games.head())