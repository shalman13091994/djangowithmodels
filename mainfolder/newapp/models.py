from django.db import models

class member(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    password=models.CharField(max_length=12)
    email=models.EmailField(max_length=40)
    birthdate=models.DateField()

    def __str__(self):
        return self.fname + " | " +self.lname

    # created another table in databae

# class section(models.Model):
#     music=models.CharField(max_length=30)
#     fname=models.CharField(max_length=30)
#     artist=models.CharField(max_length=100)
#
#
#     def __str__(self):
#         return self.music + " || "+self.artist
