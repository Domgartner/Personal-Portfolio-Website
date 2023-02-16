#233 Final Projet.py
#DOMINIC GARTNER (30154504), RACHEL GIANG (30143749), ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and csv files.
#Imported modules include numpy, matplotlib.pyplot, and pandas

import numpy as np                
import matplotlib.pyplot as plt     #Imports numpy, pandas, and matplotlib.pyplot
import pandas as pd

class Endangered:
    '''
    A class used to create an instance representing endangered species in country

    Attributes:
    country(str): a string that represents a countries name

    Methods:
    print_data_endanger: Calculates and prints data of the country instance
    '''

    def __init__(self, country):
        self.country = country

    def print_data_endanger(self):
        '''
        A function that calculates and prints data from an imported data file 'Threatened_Species.csv'. The printed data is unique
        for each country instance

        Parameters:
        none

        Returns:
        none
        '''
        threatened_data = pd.read_csv('Threatened_Species.csv', delimiter = ',') 
        threatened_data = np.array(threatened_data).tolist()    #Use pandas to read in 'Country_Data.csv' file and convert the data to a list using numpy and .tolist() function

        for i in range(len(threatened_data)):     #Iterates through each country in the range and length of threatened_data and assigns the index of the entered country in threatened_data to index
            if self.country in threatened_data[i]:
                index_threat = i

        threatened_plants = threatened_data[index_threat][1]   #Assigns threatened_plants with the value of endangered plant species for the country instance
        print(f'\tNumber of endangered plant species in {self.country}: {threatened_plants}')          #Outputs number of endangered plant species
        threatened_fish = threatened_data[index_threat][2]     #Assigns threatened_fish with the value of endangered fish species for the country instance
        print(f'\tNumber of endangered fish species in {self.country}: {threatened_fish}')            #Outputs number of endangered fish species
        threatened_birds = threatened_data[index_threat][3]    #Assigns threatened_birds with the value of endangered bird species for the country instance
        print(f'\tNumber of endangered bird species in {self.country}: {threatened_birds}')          #Outputs number of endangered bird species
        threatened_mammals = threatened_data[index_threat][4]  #Assigns threatened_mammals with the value of endangered mammal species for the country instance
        print(f'\tNumber of endangered mammal species in {self.country}: {threatened_mammals}')     #Outputs number of endangered mammal species
        total_endanger = (threatened_birds + threatened_fish + threatened_mammals + threatened_plants)  #Adds all the endangered species to calculate the total number of endangered species in the country instance
        print(f'\t\tTotal endangered species in {self.country}: {total_endanger}\n')        #Outputs total number of endangered species

        threatened_data = pd.read_csv('Threatened_Species.csv', delimiter = ',')
        threatened_data = np.array(threatened_data)                          #Redefines threatened_data as an array, and not a list
        country_data = pd.read_csv('Country_Data.csv', delimiter = ',')  
        country_data = np.array(country_data)               #Reads country_data in using pandas and converts to array with numpy
        
        plant = threatened_data[:,1]    #Defines plant as the second column of threatened_data
        fish = threatened_data[:,2]     #Defines fish as the third column of threatened_data
        bird = threatened_data[:,3]     #Defines bird as the fourth column of threatened_data
        mammal = threatened_data[:,4]   #Defines mammal as the fifth column of threatened_data
    
        total = []
        index_country = 0
        for r in range(len(threatened_data)):           #iterates through threatened_data and adds each list of endangered plants, fish, mammals, and birds. Appends value to total
            added = fish[index_country] + plant[index_country] + mammal[index_country] + bird[index_country]
            total.append(added)
            added = 0
            index_country += 1
            
        total = sorted(total, reverse = True)       #Sorts total from largest to smallest

        count = 1
        for q in range(len(total)):
            if total_endanger == total[0]:       #Iterates through total. If total endangered species for country instance equals the first total endangered in total, break loop. If not, increase count by 1 until the total_endagered value equals total at index
                break
            if total_endanger == total[q]:
                break
            else:
                count += 1

        if count == 1:      #If count is 1, country has most endangered species
            print(f'\t{self.country} has the most endangered species in the world!\n')
        else:               #If count is not 1, print the following
            print(f'\t{self.country} is ranked #{count} for most endangered species in the world!\n')
        

