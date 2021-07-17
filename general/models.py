from django.db import models

class Soal(models.Model):
    nama = models.CharField(max_length=200)
    nim =  models.CharField(max_length=20)
