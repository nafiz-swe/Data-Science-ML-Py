# Create a class named 'Student' with the variable 'name' and 'roll_no'.
# And write a Display method to display the name and roll_no.
# Assign the value of roll_no as '2' and that of name as "John" by creating an object of the class Student.

# Define the Student class
class Student:
    # Constructor to initialize name and roll_no
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    # Method to display student's information
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

# Create an object of the Student class and assign values
student1 = Student("John", 2)

# Call the display method to show the student's information
student1.display()
