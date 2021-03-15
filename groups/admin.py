from django.contrib import admin

from .models import Group, GroupCategory , Message , MessegeComment

admin.site.register(GroupCategory)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(MessegeComment)
