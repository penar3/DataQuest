#Ruben Pena
#Data Analysis with Pandas: Intermediate Course
	#Getting Started and Computation with NumPy
#8/17/2017

# Intro to Numpy
import numpy as np
vector = np.array([10,20,30])
matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])

vector_shape = vector.shape
print(vector_shape)
matrix_shape = matrix.shape
print(matrix_shape)

#--Reading in datasets with Numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter = ",")
type(world_alcohol)
print(world_alcohol)

#Data Types
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)

#Specify  the data type param
world_alcohol = np.genfromtxt("world_alcohol.csv", delimiter="," , skip_header = 1, dtype = "U75")
print(world_alcohol)

#Indexing arrays
uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

#Slicing Arrays
countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]

#Slicing One Dimension
first_two_columns = world_alcohol[:,:2]
first_ten_years = world_alcohol[:10,0]
first_ten_rows = world_alcohol[:10,:]

#Slicing Arrays
first_twenty_regions = world_alcohol[:20,1:3]

#Array Comparisons
countries_canada = (world_alcohol[:,2] == "Canada")
years_1984 = (world_alcohol[:,0] == "1984")

#Selecting Elements in arrays
country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria,:]

#Comparisons with Conditions
is_algeria_and_1986 = ((world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria"))
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

#Replacing values
is_1986 = (world_alcohol == "1986")
is_wine = (world_alcohol == "Wine")
replace_1986 = world_alcohol[is_1986] = "2014"
replace_wine = world_alcohol[is_wine] = "Grog"

world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'
world_alcohol[:,3][world_alcohol[:,3] == 'Wine'] = 'Grog'

#Replacing empty strings
is_value_empty = (world_alcohol[:,4] == "")
world_alcohol[is_value_empty,4] = "0"

#Convert Data Types
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

#Computing
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

#Bringing it all togetgher
	# Total Annual Alcohol Consumption
is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

	#Consumption for each Country
totals = {}
is_year = world_alcohol[:,0] == "1989"
year = world_alcohol[is_year,:]

for country in countries:
    is_country = year[:,2] == country
    country_consumption = year[is_country,:]
    alcohol_column = country_consumption[:,4]
    is_mv = alcohol_column == ""
    alcohol_column[is_mv] = "0"
    alcohol_column = alcohol_column.astype(float)
    totals[country] = alcohol_column.sum()

	#Country that drinks the most!
highest_value = 0
highest_key = None

for x in countries:
    consumed = totals[x]
    if consumed > highest_value:
        highest_value = consumed
        highest_key = x
