from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Class)
admin.site.register(Payments)