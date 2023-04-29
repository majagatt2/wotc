from django.db import models
from datetime import date

from django.contrib.auth.models import AbstractUser
# Create your models here.


class Gender(models.Model):
    gender = models.CharField((""), max_length=50, default='')
   
    def __str__(self):
        return f"{self.gender}"


class Person(AbstractUser):
    
    first_name = models.CharField(max_length=30,  null = False)
    last_name = models.CharField(max_length=30,  null = False)
    adress = models.CharField(max_length=80)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    zip = models.IntegerField(null=True)
    phone = models.CharField(max_length=40)
    
    
    # default=date.today para cuando inicio primera vez
    birthdate = models.DateField(default=date.today )
    
    gender = models.ForeignKey(Gender, verbose_name=("Select gender"), on_delete=models.CASCADE, null=True)
    ntrp_rating = models.CharField(("NTRP Rating"), max_length=10, blank=True, null=True)
    profilePicture = models.ImageField(
        upload_to='media/profilePicture', null=False, default='Profile  Picture')
    family_members = models.ManyToManyField(
        'self', through='FamilyMemberRelationship', through_fields=('person', 'relation'))
   
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        
        return f"{self.last_name}, {self.first_name}"

    @property
    def get_age(self):
        return date.today().year - self.birthdate.year
    
    
    
    


class Relations(models.Model):
    relation = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.relation}"
    
    class Meta:
        verbose_name = 'Relation'
        verbose_name_plural = 'Relations'
       

    


class FamilyMemberRelationship(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,
                        related_name='relationships')
    relation = models.ForeignKey(Person, on_delete=models.CASCADE,
                         related_name='reverse_relationships')
    relation_type = models.ForeignKey(Relations, verbose_name="Select relation:",on_delete=models.CASCADE)


