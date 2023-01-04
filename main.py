# Program written by Eric Trevorrow

import csv
import addresses
import distances
import hashTable
import package

# Time complexity of program: O(n^2)
# Space complexity of program: O(n)

print("Truck Package App Started")

# Time complexity : O(1)
# Space complexity: O(1)
def time_adjuster(time_to_format):
    """
    time_adjuster:
    time_adjuster takes a time in military format and adjusts it so that it returns as pseudo-time. Ex: "08:30" --> "8.5"

    Args:
    time_to_format: this represents the time that will be passed into the function

    Returns:
    final_formatted_time: this represents the time that is returned after being adjusted from military time into pseudo-time.

    Raises:
    Raises no exceptions.

    Time Complexity: time_adjuster uses many assignment operators, but employs no loops. Its time complexity is O(1).

    Space Complexity: There are four assignment operations that equal up to 4(O(1) = (O(1).
    """
    starting_time_adjust = time_to_format
    formatted_time = starting_time_adjust.replace(":",".")
    substring_time = formatted_time[3:5]
    final_formatted_time = float(formatted_time[0:2]) + float(substring_time)/60
    return final_formatted_time

# Prompts the user for a time, and if it is a valid time, proceeds to the next while loop
# Time complexity: O(1)
# Space complexity: O(1)
usertime_valid = False
while (usertime_valid != True):
    usertime = input("Please enter a time:" + "\n" + "Format: 'HH:MM' Military time (Example: 08:00)" + "\n")

    # Checks if the entered time is valid, between 00:00 and 24:00 and makes sure that the minutes do not exceed 60.
    if (len(usertime) == 5 and usertime[2] == ":" and usertime > "00:00" and usertime < "24:00" and (usertime[3:5] < "60")):
        usertime_valid = True

    # If the user enters an invalid time, it prints out that they need to enter a valid time and goes through the loop again.
    if (usertime_valid == False):
        print("Please enter a valid time.")


