from django.test import TestCase
from .models import Editor,Profile,tags

# Create your tests here.
class EditorTestClass(TestCase):
# Set up method
    def setUp(self):
        self.Frenky= Editor(first_name = 'Frenky', last_name ='Kyser', email ='frenkykyser@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Frenky,Editor))