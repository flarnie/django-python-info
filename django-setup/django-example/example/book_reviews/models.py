from django.db import models

# Create your models here.

class Author(models.Model):
	books = models.ManyToManyField('Book', null=True, blank=True) 
	# We use the string 'Book' instead of the class name
	# Because it hasn't been defined yet.
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	homepage = models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.lname + ", " + self.fname
	class Meta:
		ordering = ['lname']
	
class Book(models.Model):
	genres = models.ManyToManyField('Genre', null=True, blank=True)
	authors = models.ManyToManyField(Author)
	title = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date first published')
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['title']
	
class Genre(models.Model):
	books = models.ManyToManyField(Book, null=True, blank=True)
	name = models.CharField(max_length=200, unique=True)
	desc = models.TextField(max_length=500)
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ['name']
	
class Review(models.Model):
	book = models.ForeignKey(Book)
	reviewer_handle = models.CharField(max_length=200)
	text = models.TextField()
	def __unicode__(self):
		return (" about " + self.book.title + " by " + self.reviewer_handle)
	class Meta:
		ordering = ['reviewer_handle']
	