# This is the main while loop of the program. Prompts the user for one of the options and runs the specified if statement depending on what the user enters.
program_exit = False
while(program_exit != True):
    print("Your time is currently set to " + str(usertime))
    print("Please select an option: ")
    print("1. Print truck status reports and total miles.")
    print("2. Print specific package data.")
    print("3. Print detailed data of all packages.")
    print("4. Enter new time.")
    print("5. Quit the program.")
    userinput = input("Select a choice: ")

    # When the user inputs 4, the following code runs
    # Prompts the user for a time, and if it is a valid time, runs through the main while loop again with the new inputted time.
    # Time complexity: O(1)
    # Space complexity: O(1)
    if (userinput == "4"):
        usertime_valid = False
        while (usertime_valid != True):
            usertime = input("Please enter a time:" + "\n" + "Format: 'HH:MM' Military time (Example: 08:00)" + "\n")

            # Checks if the entered time is valid, between 00:00 and 24:00 and makes sure that the minutes do not exceed 60.
            if (len(usertime) == 5 and usertime[2] == ":" and usertime > "00:00" and usertime < "24:00" and (usertime[3:5] < "60")):
                usertime_valid = True

            # If the user enters an invalid time, it prints out that they need to enter a valid time and goes through the loop again.
            if (usertime_valid == False):
                print("Please enter a valid time.")

    # This creates the hash table that is primarily used within the program
    # Loops through the package file CSV and uses the package ID as keys and the attributes as values to insert them into the hash table
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    packageTable = hashTable.Chaining_Hash_Table()
    with open("Package File.csv") as packageFile:
        reader = csv.reader(packageFile, delimiter=",", quotechar='"')
        for row in reader:
            packageTable.insert(row[0], package.PackageObject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],"At the hub","None"))


    # Manually loading the truck lists with numbers that represent package IDs and creating a static copy of each list
    # Time complexity: O(1)
    # Space complexity: O(n)
    truck1 = ["1","13","14","15","16","17","19","20","22","27","29","30","31","34", "37","40"]
    truck1_static_list = truck1.copy()
    truck2 = ["2","3","6","7","11","12","18","23","25","26","28","32","33","36","38","39"]
    truck2_static_list = truck2.copy()
    truck3 = ["4","5","8","9","10","21","24","35"]
    truck3_static_list = truck3.copy()


    # This algorithm employs the nearest neighbor algorithm and applies it to the truck 1 list and all of the package IDs within it.
    # Searches for the shortest available path from one package object to the next, and calculates time as well as miles traveled.
    # Updates the package objects in the hash table with a timestamp of the time the package is "delivered".
    # Time Complexity: Two while loops, one nested within the other. O(n^2)
    # Space Complexity: Algorithm contains a hash function search and updates the hash table too. O(n)
    i=0
    truck_address1 = '4001 South 700 East'
    package_to_be_delivered = "None"
    miles_driven1 = 0.0
    truck1_start_time = 8.0
    truck1_current_time = 8.0

    # Loops through the length of the truck1 list, iterating on each object within it. At the end of each iteration, an object is removed from truck1,
    # eventually reducing the truck1 list to 0 and ending the loop
    while i < len(truck1):
        j=0
        min_value = 100.0

        # Loops through every object in the truck1 again, comparing the current address of the truck to the address of each object within the truck.
        # Uses the address lookup function and distance_list to look up the correct distance between each address
        while j < len(truck1):
            calculated_distance = distances.distance_list[addresses.address_lookup(truck_address1)][addresses.address_lookup(packageTable.lookup(truck1[j], "address"))]

            # Looks for the smallest distance between all of the values looked up in the while loop. If it finds a new smaller distance, it sets min_value to
            # that distance and sets the truck address to the address of the package object with the smallest distance.
            if(float(calculated_distance) < float(min_value)):
                min_value = calculated_distance
                package_to_be_delivered = truck1[j]
                temp_truck_address = [packageTable.lookup(truck1[j], "address")]
            j = j + 1

        # Updates the variables that are keeping track of miles driven, the truck address, and the time.
        # Timestamps the package objects in the hash table with a timestamp of when they are delivered.
        # Removes the package that is delivered from the truck 1 list.
        miles_driven1 = miles_driven1 + float(min_value)
        truck1_temp_time = float(min_value)/18.0
        truck1_current_time = truck1_current_time + truck1_temp_time
        delivered_package = packageTable.search(package_to_be_delivered)
        truck1_time_to_timestamp = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_current_time * 60, 60))
        delivered_package.timestamp = truck1_time_to_timestamp
        delivered_package.status = "Delivered"
        truck1.remove(package_to_be_delivered)
        truck_address1 = str((temp_truck_address)).lstrip("['").rstrip("']")

    #Calculates the travel distance to the hub and the time required to do so and adds it to truck 1's totals.
    back_to_hub_travel = distances.distance_list[addresses.address_lookup(truck_address1)][addresses.address_lookup('4001 South 700 East')]
    truck1_back_hub_time = float(back_to_hub_travel)/18.0
    truck1_current_time = truck1_current_time + truck1_back_hub_time
    miles_driven1 = miles_driven1 + float(back_to_hub_travel)


    # This algorithm employs the nearest neighbor algorithm and applies it to the truck 2 list and all of the package IDs within it.
    # Searches for the shortest available path from one package object to the next, and calculates time as well as miles traveled.
    # Updates the package objects in the hash table with a timestamp of the time the package is "dropped off".
    # Time Complexity: Two while loops, one nested within the other. O(n^2)
    # Space Complexity: Algorithm contains a hash function search and updates the hash table too. O(n)
    i=0
    truck_address2 = '4001 South 700 East'
    package_to_be_delivered = "None"
    miles_driven2 = 0.0
    truck2_start_time = 9.5
    truck2_current_time = 9.5

    # Loops through the length of the truck2 list, iterating on each object within it. At the end of each iteration, an object is removed from truck2,
    # eventually reducing the truck2 list to 0 and ending the loop
    while i < len(truck2):
        j=0
        min_value = 100.0

        # Loops through every object in the truck2 again, comparing the current address of the truck to the address of each object within the truck.
        # Uses the address lookup function and distance_list to look up the correct distance between each address
        while j < len(truck2):
            calculated_distance = distances.distance_list[addresses.address_lookup(truck_address2)][addresses.address_lookup(packageTable.lookup(truck2[j], "address"))]

            # Looks for the smallest distance between all of the values looked up in the while loop. If it finds a new smaller distance, it sets min_value to
            # that distance and sets the truck address to the address of the package object with the smallest distance.
            if(float(calculated_distance) < float(min_value)):
                min_value = calculated_distance
                package_to_be_delivered = truck2[j]
                temp_truck_address = [packageTable.lookup(truck2[j], "address")]
            j = j + 1

        # Updates the variables that are keeping track of miles driven, the truck address, and the time.
        # Timestamps the package objects in the hash table with a timestamp of when they are delivered.
        # Removes the package that is delivered from the truck 2 list.
        miles_driven2 = miles_driven2 + float(min_value)
        truck2_temp_time = float(min_value) / 18.0
        truck2_current_time = truck2_current_time + truck2_temp_time
        delivered_package = packageTable.search(package_to_be_delivered)
        truck2_time_to_timestamp = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_current_time * 60, 60))
        delivered_package.timestamp = truck2_time_to_timestamp
        delivered_package.status = "Delivered"
        truck2.remove(package_to_be_delivered)
        truck_address2 = str((temp_truck_address)).lstrip("['").rstrip("']")


    # This algorithm employs the nearest neighbor algorithm and applies it to the truck 3 list and all of the package IDs within it.
    # Searches for the shortest available path from one package object to the next, and calculates time as well as miles traveled.
    # Updates the package objects in the hash table with a timestamp of the time the package is "dropped off".
    # Time Complexity: Two while loops, one nested within the other. O(n^2)
    # Space Complexity: Algorithm contains a hash function search and updates the hash table too. O(n)
    i=0
    truck_address3 = '4001 South 700 East'
    package_to_be_delivered = "None"
    miles_driven3 = 0.0
    truck3_start_time = truck1_current_time
    truck3_current_time = truck1_current_time

    # Loops through the length of the truck3 list, iterating on each object within it. At the end of each iteration, an object is removed from truck3,
    # eventually reducing the truck3 list to 0 and ending the loop
    while i < len(truck3):
        j=0
        min_value = 100.0

        # Loops through every object in the truck2 again, comparing the current address of the truck to the address of each object within the truck.
        # Uses the address lookup function and distance_list to look up the correct distance between each address
        while j < len(truck3):
            calculated_distance = distances.distance_list[addresses.address_lookup(truck_address3)][addresses.address_lookup(packageTable.lookup(truck3[j], "address"))]

            # updates package number 9 to the correct address and zip code after 10:20
            if (('{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_current_time * 60, 60)) >= "10:20")):
                packageTable.search("9").address = "410 S State St"
                packageTable.search("9").zipCode = "84111"

            # Looks for the smallest distance between all of the values looked up in the while loop. If it finds a new smaller distance, it sets min_value to
            # that distance and sets the truck address to the address of the package object with the smallest distance.
            if(float(calculated_distance) < float(min_value)):
                min_value = calculated_distance
                package_to_be_delivered = truck3[j]
                temp_truck_address = [packageTable.lookup(truck3[j], "address")]
            j = j + 1

        # Updates the variables that are keeping track of miles driven, the truck address, and the time.
        # Timestamps the package objects in the hash table with a timestamp of when they are delivered.
        # Removes the package that is delivered from the truck 3 list.
        miles_driven3 = miles_driven3 + float(min_value)
        truck3_temp_time = float(min_value) / 18.0
        truck3_current_time = truck3_current_time + truck3_temp_time
        delivered_package = packageTable.search(package_to_be_delivered)
        truck3_time_to_timestamp = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_current_time * 60, 60))
        delivered_package.timestamp = truck3_time_to_timestamp
        delivered_package.status = "Delivered"
        truck3.remove(package_to_be_delivered)
        truck_address3 = str((temp_truck_address)).lstrip("['").rstrip("']")


    # Time complexity: O(n)
    # Space complexity: O(1)
    def find_status(usertime):
        """
        find_status:
        find_status takes in a user defined time and runs it through many operations to build a report on the current status of the trucks
        and their packages.

        Args:
        usertime: this represents the user-inputted time

        Returns:
        Prints out miles driven and the status of each package using the designated usertime

        Raises:
        Raises no exceptions.

        Time Complexity:
        find_status uses many if statements and while loops. Each if statement and print statement is constant time, or O(1).
        As the number of items in the truck increases, the number of loops ran increases accordingly. O(3n), or O(n) for the whole function.

        Space Complexity:
        There are 3 while loops that each have assignments within them, as well as print statements. While each while loop runs n amount of times,
        no new space is created n times within the loops. No new lists or arrays are created. O(1), constant time.

        """

        i = 0
        j = 0
        k = 0

        # Prints out the status report information for truck 1
        print("Truck 1 Status Report for " + usertime)

        # Calculates what the current miles driven for truck 1 would be based on the inputted user time. Uses the time information for truck 1
        # gathered from the nearest neighbor algorithm that runs automatically.
        truck1_formatted_end_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_current_time * 60, 60))
        truck1_formatted_start_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_start_time * 60, 60))

        # If the inputted usertime is equal to or greater than the end time of truck 1, prints the total miles driven for truck 1.
        if (usertime == truck1_formatted_end_time or usertime > truck1_formatted_end_time):
            print("Truck 1 has driven " + str(miles_driven1)[0:5] + " miles as of " + str(usertime))

        # If the inputted usertime is less than the end time and greater than the start time, calculates the total miles driven so far for truck 1.
        if (usertime < truck1_formatted_end_time and usertime > truck1_formatted_start_time):
            specific_miles_driven1 = (time_adjuster(usertime) - truck1_start_time) * 18.0
            print("Truck 1 has driven " + str(specific_miles_driven1)[0:5] + " miles as of " + str(usertime))

        # If the inputted usertime is less than the start time, prints out that the total miles driven so far for truck 1 is zero because it has not started yet.
        if (usertime <= truck1_formatted_start_time):
            print("Truck 1 has driven 0.0 miles as of " + str(usertime))

        # Uses a while loop that iterates over the static list of truck 1, which was a copied list of truck 1.
        # Checks each package object within the static truck list and compares the inputted user time to the timestamps generated from the
        # nearest neighbor algorithm that ran automatically before. Prints out the current status of where the package would be.
        while i < len(truck1_static_list):
            package_to_check = truck1_static_list[i]
            if (usertime < packageTable.search(
                    package_to_check).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                *divmod(truck1_start_time * 60, 60))):
                print("Package " + packageTable.search(package_to_check).packageID + " is En route")
            if (usertime >= packageTable.search(package_to_check).timestamp):
                print("Package " + packageTable.search(
                    package_to_check).packageID + " was Delivered at " + packageTable.search(
                    package_to_check).timestamp)
            if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_start_time * 60, 60))):
                print("Package " + packageTable.search(package_to_check).packageID + " is At hub")
            i = i + 1


        # prints out the status report information for truck 2
        print("Truck 2 Status Report for " + usertime)

        # Calculates what the current miles driven for truck 2 would be based on the inputted user time. Uses the time information for truck 2
        # gathered from the nearest neighbor algorithm that runs automatically.
        truck2_formatted_end_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_current_time * 60, 60))
        truck2_formatted_start_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_start_time * 60, 60))

        # If the inputted usertime is equal to or greater than the end time of truck 2, prints the total miles driven for truck 2.
        if (usertime == truck2_formatted_end_time or usertime > truck2_formatted_end_time):
            print("Truck 2 has driven " + str(miles_driven2)[0:5] + " miles as of " + str(usertime))

        # If the inputted usertime is less than the end time and greater than the start time, calculates the total miles driven so far for truck 2.
        if (usertime < truck2_formatted_end_time and usertime > truck2_formatted_start_time):
            specific_miles_driven2 = (time_adjuster(usertime) - truck2_start_time) * 18.0
            print("Truck 2 has driven " + str(specific_miles_driven2)[0:5] + " miles as of " + str(usertime))

        # If the inputted usertime is less than the start time, prints out that the total miles driven so far for truck 2 is zero because it has not started yet.
        if (usertime <= truck2_formatted_start_time):
            print("Truck 2 has driven 0.0 miles as of " + str(usertime))

        # Uses a while loop that iterates over the static list of truck 2, which was a copied list of truck 2.
        # Checks each package object within the static truck list and compares the inputted user time to the timestamps generated from the
        # nearest neighbor algorithm that ran automatically before. Prints out the current status of where the package would be.
        while j < len(truck2_static_list):
            package_to_check = truck2_static_list[j]
            if (usertime < packageTable.search(
                    package_to_check).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                *divmod(truck2_start_time * 60, 60))):
                print("Package " + packageTable.search(package_to_check).packageID + " is En route")
            if (usertime >= packageTable.search(package_to_check).timestamp):
                print("Package " + packageTable.search(
                    package_to_check).packageID + " was Delivered at " + packageTable.search(
                    package_to_check).timestamp)
            if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_start_time * 60, 60))):
                print("Package " + packageTable.search(package_to_check).packageID + " is At hub")
            j = j + 1


        # prints out the status report information for truck 3
        print("Truck 3 Status Report for " + usertime)

        # Calculates what the current miles driven for truck 3 would be based on the inputted user time. Uses the time information for truck 3
        # gathered from the nearest neighbor algorithm that runs automatically.
        truck3_formatted_end_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_current_time * 60, 60))
        truck3_formatted_start_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_start_time * 60, 60))

        # If the inputted usertime is equal to or greater than the end time of truck 3, prints the total miles driven for truck 3.
        if (usertime == truck3_formatted_end_time or usertime > truck3_formatted_end_time):
            print("Truck 3 has driven " + str(miles_driven3)[0:5] + " miles as of " + str(usertime))

        # If the inputted usertime is less than the end time and greater than the start time, calculates the total miles driven so far for truck 3.
        if (usertime < truck3_formatted_end_time and usertime > truck3_formatted_start_time):
            specific_miles_driven3 = (time_adjuster(usertime) - truck3_start_time) * 18.0
            print("Truck 3 has driven " + str(specific_miles_driven3)[0:5] + " miles as of " + str(usertime))

        # If the inputted usertime is less than the start time, prints out that the total miles driven so far for truck 3 is zero because it has not started yet.
        if (usertime <= truck3_formatted_start_time):
            print("Truck 3 has driven 0.0 miles as of " + str(usertime))

        # Uses a while loop that iterates over the static list of truck 3, which was a copied list of truck 3.
        # Checks each package object within the static truck list and compares the inputted user time to the timestamps generated from the
        # nearest neighbor algorithm that ran automatically before. Prints out the current status of where the package would be.
        while k < len(truck3_static_list):
            package_to_check = truck3_static_list[k]
            if (usertime < packageTable.search(
                    package_to_check).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                *divmod(truck1_current_time * 60, 60))):
                print("Package " + packageTable.search(package_to_check).packageID + " is En route")
            if (usertime >= packageTable.search(package_to_check).timestamp):
                print("Package " + packageTable.search(
                    package_to_check).packageID + " was Delivered at " + packageTable.search(
                    package_to_check).timestamp)
            if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_start_time * 60, 60))):
                print("Package " + packageTable.search(package_to_check).packageID + " is At hub")
            k = k + 1


    # When the user inputs 1, the following code runs
    # Time complexity: O(1)
    # Space complexity: O(1)
    if(userinput == "1"):

        # Runs the find status function with user time as an argument
        find_status(usertime)

        # Calculates the total miles driven for each truck dependent on the entered user time, comparing it to variables and variable data
        # gathered from the nearest neighbor algorithm running automatically beforehand.
        truck1_formatted_start_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_start_time * 60, 60))
        truck1_formatted_end_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_current_time * 60, 60))
        truck2_formatted_end_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_current_time * 60, 60))
        truck2_formatted_start_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_start_time * 60, 60))
        truck3_formatted_end_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_current_time * 60, 60))
        if (usertime < truck2_formatted_end_time and usertime > truck1_formatted_start_time):
            total_miles_driven1_for_usertime = (time_adjuster(usertime) - truck1_start_time) * 18
            if (usertime > truck1_formatted_end_time):
                total_miles_driven1_for_usertime = miles_driven1
            total_miles_driven2_for_usertime = (time_adjuster(usertime) - truck2_start_time) * 18
            if (usertime > truck2_formatted_end_time):
                total_miles_driven2_for_usertime = miles_driven2
            total_miles_driven3_for_usertime = (time_adjuster(usertime) - truck3_start_time) * 18
            if (usertime > truck3_formatted_end_time):
                total_miles_driven3_for_usertime = miles_driven3
            if (usertime < truck1_formatted_end_time):
                total_miles_driven3_for_usertime = 0.0
            if (usertime < truck2_formatted_start_time):
                total_miles_driven2_for_usertime = 0.0
            print("Total miles driven between trucks is approximately " + str(total_miles_driven1_for_usertime + total_miles_driven2_for_usertime + total_miles_driven3_for_usertime)[0:5] + " miles as of " + usertime + ".")

        if (usertime >= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_current_time * 60, 60))):
            print("Total miles driven between trucks is approximately " + str(miles_driven1 + miles_driven2 + miles_driven3)[0:6] + " miles.")

        if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_start_time * 60, 60))):
            print("Total miles driven between trucks is 0.0 miles.")

    # Time complexity: O(n)
    # Space complexity O(1)
    def find_status_specific_package(usertime, package_to_check):

        """
        find_status_specific_package:
        find_status_specific_package takes in a user defined time and a specific package object as a string and returns details of
        the specified package that correspond to the selected usertime.

        Args:
        usertime: this represents the user-inputted time
        package_to_check: this represents the package the user wants the details of

        Returns:
        Prints out the current details of the package object, as well as the delivery status of it.

        Raises:
        Raises no exceptions.

        Time Complexity:
        find_status_specific_package uses many if statements and print statements that equal up to O(1). However, there are three if statements
        that contain in statements, totalling up to O(3n), which makes the time complexity of the function overall O(n).

        Space Complexity:
        There are 3 in statements that each runs n amount of times as it searches if the package_to_check is in the truck lists, but
        no new space is created n times within any statement. No new lists or arrays are created. O(1), constant time.

        """

        # Updates package number 9 to display the correct address if the user inputs a time before 10:20, as the address is updated automatically
        # through the nearest neighbor algorithm. This reverts that update to correspond to package 9's information accurately before 10:20.
        if((package_to_check) == "9"):
            if (usertime < "10:20"):
                packageTable.search("9").address = "300 State St"
                packageTable.search("9").zipCode = "84103"


        # This if statement checks to see if the current package is in the truck 1 static list. If it is, it updates the status and timestamp information
        # for the corresponding package in the hash table, comparing the inputted user time with the timestamps generated from the nearest neighbor algorithm
        # from before.
        if (package_to_check in truck1_static_list):

            # Checks if user time is greater than the timestamp marked in the hash table
            if (usertime >= packageTable.search(package_to_check).timestamp):
                packageTable.search(package_to_check).status = "Delivered at " + packageTable.search(package_to_check).timestamp
                print("Delivered by truck 1 at " + packageTable.search(package_to_check).timestamp)
                print(packageTable.search(user_package_input))

            # Checks if user time is less than the timestamp marked in the hash table and is greater than the start time for the truck
            if (usertime < packageTable.search(package_to_check).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                    *divmod(truck1_start_time * 60, 60))):
                packageTable.search(package_to_check).status = "En route"
                packageTable.search(package_to_check).timestamp = " "
                print("En route on truck 1.")
                print(packageTable.search(user_package_input))

            # Checks if the user time is less than the start time for the truck
            if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_start_time * 60, 60))):
                packageTable.search(package_to_check).status = "At hub"
                packageTable.search(package_to_check).timestamp = " "
                print("At hub, waiting to be loaded into truck 1.")
                print(packageTable.search(user_package_input))


        # This if statement checks to see if the current package is in the truck 2 static list. If it is, it updates the status and timestamp information
        # for the corresponding package in the hash table, comparing the inputted user time with the timestamps generated from the nearest neighbor algorithm
        # from before.
        if (package_to_check in truck2_static_list):

            # Checks if user time is greater than the timestamp marked in the hash table
            if (usertime >= packageTable.search(package_to_check).timestamp):
                packageTable.search(package_to_check).status = "Delivered at " + packageTable.search(package_to_check).timestamp
                print("Delivered by truck 2 at " + packageTable.search(package_to_check).timestamp)
                print(packageTable.search(user_package_input))

            # Checks if user time is less than the timestamp marked in the hash table and is greater than the start time for the truck
            if (usertime < packageTable.search(package_to_check).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                    *divmod(truck2_start_time * 60, 60))):
                packageTable.search(package_to_check).status = "En route"
                packageTable.search(package_to_check).timestamp = " "
                print("En route on truck 2.")
                print(packageTable.search(user_package_input))

            # Checks if the user time is less than the start time for the truck
            if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_start_time * 60, 60))):
                packageTable.search(package_to_check).status = "At hub"
                packageTable.search(package_to_check).timestamp = " "
                print("At hub, waiting to be loaded into truck 2.")
                print(packageTable.search(user_package_input))


        # This if statement checks to see if the current package is in the truck 3 static list. If it is, it updates the status and timestamp information
        # for the corresponding package in the hash table, comparing the inputted user time with the timestamps generated from the nearest neighbor algorithm
        # from before.
        if (package_to_check in truck3_static_list):

            # Checks if user time is greater than the timestamp marked in the hash table
            if (usertime >= packageTable.search(package_to_check).timestamp):
                packageTable.search(package_to_check).status = "Delivered at " + packageTable.search(package_to_check).timestamp
                print("Delivered by truck 3 at " + packageTable.search(package_to_check).timestamp)
                print(packageTable.search(user_package_input))

            # Checks if user time is less than the timestamp marked in the hash table and is greater than the start time for the truck
            if (usertime < packageTable.search(package_to_check).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                    *divmod(truck3_start_time * 60, 60))):
                packageTable.search(package_to_check).status = "En route"
                packageTable.search(package_to_check).timestamp = " "
                print("En route on truck 3.")
                print(packageTable.search(user_package_input))

            # Checks if the user time is less than the start time for the truck
            if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_start_time * 60, 60))):
                packageTable.search(package_to_check).status = "At hub"
                packageTable.search(package_to_check).timestamp = " "
                print("At hub, waiting to be loaded into truck 3.")
                print(packageTable.search(user_package_input))


    # When the user inputs 2, the following code runs
    # Takes in a user inputted package number and runs it through the find_status_specific_package function as an argument
    # Time Complexity: O(n)
    # Space Complexity: 0(1)
    if(userinput == "2"):
        valid_package = False

        # While loop that asks for a package number
        while (valid_package != True):
            user_package_input = input("Select a package: ")

            # Checks to see if the user is inputting a valid package number that is within the hash table and runs the find_status_specific_package function
            if(packageTable.search(user_package_input)):
                valid_package = True
                find_status_specific_package(usertime, user_package_input)

            # Prints out if the package the user entered is not within the hash table
            if(packageTable.search((user_package_input)) == None):
                print("Package not found. Please enter a valid package ID.")


    # When the user inputs 3, the following code runs
    # Prints out all package data from the hash table and sets the status and timestamp on them depending on the user input
    # Time complexity: A while loop that loops through all packages, and for each package object, it searches through 3 separate lists that equal up to
    # the total of all_packages. O(n^2)
    # Space complexity: creates a concatenated list of current truck lists. O(n)
    if(userinput == "3"):
        print("All package data as of " + usertime)

        # A concatenated list of the current static truck lists is created and sorted
        all_packages = truck1_static_list + truck2_static_list + truck3_static_list
        all_packages.sort(key=float)
        i = 1

        # Updates package number 9 to display the correct address if the user inputs a time before 10:20, as the address is updated automatically
        # through the nearest neighbor algorithm. This reverts that update to correspond to package 9's information accurately before 10:20.
        if (usertime < "10:20"):
            packageTable.search("9").address = "300 State St"
            packageTable.search("9").zipCode = "84103"

        # Loops through every package in the all_packages list and checks to see if the package was in truck 1, truck 2, or truck 3.
        # Updates the corresponding hash table package information for each package.
        while i < len(all_packages)+1:

            # Checks to see if the package is in truck 1 and updates the information accordingly, comparing the user time with
            # the timestamps generated from the nearest neighbor algorithm ran automatically before.
            if (str(i) in truck1_static_list):
                if (usertime >= packageTable.search(str(i)).timestamp):
                    packageTable.search(str(i)).status = "Delivered at " + packageTable.search(str(i)).timestamp
                if (usertime < packageTable.search(str(i)).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                        *divmod(truck1_start_time * 60, 60))):
                    packageTable.search(str(i)).status = "En route on truck 1."
                    packageTable.search(str(i)).timestamp = " "
                if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck1_start_time * 60, 60))):
                    packageTable.search(str(i)).status = "At hub, waiting to be loaded into truck 1."
                    packageTable.search(str(i)).timestamp = " "

            # Checks to see if the package is in truck 2 and updates the information accordingly, comparing the user time with
            # the timestamps generated from the nearest neighbor algorithm ran automatically before.
            if (str(i) in truck2_static_list):
                if (usertime >= packageTable.search(str(i)).timestamp):
                    packageTable.search(str(i)).status = "Delivered at " + packageTable.search(str(i)).timestamp
                if (usertime < packageTable.search(str(i)).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                        *divmod(truck2_start_time * 60, 60))):
                    packageTable.search(str(i)).status = "En route on truck 2."
                    packageTable.search(str(i)).timestamp = " "
                if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck2_start_time * 60, 60))):
                    packageTable.search(str(i)).status = "At hub, waiting to be loaded into truck 2."
                    packageTable.search(str(i)).timestamp = " "

            # Checks to see if the package is in truck 3 and updates the information accordingly, comparing the user time with
            # the timestamps generated from the nearest neighbor algorithm ran automatically before.
            if (str(i) in truck3_static_list):
                if (usertime >= packageTable.search(str(i)).timestamp):
                    packageTable.search(str(i)).status = "Delivered at " + packageTable.search(str(i)).timestamp
                if (usertime < packageTable.search(str(i)).timestamp and usertime > '{0:02.0f}:{1:02.0f}'.format(
                        *divmod(truck3_start_time * 60, 60))):
                    packageTable.search(str(i)).status = "En route on truck 3."
                    packageTable.search(str(i)).timestamp = " "
                if (usertime <= '{0:02.0f}:{1:02.0f}'.format(*divmod(truck3_start_time * 60, 60))):
                    packageTable.search(str(i)).status = "At hub, waiting to be loaded into truck 3."
                    packageTable.search(str(i)).timestamp = " "

            # Prints out each package object data from the hash table in the same order that it iterates through with the current while loop,
            # with the newly updated information from the previous if statements.
            print(packageTable.search(str(i)))
            i = i+1

    # When the user inputs 5, the following code runs
    # This exits the program
    if (userinput == "5"):
        quit()

