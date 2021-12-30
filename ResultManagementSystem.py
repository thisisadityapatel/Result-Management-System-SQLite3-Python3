# RESULT MANAGEMENT SYSTEM

'''
PROGRAM PURPOSE:
---------------
    Python was used to create the programme, and the SQLite3 database was used to store the data. 
    The primary goal of this project was to learn SQLite3 Database Implementation in Python. 
    The applications are modelled around a school result decleration management system, 
    where students may connect with their student identity and password and access their results online.
    Teachers and school administration can log in separately using unique credentials and add, edit, 
    and delete student information from the school database.

    To login as a faculty please enter the credentials as:
    username = thisisadityapatel
    password = adityaisthebest2112

'''
import time
import os
import sqlite3

#linking the python program using SQL database
conn = sqlite3.connect("results.db")
db = conn.cursor()

#Program Implementation
print("")
print("------------------")
print("Ryerson University")
print("------------------")

print("")
print("Welcome to the Ryerson University Result Decleration Portal")
time.sleep(1.5)

print("")
print("All the Very Best for your results!! You got this !!")
time.sleep(1.5)
print("")

print("Connect us at issask@ryerson.ca")
time.sleep(1.5)
print("", end = "\n"*5)

print("What describes you at Ryerson? ")
print("1. Teacher/Faculty/Employee at Ryerson")
print("2. Student")

choice = int(input("Enter the serial number : "))
while choice not in [1, 2]:
    choice = int(input("Enter a valid serial number : "))

#Logging in as Teacher/Faculty/Employee at Ryerson University
if choice == 1:
    print("", end = "\n" * 5)
    print("Login as a TEACHER / FACULTY / EMPLOYEE : ")
    print("----------------------------------------- ")
    username = input("Username : ")
    password = input("Password : ")
    db.execute("SELECT * FROM ryerson_faculty WHERE username = ?", (username,))
    c = db.fetchone()
    if c[1] == password:
        print("", end = "\n"*5)
        print("Logged in at Ryerson Faculty")
        print("----------------------------")
        print("What would you like to perform? ")
        print("1 - ENTER a new student detail")
        print("2 - UPDATE an existing student detail.")
        print("3 - DELETE a student detail")
        print("4 - See all student details.")
        choice = int(input("Enter the serial number of the choice : "))

        while choice not in [1, 2, 3, 4]:
            choice = int(input("Please enter valid serial number : "))
        
        # ENTER a new student detail
        if choice == 1:
            print("", end = "\n"*5)
            print("ENTER THE STUDENT DETAILS : ")
            print("----------------------------")
            name = input("NAME : ")
            password = input("PASSWORD : ")
            major = input("MAJOR : ")
            gpa = float(input("OVERALL GPA : "))
            percent = float(input("PERCENT : "))

            #entering the details into the SQLite Database
            db.execute("INSERT INTO ryerson_students VALUES(?, ?, ?, ?, ?)", (name, password, major, gpa, percent))
            time.sleep(0.6)
            print("Details Successfully Entered........ ")
        
        # UPDATE an existing student detail.
        elif choice == 2:
            print("", end = "\n"*5)
            print("UPDATE STUDENT DETAILS")
            print("----------------------")
            print("Enter the Details of the student whose details are to be modified : ")
            search_pass = input("PASSWORD : ")
            print()
            print("Current Details : ")
            print("------------------")
            db.execute("SELECT * FROM ryerson_students WHERE password = ?", (search_pass,))
            print(db.fetchone())

            print("Enter the new details of the student : ")
            name = input("NEW NAME : ")
            password = input("NEW PASSWORD : ")
            major = input("NEW MAJOR : ")
            gpa = float(input("NEW OVERALL GPA : "))
            percent = float(input("NEW PERCENT : "))
            db.execute("DELETE FROM ryerson_students WHERE password = ?", (search_pass,))
            db.execute("INSERT INTO ryerson_students VALUES(?, ?, ?, ?, ?)", (name, password, major, gpa, percent,))
            time.sleep(0.6)
            print("Details updated successfully.......... ")
        
        #DELETING a student detail from the database
        elif choice == 3:
            print("", end = "\n"*5)
            print("DELETE STUDENT DETAILS")
            print("----------------------")
            print("Enter the Details of the student whose details are to be deleted : ")
            search_pass = input("PASSWORD : ")
            db.execute("SELECT * FROM ryerson_students WHERE password = ?", (search_pass,))
            print(db.fetchone())
            print()
            print("Are sure you want to delete? : ")
            print("1 - Yes, Delete.")
            print("2 - No, Dont Delete.")
            del_choice = int(input("Enter your choice number : "))

            if del_choice == 1:
                db.execute("DELETE FROM ryerson_students WHERE password = ?", (search_pass,))
                time.sleep(0.6)
                print("Details Deleted successfully.......... ")
            elif del_choice == 2:
                time.sleep(0.6)
                print("Details Secured back.........")
        
        #showing all the student details
        elif choice == 4:
            print("", end = "\n"*5)
            print("ALL STUDENT DETAILS")
            print("----------------------")
            db.execute("SELECT * FROM ryerson_students;")
            for x in db.fetchall():
                print(x)
    #If the password Entered is Incorrect
    else:
        print("Access Denied!! Incorrect password.")

#Logging in as a Student at Ryerson University
else:
    print("", end = "\n" * 5)
    print("Login as a STUDENT: ")
    print("------------------ ")
    name = input("Name     : ")
    password = input("Password : ")
    db.execute("SELECT * FROM ryerson_students WHERE password = ?", (password,))
    x = db.fetchone()
    if x[0] == name:
        print("", end="\n" * 2)
        print("Drum Roll !!!!!")
        time.sleep(4)
        print("***********************************")
        print(f"NAME     = {x[0]} ")
        print(f"PASSWORD = {x[1]} ")
        print(f"MAJOR    = {x[2]} ")
        print(f"GPA      = {x[3]} ")
        print(f"PERCENT  = {x[4]} ") 
        print("***********************************")
    else:
        print("INVALID Credentials !! Please contact issask@ryerson.ca")
        print("")

print("")
conn.commit()
conn.close()



 
