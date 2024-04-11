from django import template

register = template.Library()
    
@register.filter
def isHaveValue(value):
    if value:
        return f"{value}"
    else:
        return f"-"
    
    
