import mysql.connector as mysql

#variables
host = "localhost"
user = "root"
password = ""

try:
    db = mysql.connect(host=host,user=user,password=password)
    print("Connected Successfully")
    db_command_handler = db.cursor()
except Exception as e:
    print(e)
    print("Failed to connect")
    
#Connecting to mysql
try:
    db_command_handler.execute("DROP DATABASE KeepSmilingDatabase") #Drop an already created database
    db_command_handler.execute("CREATE DATABASE KeepSmilingDatabase")
    print("Dentist database has been created")
except Exception as e:
    print("Could not create database")
    print(e)

#Connecting to SmileDatabase
try:
    db1 = mysql.connect(host=host,user=user,password=password,database = "KeepSmilingDatabase")
    print("Connected Successfully")
except Exception as e:
    print("Could not connect to KeepSmilingDatabase Server")
    print(e)
    
#Adding tables
try: 
    db1_command_handler = db1.cursor()
    db1_command_handler.execute("CREATE TABLE Dentist (DentistID INT PRIMARY KEY, DentistName VARCHAR(50),HiredDate DATE)")
    db1_command_handler.execute("CREATE TABLE Patient(PatientID INT PRIMARY KEY,HealthServiceNumber INT UNIQUE,DateOfBirth DATE,PatientAddress VARCHAR(100),PatientName VARCHAR(50),PatientPhone CHAR(10))")
    db1_command_handler.execute("CREATE TABLE PatientRelationship(PatientID INT PRIMARY KEY, Relationship VARCHAR(20), FOREIGN KEY (PatientID) REFERENCES Patient(PatientID))")
    db1_command_handler.execute("CREATE TABLE PatientRelationshipContact(PatientID INT PRIMARY KEY, PatientRelationName VARCHAR(50), PatientRelationPhone VARCHAR(10), FOREIGN KEY (PatientID) REFERENCES Patient(PatientID))")
    db1_command_handler.execute("CREATE TABLE InsuranceProvider(InsuranceIDNumber VARCHAR(20) PRIMARY KEY, InsuranceCompanyName VARCHAR(40), InsuranceProviderLocation VARCHAR(100), InsurancePolicy VARCHAR(100),PatientID INT, FOREIGN KEY (PatientID) REFERENCES Patient(PatientID))")
    db1_command_handler.execute("CREATE TABLE Appointment(AppointmentID INT PRIMARY KEY, DateOfAppointment DATE, TimeOfAppointment TIME, DentistID INT, FOREIGN KEY (DentistID) REFERENCES Dentist(DentistID))")
    db1_command_handler.execute("CREATE TABLE AppointmentPurposeOfVisit(PurposeOfVisit VARCHAR(15), AppointmentID INT PRIMARY KEY, FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID))")
    db1_command_handler.execute("CREATE TABLE AppointmentPatientID(AppointmentID INT PRIMARY KEY, PatientID INT, FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID), FOREIGN KEY (PatientID) REFERENCES Patient(PatientID))")
    db1_command_handler.execute("CREATE TABLE AppointmentPaymentHistory(PaymentID INT, AppointmentID INT, AmountPaid INT, AmountPaidByPatient INT,AmountPaidByInsurance INT, PRIMARY KEY(PaymentID), FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID))")
    db1_command_handler.execute("CREATE TABLE PatientPaid(PatientID INT, PaymentID INT, PRIMARY KEY (PatientID, PaymentID), FOREIGN KEY (PatientID) REFERENCES Patient(PatientID), FOREIGN KEY (PaymentID) REFERENCES AppointmentPaymentHistory(PaymentID))")
    db1_command_handler.execute("CREATE TABLE InsuranceProviderPaid(InsuranceIDNumber VARCHAR(20), PaymentID INT, PRIMARY KEY (InsuranceIDNumber, PaymentID), FOREIGN KEY (InsuranceIDNumber) REFERENCES InsuranceProvider(InsuranceIDNumber), FOREIGN KEY (PaymentID) REFERENCES AppointmentPaymentHistory(PaymentID))")
    print("Table created successfully")
except Exception as e:
    print("Table could not be created")
    print(e)

#User Interactive Interface
end = False
mainMenuOption = 0
while(end != True):

    # try:
        print("Welcome to KeepSmiling Dentist Office Database Server Main Menu, what would you like to do?")
        print("Type 1 for Dentist Related Actions, Type 2 for Patient Related Actions, Type 3 for Appointment Related Actions, Type 4 for Database Related Actions")
        mainMenuOption = int(input("Enter your choice here: "))
        if(mainMenuOption == 1):
            print("Welcome to the Dentist Specifc Actions, what would you like to do?")
            print("Type 1 to Hire a Dentist, Type 2 to Fire a Dentist, Type 3 for displaying the Dentist's information, Type 4 for displaying all hired dentists")
            dentistOption = int(input("Enter your choice here: "))
            if(dentistOption == 1):
                continues = True
                while(continues != False):
                    dentistID =  input("Input Dentist ID: ")
                    dentistName = input("Input Dentist Full Name (First name followed by last name with space inbetween): ")
                    hiredDate = input("Input the date they were hired: ")
                    query = "INSERT INTO Dentist(DentistID,DentistName,HiredDate) VALUES (%s,%s,%s)"
                    query_vals = (dentistID,dentistName,hiredDate)
                    db1_command_handler.execute(query,query_vals)
                    db1.commit()
                    print(db1_command_handler.rowcount, "record inserted")
                    print("Would you like to add more? say 1 for yes and say 2 for no")
                    decision = int(input("Answer: "))
                    if(decision == 2):
                        continues = False
            elif(dentistOption == 2):
                query = "DELETE FROM Dentist WHERE DentistID = %s"
                query_val = input("Enter Dentist ID here: ")
                db1_command_handler.execute(query,query_val)
                results = db1_command_handler.fetchall()
                print(results)
            elif(dentistOption == 4):
                db1_command_handler.execute("SELECT * FROM dentist") 
                results = db1_command_handler.fetchall()
                print(results)
            else:
                print("Not a valid option, Try Again")
        else:
            print("Not a valid option, Try Again")
    # except Exception as e:
    #     print("Not a valid option, Try Again")
    #     print(e)
    



#Delete tables and database
# try:
    # db1_command_handler.execute("DROP TABLE PatientRelationshipContact")
    # db1_command_handler.execute("DROP TABLE PatientRelationship")
    # db1_command_handler.execute("DROP TABLE AppointmentPurposeOfVisit")
    # db1_command_handler.execute("DROP TABLE InsuranceProviderPaid")
    # db1_command_handler.execute("DROP TABLE PatientPaid")
    # db1_command_handler.execute("DROP TABLE AppointmentPatientID")
    # db1_command_handler.execute("DROP TABLE AppointmentPaymentHistory")
    # db1_command_handler.execute("DROP TABLE Appointment")
    # db1_command_handler.execute("DROP TABLE InsuranceProvider")
    # db1_command_handler.execute("DROP TABLE Patient")
    # db1_command_handler.execute("DROP TABLE Dentist")
    # db_command_handler.execute("DROP DATABASE SmileDatabase") #Drop an already created database
# except Exception as e:
#     print("Could not delete table")
#     print(e)