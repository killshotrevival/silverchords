from django.contrib import admin
from .models import work_info, reviews, Userhistory

admin.site.register(work_info)
admin.site.register(reviews)
admin.site.register(Userhistory)
