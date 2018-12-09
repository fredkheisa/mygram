from django.test import TestCase
from .models import Editor,Picture,tags

# Create your tests here.
class EditorTestClass(TestCase):
# Set up method
    def setUp(self):
        self.Frenky= Editor(first_name = 'Frenky', last_name ='Kyser', email ='frenkykyser@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Frenky,Editor))


     # Testing Save Method
    def test_save_method(self):
        self.Frenky.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class PictureTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.Frenky= Editor(first_name = 'Frenky', last_name ='Kyser', email ='frenkykyser@gmail.com')
        self.Frenky.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_picture= Picture(title = 'Test Picture',post = 'This is a random test Post',editor = self.Frenky)
        self.new_picture.save()

        self.new_picture.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Picture.objects.all().delete()


    def test_get_profiles_today(self):
        today_profiles = Picture.todays_profiles()
        self.assertTrue(len(today_profiles)>0)

    