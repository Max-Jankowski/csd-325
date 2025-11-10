# Max Jankowski
# CSD-325
# Module 1 assignment 1.3
# Modified 11-9-25 to continue prompting for valid input or entry of zero


def countdown_bottles(num_bottles): #defining the function to write out the song
   
    for count in range(num_bottles, 0, -1):
        if count == 1:
            # condition to change songe to singular
            print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
            print(f"Take one down, pass it around, no more bottles of beer on the wall.\n")
        else:
            # condition to write out lyrics in the plural
            next_count = count - 1
            bottle_word = "bottle" if next_count == 1 else "bottles"
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            print(f"Take one down, pass it around, {next_count} {bottle_word} of beer on the wall.\n")


def main(): # defining the main funcion to call countdown function 
            # and get starting point by prompting user
  
    print("Welcome to the Beer Countdown Program!\n")
    
    # Get user input with validation loop
    while True:
        try:
            num_bottles = int(input("How many bottles of beer are on the wall? : "))
            
            # validating user input to ensure the number is positive and 1 or over
            if num_bottles < 1:
                print("Please enter a positive number! Try again.\n")
                continue  # Go back to the beginning of the loop added later after testing
             
            break  # Valid input received, exit the loop
            
        except ValueError: 
            print("Invalid input! Please enter a whole number. Try again.\n")
            # Loop continues, prompting again
    
    print()  
    # calling the previously defined countdown function 
    countdown_bottles(num_bottles)
    
    # Reminder after countdown completes        
    print("Time to buy more beer!")

# calling main function to run program
if __name__ == "__main__":
    main()

# sorry this one took so long, went through multiple versions and 
# had a hard time with the flow chart, just a bit scatter brained 
#trying to catch up