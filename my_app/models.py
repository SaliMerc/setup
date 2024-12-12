from django.db import models

# Create your models here.
# Inside this app, define a model in the models.py file.
#
# For this assignment, create a model called Book with the following fields:
# # title (CharField): The title of the book.
# # author (CharField): The author of the book.
# # published_date (DateField): The date the book was published.
# # isbn (CharField): The ISBN number of the book.
# # pages (IntegerField): The number of pages in the book.
# # Create and Apply Migrations:

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)
    pages=models.IntegerField()
    def __str__(self):
        return self.title

