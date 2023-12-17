from colorama import Fore, Style
from ClassPlane import Plane
from ClassPassenger import Passenger
from Logic import srt, filter

class Airport:
    def __init__(self):
        self.__planes = []
    
    @property
    def planes(self):
        return self.__planes
    @planes.setter
    def addPlane(self, plane):
        self.__planes.append(plane)

    def __str__(self):
        return str(self.planes)
    def __repr__(self):
        return str(self)
    
    #Print the list of planes
    #Input: -
    #Output: -
    def printPlanes(self):
        for plane in self.__planes:
            print(plane)

    #Add a plane to the list of planes
    #Input: name, company, seats, destinations
    #Output: -
    def addPlane(self, name, company, seats, destination):
        try:
            if type(name) != str or type(company) != str or type(seats) != int or type(destination) != str :
                raise ValueError("The arguments are not of the right type")
            self.__planes.append(Plane(name, company, seats, destination))
        except ValueError as ve:
            return ve
        
    #Remove a plane from the list of planes
    #Input: plane
    #Output: -
    def removePlane(self, plane):
        try:
            if type(plane) != Plane:
                raise ValueError("The argument is not a plane")
            if plane not in self.__planes:
                raise ValueError("The plane does not exist")
            self.__planes.remove(plane)
        except ValueError as ve:
            return ve
        
    #Update a plane from the list of planes
    #Input: plane, name, company, seats, destination, passengers
    #Output: -
    def updatePlane(self, plane, name, company, seats, destination, passengers):
        try:
            if type(plane) != Plane or type(name) != str or type(company) != str or type(seats) != int or type(destination) != str or type(passengers) != list:
                raise ValueError("The arguments are not of the right type")
            if plane not in self.__planes:
                raise ValueError("The plane does not exist")
            plane.name = name
            plane.company = company
            plane.seats = seats
            plane.destination = destination
            plane.passengers = passengers
        except ValueError as ve:
            return ve
    
    #Sort the passengers in the plane by the last name
    #Input: -
    #Output: a list of passengers
    def sortByLName(self):
        for plane in self.__planes:
            srt(plane.passengers, key = lambda x : x.lastName)

    #Sort the list of planes by the number of passengers
    #Input: -
    #Output: a list of planes
    def sortByNrPassengers(self):
        srt(self.__planes, key = lambda x : len(x.passengers))

    #Sort the list of planes according to the number of passengers with the first name starting with a given substring
    #Input: a substring
    #Output: a list of planes
    def sortByNrPassengersWithSubstr(self, substr):
        results = []
        try:
            if type(substr) != str:
                raise ValueError("The argument is not a string")
            for plane in self.__planes:
                results.append(filter(plane.passengers, key = lambda x : x.firstName.startswith(substr)))
        except ValueError as ve:
            return ve
        return results
    
    #Sort the list of planes according to the string obtained by concatenating the number of passengers and the destination
    #Input: -
    #Output: a list of planes
    def sortWConcatination(self):
        srt(self.__planes, key = lambda x : x.concatenate())

    #Sort the passengers by the passport number
    #Input: -
    #output: -
    def sortByPassportNr(self):
        for plane in self.__planes:
            srt(plane.passengers, key = lambda x : x.passportNr)

    #Identify planes that have passengers with passport numbers starting with the same 3 letters
    #Input: -
    #Output: a list of planes
    def identifyPlanes(self):
        results = []
        for plane in self.__plane:
            self.sortByPassportNr()
            for i in range(len(plane.passegers)-1):
                if plane.passengers[i].passportNr[:3] == plane.passengers[i+1].passportNr[:3]:
                    results.append(plane)
                    break
        return results
    
    #Identify passengers from a given plane for which the first name or last name contains a given string as a parameter
    #Input: a plane name, a string
    #Output: a list of passengers
    def identifyByNameWString(self, plane, string):
        results = []
        try:
            if type(plane) != str or type(string) != str:
                raise ValueError("The arguments are not strings")
            for passenger in plane.passengers:
                if string in passenger.firstName or string in passenger.lastName:
                    results.append(passenger)
        except ValueError as ve:
            return ve
        return results
    
    #Identify plane/palnes where there is a passenger with a given name 
    #Input: a string(name of the passenger))
    #Output: a list of planes
    def identifyPlaneByAGivenName(self, name):
        results = []
        try:
            if type(name) != str:
                raise ValueError("The argument is not a string")
            for plane in self.__plane:
                for passenger in plane.passengers:
                    if name == passenger.firstName or name == passenger.lastName:
                        results.append(plane)
                        break
        except ValueError as ve:
            return ve
        return results
    
    #From a group of k passengers from the same plane, but with different last names
    #Input: an integer
    #Output: a list of passengers
    def groupOfPassengers(self, k):
        results = []
        try:
            if type(k) != int:
                raise ValueError("The argument is not an integer")
            for plane in self.__planes:
                results.append(plane.name)
                group = []
                for passenger in plane.passengers:
                    if passenger.lastName not in group:
                        group.append(passenger.firstName + " " + passenger.lastName)
                results.append(group[k:])
        except ValueError as ve:
            return ve
        return results
    
    #Creats a list of all the destinations in the airport
    #Input: -
    #Output: a list of strings
    def destinations(self):
        destinations = []
        for plane in self.__planes:
            if plane.destination not in destinations:
                destinations.append(plane.destination)
    
    #form groups of planes with the same destination but different companies
    #Input: an integer
    #Output: a list of planes
    def groupOfPlanes(self, k):
        results = []
        try:
            if type(k) != int:
                raise ValueError("The argument is not an integer")
            for destination in self.destinations():
                results.append(destination)
                group = []
                for plane in self.__planes:
                    if plane.destination == destination and plane.company not in group:
                        group.append(plane.name)
                results.append(group[k:])
        except ValueError as ve:
            return ve
        return results
    

    

