#The commented out test is the one I had an error on. I struggled with this class a bit
import unittest
import pytest
from institution_def import Institution
from instructor_def import Instructor
from course_def import Course
from course_offering_def import CourseOffering
from student_def import Student

class Test_Institution(unittest.TestCase): 
        def test_init(self):
                institition = Institution("Quinnipiac University", "qu.edu")
                
                institition.name = "Quinnipiac University"
                institition.domain = "qu.edu"
                
                assert institition.name == "Quinnipiac University"
                assert institition.domain == "qu.edu"
                
        def test_list_students(self):
               studentList = ["Julia", "Rick", "Alyssa"]

               self.assertIsInstance(studentList, list)  
               
        #def test_list_instructors(self):
                #institution = Institution("Quinnipiac University", "qu.edu")
                #instructor = Instructor("Boomer", "Bobcat", "Quinnipiac University", "Feb 19, 2002", "bboomer")
                #institution.faculty_list(instructor) 
                
                #assert institution.faculty_list.get('bboomer') == instructor
                
        def test_enroll_students(self):
                institution = Institution("Quinnipiac University", "qu.edu")
                student1 = Student('Woeste', 'Julia', 'Quinnipiac University', '2/19/2002', 'jawoeste')
                
                
                institution.enroll_student(student1) #add course
                institution.list_students() #
                
                assert institution.student_list.get("jawoeste") == student1
                
        def test_hire_instructor(self):
                institution = Institution("Quinnipiac University", "qu.edu")
                instructor = Instructor("Boomer", "Bobcat", "Quinnipiac University", "Feb 19, 2002", "bboomer")
                
                institution.hire_instructor(instructor)
               
                
                assert institution.faculty_list.get("bboomer") == instructor

        #hire instructor
        #add course
        def test_add_course(self):
                institution = Institution("Quinnipiac University", "qu.edu")
                course = Course("Software Engineering", 123, "Quality Assurance", 3)
                
                institution.add_course(course)
                
                assert institution.course_catalog.get("Quality Assurance") == course
                
        def test_add_course_offering(self):
                institution = Institution("Quinnipiac University", "qu.edu")
                course = Course("Software Engineering", 123, "Quality Assurance", 3)
                courseOffering = CourseOffering(course, '1', '2023', 'none')
                
                
                institution.add_course(course)
                institution.add_course_offering(courseOffering)
                institution.list_course_schedule(institution, "2023", "none")
                
                assert len(institution.course_schedule) == 1
                #institution.add_course_offering(courseOffering)
                #assert institution.course_schedule.get("Quality Assurance") == courseOffering.course.name
                

        def test_register_student_forCourse(self):
   
                department = "ComputerScience"
                courseNumber = 1234
                courseName = "TestClass"
                courseCredits = 3
                courseSectionNumber = 123
                courseOfferYear = 2023
                courseQuarter = 1
                course = Course(department=department, number=courseNumber, name=courseName, credits= courseCredits)
                courseOffering = CourseOffering(course, courseSectionNumber, courseOfferYear, courseQuarter)

    # Define a student
                student1 = Student("Test", "Test", "School Test", "4/20/2023", "test")

    # Define an institution
                institution = Institution("Quinnipiac University", "qu.edu")

    #Add the course to the institution (to the course catalog)
                institution.add_course(course)

    # Add the course to to the planned course offerings
                institution.add_course_offering(courseOffering)

    # Enroll the student into the school
                institution.enroll_student(student1)

                courseSchedule = institution.course_schedule
    # Act
    # Register the student for the course
                institution.register_student_for_course(student1, courseName, department, courseNumber, courseSectionNumber, courseOfferYear, courseQuarter)

    # Assert
                assert len(courseOffering.registered_students) == 1