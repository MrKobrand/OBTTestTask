from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from .actions import (
    ContentTypePack,
    UserPack,
    PermissionPack,
    GroupPack
)


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экшен-паков
    """
    return controller.packs.extend([
        ContentTypePack(),
        UserPack(),
        PermissionPack(),
        GroupPack(),
    ])


def register_desktop_menu():
    """
    Регистрация элементов рабочего стола
    """
    desktop.uificate_the_controller(
        controller
    )
