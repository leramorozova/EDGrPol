"""
        Данный файл содержит модели к каждой таблице базы данных проекта.
Классы и признаки названы в соответствии с названиями таблиц и столбцов базе данных.
Об устройсве БД читайте соответствующий раздел документации.
В случае необходорсти допустимо перемещать и переименовывать классы и переменные, но
    запрещено изменять содержимое подклассов Meta
"""
from django.db import models


class Article(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    lemma_rus = models.TextField()
    deriv_source = models.TextField()
    pos = models.TextField()
    lemma_orig = models.TextField()
    if_hapax = models.TextField()
    if_middle_lang = models.TextField()
    vasmer = models.TextField()
    translated_srcs = models.TextField()
    rewrit_date = models.TextField()
    orig_creation = models.TextField()
    theme = models.TextField()
    lang = models.TextField()
    etymology = models.TextField()
    semantics = models.TextField()
    slavic_dict = models.TextField()
    orig_srcs = models.TextField()
    citation = models.TextField()
    add_philol = models.TextField()
    add_histor = models.TextField()
    historic_sources = models.TextField()
    slavic_sources = models.TextField()
    phonetic_variants = models.TextField()
    morph_variants = models.TextField()
    linking_references = models.TextField()

    class Meta:
        managed = False
        db_table = 'articles'

