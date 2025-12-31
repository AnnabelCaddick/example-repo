no_students = int(input("Enter how many students are registering :"))
attendees = []
for i in range(no_students):
    student_id = input(f"Enter the student ID of the student {i +1}: ")
    attendees.append(student_id)


with open("reg_form.txt", "w") as file:
   file.write ("\n#### ATTENDANCE REGISTER #####")
   file.write("\n")
   file.write ("\nStudent IDs of the students scheduled to take the exam :")
   for id in attendees:
       
       file.write(f"\n Student ID Number {id} Please sign here : .................................")

print ("Student attendance register written to reg_form.txt")
    