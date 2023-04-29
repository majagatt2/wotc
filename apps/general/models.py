from django.db import models
from datetime import date 
from ckeditor.fields import RichTextField

# Create your models here.
    


class OtherEvent(models.Model):
    other_event = models.CharField(("Event"), max_length=50)
    
    def __str__(self):
        return f'{self.other_event}'
    
class ActivityName(models.Model):
    activity_name = models.CharField((""), max_length=50)
    
    def __str__(self):
        return f'{self.activity_name}'
    

class ActivityTime(models.Model):
    activity = models.ForeignKey(ActivityName, verbose_name=(""), on_delete=models.CASCADE)
    time_start = models.TimeField((""), auto_now=False, auto_now_add=False)
    time_finish = models.TimeField((""), auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f'{self.activity} - {self.time_start} to {self.time_finish}'

    
class Activities(models.Model):
    other_event = models.ForeignKey(OtherEvent, verbose_name=("Event"), on_delete=models.CASCADE)
    day = models.DateField(("Day"), auto_now=False, auto_now_add=False)
    activity_time = models.ForeignKey(ActivityTime, verbose_name=("Time"), on_delete=models.CASCADE)
    persons = models.IntegerField(("Persons"))
    status = models.BooleanField(("Status"), default=True)
    
    
    def __str__(self):
        return f'{self.other_event} - {self.activity_time} - {self.day}'
    
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        
        
        
    @property
    def get_volunteers(self):
        count = 0
        volunteers = Volunteer.objects.all()
        for v in volunteers:
            if v.activities.id == self.id:
                count += 1
        return count
    
    @property
    def get_spots_left(self):
        left = self.persons - self.get_volunteers
        return left
        

class Volunteer(models.Model):
    activities = models.ForeignKey(Activities, verbose_name=("Your chosen activity"), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,  null=False)
    last_name = models.CharField(max_length=30,  null=False)
    email = models.EmailField(("emali:"), max_length=254)
    phone = models.CharField(max_length=40)
    

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


