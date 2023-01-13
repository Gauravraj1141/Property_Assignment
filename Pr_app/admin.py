from django.contrib import admin

from .models import Property_detail


@admin.register(Property_detail)
class Property_detailAdmin(admin.ModelAdmin):
    list_display = ('Pr_id', 'Property_name',
                    'Property_address', 'City_name', 'State_name', )
