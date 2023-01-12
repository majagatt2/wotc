from django.contrib import admin
from apps.users.models import FamilyMemberRelationship
from apps.member.models import Member, MemberPeriod, About
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class PersonResource(resources.ModelResource):
    class meta:
        model = Member


class MemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('date_activate', 'person', 'family_depends', 'is_member')
    list_editable = ['is_member',]
    list_filter = ('person', 'is_member')
    

    def family_depends(self,obj):
        family = FamilyMemberRelationship.objects.filter(relation= obj.person)
        for m in family:
            return m.person
    
    

    list_per_page = 20



admin.site.register(Member,MemberAdmin)
admin.site.register(About)
admin.site.register(MemberPeriod)