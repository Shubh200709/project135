import pandas as pd
import csv
import matplotlib.pyplot as plp
import seaborn as sns
from sklearn.cluster import KMeans
import plotly.express as px

# data = pd.read_csv('project131output(2).csv')
# mass = data['Mass']
# gravity = data['Gravity(in m/s2)']
# radius = data['Radius']

# mass.sort_values()
# radius.sort_values()
# gravity.sort_values()

# plp.figure(figsize=(15,7))
# plp.scatter(x=mass, y=radius)
# plp.xlabel('Mass Of Planet')
# plp.ylabel('Radius Of Planet')
# plp.show()

# plp.figure(figsize=(15,7))
# plp.scatter(x=mass, y=gravity)
# plp.xlabel('Mass Of Planet')
# plp.ylabel('Gravity Of Planet')
# plp.show()

data = pd.read_csv('project131output(2).csv')
data2 = data.dropna(subset=['Mass', 'Radius'])

mass = data2['Mass']
radius = data2['Radius']

# x = []
x = data2.iloc[:,[3,4]].values
# for i, v in enumerate(mass):
#     temp2 = data2.get([radius[i],v])
#     x.append(temp2)
  
wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

# plp.figure(figsize=(10,5))
# sns.lineplot(x=range(1,11), y=wcss, marker='o', color='red')
# plp.xlabel('No, Of Clusters')
# plp.ylabel('WCSS')
# plp.title('Elbow Method')
# plp.show()

# scatter = px.scatter(x=mass, y=radius)
# scatter.show()

distance = data2['Distance']
gravity = data2['Gravity(in m/s2)']
name = data2['Name']
suitable_distance = []
suitable_gravity = []

for i in distance:
  if i<=100:
    suitable_distance.append(i)

for i in gravity:
  if i > 1500 and i < 3500:
    suitable_gravity.append(i)

headers = ['name','distance','mass','radius','gravity']
# new_data = pd.DataFrame(zip(name, suitable_distance, mass, radius, suitable_gravity),columns=headers)
# new_data.to_csv('class134(1).csv')

data3 = pd.read_csv('class134(1).csv')

name = data3['name']
mass = data3['mass']
dist = data3['distance']
radius = data3['radius']
gravity = data3['gravity']

plp.figure(figsize=(15,8))
sns.barplot(data3, x=name, y=dist)
plp.xlabel('Name Of Planet')
plp.ylabel('distance Of Planet')
plp.title('Name vs distance')
plp.show()

plp.figure(figsize=(15,8))
sns.barplot(data3, x=name, y=radius)
plp.xlabel('Name Of Planet')
plp.ylabel('radius Of Planet')
plp.title('Name vs radius')
plp.show()

plp.figure(figsize=(15,8))
sns.barplot(data3, x=name, y=gravity)
plp.xlabel('Name Of Planet')
plp.ylabel('gravity Of Planet')
plp.title('Name vs gravity')
plp.show()
