from django.db import models
from datetime import datetime


class Collection(models.Model):
	collection_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', editable=False, default=datetime.now)

	def __str__(self):
		return self.collection_name

	


class Memory(models.Model):
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published', editable=False, default=datetime.now)
	memory_name = models.CharField(max_length=200)
	memory_details = models.TextField()
	memory_date = models.DateTimeField()

	def __str__(self):
		return self.memory_name


class Phase(models.Model):
	# TODO: possibly link phase begining and end to two specific memories
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published', editable=False, default=datetime.now)
	phase_name = models.CharField(max_length=200)
	phase_details = models.TextField()
	phase_start_date = models.DateTimeField()
	phase_end_date = models.DateTimeField()

	def __str__(self):
		return self.phase_name

