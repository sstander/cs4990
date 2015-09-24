from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(upload_to="pics/%Y/%m/%d", blank=True, null=True)
    pub_date = models.DateTimeField()
    category = models.ManyToManyField('Category', blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    person = models.CharField(max_length=200)
    comment_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return "%s - %s" %(self.person, self.comment_text[:50])

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.category_name
