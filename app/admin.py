from django.contrib import admin
from django.template.defaultfilters import safe
from django.urls import reverse

from . import models


@admin.register(models.Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ['name', 'advices_list']
    readonly_fields = ['advices_view_list']
    autocomplete_fields = ['advices']

    def _get_advice_link(self, advice):
        href = reverse('admin:app_advice_change', args=[advice.id])
        return f'<a href="{href}">{advice.recommendation}</a>'

    def advices_list(self, obj):
        advices = [self._get_advice_link(a) for a in obj.advices.all()]
        return safe(', '.join(advices))

    def _advice_to_html(self, advice):
        out = '<li style="margin-bottom: 5px">'
        out += '<div>'
        out += self._get_advice_link(advice)
        out += f'<div>{advice.scientic_recommendation}</div>'

        if advice.sources.count():
            out += '<b>Sources:</b>'
            out += '<ul style="margin-left: 0">'
            for source in advice.sources.all():
                out += f'<li><a href="">{source.url}</a></li>'
            out += '</ul>'

        out += '</div>'
        out += '</li>'
        return out

    def advices_view_list(self, obj):
        ls = ''.join([self._advice_to_html(a) for a in obj.advices.all()])
        return safe(f'<ul style="margin-left: 0">{ls}</ul>')


class AdviceSourceInline(admin.StackedInline):
    model = models.AdviceSource
    extra = 3


@admin.register(models.Advice)
class AdviceAdmin(admin.ModelAdmin):
    inlines = [AdviceSourceInline]
    search_fields = ['recommendation']
