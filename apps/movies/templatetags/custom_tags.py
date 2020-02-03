"""This module contains custom template tags."""
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """Updates url with new page number."""
    query = context['request'].GET.copy()
    if query.get('page'):
        query.pop('page')
    query.update(kwargs)
    return query.urlencode()
