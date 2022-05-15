from m3_ext.ui import all_components as ext
from objectpack.ui import BaseEditWindow


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%',
            max_length=128
        )

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%',
            allow_blank=True,
            format='d.m.Y'
        )

        self.field__superuser_status = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            anchor='100%',
        )

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%',
            max_length=150,
            max_length_text='Никнейм должен иметь не более 150 символов!',
        )

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=True,
            anchor='100%',
            max_length=30
        )

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=True,
            anchor='100%',
            max_length=150
        )

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%',
            regex=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        )

        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            anchor='100%',
            checked=False
        )

        self.field__is_active = ext.ExtCheckBox(
            label=u'active',
            name='is_active',
            anchor='100%',
            checked=True
        )

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            anchor='100%',
            allow_blank=True,
            format='d.m.Y'
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined
        ))

    def set_params(self, params):
        """
        Установка параметров окна
        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
