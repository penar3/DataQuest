#Ruben Pena
#Data Analysis with Pandas: Intermediate Course
	#Line Charts
#8/17/2017

#Introduction to the Data
import pandas as pd
unrate = pd.read_csv("unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
unrate.head(12)

#Introduction to matplotlib
Iimport matplotlib.pyplot as plt
plt.plot()
plt.show()

#Adding Data
plt.plot(unrate[:12]["DATE"],unrate[:12]["VALUE"])
plt.show()

#Axis Ticks
plt.plot(unrate[:12]["DATE"],unrate[:12]["VALUE"])
plt.xticks(rotation = 90)
plt.show()

#Axis Labels and Title
plt.plot(unrate[:12]["DATE"],unrate[:12]["VALUE"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")


#Ruben Pena
#Data Analysis with Pandas: Intermediate Course
	#Multiple Plots
#8/17/2017

#matplotlib Class
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
plt.show()

#Adding Data
fig = plt.figure()
first = fig.add_subplot(2,1,1)
second = fig.add_subplot(2,1,2)
first.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
second.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
plt.show()

#Formatting and Spacing
fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()

#Comparing Across More Years
fig = plt.figure(figsize=(12,12))
yr1948 = fig.add_subplot(5,1,1)
yr1949 = fig.add_subplot(5,1,2)
yr1950 = fig.add_subplot(5,1,3)
yr1951 = fig.add_subplot(5,1,4)
yr1952 = fig.add_subplot(5,1,5)
yr1948.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
#yr1948.set_title("Unemployment Rate, 1948")
yr1949.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
#yr1949.set_title("Unemployment Rate, 1949")
yr1950.plot(unrate[24:36]['DATE'], unrate[24:36]['VALUE'])
#yr1950.set_title("Unemployment Rate, 1950")
yr1951.plot(unrate[36:48]['DATE'], unrate[36:48]['VALUE'])
#yr1951.set_title("Unemployment Rate, 1951")
yr1952.plot(unrate[48:60]['DATE'], unrate[48:60]['VALUE'])
#yr1952.set_title("Unemployment Rate, 1952")
plt.show()

#Overlaying Line Charts
unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c = "red")
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c= "blue")
plt.show

#Adding More Lines
fig = plt.figure(figsize=(10,6))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'],c = "red")
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'],c = "blue")
plt.plot(unrate[24:36]['MONTH'], unrate[24:36]['VALUE'],c = "green")
plt.plot(unrate[36:48]['MONTH'], unrate[36:48]['VALUE'],c = "orange")
plt.plot(unrate[48:60]['MONTH'], unrate[48:60]['VALUE'],c = "black")
plt.show()

#Adding a Legend
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label = str(1948 + i))
plt.legend(loc="upper left")
plt.show()

#Final Tweaks
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='upper left')
plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.show()

#Ruben Pena
#Data Analysis with Pandas: Intermediate Course
	#Bar Plots and Scatter Plots
#8/17/2017

#Introduction to the Data
import pandas as pd
reviews = pd.read_csv("fandango_scores.csv")
columns = ["FILM","RT_user_norm","Metacritic_user_nom","IMDB_norm","Fandango_Ratingvalue","Fandango_Stars"]
norm_reviews = reviews[columns]
norm_reviews.head(1)

#Creating Bars
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
plt.show()

#Aligning Axis Ticks and Labels
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)
plt.xlabel("Rating Source")
plt.ylabel("Average Rating")
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

#Horizontal Bar Plots
import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
plt.ylabel("Rating Source")
plt.xlabel("Average Rating")
plt.title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

#Scatters
fig, ax = plt.subplots()
ax.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")
plt.show()

#Switching Axes (Inverse)
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax2.scatter(norm_reviews["RT_user_norm"],norm_reviews["Fandango_Ratingvalue"])
ax2.set_xlabel("Rotten Tomatoes")
ax2.set_ylabel("Fandango")
plt.show()

#Benchmarking Correlation
import matplotlib.pyplot as plt
#create a figure with 3 rows, 1 col, Axes in postitions 1-3
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

#1 Fandango v Rotten Tomatoes
ax1.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["RT_user_norm"])
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
#2 Fandango v Metacritc
ax2.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["Metacritic_user_nom"])
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
#3Fandango v IMDb
ax3.scatter(norm_reviews["Fandango_Ratingvalue"],norm_reviews["IMDB_norm"])
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)
plt.show()

#Ruben Pena
#Data Analysis with Pandas: Intermediate Course
	#Histograms and Box Plots
#8/17/2017

#Introduction to the Data
import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])

#Frequency Distributions
fandango_distribution=(norm_reviews['Fandango_Ratingvalue'].value_counts()).sort_index()
imdb_distribution=(norm_reviews['IMDB_norm'].value_counts()).sort_index()
print(fandango_distribution)
print(imdb_distribution)

#Histograms in matplotlib
fig, ax = plt.subplots()
ax.hist(norm_reviews["Fandango_Ratingvalue"], range = (0,5))
plt.show()

#Comparing Histograms
fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews["Fandango_Ratingvalue"], bins =20, range=(0,5))
ax1.set_title("Distribution of Fandango Ratings")
ax1.set_ylim(0,50)
ax1.set_ylabel("Frequency")

ax2.hist(norm_reviews["RT_user_norm"], bins=20, range=(0,5))
ax2.set_title("Distribution of Rotten Tomatoes Ratings")
ax2.set_ylim(0,50)
ax2.set_ylabel("Frequency")

ax3.hist(norm_reviews["Metacritic_user_nom"],bins=20,range=(0,5))
ax3.set_title("Distribution of Metacritic Ratings")
ax3.set_ylim(0,50)
ax3.set_ylabel("Frequency")

ax4.hist(norm_reviews["IMDB_norm"],bins=20,range=(0,5))
ax4.set_title("Distribution of IMDB Ratings")
ax4.set_ylim(0,50)
ax4.set_ylabel("Frequency")

plt.show()

#Box Plots
fig, ax = plt.subplots()
ax.boxplot(norm_reviews['RT_user_norm'])
ax.set_ylim(0,5)
ax.set_xticklabels(["Rotten Tomatoes"])
plt.show()

#Multiple Box Plots
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols,rotation=90)
ax.set_ylim(0,5)
plt.show()




