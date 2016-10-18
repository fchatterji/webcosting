from django import template

register = template.Library()


@register.filter()
def addCssClass(value, arg):
    return value.as_widget(attrs={'class': arg})