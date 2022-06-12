from django.db import models


class School(models.Model):

    name = models.CharField(max_length=200)
    region = models.IntegerField()
    email = models.EmailField(blank=False)
    principal = models.CharField(max_length=100)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    publishing_date = models.CharField(max_length=100)
    pages = models.IntegerField(blank=False)

    def __str__(self):
        return self.title


class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
