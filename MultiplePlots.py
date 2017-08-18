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