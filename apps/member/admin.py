from django.contrib import admin
from apps.users.models import FamilyMemberRelationship
from apps.member.models import Member, MemberPeriod, About, CostsMembers, TypeMember
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class PersonResource(resources.ModelResource):
    class meta:
        model = Member


class MemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','date_activate', 'person','payment_cost','type_member','amount','payment_method','family_head','family_members','is_member')
    list_editable = ['is_member',]
    list_display_links = ( 'person',)
    list_filter = ('person', 'is_member')
    

    def family_head(self,obj):
        family = FamilyMemberRelationship.objects.filter(relation= obj.person)
        for m in family:
            return m.person
        
    def family_members(self, obj):
        family = FamilyMemberRelationship.objects.filter(person=obj.person)
        return "\n,".join([str(m.relation.first_name) for m in family])
        # for m in family:
        #     return m.relation
    
    

    list_per_page = 500



admin.site.register(Member,MemberAdmin)
admin.site.register(About)
admin.site.register(MemberPeriod)
admin.site.register(CostsMembers)
admin.site.register(TypeMember)
