from django.contrib import admin
from apps.tournament.models import *
# Register your models here.


class DaysTournamentAdmin(admin.ModelAdmin):
    list_display = ('day', 'time_start', 'time_finished')
    list_editable = []

    #search_fields = ()

    list_per_page = 10


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'condition', 'public', 'members')
    list_editable = ['condition', 'public', 'members']


class CostsAdmin(admin.ModelAdmin):
    list_display = ('category', 'price')
    list_editable = ['price',]


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('person', 'tournament','day_time','division','condition')
    list_editable = ['condition', ]
    list_filter = ('tournament', 'division', 'person')
    

    list_per_page = 20





admin.site.register(Payment)
admin.site.register(Level)
admin.site.register(DaysTournament, DaysTournamentAdmin)
admin.site.register(Type)
admin.site.register(Division)
admin.site.register(Tournament,TournamentAdmin)
admin.site.register(Costs,CostsAdmin)
admin.site.register(Registration,RegistrationAdmin)
