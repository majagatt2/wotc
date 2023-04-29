from django.contrib import admin
from apps.users.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin




# Register your models here.


class PersonResource(resources.ModelResource):
    class meta:
        model = Person
        fields = ('last_name', 'first_name','birthdate', )
        #exclude = ('id','password', 'last_login','is_super','groups','username','is_staff','is_active','date_joined','profilePicture', 'get_age','get_familyMembers','adress','city','state','zip','phone','ntrp_rating','family_members')
        export_order = ('first_name', 'last_name', )


class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','last_name', 'first_name', 'last_login','family_Members','birthdate', )
    search_fields = ('last_name', 'first_name',)
    list_editable = []
    

    def family_Members(self, obj):
        return "\n, ".join([str(m.first_name) for m in obj.family_members.all()])
    
    
    list_per_page= 30
    
    
    
class RelationsAdmin(admin.ModelAdmin):
    list_display = ('relation',)
    
    
    
    
class FamilyMemberRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id','person','relation','relation_type')
    list_filter = ('person','relation',)

    list_per_page = 10




    
admin.site.register(Person, PersonAdmin)
admin.site.register(Gender)
admin.site.register(Relations, RelationsAdmin)
admin.site.register(FamilyMemberRelationship,
                    FamilyMemberRelationshipAdmin)


