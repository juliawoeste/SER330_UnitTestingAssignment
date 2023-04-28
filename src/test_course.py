import unittest
from course_def import Course

class Test_Course(unittest.TestCase):
    def test_course_department(self):
        course = Course('department', 'number', 'name', 'credits')
        
        course.department = 'Software Engineering'
        course.number = '330'
        course.name = 'SER330'
        course.credits = '3'
        
        assert course.department == 'Software Engineering' 
        assert course.number == '330' 
        assert course.name == 'SER330' 
        assert course.credits == '3' 
        
if __name__ == '__main__':
    unittest.main() 