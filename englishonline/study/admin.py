from django.contrib import admin

from study.models import *


admin.site.register(UserProfile)

admin.site.register(BaseAudio)
admin.site.register(Task1)
admin.site.register(Task2)
admin.site.register(Task3)
admin.site.register(Task4)
admin.site.register(EGEVariant)
admin.site.register(OGEVariant)
admin.site.register(VPRVariant)
admin.site.register(EGEPopularity)
admin.site.register(OGEPopularity)
admin.site.register(VPRPopularity)


