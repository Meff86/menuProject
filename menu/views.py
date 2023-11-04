from django.shortcuts import render
from .models import MenuItem


def render_menu(request, menu_name):
    """
    Возвращает HTML-страницу с динамически сформированным меню.
    :param request:Объект запроса Django.
    :param menu_name:Имя меню, для которого формируется навигация.
    :return:HTTP-ответ с HTML-страницей.
    """
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    context = {"menu_items": menu_items, "request": request, "menu_name": menu_name}
    return render(request, 'menu/render_menu.html', context)
