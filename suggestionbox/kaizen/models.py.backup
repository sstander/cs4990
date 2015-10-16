from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

STATUS = (
    ('new', 'New'),
    ('den', 'Denied'),
    ('rev', 'In Review'),
    ('2do', 'To Do'),
    ('imp', 'Implemented'),
)

# Create your models here.
class Profile(UserenaBaseProfile):
    user = models.ForeignKey(User)
    is_admin = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.get_full_name() or self.user.username

class Idea(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, 
                choices=STATUS)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    class Meta:
	verbose_name_plural='categories'

class Comment(models.Model):
    person = models.CharField(max_length=200)
    comment_text = models.TextField()
    idea = models.ForeignKey(Idea)
    pub_date = models.DateTimeField(auto_now_add=True)
