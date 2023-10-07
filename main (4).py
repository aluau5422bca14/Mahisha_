class student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_stundents(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
       key=lambda student: student.cgpa,
       reverse=True)
  
  return sorted_students

# Example usage:
students = [student("Hari","A123",7.8),
           student("Srikanth","A124",8.9),
           student("saumya","A125",9.1),
           student("Mahidhra","A126",9.9),]
sorted_students = sort_stundents(students)

# Print the sorted list of students 
for student in sorted_students:
  print("Name: {}, Roll_number: {}, CGPA: {}".format(student.name,
                                                         student.roll_number,
                                                         student.cgpa))