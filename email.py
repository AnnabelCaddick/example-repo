"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.
#Method to mark the email as read
    def mark_as_read(self):
        self.has_been_read = True
        return f"'{self.subject_line}' has been marked as read."


#Create an empty inbox list to store Email objects
inbox = []

#Create email objectd

# --- Functions --- #
# Build out the required functions for your program.
# Create 3 sample emails and add them to the inbox list.
# Create a function that prints each email's subject line
# alongside its corresponding index number,
# regardless of whether the email has been read.
def populate_inbox():
    inbox.append(Email(
        "rashy@python.com", 
        "Dog training", 
        "Dog training will commence on the 4th April."
        ))
    
    inbox.append(Email(
        "benji@apple.com", 
        "Christmas dinner", 
        "Hello do you want me to bring pudding?"
        ))
    
    inbox.append(Email(
        "grandma@kingsroad.com", 
        "Staying for chistmas",
        "Are you expecting me to stay until New Years Day?" 
        ))


def list_emails():
    print("\nALL EMAILS:")
    for index, email in enumerate(inbox, start=1):
        status = "Read" if email.has_been_read else "Unread"
        print(f"{index}: {email.subject_line} ({status})")
  
    


def read_email(index):
    email = inbox[index]
    
    print("\n ### Email ###\n")
    print(f"From: {email.email_address}")
    print(f"Suject:{email.subject_line}")
    print("Content:")
    print(email.email_content)

    email.mark_as_read()





    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    


def view_unread_emails():
    print("\nUnread Emails:")
    for index, email in enumerate(inbox, start=1):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line}")
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    

populate_inbox()
# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
       list_emails()
       index = int(input("Enter the index of the email you want to read:")) - 1
       read_email(index)

    elif user_choice == 2:
        # Add logic here to view unread emails
       view_unread_emails()

    elif user_choice == 3:
        # Add logic here to quit application.
        print("You have chosen to quit the application. GOODBYE!")
        break

    else:
        print("Oops - incorrect input.")
