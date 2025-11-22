# Max Jankowski
# CSD-325 Module 7 Assignemnt
# Bellevue University

# writing and function that takes city and contry parameters
# returns and prints them in single string

# defining the functon revision for passed test
def city_country(city, country, population=None, language=None ):
    result = f"{city}, {country}"

    if population:
        result += f" - population {population}"

    if language:
        result += f", {language}"

    return result



# calling the function 3 times in the same file
# first city called is from example
# 1) Just city and country
print(city_country("Santiago", "Chile", ))
# call 2) including population
print(city_country("Warsaw", "Poland", 3000000, ))
# call 3) includes language
print(city_country("London", "England", 4500000, "English"))