def plot_endanger(country):
    '''
    Plots data of threatened species instance using matplotlib.pyplot

    Arguments:
    none

    Returns:
    none
    '''
    threatened_data = pd.read_csv('Threatened_Species.csv', delimiter = ',')  
    threatened_data = np.array(threatened_data)     #Use pandas to read in 'Threatened_Species.csv' file and convert the data to an array using numpy

    for i in range(len(threatened_data)):
        if country in threatened_data[i]:    #Iterates through each country in the range and length of threatened_data and assigns the index of the entered country in threatened_data to index
            index = i

    threatened_plants = threatened_data[index][1]   #Assigns threatened_plants with the value of endangered plant species for the country instance
    threatened_fish = threatened_data[index][2]     #Assigns threatened_fish with the value of endangered fish species for the country instance
    threatened_birds = threatened_data[index][3]    #Assigns threatened_birds with the value of endangered bird species for the country instance
    threatened_mammals = threatened_data[index][4]  #Assigns threatened_mammals with the value of endangered mammal species for the country instance

    plt.title(f'Endangered Species in {country}')  #Declares plot title 
    x = ['Plants', 'Fish', 'Birds', 'Mammals']      #Declares x-axis values
    x_space = list(range(len(x)))            #creates a list of the range and length of x-axis values in order to space x-axis values evenly on the x-axis
    plt.xlabel('Organism')         #Sets x-axis label
    plt.ylabel('Number of Threatened Species')     #Sets y-axis label
    plt.bar('Plants', threatened_plants, bottom = 0, color = 'green', width = 0.6)  #Creates first bar for the plants, bar colour is green
    plt.bar('Fish', threatened_fish, bottom = 0, color = 'yellow', width = 0.6)     #Creates second bar for the fish, bar colour is green
    plt.bar('Birds', threatened_birds, bottom = 0, color = 'blue', width = 0.6)     #Creates third bar for the birds, bar colour is green
    plt.bar('Mammals', threatened_mammals, bottom = 0, color = 'black', width = 0.6)  #Creates fourth bar for the mammals, bar colour is green
    plt.xticks(x_space, x)          #Sets and spaces x-axis values evenly along x-axis
    plt.show()          #Reveals bar graph to user 

    country_data = pd.read_csv('Country_Data.csv', delimiter = ',')     #Reads in 'Country_data.csv' using pandas and changes into an array using numpy
    country_data = np.array(country_data)  
    country_area = country_data[index][3]           #Takes the list of user's country and the fourth element of the resulting list

    plants_per_area = (threatened_plants / country_area)
    fish_per_area = (threatened_plants / country_area)              #Takes number of species for plants, mammals, birds, and fish, and divides by area of country
    birds_per_area = (threatened_birds / country_area)
    mammals_per_area = (threatened_mammals / country_area)

    plot_per_km = []                #Defines empty list
    plot_per_km.append(plants_per_area)
    plot_per_km.append(fish_per_area)       #appends each divided value to list
    plot_per_km.append(birds_per_area)
    plot_per_km.append(mammals_per_area)

    plt.title(f'Number of Endangered Species Per Square Kilometer of Land in {country}')        #Set plot title
    plt.xlabel('Organism')                          #Set x-axis label
    plt.ylabel('Threatened Species')     #Sets y-axis label
    plt.plot(x, plot_per_km, 'c--')  #Creates first bar for the plants, bar colour is green
    plt.xticks(x_space, x)          #Sets and spaces x-axis values evenly along x-axis
    plt.grid()
    plt.show()          #Reveals bar graph to user 

