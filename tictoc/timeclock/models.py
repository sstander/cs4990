from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.title

class Punch(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length = 200, blank=True, null=True)

    def is_clocked_in(self):
        if self.time_out == None:
            return True
        return False

    def duration(self):
        if self.time_out and self.time_in:
            return self.time_out - self.time_in
        else:
            return datetime.timedelta()

    def __unicode__(self):
        return "%s (in: %s, out: %s, dur: %s)" % (self.user.username, str(self.time_in), str(self.time_out), str(self.duration()))
        return "%s (%s)" % (self.user.username, str(self.duration()))

    class Meta:
        verbose_name_plural = "punches"
        ordering = ('-time_in',)

        
