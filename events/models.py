from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Collection(models.Model):
	user = models.ForeignKey(User, editable=False)
	collection_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', editable=False, default=datetime.now)

	def __str__(self):
		return self.collection_name

	


class Memory(models.Model):
	user = models.ForeignKey(User, editable=False)
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published', editable=False, default=datetime.now)
	memory_name = models.CharField(max_length=200)
	memory_details = models.TextField()
	memory_date = models.DateField()

	def __str__(self):
		return self.memory_name


class Phase(models.Model):
	user = models.ForeignKey(User, editable=False)
	# TODO: possibly link phase beginning and end to two specific memories
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published', editable=False, default=datetime.now)
	phase_name = models.CharField(max_length=200)
	phase_details = models.TextField()
	phase_start_date = models.DateField()
	phase_end_date = models.DateField()

	def __str__(self):
		return self.phase_name

