from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(WorkingUser)
admin.site.register(User)
admin.site.register(Recruiter)
admin.site.register(AdminUser)