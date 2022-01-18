# Foreign Keys: 
'''
HemployeeID
SupercomputerID
AemployeeID
GameID
DemployeeID
PgameID
FgameID
CustomerID
EmployeeID
'''

import random
from datetime import datetime, timedelta
def gen_datetime(min_year=1900, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()
from random import randint
import names
from random_word import RandomWords
import random
import datetime

# create function accepting a single parameter, the year as a four digit number
def get_random_date(year):

    # try to get a date
    try:
        return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')

    # if the value happens to be in the leap year range, try again
    except ValueError:
        get_random_date(year)
# Employee Table
# INSERT INTO Employee_T  (EmployeeID, EmployeeType, EmployeeName)
# VALUES  (498, 'p', 'George Michael');
i = 0
EmployeeIDS = []
EmployeeType = []
while i <= 35:
    EmployeeID = randint(100, 999)
    EmployeeIDS.append(EmployeeID)
    if i <= 11:
        types = "h"
    if i <= 23 and i >= 12:
        types = "a"
    if i >= 24:
        types = "d"
    print("INSERT INTO Employee_T (EmployeeID, EmployeeType, EmployeeName)\n VALUES (" + str(EmployeeID) + ", '" + str(types) + "', '" + str(names.get_full_name()) + "');")
    i = i + 1
# Hardware Eng Table
# INSERT INTO HardwareEng_T  (HemployeeID, HmanagerID)
# VALUES  (444, 444);
HEngIDS = []
i = 0
j = 1
while i <= 11:
    ID = randint(0, 11)
    print("INSERT INTO HardwareEng_T (HemployeeID, HmanagerID)\n VALUES (" + str(EmployeeIDS[i]) + ", " + str(EmployeeIDS[j]) + ");")
    i = i + 1
    if j < 11:
        j = j + 1
    else:
        j = 1
# Supercomputer Table
# INSERT INTO Supercomputer_T (SupercomputerID, Capacity, LocationArea)
# VALUES (444, 444, Spain)
SupercomputerIDS = []
i = 0
while i <= 35:
    ID = randint(100, 999)
    ID2 = randint(100, 999)
    SupercomputerIDS.append(ID)
    Location = randint(1000000, 9999999)
    print("INSERT INTO Supercomputer_T (SupercomputerID, Capacity, LocationArea)\n VALUES (" + str(ID) + ", " + str(ID2) + ", " + str(Location) + ");")
    i = i + 1
# Maintenance Table
# INSERT INTO Maintenance_T (SupercomputerID, HemployeeID, TimeSpent)
# VALUES (444, 444, 44)
i = 0
while i <= 35:
    ID = randint(0, 35)
    ID2 = randint(0, 11)
    Time = randint(00, 99)
    print("INSERT INTO Maintenance_T (SupercomputerID, HemployeeID, TimeSpent)\n VALUES (" + str(SupercomputerIDS[ID]) + ", " + str(EmployeeIDS[j]) + ", " + str(Time) + ");")
    i = i + 1
    if j < 11:
        j = j + 1
    else:
        j = 1
# Administrator Table
# INSERT INTO Administrator_T (AemployeeID)
# VALUES (444)
i = 12
while i <= 23:
    print("INSERT INTO Administrator_T (AemployeeID)\n VALUES (" + str(EmployeeIDS[i]) + ");")
    i = i + 1
# Video Game Table
# INSERT INTO VideoGame_T (GameID, ReleaseDate, GameType, VideoGameName)
i = 0
GameIDS = []
while i <= 35:
    ID = randint(100, 999)
    ID2 = randint(100, 999)
    if i <= 17:
        types = "f"
    if i > 17:
        types = "p"
    GameIDS.append(ID)
    print("INSERT INTO VideoGame_T (GameID, ReleaseDate, GameType, VideoGameName)\n VALUES (" + str(ID) + ", '" + str(get_random_date(2016)) + "', '" + str(types) + "', '" + str(names.get_last_name()) + "');")
    i = i + 1
# Server Table
# INSERT INTO Server_T (ServerID, ServerName, Bandwidth, SupercomputerID, GameID)
i = 0
ServerIDS = []
while i <= 35:
    ID = randint(100, 999)
    ID2 = randint(100, 999)
    ServerIDS.append(ID)
    print("INSERT INTO Server_T (ServerID, ServerName, Bandwidth, SupercomputerID, GameID)\n VALUES (" + str(ID) + ", '" + str(names.get_full_name()) + "', " + str(ID2) + ", " + str(SupercomputerIDS[i]) + ", " + str(GameIDS[i]) + ");")
    i = i + 1
# Server Admin Table
# INSERT INTO ServerAdmin_T (ServerID, AemployeeID)
i = 0
j = 12
while i <= 35:
    print("INSERT INTO ServerAdmin_T (ServerID, AemployeeID)\n VALUES (" + str(ServerIDS[i]) + ", " + str(EmployeeIDS[j]) + ");")
    i = i + 1
    if j < 23:
        j = j + 1
    if j == 23:
        j + 12
# Administrator Permission Number Table
# INSERT INTO AdministratorPermission_T (AemployeeID, PermissionNumber)
i = 12
while i <= 23:
    number = randint(10000000, 99999999)
    print("INSERT INTO AdministratorPermission_T (AemployeeID, PermissionNumber)\n VALUES (" + str(EmployeeIDS[i]) + ", " + str(number) + ");")
    i = i + 1
# Developer Table
# INSERT INTO Developer_T (DemployeeID, AemployeeID)
i = 24
j = 12
while i <= 35:
    print("INSERT INTO Developer_T (DemployeeID, AemployeeID)\n VALUES (" + str(EmployeeIDS[i]) + ", " + str(EmployeeIDS[j]) + ");")
    if j < 23:
        j = j + 1
    if j == 23:
        j + 12
    i = i + 1
# Developer Skills Table
# INSERT INTO DeveloperSkills_T (DemployeeID, Skill)
i = 24
while i <= 35:
    print("INSERT INTO DeveloperSkills_T (DemployeeID, Skill)\n VALUES (" + str(EmployeeIDS[i]) + ", '" + str(names.get_last_name()) + "');")
    i = i + 1
# Development Table
# INSERT INTO Development_T (DemployeeID, GameID, Checkintime, Checkouttime, Feature)
i = 0
j = 24
while i <= 35:
    print("INSERT INTO Development_T (DemployeeID, GameID, Checkintime, Checkouttime, Feature)\n VALUES (" + str(EmployeeIDS[j]) + ", " + str(GameIDS[i]) + ", '" + str(get_random_date(2016)) + "', '" + str(get_random_date(2016)) + "', '" + str(names.get_last_name()) + "');")
    i = i + 1
    if j == 35:
        j = 24
    else:
        j = j + 1
# Customer Table
# INSERT INTO Customer_T (CustomerID, CustomerName, CustomerIPAddress)
i = 0
CustomerIDS = []
while i <= 35:
    ID = randint(100, 999)
    ID2 = randint(10000000, 99999999)
    CustomerIDS.append(ID)
    print("INSERT INTO Customer_T (CustomerID, CustomerName, CustomerIPAddress)\n VALUES (" + str(ID) + ", '" + str(names.get_full_name()) + "', " + str(ID2) + ");")
    i = i + 1
# P2P Table
# INSERT INTO P2P_T (PgameID, Price)
i = 18
while i <= 35:
    ID = randint(10, 99)
    print("INSERT INTO P2P_T (PgameID, Price)\n VALUES (" + str(GameIDS[i]) + ", " + str(ID) + ");")
    i = i + 1
# F2P Table
# INSERT INTO F2P_T (FgameID)
i = 0
while i <= 17:
    ID = randint(10, 99)
    print("INSERT INTO F2P_T (FgameID)\n VALUES (" + str(GameIDS[i]) + ");")
    i = i + 1
# Download Table
# INSERT INTO Download_T (FgameID, CustomerID)
i = 0
while i <= 17:
    print("INSERT INTO Download_T (FgameID, CustomerID)\n VALUES (" + str(GameIDS[i]) + ", " + str(CustomerIDS[i]) + ");")
    i = i + 1
# Free Account Table
# INSERT INTO FreeAccount_T (FreeAccountID, CharacterName, CharacterType, CharacterCreationDate, FgameID, CustomerID)
i = 0
while i <= 17:
    ID = randint(100, 999)
    print("INSERT INTO FreeAccount_T (FreeAccountID, CharacterName, CharacterType, CharacterCreationDate, FgameID, CustomerID)\n VALUES (" + str(ID) + ", '" + str(names.get_full_name()) + "', '" + str(names.get_first_name()) + "', '" + str(get_random_date(2016)) + "', " + str(GameIDS[i]) + ", " + str(CustomerIDS[i]) + ");")
    i = i + 1
# Purchase Table
# INSERT INTO Purchase_T (CustomerID, PgameID)
i = 18
while i <= 35:
    print("INSERT INTO Purchase_T (CustomerID, PgameID)\n VALUES (" + str(CustomerIDS[i]) + ", " + str(GameIDS[i]) + ");")
    i = i + 1
# Premium Account Table
# INSERT INTO PremiumAccount_T (PremiumAccountID, PremiumStatus, CustomerID, PgameID)
i = 18
while i <= 35:
    ID = randint(100, 999)
    ID2 = randint(0, 1)
    print("INSERT INTO PremiumAccount_T (PremiumAccountID, PremiumStatus, CustomerID, PgameID)\n VALUES (" + str(ID) + ", " + str(ID2) + ", " + str((CustomerIDS[i])) + ", " + str(GameIDS[i]) + ");")
    i = i + 1
