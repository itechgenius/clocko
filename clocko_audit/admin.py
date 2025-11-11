"""
admin.py
"""

from django.contrib import admin

from Clocko_audit.models import AuditTag, ClockoAuditInfo, ClockoAuditLog

# Register your models here.

admin.site.register(AuditTag)

