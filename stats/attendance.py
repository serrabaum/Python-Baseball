
import pandas as pd
import matplotlib.pyplot as plt

#import games df from data.py module
from data import games

#create new attendance df for filtered condition and selected collumns
attendance = games.loc[(games['type']=='info') & (games['multi2']=='attendance'),['year','multi3']]

#rename columns
attendance.columns = ['year', 'attendance']

#select all rows for attendance column and convert to numeric
attendance.loc[:,'attendance']=pd.to_numeric(attendance.loc[:,'attendance'])

#use df.plot
attendance.plot(x = 'year', y='attendance', figsize=(15,7), kind='bar')
plt.xlabel('year')
plt.ylabel('attendance')
#Add horiz line from attendance mean & specify keyword arguments
plt.axhline(attendance['attendance'].mean(),label='Mean Attendance',color='g',linestyle='dashed' )
#required to show plot
plt.show()



