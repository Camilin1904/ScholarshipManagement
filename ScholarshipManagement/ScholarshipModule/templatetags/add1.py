from django import template
register = template.Library()

@register.filter(name='add1')
def index(num):
    return num+1