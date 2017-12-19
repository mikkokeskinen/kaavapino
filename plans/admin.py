from django.contrib import admin

from .models import Attribute, PlanProject, ValueChoice


@admin.register(PlanProject)
class PlanProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')


class ValueChoiceInline(admin.TabularInline):
    model = ValueChoice
    extra = 0
    prepopulated_fields = {'slug': ('value',)}


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ValueChoiceInline,)
