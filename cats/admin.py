from django.contrib import admin

from cats.models import SpyCat, Mission, Target

admin.site.register(SpyCat)
admin.site.register(Mission)
admin.site.register(Target)