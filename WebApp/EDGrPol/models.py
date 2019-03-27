"""
        Данный файл содержит модели к каждой таблице базы данных проекта.
Классы и признаки названы в соответствии с названиями таблиц и столбцов базе данных.
Об устройсве БД читайте соответствующий раздел документации.
В случае необходорсти допустимо перемещать и переименовывать классы и переменные, но
    запрещено изменять содержимое подклассов Meta
"""
from django.db import models


class SimpleFields(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    lemma_rus = models.TextField()
    pos = models.TextField()
    lemma_greek = models.TextField()
    if_hapax = models.TextField()
    if_middle_lang = models.TextField()
    vasmer = models.TextField()
    translated_srcs = models.TextField()
    rewrit_date = models.TextField()
    orig_creation = models.TextField()
    theme = models.TextField()
    lang = models.TextField()

    class Meta:
        managed = False
        db_table = 'simple_fields'


class ComplexFields(models.Model):
    lemma = models.TextField()
    etymology = models.TextField()
    semantics = models.TextField()
    slavic_dict = models.TextField()
    orig_srcs = models.TextField()
    citation = models.TextField()
    add_philol = models.TextField()
    add_histor = models.TextField()
    lang = models.TextField()

    class Meta:
        managed = False
        db_table = 'complex_fields'


class Sources(models.Model):
    lemma = models.TextField()
    source = models.TextField()
    type = models.TextField()
    lang = models.TextField()

    class Meta:
        managed = False
        db_table = 'sources'


class Variants(models.Model):
    lemma = models.TextField()
    var_type = models.TextField()
    variant = models.TextField()
    lang = models.TextField()

    class Meta:
        managed = False
        db_table = 'variants'
