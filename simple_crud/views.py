from django.shortcuts import render
from django.views.generic import TemplateView
from simple_crud.forms import AuthorForm, Author
# Create your views here.


class TestView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Author.objects.all()
        context['crud'] = {
            'form_list': AuthorForm(),
            'list_data': data
        }
        return context