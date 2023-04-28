import unittest
from datetime import date
from student_def import Student
from course_def import Course
from course_offering_def import CourseOffering

class Test_Student(unittest.TestCase): 
    def test_init(self):
        student = Student("Woeste", "Julia", "Quinnipiac University", "2/19/2002", "jawoeste")
        
        student.last_name = "Woeste"
        student.first_name = "Julia"
        student.school = "Quinnipiac University"
        student.date_of_birth = "2/19/2002"
        student.username = "jawoeste"
        
        assert student.last_name == "Woeste"
        assert student.first_name == "Julia"
        assert student.school == "Quinnipiac University"
        assert student.date_of_birth == "2/19/2002"
        assert student.username =="jawoeste"

        
    def test_str(self):
        student = Student("Woeste", "Julia", "Quinnipiac University", "Feb 19, 2002", "jawoeste")
      
        
        string = ('\n' + 'Student Name: ' + "Julia" + ' ' + "Woeste" + '\n' +
            'School: ' + "Quinnipiac University" + '\n' +
            'DOB: ' + "Feb 19, 2002" + '\n' +
            'Username: ' + "jawoeste" + '\n' )
        
        assert string == Student.__str__(student)
        
    def test_student_list_courses(self):
        student = Student("Woeste", "Julia", "Quinnipiac University", "Feb 19, 2002", "jawoeste")
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        course2 = Course("Math", 1234, "Calc", 3)
        courseOffering = CourseOffering(course, '1', '2023', 'none')
        courseOffering2 = CourseOffering(course2, '1', '2022', 'none')
        student.transcript = {courseOffering: "A", courseOffering2: "B"}
        
        courseList = Student.list_courses(student)
        assert courseList == [courseOffering, courseOffering2]

        
    def test_student_credits(self):
        student = Student("Woeste", "Julia", "Quinnipiac University", "Feb 19, 2002", "jawoeste")
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        course2 = Course("Math", 1234, "Calc", 3)
        courseOffering = CourseOffering(course, '1', '2023', 'none')
        courseOffering2 = CourseOffering(course2, '1', '2022', 'none')
        
        student.course_list = [courseOffering, courseOffering2]
        assert student.credits == 6
        
    def test_gpa(self):
        student = Student("Woeste", "Julia", "Quinnipiac University", "Feb 19, 2002", "jawoeste")
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        courseOffering = CourseOffering(course, '1', '2023', 'none')
        courseOffering.register_students([student])
      
        courseOffering.submit_grade(student, "A")
        
        self.assertEqual(student.gpa, 4.0)
 



    def test_list_courses(self):
       student1 = Student('Woeste', 'Julia', 'Quinnipiac University', '2/19/2002', 'jawoeste')

       course = Course("Software Engineering", 123, "Quality Assurance", 3)

       student1.course_list.append(course)
       
       student1.transcript[course] = 'A'
       
    


        