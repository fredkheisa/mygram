from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name


    def save_editor(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length = 60)


    def save_location(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        self.delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Location.objects.get(id = self.id).update(field = val)


    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length = 60)

    def save_category(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete(self):
        """
        This is the method to delete the instance
        """
        Category.objects.get(id = self.id).delete()

    def update(self,field,val):
        """
        This is the method to update the instance
        """
        Category.objects.get(id = self.id).update(field = val)


    def __str__(self):
        return self.category


class Picture(models.Model):
    category = models.CharField(max_length = 60)
    picture_name = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    picture_image = models.ImageField(upload_to = 'pictures/')

    def save_picture(self):
        """
        This is the function that we will use to save the instance of this class
        """
        self.save()

    def delete_picture(self):
        """
        This is the function that we will use to delete the instance of this class
        """
        Image.objects.get(id = self.id).delete()

    def update_picture(self,val):
        """
        This is the method to update the instance
        """
        Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def todays_profiles(cls):
        today = dt.date.today()
        profiles = cls.objects.filter(pub_date__date = today)
        return profiles


    @classmethod
    def days_profiles(cls,date):
        profiles = cls.objects.filter(pub_date__date = date)
        return profiles

    @classmethod
    def search_by_category(cls,search_term):
        profiles = cls.objects.filter(category__icontains=search_term)
        return profiles