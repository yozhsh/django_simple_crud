from django import template

register = template.Library()

def fields_injector(model_object):
    data = []
    fields_cls = []
    fields = model_object._meta.get_fields()[1:]
    for field in fields:
        data.append(getattr(model_object, field.name))
        fields_cls.append(field.__class__.__name__)


    model_object.fields = zip(data, fields_cls)
    return model_object

@register.inclusion_tag('crud/table.html', takes_context=True)
def make_crud(context):
    list_queryset = context['crud']['list_data']
    context['crud']['list_data'] = map(fields_injector, list_queryset)
    return context