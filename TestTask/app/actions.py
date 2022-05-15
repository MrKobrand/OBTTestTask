from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow


class ContentTypePack(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True
    add_to_desktop = True
