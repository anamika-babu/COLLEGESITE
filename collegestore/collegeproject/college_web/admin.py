from django.contrib import admin
from . models import Detail,Gender,Department,Course,Purpose
# Register your models here.


admin.site.register(Detail)

class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Gender,GenderAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Course,CourseAdmin)

class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Purpose,PurposeAdmin)

