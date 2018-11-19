from django.db import models


class User(models.Model):
    user = models.CharField(max_length=50, default='anonymous')
    comment = models.TextField()
    pos = models.IntegerField(null=True,blank=True)
    neg = models.IntegerField(null=True,blank=True)
    neu = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user


class Topic(models.Model):
    topic = models.CharField(max_length=160, null=False, blank=False, )
    creator = models.CharField(max_length=50, null=False, blank=False, )
    comment = models.TextField()
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.creator
