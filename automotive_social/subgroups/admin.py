from django.contrib import admin
from . import models

# Register your models here.


# inline class used allows us to utlize the admin interface in the django website
# with the ability to edit models on the same page as the parent model
# our GroupMember has a bit of a parent model with Group
# we can use the tabular inline class,so when we visit the admin page, 
# i can click on Group and then see all the GroupMembers which i can then edit as well
# class SubGroupInLine(admin.TabularInline):
# 	model = models.Subscriber


admin.site.register(models.SubGroup)