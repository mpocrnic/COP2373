# Import the CSV module to handle reading and writing CSV files
import csv

def create_grades_file():
    # Ask how many students they want to enter data for
    num_students = int(input("Enter the number of students: "))

    # Open the file 'grades.csv' in write mode
    with open("grades.csv", mode="w", newline="") as file:
        # Create a CSV writer object to write rows to the file
        writer = csv.writer(file)
        
        # Write the first row of the file, which will be the column headers
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
        
        # Loop through for the number of students entered
        for i in range(num_students):
           
            print(f"\nEnter data for student {i + 1}:")
            
            first = input("First name: ")
            
            last = input("Last name: ")
            
            # Prompt for each of the three exam scores (converted to integers)
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))
            
            # Write the student's full data as a row in the CSV file
            writer.writerow([first, last, exam1, exam2, exam3])

# Call the function to start the data entry process
create_grades_file()

# Import the CSV module for reading the file
import csv

def display_grades_file():
    print("\nStudent Grades:")
    
    # Print column titles
    print("{:<12} {:<12} {:<8} {:<8} {:<8}".format("First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"))
    
    # Print a line of dashes to separate the header from the data
    print("-" * 52)

    # Open the grades.csv file in read mode
    with open("grades.csv", mode="r") as file:
        reader = csv.reader(file)
        
        # Skip the first row of the file, which is the header
        next(reader)

        # Loop through each remaining row in the CSV
        for row in reader:
            # Print each student's data in a line
            print("{:<12} {:<12} {:<8} {:<8} {:<8}".format(row[0], row[1], row[2], row[3], row[4]))

# Call the function to display the contents of the grades file
display_grades_file()

import csv

def create_grades_file():
    num_students = int(input("Enter the number of students: "))
    with open("grades.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
        for i in range(num_students):
            print(f"\nEnter data for student {i + 1}:")
            first = input("First name: ")
            last = input("Last name: ")
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))
            writer.writerow([first, last, exam1, exam2, exam3])

create_grades_file()

