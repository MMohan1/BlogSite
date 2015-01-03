from django.db import models


class Blog(models.Model):
    BUILDING_MATERIALS = (
        ('Genral', 'Genral'),
        ('Science', 'Science'),
        ('IT Scotor', 'IT Scotor'),
        ('History', 'History'),
        ('New Teachnology', 'New Teachnology'),
    )
    Blog_Title = models.CharField(max_length=200)
    Blog_Field = models.CharField(
        max_length=100, choices=BUILDING_MATERIALS, null=False)
    URL = models.URLField()
    Blog_Description = models.TextField()
    pub_date = models.CharField(max_length=40)
    Like = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.Blog_Title


class Action(models.Model):
    Blog_Title = models.ForeignKey(Blog)
    User_Name = models.CharField(max_length=50)
    Comment = models.TextField()
    Like = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.Comment
# Create your models here.
