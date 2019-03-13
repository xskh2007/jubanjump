from django.db import models
# from django.utils.translation import ugettext_lazy as _

# __all__ = ['MongoScript']
#
#
# class MongoScript(models.Model):
#     title = models.CharField(max_length=128, unique=True, verbose_name='title')
#     database = models.CharField(max_length=128, unique=True, verbose_name='database')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "title"

# class MongoDbs(models.Model):
#     dbname = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.dbname
#
#
# class MongoScript(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __unicode__(self):
#         return self.question_text + '\n' + str(self.pub_date)