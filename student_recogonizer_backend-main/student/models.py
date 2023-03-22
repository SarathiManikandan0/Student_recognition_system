from django.db import models

# Create your models here.

# class Student(models.Model):
#     sid = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     contact = models.CharField(max_length=15)
#     # image    = models.ImageField(upload_to=photos_dir, null=True, blank=True, default=None)
#     # filename = models.CharField(max_length=60, blank=True, null=True)
#     class Meta:
#         db_table = "student"
# class Meta:
#     db_table = "student"

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')