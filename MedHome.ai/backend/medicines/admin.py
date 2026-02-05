from django.contrib import admin
from .models import Medicines


@admin.register(Medicines)
class MedicinesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'brand',
        'dosage',
        'price',
        'stock',
        'required_prescriptions',
        'created_on',
        'updated_on',
    )

    search_fields = ('name', 'brand')
    list_filter = ('brand', 'dosage', 'required_prescriptions')
    ordering = ('-created_on',)

    fieldsets = (
        ("Basic Info", {
            "fields": ('name', 'brand', 'dosage')
        }),
        ("Details", {
            "fields": ('description', 'price', 'stock')
        }),
        ("Prescription", {
            "fields": ('required_prescriptions',)
        }),
        ("Timestamps", {
            "fields": ('created_on', 'updated_on')
        }),
    )

    readonly_fields = ('created_on', 'updated_on')