class Population:
    '''
    A class used to create a population object for calculating population
    
    Attributes:
    country(str): a string that represents a countries name

    Methods:
    calc_max_min: Calculates the max and min population for each country instance
    '''
    
    def __init__(self, country):
        self.country = country

    def calc_max_min(self):
        '''
        Calculates the max and min population for each country instance

        Arguments:
        none

        Returns:
        none
        '''
        population_data = pd.read_csv('Population_Data.csv', delimiter = ',')  
        population_data = np.array(population_data).tolist()    #Use pandas to read in 'Population_Data.csv' file and convert the data to a list using numpy and the .tolist() function
        
        for i in range(len(population_data)):
            if self.country in population_data[i]:       #Iterates through each country in the range and length of population_data and assigns the index of the country instance in population_data to index
                index = i
                country_pop = population_data[index]    #Retrieves the population of country instance at each year in population_data. Contains country instance
                country_pop.remove(self.country)        #Removes country instance from country_pop
                country_pop_array = np.array(country_pop)

        max = np.amax(country_pop_array)

        year = 2000     #Defines year as the minimum year data is available for
        for p in range(len(country_pop)):
            if max == country_pop[p]:   #Determines the year which max occurs in by iterating through country_pop. Iteration ends when max value equals the population value at the country instance index of country_pop. Else increase year by 1
                year = year
                break        #Breaks the loop
            else:
                year = year +1

        print(f'\tThe highest population of {self.country} is {max} in the year {year}')     #Outputs the maximum population at the year it occurs in

        min = np.amin(country_pop_array)
        
        year_min = 2000             #Defines year_min as the minimum year data is available for
        for p in range(len(country_pop)):
            if min == country_pop[p]:      #Determines the year which min occurs in by iterating through country_pop. Iteration ends when min value equals the population value at the country instance index of country_pop. Else increase year by 1
                year_min = year_min
                break   #Break the loop
            else:
                year_min = year_min +1

        print(f'\tThe lowest population of {self.country} is {min} in the year {year_min}')    #Outputs the minimum population at the year it occurs in

        total_pop = 0
        for n in range(0,21):
            year_pop = country_pop[n]       #Calculates total population through iteration of every year in data set at country instance. Adds all populations throughout the years to total_pop
            total_pop += year_pop 
        mean_pop = total_pop / 21           #Divides total_pop by the number of years data was collected for calculating total_pop

        print(f'\tThe mean population of {self.country} from years 2000 - 2020 is {mean_pop:.0f}')      #Outputs the mean population through the years 2000 - 2020

class Mean:
    '''
    A class used to create a mean object for calculating mean population

    Attributes:
    country(str): a string that represents a countries name
    starting_year(int): an integer that represets the beginning year for mean population calculation
    ending_year(int): an integer that represets the ending year for mean population calculation

    Methods:
    calc_my_mean: Calculates mean population
    '''

    def __init__(self, country, starting_year, ending_year):
        self.country = country
        self.starting_year = starting_year
        self.ending_year = ending_year
    
    def calc_my_mean(self):
        '''
        Calculates the mean population for each country instance depending on starting_year and ending_year instances

        Arguments:
        none

        Returns:
        mean - The calculated mean value unique to the country, starting_year, and ending_year instances
        '''
        population_data = pd.read_csv('Population_Data.csv', delimiter = ',') 
        population_data = np.array(population_data).tolist()      #Use pandas to read in 'Population_Data.csv' file and convert the data to a list using numpy and the .tolist() function
        
        for i in range(len(population_data)):
            if self.country in population_data[i]:      #Iterates through each country in the range and length of population_data and assigns the index of the entered country in population_data to index
                index = i                       
                country_pop = population_data[index]    #Retrieves the population of country instance at each year in population_data. Contains country instance
                country_pop.remove(self.country)        #Removes country instance from country_pop
       
        year = 2000         #Sets year as the minimum year data is available for
        for i in range(len(country_pop)):
            if year != self.starting_year:      #Iterates through country_pop. If year is not equal to the starting_year instance, adds 1 to year
                year = year +1
            else:
                starting_year_pop = country_pop[i]          #If year is equal to starting_year instance, then starting population is equal to the index of country_pop at the number of iterations through the for loop
                starting_year_index = country_pop.index(starting_year_pop)      #starting_year_index is equal to the index of country_pop which contains te value of starting_year_pop
                break           #Breaks loop

        year_2 = 2000           #Sets year_2 as the minimum year data is available for
        for p in range(len(country_pop)):
            if year_2 != self.ending_year:      #Iterates through country_pop. If year_2 is not equal to the ending_year instance, adds 1 to year_2
                year_2 = year_2 +1
            else:
                ending_year_pop = country_pop[p]        #If year_2 is equal to ending_year instance, then ending population is equal to the index of country_pop at the number of iterations through the for loop
                ending_year_index = country_pop.index(ending_year_pop)      #ending_year_index is equal to the index of country_pop which contains te value of ending_year_pop
                break           #Breaks loop

        s = starting_year_index
        e = ending_year_index +1
        years_in_mean = []
        count = 0
        for n in range(s, e):       #for element in range of the starting and ending index +1, append the value for population at each year
            years_in_mean.append(country_pop[n])      
            count+=1            #Increment count by 1 each iteration to count the number of years being accounted for


        mean = int(sum(years_in_mean) / count)      #Assigns mean with the value returned through taking the sum of the populations in the list years_in_mean and dividing by the number of iterations through the for loop (number of years)
        print(f'\tThe mean population in between years {self.starting_year} and {self.ending_year} is {mean} people')

