# -*- coding: utf-8 *-*
from django.contrib import admin

from .models import Rule


class RuleAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'order', )
    list_editable = ('order', )

admin.site.register(Rule, RuleAdmin)
