from django import template
register = template.Library()

@register.filter(name='index')
def replaceType(numType):
    a = ''
    match(numType):
        case(0): a = 'Porcentaje'
        case(1): a = 'Dinero'
    return a