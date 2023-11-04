from django import template
from ..models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    """
    Возвращает HTML-код для динамически сформированного меню.
    :param menu_name:Имя меню, для которого формируется навигация.
    :return:HTML-код для отображения меню.
    """
    menu_items = MenuItem.objects.filter(menu_name=menu_name).first()

    if not menu_items:
        return ''

    def render_menu_item(item):
        result = f'<li><a href="{item.url}">{item.title}</a>'

        children = item.children.all()
        if children:
            result += '<ul>'
            for child in children:
                result += render_menu_item(child)
            result += '</ul>'

        result += '</li>'
        return result

    return mark_safe(
        f'<ul>{render_menu_item(menu_items)}</ul>')