def pop_plot(country, starting_year, ending_year):
    '''
    Plots the mean population for each country, starting_year, and ending_year instance using matplotlib.pyplot
        
    Arguments:
    none

    Returns:
    none
    '''
    population_data = pd.read_csv('Population_Data.csv', delimiter = ',')
    population_data = np.array(population_data).tolist()             #Reads in 'Population_Data.csv' using pandas, converts into an array using numpy, and turns data into a list using .tolist() method

    for i in range(len(population_data)):
        if country in population_data[i]:       #Iterates through each country in the range and length of population_data and assigns the index of the country instance in population_data to index
            index = i

    population_list = population_data[index]   #Takes the list of all populations in country instance, includes countries name
    del population_list[0]      #Deletes countries name from population_list

    count_year = starting_year
    years = []                          #Counts the difference between starting_year and ending_year so that all years within the bounds are accounted for and appended to years list
    while count_year != ending_year:       
        years.append(int(count_year))
        count_year += 1
    years.append(int(ending_year))

    year = 2000                 #initializes year as 2000
    for i in population_list:           #finds the index of the first year chosen 
        if year != starting_year:           
            year += 1
        else:
            starting_year_index = population_list.index(i)      #if the year is the first year chosen, get the index
            break

    year_index_list = []
    for i in range(len(years)):         #from the index of the first year, the indices of the years till the last year chosen is found by incrementing by 1
        year_index_list.append(starting_year_index)
        starting_year_index+=1

    pop_at_index = []
    for i in year_index_list:           #gets the population at the indices of the years chosen
        pop_at_index.append(population_list[i])
  
    plt.title(f'Population in {country} between {starting_year} - {ending_year}')   #Sets graph title
    plt.ylabel('Population')        #Sets y-label
    plt.xlabel('Year')              #Sets x-label
    plt.plot(years, pop_at_index, 'c--')        #Plots data. Years on x_axis, population on y-axis
    plt.xticks(years)       #Sets the x-axis values as the values contained in the list of years
    plt.grid()      #Creates grid on graph
    plt.show()      #Shows graph to user

    country_data = pd.read_csv('Country_Data.csv', delimiter = ',')  
    country_data = np.array(country_data)               #Reads in 'Country_Data.csv' using pandas and changes into an array using numpy
    country_area = country_data[index][3]       #takes the list of the user's country and the fourth element of the resulting list

    plot_area = []                  #Defines an empty list
    for m in pop_at_index:
        m /= country_area           #Takes each element in pop_index and divides it by the square kilometers of the country
        plot_area.append(m)             #Append each resulting value to list

    plt.title(f'Population in {country} per Square Kilometer between {starting_year} - {ending_year}')   #Sets graph title
    plt.ylabel('Population')        #Sets y-label
    plt.xlabel('Year')              #Sets x-label
    plt.plot(years, plot_area, 'r--')        #Plots data. Years on x_axis, plot_area on y-axis. Plots a red dashed line
    plt.xticks(years)       #Sets the x-axis values as the values contained in the list of years
    plt.grid()      #Creates grid on graph
    plt.show()      #Shows graph to user

