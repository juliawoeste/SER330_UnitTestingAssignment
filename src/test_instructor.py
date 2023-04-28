import pytest
from instructor_def import Instructor
from course_def import Course
from course_offering_def import CourseOffering
class Test_Instructor():
    def test_instructor(self):
        instructor = Instructor('last_name', 'first_name', 'school', 'date_of_birth', 'username')
        
        instructor.last_name = 'Boomer'
        instructor.first_name = 'Bobcat'
        instructor.school = 'Quinnipiac University'
        instructor.date_of_birth = 'Feb 19, 2002'
        instructor.username = 'bboomer'
        
        assert instructor.last_name == 'Boomer'
        assert instructor.first_name == 'Bobcat'
        assert instructor.school == 'Quinnipiac University'
        assert instructor.date_of_birth == 'Feb 19, 2002'
        assert instructor.username == 'bboomer'
        
    def test_list_courses_whenNoFiltersArePresent(self):
        #Arrange
        
        #need instructor
        instructor = Instructor("Last Name", "First Name", "Quinnipiac University", "4/20/2023", "test")
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        courseOffering = CourseOffering(course, '123', '2023', '1')
        courseOffering2 = CourseOffering(course, '123', '2023', '1')
        courseOfferingList =[courseOffering, courseOffering2]
        instructor.course_list = courseOfferingList
        
        #Act
        returnedCourse = instructor.list_courses()

        #Assert
        assert len(returnedCourse) == len(courseOfferingList)
        
    def test_list_courses_whenYearIsPresent(self):
        instructor = Instructor("Last Name", "First Name", "Quinnipiac University", "4/20/2023", "test")
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        courseOffering = CourseOffering(course, '123', '2023', "1")
        courseOffering2 = CourseOffering(course, '123', '2023', "1")
        courseOfferingList =[courseOffering, courseOffering2]
        instructor.course_list = courseOfferingList
        
        #Act
        returnedCourse = instructor.list_courses(year="2023")
        
        assert len(returnedCourse) == len(courseOfferingList)
        
        
    def test_list_courses_whenQuarterIsPresent(self):
        instructor = Instructor("Last Name", "First Name", "Quinnipiac University", "4/20/2023", "test")
        course = Course("Software Engineering", 123, "Quality Assurance", 3)
        courseOffering = CourseOffering(course, '123', '2023', "1")
        courseOffering2 = CourseOffering(course, '123', '2023', "1")
        courseOfferingList =[courseOffering, courseOffering2]
        instructor.course_list = courseOfferingList
        
        #Act
        returnedCourse = instructor.list_courses(quarter="1")
        
        assert len(returnedCourse) == len(courseOfferingList)
        
        
        
        
        
    
        
    
        
        
        
        
        
        
        