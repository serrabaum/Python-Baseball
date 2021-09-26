import pandas as pd
import matplotlib.pyplot as plt

from games import games

plays = games[games['type']=='play']

print(plays.dtypes)


