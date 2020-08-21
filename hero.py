import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import plotly.offline as py
color = sns.color_palette()
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
from plotly.offline import plot



info = pd.read_csv('C:\\Users\\user\\.spyder-py3\\Hero\\hero_info.csv')
powerful = pd.read_csv('C:\\Users\\user\\.spyder-py3\\Hero\\hero_power.csv')



#SEE IF NaN VALUES EXISTS
print(info.isna().any())
print(powerful.isna().any())

#ADDS UP ALL THE NULL VALUES
print(info.isnull().sum())
print(powerful.isnull().sum())

#REPLACE THE '-' WITH 'N/A'
info.replace(to_replace='-',value='N/A',inplace=True)
info['Publisher'].fillna('N/A',inplace=True)

#DROP THE 'UNNAMED COLUMN' IN HERO_INFO CSV
info.drop('Unnamed: 0',axis=1,inplace=True)

#REPLACES NEGATIVE VALUE OF HEIGHT AND WEIGHT WITH 'N/A'
info.replace(-99.0, np.nan, inplace=True)




print(info.shape)
print(info.info())
print(info.head())
print(info.dtypes)




#PUBLISHER BREAKDOWN
#PRINTS OUT THE NUMBER FOR EACH PUBLISHER
print(info['Publisher'].value_counts())

#PRINTS OUT THE TOTAL NUMBER OF PUBLISHER COUNT
print(info.Publisher.count())

#BAR GRAPH OF PUBLISHER BY COUNT
fig = plt.figure(figsize=(12,7))
fig.add_subplot(1,1,1)
sns.countplot(x='Publisher',data=info)
plt.xticks(rotation=70)
plt.tight_layout()
plt.show()

#PIE CHART OF MARVEL, DC AND OTHER PUBLISHERS
labels = 'Marvel', 'DC', 'Others'
sizes = [388, 215, 131]
explode = (0.1, 0, 0 )

fig1 , ax1 = plt.subplots()

ax1.pie(sizes,
        explode = explode,
        labels = labels,
        autopct = '%1.1f%%',
        shadow = True,
        startangle = 100)
ax1.axis ('equal')
plt.show()








#ALIGNMENT BREAKDOWN
print(info['Alignment'].value_counts())







#GENDER BREAKDOWN
#BOX PLOT OF HEIGHT & WEIGHT DISTRIBUTION BY GENDER
fig=plt.figure(figsize=(14,8))
fig.add_subplot(1,2,1)
sns.boxplot(x='Gender',y='Weight',data=info)
fig.add_subplot(1,2,2)
sns.boxplot(x='Gender',y='Height',data=info)
plt.show()


#BAR GRAPH OF GENDER COUNT FOR MARVEL HEROES
sns.countplot(info['Gender'][info['Publisher']=='Marvel Comics'])
plt.title('Gender count - Marvel Comics')

#BAR GRAPH OF GENDER COUNT FOR DC HEROES
sns.countplot(info['Gender'][info['Publisher']=='DC Comics'])
plt.title('Gender Count - DC comics')


#BAR GRAPH OF MALE/FEMALE SUPERHEROS
info_gender = info['Gender'].value_counts().head()
trace = go.Bar(
    y=info_gender.index[::-1],
    x=info_gender.values[::-1],
    orientation = 'h',
    marker=dict(
        color=info_gender.values[::-1]
    ),
)

layout = dict(
    title='Gender Distribution of Superheroes',
    )
data = [trace]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename="Superheroes")
plot(fig)
#%%

#POWER BREAKDOWN

#SEE IF NaN VALUES EXISTS
print(powerful.isna().any())

#THIS ONE ADDS UP ALL THE NULL VALUES
print(powerful.isnull().sum())

#TURNS TRUE/FALSE TO A "0" & "1" FORMATION
power=powerful*1





print(power.shape)
print(power.info())
print(power.head())
print(power.dtypes)





#ADDS ALL THE '1' IN THE ROW AND GIVES US A SUM FOR EACH CHARACTER
power.loc[:, 'no_of_powers'] = power.iloc[:, 1:].sum(axis=1)




#GETTING A TABLE OF NAME TO POWER NUMBER FROM MOST TO LEAST
most_powers=power[['hero_names','no_of_powers']]
most_powers=most_powers.sort_values('no_of_powers',ascending=False)

#GIVES THE TOP 10 HERO NAMES WITH MOST POWER
print(most_powers.head(10))



print(np.mean(most_powers.no_of_powers))
print(np.median(most_powers.no_of_powers))




#BAR GRAPH OF THE TOP 20 SUPERHERO POWERS. NUMBER OF POWERS BY NAME OF SUPERHERO
fig, ax = plt.subplots()

fig.set_size_inches(13.7, 10.27)

sns.set_context("paper", font_scale=1.5)
f=sns.barplot(x=most_powers["hero_names"].head(20), y=most_powers['no_of_powers'].head(20), data=most_powers)
f.set_xlabel("Name of Superhero",fontsize=18)
f.set_ylabel("No. of Superpowers",fontsize=18)
f.set_title('Top 20 Superheroes having highest no. powers')
for item in f.get_xticklabels():
    item.set_rotation(90)
    
    
    
    
    
#PRINTS HOW MANY CAN FLY
print(len(power[(power['Flight'] == 1)]))