class Country:
    '''
    A class used to creeate a country object used for calculating geographical and locational data

    Attributes:
    country(str): a string that represents a countries name

    Methods:
    print_geography: Prints geographical data for country instance
    '''

    def __init__(self, country):
        self.country = country
    
    def print_geography(self):
        '''
        Prints the geographical data for country instance

        Arguments:
        none

        Returns:
        none
        '''
        country_data = pd.read_csv('Country_Data.csv', delimiter = ',')  
        country_data = np.array(country_data).tolist()      #Use pandas to read in 'Country_Data.csv' file and convert the data to a list using numpy and the .tolist() function

        for n in range(len(country_data)):
            if self.country in country_data[n]:   #Iterates through each country in the range and length of threatened_data and assigns the index of the entered country in threatened_data to index
                index = n

        un_region = country_data[index][1]  #Assigns un_region to the un region of country instance
        sub_region = country_data[index][2] #Assigns sub_region to the sub region of country instance
        sq_km = country_data[index][3]      #Assigns sq_km to the value of square kilometers of country instance

        country_data = pd.read_csv('Country_Data.csv', delimiter = ',')  
        country_data = np.array(country_data)                           #Redefines country_data as an array
        country_areas = sorted(country_data[:,3], reverse = True)       #Takes the fourth column (areas) and reverses the list

        for i in range(len(country_data)):    
            if self.country in country_data[i]:
                index_country = i                   #Finds the index the country instance is in in the data set

        self_area = country_data[index_country][3]      #Defines self_area as the area of the country instance using the index of country instance and taking element 4 in the list

        count = 1
        for q in range(len(country_areas)):
            if self_area == country_areas[0]:       #Iterates through the reversed list. If country instance area is the area, break loop. If not, increase count by 1 until country instance area is the area at the index
                break
            if self_area == country_areas[q]:
                break
            else:
                count += 1

        if count == 1:          #If count is 1, the country is the largest
            print(f'\t{self.country} is the largest country in the world!')
        else:               #If count is not 1, print the following
            print(f'\t{self.country} is the #{count} largest country in the world!')

        print(f'\tGeographical data for {self.country}: ')
        print(f'\tUN region: {un_region}')            #Outputs data above
        print(f'\tUN sub-region: {sub_region}')
        print(f'\tSquare kilometers: {sq_km}km\n')

