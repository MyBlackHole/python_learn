from django.db.models.fields import Field


def generate_fields(model, add=None, remove=None):
    """
        @author: Zhong Lv
        if `add` and `remove` is None
            :return all fields of model
        else:
            :return fields of models after add and remove
    """
    if add is None:
        add = []
    if remove is None:
        remove = []

    result = ['url', 'id']
    for field in model._meta.get_fields():
        if isinstance(field, Field):
            result.append(field.name)
    for item in remove:
        try:
            result.remove(item)
        except ValueError:
            pass
    for item in add:
        result.append(item)
    return tuple(result)


def can_not_delete_group(**kwargs):
    instance = kwargs.get('instance')
    if instance == instance._meta.model.objects.first():
        return False
    return True
