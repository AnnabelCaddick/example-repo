class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # New method to display head office location
    def head_office_location(self):
        print("The head office is located in Cape Town.")

#Create a subclass of the Course class named OOPCourse.

# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()
course.head_office_location()

#Constructor with default values 
class OOPCourse(Course):
    
    def __init__(self):
        self.description = "OPP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.id = "#12345"


    def trainer_details(self):
        print("Course Description:", self.description)
        print("Trainer:", self.trainer)
    

    
    def show_course_id(self):
        print("Course ID:", self.id)

#Create an instance of OOPCourse
course_1 = OOPCourse()

#Call the trainer_details method

course_1.trainer_details()

#Call the show_course_id method

course_1.show_course_id()