def plot_geography(country):
        '''
        Plots data using matplotlib.pyplot for country instance

        Arguments:
        none

        Returns:
        none
        '''
        country_data = pd.read_csv('Country_Data.csv', delimiter = ',')    
        country_data = np.array(country_data)            #Use pandas to read in 'Country_Data.csv' file and convert the data to an array using numpy

        area_list = []          #Creates an empty list for country areas
        for c in country_data[:,3]:
            area_list.append(c)         #Appends each country area to area_list and uses reverse sorting to sort data from largest to smallest
            area_list = sorted(area_list, reverse = True)
        top_5 = area_list[:5]           #assigns top_5 with the 5 largest countries
        bottom_5 = area_list[-5:]       #assigns bottom_5 with the 5 smallest countries

        country_column = country_data.tolist()      #Creates a list out of the numpy array 'country_data' for iteration

        index_top_5 = []        #Creates empty list for the index's of the largest five countries
        for i in country_column:
            if i[3] in top_5:       #Iterates through country names and appends the lists in which the countries in top_5 are contained
                index_top_5.append(i)
 
        k = 0
        country_index = []
        for i in country_column:
            for k in range(5):              #Iterates through the list of 'Country_Data.csv' and appends the five index's of the countries in index_top_5 to country_index
                if i == index_top_5[k]:
                    k += 1
                    ind = country_column.index(i)
                    country_index.append(ind)

        r = 0
        list_km = []
        for i in country_index:         #Iterates through country_index and appends the value of the countries area in the order which the countries index's appear in country_index
            for r in range(5):                      #Once iterations complete, countries index and areas line up at the same index's in country_index and list_km
                if top_5[r] == country_column[i][3]:
                    list_km.append(top_5[r])
         
        w = 0
        list1 = []
        for i in country_index:
            for w in range(5):          #Iterates through country_index, which contains the countries index's, and uses the index's to find the country name in country_column in which they belong to
                if list_km[w] == country_column[i][3]:
                    list1.append(country_column[i][0])      #Appends each country name to list1

        index_bottom_5 = []     #Creates empty list for the index's of the smallest five countries
        for i in country_column:
            if i[3] in bottom_5:
                index_bottom_5.append(i)        #Iterates through country names and appends the lists in which the countries in bottom_5 are contained

        k = 0
        country_index_2 = []
        for i in country_column:
            for k in range(5):            #Iterates through the list of 'Country_Data.csv' and appends the five index's of the countries in index_bottom_5 to country_index_2
                if i == index_bottom_5[k]:
                    k += 1
                    ind = country_column.index(i)
                    country_index_2.append(ind)

        r = 0
        list_km_2 = []
        for i in country_index_2:           #Iterates through country_index_2 and appends the value of the countries area in the order which the countries index's appear in country_index_2
            for r in range(5):              
                if bottom_5[r] == country_column[i][3]:
                    list_km_2.append(bottom_5[r])       #Once iterations complete, countries index and areas line up at the same index's in country_index_2 and list_km_2

        w = 0
        list2 = []          
        for i in country_index_2:
            for w in range(5):              #Iterates through country_index_2, which contains the countries index's, and uses the index's to find the country name in country_column in which they belong to
                if list_km_2[w] == country_column[i][3]:
                    list2.append(country_column[i][0])      #Appends each country name to list2
        
        total_index = list1 + list2             #Adds list1 and list2 to create a list containing all countries (doesnt include country instance yet)
        total_area = list_km + list_km_2        #Adds list_km and list_km_2 to create a list containing all areas (doesnt include country instance yet)

        if country not in total_index:
            total_index.append(country)            #If the country instance is not in the list of countries, append the country instance to the list of countries
            for i in country_column:            
                g = i[3]
                for g in i:                             
                    if country == i[0]:         #Appends the country instances list to total_area (includes Country, UN Region, UN Sub-Region, Sq Km)
                        total_area.append(g)

            del total_area[10]
            del total_area[10]      #Removes Country, UN Region, and UN Sub-Region values from total_area list
            del total_area[10]
   
        wanted_value = []       #Creates empty list
        if country not in list1 and country not in list2:     #If country instance not in list1 or list2, append the last value of total area to wanted_value
            wanted_value.append(total_area[-1])
        elif country in list1 or country in list2:
            for s in range(len(total_index)):               #Else, if country instance is in list or list2, iterate through total_index. If total_index equals country instance at an index, append that index of total_area to wanted_value
                if total_index[s] == country:
                    wanted_value.append(total_area[s])

        total_dict = dict(zip(total_index, total_area))     #Creates a dictionary of country names and their areas by zipping two lists together

        plt.title(f'Size of {country} Compaired to the Worlds Top Five Biggest and Smallest Countries')    #Sets graph title
        plt.xlabel('Countries')                             #Sets x-axis label
        plt.ylabel('Square Kilometers (km)')          #Sets y-axis label
        plt.plot(total_dict.keys(), total_dict.values(), 'r-')      #Plots data with x-axis values as the country names and y-axis values as the country areas. Plots a solid red line
        plt.plot(country, wanted_value, 'bo', label = (f'Specified Country: {country}'))  #Labels country instance with a blue dot at its calculated x and y values
        plt.xticks(total_index, fontsize = 8)  ##Sets and spaces x-axis values evenly along x-axis. Specified fontsize as 8
        plt.legend(shadow = True, loc = 'best')
        plt.gca().set_ylim([0, 17100000])             #Sets the max and min y values 
        plt.grid()                                    #Displays a grid on graph for easier data lookup
        plt.show()                                    #Displays graph to user
        

