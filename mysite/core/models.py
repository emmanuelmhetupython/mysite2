from django.db import models
from datetime import datetime

# Create your models here.
class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    tutorial_category = models.ForeignKey(TutorialCategory,default=1,verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

# Create your models here.
class Tutorials(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published",default=datetime.now())
    tutorial_series = models.ForeignKey(TutorialSeries,default=1,verbose_name="Series",on_delete=models.SET_DEFAULT)
    tutorials_slug = models.CharField(max_length=200, default = 1)


    def __str__(self):
        return self.tutorial_title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,default='Emmanuel')
    pdf   = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers', null=True,blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=10)
    post = models.TextField(max_length=200)

    def __str__(self):
        return self.post

class Question(models.Model):
    question = models.TextField(max_length=20)

    def __str__(self):
        return self.question

class Note(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_deletes_url(self):
        return
class CV(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    Highest_degree_achieved = models.CharField(max_length=120)
    cv = models.FileField(upload_to='cv/cvs')
    Highest_Certtificate = models.FileField(upload_to='certificates')
    cover_letter = models.FileField(upload_to='covers/letters')
   
    def __str__(self):
        return self.name
