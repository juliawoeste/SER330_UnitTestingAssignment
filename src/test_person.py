
import unittest

from person_def import Person

class Test_Person(unittest.TestCase):
    def test_PersonInit_WhenAllConditionsAreMet_CreatesObject(self):
        # Arrange
        person = Person('Woeste', 'Julia', 'Quinnipiac University', '2/19/2002', 'jawoeste', 'student')

        # Act
        person.last_name = 'Woeste'
        person.first_name = 'Julia'
        person.school = 'Quinnipiac University'

        # Assert
        assert person.last_name == 'Woeste'
        assert person.first_name == 'Julia'
        assert person.school == 'Quinnipiac University'
        assert person.date_of_birth == '2/19/2002'
        assert person.username == 'jawoeste'
        assert person.affiliation == 'student'

if __name__ == '__main__':
    unittest.main() 