from django.db import models

class Soal(models.Model):
    nama = models.CharField(max_length=200)
