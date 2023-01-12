from django.db import models
from datetime import date, datetime
from apps.users.models import Person
from ckeditor.fields import RichTextField

# Create your models here.


class MemberPeriod(models.Model):
    date_start = models.DateField()
    date_finished = models.DateField()
    
    def __str__(self):
        return f"{self.date_start} to {self.date_finished}"
    
    
class About(models.Model):
    about = RichTextField()

    def __str__(self):
        return str(self.about)
    
    
    
   
class Member(models.Model):
    date_period = models.ForeignKey(MemberPeriod, verbose_name=(""),  on_delete=models.CASCADE)
    date_activate = models.DateField(("date_activate"), default=date.today,  editable=True)
    person = models.ForeignKey(Person, verbose_name=("Member"), on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)
    
    def get_start(self):
        return self.date_start

        
    @property
    def get_today(self):
        today = date.today()
        return today

    @property
    def get_current_start(self):
        today = date.today()
        day = 1
        month = 5
        year_before = today.year - 1
        year_current = today.year
      
        if today >= date(year_current,1,1) and today <= date(year_current,4,30):
            date_current_start = date(year_before, month, day)
            return date_current_start
        if today >= date(year_current, 5, 1) and today <= date(year_current, 12, 31):
            date_current_start = date(year_current, month, day)
            return date_current_start
        
    
    
    @property
    def get_current_expiration(self):
        today = date.today()
        day = 30
        month = 4
        year_current = today.year
        year_next = today.year + 1
        if today >= date(year_current, 5, 1) and today <= date(year_current, 12, 31):
            date_expiration = date(year_next, month, day)
            return date_expiration
        if today >= date(year_current, 1, 1) and today <= date(year_current, 4, 30):
            date_expiration = date(year_current, month, day)
            return date_expiration
        
    @property
    def get_status(self):
        status = True
        if self.date_activate >= self.get_current_start:
            status = True
        else:
            status = False
        return status
        

            
        
     


