## Data frame as a dictionary


import pandas as pd
songs={'Album':["abc","fgh","xyz","uiop"],
       'Year':["122","456","545","5465"],
       'length':["21","45","54","5"]}
#songs is a dictionary made with 3 keys and values as list

## songs_frame is the data frame name here

songs_frame=pd.DataFrame(songs)
print(songs_frame)
#new_frame is the new frame made from the songs_frame~

new_frame=songs_frame[['Album','Year']]

print(new_frame)
