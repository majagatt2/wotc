from django.db import models
from apps.users.models import Person
from ckeditor.fields import RichTextField

# Create your models here.


class Newsletter(models.Model):

    EMAIL_STATUS_CHOICES = (
        ('Draft', "Draft"),
        ('Published', 'Published')
    )

    name = models.CharField(max_length=250, default="",blank=True)
    subject = models.CharField(max_length=250)
    #body = models.TextField(blank=True, null=True)
    body = RichTextField(blank=True,null=True)
    email = models.CharField(("Email"),max_length=250)
    bcc = models.CharField(("BCC"), max_length=250)
    created = models.DateTimeField(auto_now_add=True)
   

    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)

    def __str__(self):
        return self.name
    
    def get_email(self):
        return Person.objects.filter(email=self)

    class Meta:
        ordering = ('-created',)


