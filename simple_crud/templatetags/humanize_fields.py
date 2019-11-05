from django import template

register = template.Library()

@register.filter(is_safe=True)
def h_fields(field):
    human_name = field.split("_")
    if len(human_name) > 0:
        human_name[0] = human_name[0].capitalize()
    else:
        human_name[0] = human_name[0].capitalize()

    return " ".join(human_name)
