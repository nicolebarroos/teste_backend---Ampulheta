from django.contrib import admin

from api.models import User, Project, Time


class UserInLine(admin.StackedInline):
    model = User
    #classes = ['collapse']
    #fk_name = None
    #fields = ('email', 'username', 'first_name', )
    #max_num = 20


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ['users', 'times',]


admin.site.register(User)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Time)
