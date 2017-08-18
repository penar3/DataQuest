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