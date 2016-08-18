from django.db import models


class Collection(models.Model):
	collection_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.collection_name

	


class Memory(models.Model):
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	memory_name = models.CharField(max_length=200)
	memory_details = models.TextField()
	memory_date = models.DateTimeField()

	def __str__(self):
		return self.memory_name


class Phase(models.Model):
	# TODO: possibly link phase begining and end to two specific memories
	collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
	phase_name = models.CharField(max_length=200)
	phase_details = models.TextField()
	phase_start_date = models.DateTimeField()
	phase_end_date = models.DateTimeField()

	def __str__(self):
		return self.phase_name

