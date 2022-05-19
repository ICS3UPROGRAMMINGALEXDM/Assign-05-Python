#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: This assignment I will be making a pogram that either
# calculates the acceleration given the force and mass or b) calculates the
# hypoteneuse of a right angle triangle given the base and height
import math

# This function calculates the acceleration with the given mass and force
def calc_acc(force, mass):
    acc = force / mass
    # returning to  where the function was called
    return acc


# This function calulates teh hypoteneuse with the inputted base and height
def calc_hyp(base, height):
    # calculations
    hyp_sqr = (base**2) + (height**2)
    hyp = math.sqrt(hyp_sqr)
    # returns it to where the function was called
    return hyp


# This function calculates the average speed given the distance and time
def calc_speed(time, distance):
    speed = distance / time
    # returns to the where the function was called
    return speed


# This is the function that gets the unit and measurements and will later call
# another function to make the calculations for the hypoteneuse
def hypoteneuse():
    unit_failure = True
    # Allows to re-enter the unit if it was incorrectly inputted originally
    while unit_failure:

        unit = input(
            "Which of the following units would you like to use? " + "(cm, m, mm, km): "
        )
        # Ensuring a positive number
        if (unit == "cm") or (unit == "mm") or (unit == "m") or (unit == "km"):
            measure_failure = True
        else:
            print("I don't understand, try again!")
        # Allows to re-enter measurements if they were incorrectly inputted
        while measure_failure:
            u_base = input("What is the base length of your triangle: ")
            u_height = input("What is the height of your triangle: ")

            try:
                # converting to float
                base_flt = float(u_base)
                height_flt = float(u_height)

                if (base_flt > 0) and (height_flt > 0):
                    measure_failure = False
                    unit_failure = False
                    # calling the function that will calculate the hhypoteneuse
                    answer1 = calc_hyp(base_flt, height_flt)
                    # Displays the results
                    print(
                        "The hypoteneuse of your triangle is {} {}".format(
                            answer1, unit
                        )
                    )
                else:
                    print("Numbers must be positive")
            except ValueError:
                print("Numbers entered weren't valid numbers")


# This is the function that gets the unit and measurements and will later call
# another function to make the calculations for the acceleration
def acceleration(acc_unit="m/s"):
    measure_failure2 = True
    while measure_failure2:
        # getting user input
        u_force = input("Input the force (Already set to newtons): ")
        u_mass = input("Enter the mass (Already set to kg): ")

        try:
            # converting to float
            force_flt = float(u_force)
            mass_flt = float(u_mass)
            # Ensuring mass is positive
            if mass_flt > 0:
                measure_failure2 = False
                # calling the funciton that will calculate the acceleration
                answer2 = calc_acc(force_flt, mass_flt)

                print("The resulting acceleration is {}{}^2".format(answer2, acc_unit))
            else:
                print("The inputted mass can't be negative")
        except ValueError:
            print("Numbers were entered")


# This is the function that gets the unit and measurements and will later call
# another function to make the calculations for the average speed
def speed():
    unit_failure2 = True
    # Allows to re-enter the unit if it was invalid
    while unit_failure2:
        time_unit = input("Please enter the unit of time(s, min, hr): ")
        distance_unit = input("Please enter the unit of distance(m, km): ")
        # Ensuring that all units were valid
        if ((distance_unit == "m") or (distance_unit == "km")) and (
            (time_unit == "s") or (time_unit == "min") or (time_unit == "hr")
        ):
            # allows for the next part of the function to continue
            measure_failure3 = True
        else:
            print("Unit(s) entered were incorrect")
        # allows for the measurements to be re-entered if they were invalid
        while measure_failure3:
            # getting user input
            u_time = input("Enter how long the trip took: ")
            u_distance = input("Enter the distance: ")

            try:
                # converting to float
                time_flt = float(u_time)
                distance_flt = float(u_distance)
                # Ensuring positive numbers
                if (time_flt > 0) and (distance_flt > 0):
                    unit_failure2 = False
                    measure_failure3 = False
                    # calls the function that'll calculate the average speed
                    answer3 = calc_speed(time_flt, distance_flt)
                    # Display results
                    print(
                        "The average speed is {}{}/{}".format(
                            answer3, distance_unit, time_unit
                        )
                    )
                else:
                    print("Inputted numbers must be positive")
            except ValueError:
                print("Inputted numbers weren't valid numbers")


def main():
    restart_loop = True
    # Loop allows for the user to choose a new program once the calculations
    # are finished
    while restart_loop:
        retry_loop = True

        choice = input(
            "Choose a calculator to use: \n\n"
            + "1 - Hypotneuse given base and height \n2 - Acceleration given "
            + "mass and force\n3 - Average speed given distance and time\n\n"
        )
        # Calls whichever fnction was chosen
        if choice == "1":
            hypoteneuse()
        elif choice == "2":
            acceleration()
        elif choice == "3":
            speed()
        else:
            print("I don't understand, please try again!")

        while retry_loop:
            choice2 = input("Would you like to play again? (y/n): ")
            # this is what decides whether or not to run the program again
            if choice2 == "y":
                retry_loop = False
            elif choice2 == "n":
                retry_loop = False
                restart_loop = False
            else:
                print("I don't understand, try again!")


if __name__ == "__main__":
    main()
