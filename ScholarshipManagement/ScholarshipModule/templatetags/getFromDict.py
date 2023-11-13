from django import template
register = template.Library()

@register.filter(name='getFromDict')
def get(dict, key):
    return dict.get(key)