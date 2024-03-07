from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , Interviews , Faceless , Posting


admin.site.register(CustomUser )
admin.site.register(Interviews )
admin.site.register(Faceless )
admin.site.register(Posting)
