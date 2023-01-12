from django.db import models
from ckeditor.fields import RichTextField
from apps.users.models import Person

# Create your models here.

class Payment(models.Model):
    payment = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.payment}"


class Level(models.Model):
    level = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.level}"

    
class DaysTournament(models.Model):
    day = models.DateField((""), auto_now=False, auto_now_add=False)
    time_start = models.TimeField(null=True, blank=True)
    time_finished = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.day} - {self.time_start}"
    
    class Meta:
        verbose_name = 'Day Event'
        verbose_name_plural = 'Days Event'
    
    
class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.type}"


class Division(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    division = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.type} - {self.division}"


class Costs(models.Model):
    category = models.CharField((""), max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.category} - ${self.price}"

    class Meta:
        verbose_name = 'Cost'
        verbose_name_plural = 'Costs'

class Tournament(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tournament")
    place = models.CharField(max_length=80, default='')
    day = models.ManyToManyField(DaysTournament)
    type = models.ManyToManyField(Type)
    division = models.ManyToManyField(Division)
    level = models.ManyToManyField(Level, blank=True)
    payment = models.ManyToManyField(Payment)
    payment_cost = models.ManyToManyField(Costs, blank=True)
    condition = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    members = models.BooleanField(default=False)
    details = RichTextField(default='')

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    


class Registration(models.Model):
    
    person = models.ForeignKey(Person, verbose_name=("Person"), on_delete=models.CASCADE)
    tournament= models.ForeignKey(Tournament, verbose_name="Tournament", on_delete=models.CASCADE)
    day_time = models.ForeignKey(DaysTournament, verbose_name=("Select Day Time"), null=True,on_delete=models.CASCADE)
    division = models.ForeignKey(Division, verbose_name=("Select Division"), on_delete=models.CASCADE)
    level = models.ForeignKey(Level, verbose_name=("Select Level"), on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, verbose_name=("Select Payment"), on_delete=models.CASCADE)
    payment_cost = models.ForeignKey(Costs, verbose_name=("Select Cost you'll pay"), on_delete=models.CASCADE)
    payment_comment = models.CharField(
        (""), max_length=80, default='', blank=True)
    partner = models.CharField(max_length=50, blank=True, null=True)
    conflicts = models.TextField(max_length=100, blank=True, null=True)
    parent = models.CharField((""), max_length=50,  blank=True, null=True)
    parent_relation = models.CharField((""), blank=True, null=True, max_length=50, choices=[
                                       ('1', 'Mather'), ('2', 'Father'), ('3', 'Other')])
    email_parent = models.EmailField((""), max_length=254, blank=True, null=True)
    phone_parent = models.CharField((""), max_length=50, blank=True, null=True)
    condition = models.BooleanField(default=False)
    
