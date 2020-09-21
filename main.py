import pandas as pd
import plotly.express as px

data = pd.read_csv('C:/Users/선동환/Desktop/python/dataset/season-1819_csv.csv')
Everton_home = data[data.HomeTeam == "Everton"]
Everton_away = data[data.AwayTeam == "Everton"]
print("Everton_home:{0}\n Everton away:{1} ".format(Everton_home, Everton_away))
Everton = pd.concat([Everton_home, Everton_away])
print(Everton)
fig = px.scatter(Everton, x='FTAG', y='FTHG', size='HS')
fig.show()