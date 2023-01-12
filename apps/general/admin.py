from django.contrib import admin
from apps.general.models import *

# Register your models here.


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('activities', 'first_name', 'last_name','email','phone')
    list_editable = []

    #search_fields = ()
    list_per_page = 20
    
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('other_event', 'day', 'activity_time', 'persons', 'status')
    list_editable = ['persons', 'status']

    #search_fields = ()
    list_per_page = 20
    
    
    


admin.site.register(OtherEvent)
admin.site.register(ActivityName)
admin.site.register(ActivityTime)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
