from django import template
register = template.Library()

@register.filter(name='sub1')
def sub1(num):
    return num-1