def main():
    '''
    Contains main program user interacts with

    Arguments:
    none

    Returns:
    none

    '''
    country_data = pd.read_csv('Country_Data.csv', delimiter = ',')  
    country_data = np.array(country_data)      #Use pandas to read in 'Country_Data.csv' file and convert the data to an array using numpy
    country_country = country_data[:,0]         #Gain the list of countries by taking the 0th index of country_data

    country = input('Please enter a country: ')     #Request input from user for the country they would like to research
    if country not in country_country:      
        print(f'Sorry, {country} is not a valid entry. Please enter an available country. ')
        main()                                      #If the entered country is not in the list of available countries, restart main function
        
    elif country in country_country:            #If entered country is in the list of available countries, do the following code
        choice_pop = input(f"Would you like to access {country}'s population data? (yes/no): ")     #Request input from user if they want to access population data for their chosen country
        if choice_pop.lower() == 'yes':
            my_country = Population(country)            #If user enters 'yes' for user_pop, call calc_max_min function in Population class
            my_country.calc_max_min()
            years = range(2000, 2021)       #Defines the years data is available for
            starting_year = int(input(f'Enter a starting year to calculate the mean of {country} (between 2000 and 2020): '))   #Request input for the starting year user wants to calculate the mean population for within their chosen country
            if starting_year not in years:
                while starting_year not in years:
                    print(f'Sorry, {starting_year} is not an available year within the data set')      #If the starting year is not in list of years, entry is invalid. Run loop until valid entry. When entry is valid continue
                    starting_year = int(input(f'Enter a starting year to calculate the mean of {country} (between 2000 and 2020): '))
                    if starting_year in years:
                        continue
            ending_year = int(input((f'Enter an ending year to calculate the mean of {country} (between 2000 and 2020): ')))   #Request input for the ending year user wants to calculate the mean population for within their chosen country
            if ending_year not in years:
                while ending_year not in years:
                    print(f'sorry, {ending_year} is not an available year within the data set')      #If the ending year is not in list of years, entry is invalid.  Run loop until valid entry. When entry is valid continue
                    ending_year = int(input((f'Enter an ending year to calculate the mean of {country} (between 2000 and 2020): ')))
                    if ending_year in years:
                        continue
            if (2000 <= starting_year <= 2020) and (2000 <= ending_year <= 2020) and (starting_year <= ending_year):  #If starting year is between the years 200 and 2020, ending year between the years 200, 2020, and starting year is less than the ending year, continue
                my_mean = Mean(country, starting_year, ending_year)     #Call calc_mean function within Mean class to calculate the mean population within starting year and ending year
                my_mean.calc_my_mean()
            else:
                while starting_year > ending_year:          #While the starting year is greater than the ending year, run the following while loop
                    print('Starting year cannot be larger than ending year')   #If starting year is not between the years 2000 and 2020 or ending year is not between the years 200, 2020 or starting year is greater than the ending year, entry invalid
                    starting_year = int(input(f'Enter a starting year to calculate the mean of {country} (between 2000 and 2020): '))   #Request re-input for the starting year user wants to calculate the mean population for within their chosen country
                    if starting_year not in years:
                        while starting_year not in years:
                            print(f'Sorry, {starting_year} is not an available year within the data set')      #If the starting year is not in list of years, entry is invalid. Run loop until valid entry. When entry is valid continue
                            starting_year = int(input(f'Enter a starting year to calculate the mean of {country} (between 2000 and 2020): '))
                            if starting_year in years:
                                continue
                    ending_year = int(input((f'Enter an ending year to calculate the mean of {country} (between 2000 and 2020): ')))   #Request re-input for the ending year user wants to calculate the mean population for within their chosen country
                    if ending_year not in years:
                        while ending_year not in years:
                            print(f'sorry, {ending_year} is not an available year within the data set')      #If the ending year is not in list of years, entry is invalid.  Run loop until valid entry. When entry is valid continue
                            ending_year = int(input((f'Enter an ending year to calculate the mean of {country} (between 2000 and 2020): ')))
                            if ending_year in years:
                                continue
                    if (2000 <= starting_year <= 2020) and (2000 <= ending_year <= 2020) and (starting_year <= ending_year):  #If starting year is between the years 200 and 2020, ending year between the years 200, 2020, and starting year is less than the ending year, continue
                        my_mean = Mean(country, starting_year, ending_year)     #Call calc_mean function within Mean class to calculate the mean population within starting year and ending year
                        my_mean.calc_my_mean()
                        break                    
        elif choice_pop.lower() == 'no':
            pass                #If choice_pop is 'no' skip to threatened species 
        else:  
            print(f'Sorry, {choice_pop} is an invalid entry.')      #If choice_pop is not 'yes' or 'no', entry is invalid. Call main function
            main()
        
    choice_threat = input(f"Would you like to access {country}'s endangered species information? (yes/no): ")   #Request input for whether user woud like to access endangered species information for their country

    if choice_threat.lower() == 'yes':
        print_choice = Endangered(country)              #If user enters 'yes', call print_data_endanger function within the Endangered class, passing through the users chosen country
        print_choice.print_data_endanger()
    elif choice_threat == 'no' or choice_threat == 'No':
        pass            #If user enters 'no' for choice_threat, skip to location / geographical data
    else:
        while choice_threat.lower() != 'yes' or choice_threat.lower() != 'no':  #While user enters an invalid input, run loop until user input is valid
            print(f'Sorry, {choice_threat} is an invalid entry.')
            choice_threat = input(f"Would you like to access {country}'s endangered species information? (yes/no): ")
            if choice_threat.lower() == 'yes':    #If user enters 'yes', call print_data_endanger function in Endangered class
                print_choice = Endangered(country)
                print_choice.print_data_endanger()
                break                               #Break the loop
            elif choice_threat.lower() == 'no':
                pass            #If user enters 'no' for choice_threat, skip to location / geographical data
                break           #Break the loop

    choice_location = input(f"Would you like to access {country}'s location / geographical data? (yes/no): ") #Asks user if they want to display location/geographical data

    if choice_location.lower() == 'yes':
        print_choice = Country(country)         #If user inputs 'yes', call print_geography function within Country class, passing through their chosen country, to calculate and return data relating to the countries geographical data
        print_choice.print_geography()
    elif choice_location.lower() == 'no':
        pass                                        #If user inputs 'no' skip to plotting
    else:
        while choice_location.lower() != 'yes' or choice_location.lower() != 'no':        #If user input is not within the list, input is invalid
            print(f'Sorry, {choice_location} is an invalid entry.')     #Runs loop until user inputs a valid entry
            choice_location = input(f"Would you like to access {country}'s endangered species information? (yes/no): ")
            if choice_location.lower() == 'yes':    
                print_choice = Country(country)     #If re-entered input is 'yes', call print_geography function within Country class, passing through their chosen country, to calculate and return data relating to the countries geography and location
                print_choice.print_geography()      
                break           #Break loop
            elif choice_location.lower() == 'no':
                pass                #If re-entered input is 'no', skip to plotting
                break   #Break loop
    
    if choice_pop.lower() == 'yes':
        pop_plot(country, starting_year, ending_year)        #If user chose to view population data, call plot_pop to plot the calculated data

    if choice_threat.lower() == 'yes':        #If user chose to view endangered species data, call plot_endanger to plot the calculated data
        plot_endanger(country)

    if choice_location.lower() == 'yes':     #If user chose to view location data, call plot_geography to plot data
        plot_geography(country)
    
    choice_restart = input('Would you like to research another country? (yes/no): ')        #Ask user if they want to research another country

    if choice_restart.lower() == 'yes':      #If user wants to research another country, restart main function
        main()
    if choice_restart.lower() == 'no':        #If user does not want to research another country, teminate program
        print('\n\t\t\tThankyou for using the program!\n')
        quit()
    else:
        while choice_restart.lower() != 'yes' or choice_restart.lower() != 'no':     #If entry is not in the list, entry is invalid
            print(f'Sorry, {choice_restart} is an invalid entry')
            choice_restart = input('Would you like to research another country? (yes/no): ')        #Ask for re-entry until entry is valid
            if choice_restart.lower() == 'yes':      #If user wants to research another country, restart main function
                main()
            if choice_restart.lower() == 'no':        #If user does not want to research another country, teminate program
                print('\n\t\t\tThankyou for using the program!\n')
                quit()

if __name__ == '__main__':      #If the file being run is the main file, run opening print statement and main() function
    print('\n\t\t\t Welcome to the Country Information Program\n\t\t\t--------------------------------------------\n')
    main() 