from django.db import models
from django.contrib.auth.models import User
import hashlib
import re

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField('Short Bio', blank=True, null=True)
    profile_picture = models.ImageField(upload_to="pics/%Y/%m/%d", blank=True, null=True)
    #following = models.ManyToManyField('self', blank=True) One of the two below
    #following = models.ManyToManyField('Profile', blank=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False)

    def get_gravatar_img_path(self):
        if self.user.email:
            return "https://www.gravatar.com/avatar/%s" % (hashlib.md5(self.user.email).hexdigest(),)
        return "https://www.gravatar.com/avatar/%" % (hashlib.md5("no email found").hexdigest(),)

    def __unicode__(self):
        return self.user.get_full_name() or self.user.username

class Post(models.Model):
    profile = models.ForeignKey(Profile)
    body = models.CharField(max_length=140)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def body_with_links(self):
        # got this nice bit of code from http://stackoverflow.com/questions/17568168/python-regex-to-replace-urls-in-text-with-links-conversion-from-php
        _link = re.compile(r'(?:(http://)|(https://)|(www\.))(\S+\b/?)([!"#$%&\'()*+,\-./:;<=>?@[\\\]^_`{|}~]*)(\s|$)', re.I)

        def replace(match):
            groups = match.groups()
            protocol = groups[0] or groups[1] or ''  # may be None
            www_lead = groups[2] or ''  # may be None
            return '<a href="http://{1}{2}" rel="nofollow">{0}{1}{2}</a>{3}{4}'.format(

                protocol, www_lead, *groups[3:])
        return _link.sub(replace, self.body)

    def __unicode__(self):
        return self.body
