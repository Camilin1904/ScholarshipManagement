from django import template
register = template.Library()

@register.filter(name='index')
def index(indexable, x):
    return indexable[x]