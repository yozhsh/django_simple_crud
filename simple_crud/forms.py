from django.forms import ModelForm
from simple_crud.models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

