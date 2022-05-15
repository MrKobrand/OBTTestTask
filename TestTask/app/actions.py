from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from m3 import ApplicationLogicException
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow


class ContentTypePack(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True
    add_to_desktop = True


class UserPack(ObjectPack):
    model = User
    add_window = edit_window = UserAddWindow
    add_to_menu = True
    add_to_desktop = True

    columns = [
        {
            'data_index': 'password',
            'header': u'Пароль',
        },
        {
            'data_index': 'last_login',
            'header': u'last login',
        },
        {
            'data_index': 'is_superuser',
            'header': u'superuser status',
        },
        {
            'data_index': 'username',
            'header': u'username',
        },
        {
            'data_index': 'first_name',
            'header': u'first name',
        },
        {
            'data_index': 'last_name',
            'header': u'last name',
        },
        {
            'data_index': 'email',
            'header': u'email address',
        },
        {
            'data_index': 'is_staff',
            'header': u'staff status',
        },
        {
            'data_index': 'is_active',
            'header': u'active',
        },
        {
            'data_index': 'date_joined',
            'header': u'date joined',
        },
    ]

    def save_row(self, obj, create_new, request, context, *args, **kwargs):
        try:
            obj_from_db = User.objects.get(username=obj.username)
        except User.DoesNotExist:
            obj.save()
            return obj
        else:
            if create_new:
                raise ApplicationLogicException(u'Пользователь с этим никнеймом уже существует!')
            else:
                old_object_instance = User.objects.get(pk=obj.pk)
                if old_object_instance.username == obj.username:
                    obj.save(update_fields=frozenset((
                        'password', 'last_login', 'is_superuser', 'first_name', 'last_name',
                        'email', 'is_staff', 'is_active', 'date_joined'
                    )))
                    return obj
                else:
                    raise ApplicationLogicException(u'Пользователь с этим никнеймом уже существует!')
