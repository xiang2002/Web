from django.db import models


class Queue(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, default='0')

    class Meta:
        db_table = 'queue'
        verbose_name = "筛选队列"
        verbose_name_plural = "筛选队列"
