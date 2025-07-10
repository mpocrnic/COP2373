import csv          
import numpy as np  

def load_grades_from_csv(filename):
    """
    Loads student names and grades from a CSV file into separate lists/arrays.
    Skips the header row and combines first and last names into a single name.
    Returns: list of names, NumPy array of grades.
    """
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  

        # Read the remaining rows into a list
        data = [row for row in reader]

    # Combine First Name and Last Name into full names
    names = [f"{row[0]} {row[1]}" for row in data]

    # Store exams in a NumPy array 
    grades = np.array([list(map(float, row[2:])) for row in data])

    return names, grades

def exam_statistics(grades):
    """
    Prints statistics for each exam (column in the grade array).
    Includes: Mean, Median, Std Deviation, Min, and Max.
    """
    print("=== Per Exam Statistics ===")
    num_exams = grades.shape[1]  # Get number of exams (columns)

    for i in range(num_exams):
        exam = grades[:, i]  # Select column i (i.e., all student scores for this exam)

        print(f"\nExam {i + 1}:")
        print(f"  Mean: {np.mean(exam):.2f}")          
        print(f"  Median: {np.median(exam):.2f}")      
        print(f"  Std Dev: {np.std(exam):.2f}")
        print(f"  Min: {np.min(exam)}")               
        print(f"  Max: {np.max(exam)}")                

def overall_statistics(grades):
    """
    Prints statistics across all exams and all students.
    """
    print("\n=== Overall Statistics ===")
    # Convert 2D array to 1D list of all grades
    all_grades = grades.flatten()  

    # Print summary statistics
    print(f"  Overall Mean: {np.mean(all_grades):.2f}")
    print(f"  Overall Median: {np.median(all_grades):.2f}")
    print(f"  Overall Std Dev: {np.std(all_grades):.2f}")
    print(f"  Overall Min: {np.min(all_grades)}")
    print(f"  Overall Max: {np.max(all_grades)}")

def pass_fail_analysis(grades):
    """
    Calculates and prints how many students passed or failed each exam.
    A score of 60 or higher is considered a pass.
    Also calculates the overall pass percentage across all exams.
    """
    print("\n=== Pass/Fail Analysis ===")
    # Number of rows = number of students
    num_students = grades.shape[0]
    # Number of columns = number of exams
    num_exams = grades.shape[1]
    # Counter for all passing scores
    total_passes = 0               

    for i in range(num_exams):
        # Get all grades for exam i
        exam = grades[:, i]
        # Count scores that are 60 or higher
        passes = np.sum(exam >= 60)
        # Remaining students failed
        fails = num_students - passes   

        # Add to total pass count
        total_passes += passes          
        print(f"Exam {i + 1}: Passed = {passes}, Failed = {fails}")

    # Total number of grades
    total_grades = num_students * num_exams  
    overall_pass_percentage = (total_passes / total_grades) * 100  

    print(f"\nOverall Pass Percentage: {overall_pass_percentage:.2f}%")

def main():
    """
    Main function that runs the full analysis using the CSV file.
    """
    filename = "grades.csv"  

    # Load names and grade data from the CSV
    names, grades = load_grades_from_csv(filename)

    # Print a few rows to check structure
    print("=== First Few Rows ===")
    for i in range(min(5, len(names))):
        print(f"{names[i]}: {grades[i]}")

    # Call functions to compute statistics
    exam_statistics(grades)
    overall_statistics(grades)
    pass_fail_analysis(grades)

# This block ensures that main() only runs when the script is executed directly
if __name__ == "__main__":
    main()
