from django import forms
from db_app.models import Groceries, Lists

# class Groceries(forms.Form):
    # name = forms.CharField(label='Name', max_length=100)
    # password = forms.CharField(label='Name', max_length=100)

    
class ListsForm(forms.ModelForm):
	class Meta:
		model = Lists
		fields = '__all__'


class GroceriesForm(forms.ModelForm):

    class Meta:
        model = Groceries
        fields = ['name', 'quantity', 'measurement', 'is_bought']
