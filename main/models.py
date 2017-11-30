#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dachnik(models.Model):
	name = models.CharField(max_length = 200)
	def __str__(self):
		return self. name
class Stead(models.Model):
	street = models.CharField(max_length = 100)
	number = models.IntegerField()
	dachnik = models.ForeignKey('Dachnik')
	def __str__(self):
		
		return (self.street+" "+str(self.number))
	