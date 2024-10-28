from django import template

register = template.Library()

@register.filter(name='add_suffix')
def add_suffix(value, suffix):
    return f"{value}{suffix}"

@register.simple_tag
def print_type(liste):
    return liste