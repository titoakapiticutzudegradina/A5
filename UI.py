from colorama import Fore, Style
from os import system
from time import sleep
from Airport import Airport
from ClassPassenger import Passenger
from ClassPlane import Plane

def menu():
    print(Fore.YELLOW)
    print("0. Exit")
    print("1. Add a plane")
    print("2. Remove a plane")
    print("3. Update a plane")
    print("4. Add a passenger")
    print("5. Remove a passenger")
    print("6. Update a passenger")
    print("7. Sort passengers by last name")
    print("8. Sort the planes by the number of passengers")
    print("9. Sort the planes according to the number of passengers with the first name starting with a given substring")
    print("10. Sort the planes according to the stringg obtained by concatenating the number of passengers and the destination")
    print("11. Sort the passengers by the passport number")
    print("12. Identify planes that have passengers with passport numbers starting with the same 3 letters")
    print("13. Identify passengers from a given plane for which the first or last name contain a substring")
    print("14. Identify plane/planes where rhere is a passenger with a given name")
    print("15. Show a number of passengers from a plane with different last names")
    print("16. Show a number of planes with the same destination, but from different companies")
    print(Style.RESET_ALL)

airport = Airport()
airport.addPlane("Plane 911", "MAG", 28, "Turnurile Gemene")
airport.planes[0].addPassengers = [Passenger( "Anisia", "Bantu", 1234), Passenger("Gabriel", "Hanu", 8454 ), Passenger("Diana", "Grigore", 6969), Passenger("Stefan", "Baldean", 6660)]
airport.addPlane("Plane 356", "HGMG", 15, "New York")
airport.planes[1].addPassengers = [Passenger("Jhon", "Doe", 3876), Passenger("Jane", "Smith", 3875), Passenger("Jhon", "Smith", 7864), Passenger("Coco", "Cioco", 1234)]
airport.addPlane("Private Jet", "CM", 7, "Virginia")
airport.planes[2].addPassengers = [Passenger("Aron", "Hotchner", 1234), Passenger("Derek", "Morgan", 1234),Passenger("Spancer", "Ried", 1780), Passenger("Penelope", "Garcia", 1234), Passenger("Emily", "Prentiss", 1234)]
airport.addPlane("Plane 854", "ASD", 10, "Amsterdam")
airport.planes[3].addPassengers = [Passenger("Carla", "Lupu", 4444), Passenger("Raluca", "Cret", 4446), Passenger("Alexia", "Bora", 4445), Passenger("Andreea", "Bora", 4447)]
airport.addPlane("Plane 123", "MAG", 10, "Amsterdam")
airport.planes[4].addPassengers = [Passenger("Tito", "Catanas", 1809), Passenger("Mihai", "Ghilencea", 1810), Passenger("Andrei", "Bora", 1811), Passenger("Andreea", "Bora", 1812)]

def UI():
    try:
        system("cls || clear")
        print(Fore.YELLOW + "Welcome to the Airport Management System!" + Style.RESET_ALL)
        while True:
            menu()
            print()
            print(Fore.LIGHTCYAN_EX + "The current list of planes is: \n " + Style.RESET_ALL + str(airport.planes))
            print()
            option = int(input(Fore.LIGHTBLUE_EX + "Please enter an option: "  + Style.RESET_ALL))
            if option == 0:
                system("cls || clear")
                print(Fore.GREEN + "Very good option! See you never, bye bye :) !" + Style.RESET_ALL)
                break
            elif option == 1:
                system("cls || clear")
                print(Fore.LIGHTGREEN_EX + "You have chosen to add a plane" + Style.RESET_ALL)
                name = input(Fore.LIGHTBLUE_EX + "Please, Master, enter the name of the plane : " + Style.RESET_ALL)
                company = input(Fore.LIGHTBLUE_EX + "Please, Master, enter the company of the plane : " + Style.RESET_ALL)
                seats = int(input(Fore.LIGHTBLUE_EX + "Please, Master, enter the number of seats of the plane : " + Style.RESET_ALL))
                destination = input(Fore.LIGHTBLUE_EX + "Please, Master, enter the destination of the plane : " + Style.RESET_ALL)
                airport.addPlane(name, company, seats, destination)
                system("cls || clear")
                print(Fore.GREEN + "The plane has been added successfully!" + Style.RESET_ALL)
                answer = input(Fore.LIGHTCYAN_EX + "Do you wish to add a passenger to this plane too? (y/n): " + Style.RESET_ALL)
                if answer == 'y':
                    firstName = input(Fore.LIGHTBLUE_EX + "Please, Master, enter the first name of the passenger : " + Style.RESET_ALL)
                    lastName = input(Fore.LIGHTBLUE_EX + "Please, Master, enter the last name of the passenger : " + Style.RESET_ALL)
                    passportNr = int(input(Fore.LIGHTBLUE_EX + "Please, Master, enter the passport number of the passenger : " + Style.RESET_ALL))
                    airport.planes[len(airport.planes)-1].addPassenger(firstName, lastName, passportNr)
                    print(Fore.GREEN + "The passenger has been added successfully!" + Style.RESET_ALL)
                else:
                    system("cls || clear")
    except Exception as e:
        print(e)
        sleep(2)
UI()

    



