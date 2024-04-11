from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def draw_menu(menus):
    return mark_safe(render_menu(menus))


def render_menu(menus):
    html = '<ul>'
    for menu in menus:
        html += '<li>'
        html += f'<a href="{menu.get_absolute_url()}">{menu.title}</a>'
        html += '</li>'
    html += '</ul>'
    return html
