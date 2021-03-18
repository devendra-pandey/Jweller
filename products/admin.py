from django.contrib import admin

# Register your models here.
admin.site.site_header = "Jweler Admin"

from . models import Products

@admin.register(Products)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('image','gold_weight','diamond_carat','design_number','status')