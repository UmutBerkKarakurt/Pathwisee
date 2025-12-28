from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department, Course, LearningOutcome

# Kullanýcýlarýmýzý panelde düzgün görmek için
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'student_number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'student_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'student_number')}),
    )

# Modelleri Admin paneline kaydediyoruz
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(LearningOutcome)