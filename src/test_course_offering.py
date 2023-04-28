import unittest
from course_offering_def import CourseOffering
from student_def import Student
from instructor_def import Instructor
from course_def import Course

#assertIn(x,y) x is in y - good for checking if something is in list 
class Test_CourseOffering(unittest.TestCase):
        
    def test_register_students(self):
        #arrage 
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        courseOffering = CourseOffering(course, '1', '2023', 'none')
        student1 = Student('Woeste', 'Julia', 'Quinnipiac University', '2/19/2002', 'jawoeste')
        student2 = Student('Woeste', 'Julia', 'Quinnipiac University', '2/19/2002', 'jawoeste')
        listOfStudents = [student1, student2]
        
        #act
        
        courseOffering.register_students(listOfStudents)
        
        #assert #verify the course offering = to register students 
        #assert listOfStudents.len() == courseOffering.registered_students.len() 
        assert len(courseOffering.registered_students) == len(listOfStudents)
        #assert courseOffering.registered_students.__len__ == listOfStudents.len() 

    def test_submit_grades(self):
        #arrage 
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        courseOffering = CourseOffering(course, '1', '2023', 'none')
        student1 = Student('Woeste', 'Julia', 'Quinnipiac University', '2/19/2002', 'jawoeste')
        grade1 = 'A'
        courseOffering.submit_grade(student1, grade1)
        
        assert courseOffering.grades[student1.username] == grade1
        
    #def get_grades(self):
        #arrage 
        
        #act
        #assert
        #assert
    
    def test_str_(self):
        courseOffering = CourseOffering('Software Engineering', '1', '2023', 'none')
        instructor = Instructor('Boomer', 'Bobcat', 'Quinnipiac University', 'none', 'bbobcat')
        
        #string = 
        
        #assert string == 
        
        
        
        

    
    
        