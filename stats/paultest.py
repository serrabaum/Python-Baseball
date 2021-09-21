import pandas as pd
import numpy as np

df = pd.DataFrame({'Date' : ['11/8/2011', '11/9/2011', '11/10/2011','11/11/2011', '11/12/2011'],
                'Event' : ['Dance', 'Painting', 'Dance', 'Dance', 'Painting']})

df

df.loc[(df.Event == 'Hip-Hop'),'Event']='Dance'