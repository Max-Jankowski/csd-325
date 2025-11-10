#Max Jankowski
#csd325
#assignment module 4

# modified version sitka_highs.py to allow user to select high or low temperatures.


#import files and library, as original version 
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Providing user with instruction for selecting high and low charts
print()
print("Sitka Weather Data - 2018")
print()
print("Menu: Highs, Lows, or Exit ")
print("---------------------------------------")

filename = 'sitka_weather_2018_simple.csv'

# body of the program loop to get user selection or exit 
while True:
    # get users selection and save as choice variable, store in lower case
    choice = input("\nEnter choice (Highs/Lows/Exit): ").strip().lower()
    
    # porgramming the exit selection to shut progam down
    if choice == 'exit':
        print("\nThank you for using the program. Goodbye!")
        break
    
    # reading the csv file 
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # retriveing the dates and temprature from data file
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            
            # getting the high or lows depending on user selection
            if choice == 'highs':
                temp = int(row[5])  #  temperatures in column 5
                temps.append(temp)
            elif choice == 'lows':
                temp = int(row[6])  # temperatures in column 6
                temps.append(temp)
            else:
                print("Invalid choice! Please enter Highs, Lows, or Exit.")
                break
        
        # plot of line if valid choice made
        if choice in ['highs', 'lows']:
            # plot temp
            fig, ax = plt.subplots()
            
            # instructing to use red for highs or blue for lows
            color = 'red' if choice == 'highs' else 'blue'
            ax.plot(dates, temps, c=color)

            # format of lione plot
            title = "Daily high temperatures - 2018" if choice == 'highs' else "Daily low temperatures - 2018"
            plt.title(title, fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()
            
#https://docs.python.org/3/library/csv.html
# https://matplotlib.org/stable/users/explain/quick_start.html
# https://matplotlib.org/stable/users/explain/customizing.html#customizing