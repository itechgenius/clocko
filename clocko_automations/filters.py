"""
Clocko_automations/filters.py
"""

from Clocko.filters import ClockoFilterSet, django_filters
from Clocko_automations.models import MailAutomation


class AutomationFilter(ClockoFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"

