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
    db_command_handler.execute("DROP DATABASE SmileDatabase") #Drop an already created database
    db_command_handler.execute("CREATE DATABASE SmileDatabase")
    print("Dentist database has been created")
except Exception as e:
    print("Could not create database")
    print(e)

#Connecting to SmileDatabase
try:
    db1 = mysql.connect(host=host,user=user,password=password,database = "SmileDatabase")
    print("Connected Successfully")
except Exception as e:
    print("Could not connect to SmileDatabase Server")
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