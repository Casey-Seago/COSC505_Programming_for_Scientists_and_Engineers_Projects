#  Casey Read python calculator project for COSC 505
print("1. Cartesian distance \n2. Vector x matrix \n3. Normalize \n4. Quit")    #  Printing calculator options
command = input("Enter command number: ")  #  Having user input their command by inputing the associated number
import math # importing math for future calculations
while command != "4":     # allows loop to continue until they choose 4. Quit
    if command == "1":      #if user chose 1. Cartesian distance, progresses through this segment of code
        values = input("Enter coordinates (x1 y1 x2 y2): ").split(" ")      # prompts user to input values and shows structure input should take
        print("You entered:", values)       #  displays the values the user input
        response = input("Are these values correct, y/n? ")     # has the user check for errors
        if response == "y":     # if no errors, progresses through calculations
            for i in range(len(values)):        #  transforming user input to float step 1: creates index
                values[i] = float(values[i])    #  transforming user input to float step 2: for each spot (index) in the list called values, change the value to float
            output = math.sqrt(((values[2] - values[0])**2) + ((values[3] - values[1])**2))     # performs cartesian distance calculation using float values
            print()     # creates whitespace so printing the results stands out/ is cleaner
            print("Result: ")      # prints the word results
            print(output)       # printed the output of the cartesian distance calculation
            print()     # creates whitespace so printing the results stands out/ is cleaner
            input("Press enter to continue: ")      # thought it'd be nice to have the user to say when ready to continue instead of having the new options pop up immediately. Thought it made results look cleaner/nicer
            print("1. Cartesian distance \n2. Vector x matrix \n3. Normalize \n4. Quit")        #reprinting options for user to choose from
            command = input("Enter command number: ")      # has user input new command, original while loop cycles back through
        else: 
            continue        #  if the user finds their values to be input incorrectly, this has them re-enter values
    elif command == "2":       #If user chose 2. Vector x matrix, runs through this code
        values = input("Enter vector and matrix values (v1 v2 v3 m11 m12 m13 m21 m22 m23 m31 m32 m33): ").split(" ")    # prompting user to input their vector and matrix values and specifying the format
        print("You entered:", values)   # printing the values the user entered
        response = input("Are these values correct, y/n? ")     # asking user to verify if the values are correct
        if response == "y":     # if they are correct, progresses through this section of code
            for i in range(len(values)):        #  transforming user input to float step 1: creates index
                values[i] = float(values[i])    #  transforming user input to float step 2: for each spot (index) in the list called values, change the value to float
            input_vector = values[0:3]      #creating a vector by extracting the first three values from the transformed user input list called values
            input_matrix = (values[3:6], values[6:9], values[9:12])     #creating a matrix by extracting the last nine values from the transformed user input list called values
            math_output = []    #  creating an empty list for the output of the math equation matrix * vector to be appended to
            for num in input_matrix[0]:     #  for each number in the first row of the matrix.....
                new_value = num * input_vector[0]       #  ..... multiply it by the first value of the vector and call it new_value
                math_output.append(new_value)       #  add that new value to the math_output list
            for num in input_matrix[1]:         #  for each number in the second row of the matrix.....
                new_value = num * input_vector[1]       #  ..... multiply it by the second value of the vector and call it new_value
                math_output.append(new_value)       #  add that new value to the math_output list
            for num in input_matrix[2]:         #  for each number in the third row of the matrix.....
                new_value = num * input_vector[2]     #  ..... multiply it by the third value of the vector and call it new_value 
                math_output.append(new_value)       #  add that new value to the math_output list
            output_matrix = (math_output[0:3], math_output[3:6], math_output[6:9])      #  creating a matrix from the math_output list of multiplication results  
            print()         #  creates whitespace so printing the results stands out/ is cleaner
            print("Result: ")      #  prints the word results
            print(output_matrix)         #  prints the output_matrix 
            print()         #  prints white space for better results readability
            print("Press enter to continue: ")          #  thought it'd be nice to have the user to say when ready to continue instead of having the new options pop up immediately. Thought it made results look cleaner/nicer       
            print("1. Cartesian distance \n2. Vector x matrix \n3. Normalize \n4. Quit")        #  prints command list for user to choose from
            command = input("Enter command number: ")          #  prompts the user to choose a command from the list
        else:
            continue        #  if the user finds their values to be input incorrectly, this has them re-enter values
    elif command == "3":         #  if the user enters command 3. Normalize, this segment of code is run
        values = input("Enter values (value1 value2 value3): ").split(" ")          #  prompts the user to enter values and displays the format
        print("You entered:", values)           #  displays the values the user entered
        response = input("Are these values correct, y/n? ")         #  asks the user if the values are correct
        if response == "y":         #  if the values are correct, continues through this code
            for i in range(len(values)):         #  transforming user input to float step 1: creates index
                values[i] = float(values[i])        #  transforming user input to float step 2: for each spot (index) in the list called values, change the value to float
            norm_length = math.sqrt(values[0]**2 + values[1]**2 + values[2]**2)         #  calculating the length to use in the normalization calculation
            norm_vector = []        #  creating an empty list to append calculated values to
            for num in values:      #  for each number in the values list .....
                new_value = num / norm_length       #  ..... divide it by the length that was previously calculated
                norm_vector.append(new_value)       #  adding the calculated value to the list norm_vector
            print()         #  printing whitespace for readability
            print("Result: ")
            print(norm_vector)          #  printing the results vector
            print()         #  whitespace for readability
            input("Press enter to continue: ")      # thought it'd be nice to have the user to say when ready to continue instead of having the new options pop up immediately. Thought it made results look cleaner/nicer
            print("1. Cartesian distance \n2. Vector x matrix \n3. Normalize \n4. Quit")        #  displays the command options
            command = input("Enter command number: ")          #  prompts the user to enter a command
        else:
            continue        #  if the values aren't correct, allows the user to reenter values if they aren't correct
    else:       #  if the command entered isn't one of the 4 options .....
        print()     #  prints whitespace for readability
        print("ERROR: Please input valid command")        #  prints an error and instructs to re-enter command
        print("1. Cartesian distance \n2. Vector x matrix \n3. Normalize \n4. Quit")        #  displays command options
        command = input("Enter command number: ")      #  prompts user to input command
print("Thank you for using Casey's Calculator!")