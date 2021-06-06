from django.db import models

# Create your models here.


class Calloj(models.Model):
    mdname = models.CharField(max_length=64,
                              verbose_name="제품명")
    mdinfo = models.TextField(
        verbose_name="제품정보")
