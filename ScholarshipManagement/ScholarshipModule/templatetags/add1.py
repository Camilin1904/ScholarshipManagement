from django import template
register = template.Library()

@register.filter(name='add1')
def add1(num):
    return num+1