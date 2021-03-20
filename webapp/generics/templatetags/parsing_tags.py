from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value as a list split on key
    """
    return value.split(key)

@register.filter(name="has_group")
def has_group(user, group_name):
    """
        Returns a boolean whether the user is in the specified group
    """
    return user.groups.filter(name=group_name).exists()

@register.filter(name="get_type")
def get_type(value):
    """
        Returns the type of value
    """
    return type(value)

@register.filter(name="replace")
def replace(value, replace):
    """
        Returns the value with old replaced with new
    """
    strings = replace.split(',')
    if len(strings) == 2:
        old = strings[0]
        new = strings[1]
    else:
        raise TemplateSyntaxError("replace requires 2 arguments, {} provided".format(len(strings)))

    return value.replace(old, new)
