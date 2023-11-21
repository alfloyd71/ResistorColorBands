from django import forms 
from django.forms import  ModelForm
from .models import RCB

class RCBForm(ModelForm): # QuoteForm inherits from ModelForm
   
    class Meta:
        model = RCB
        fields = [
            'firstband', 'secondband', 'thirdband', 'fourthband','resistancevalue',
        
         
        ]
    
    def __init__(self, *args, **kwargs):
        super(RCBForm, self).__init__(*args, **kwargs)
        self.fields['firstband'].required = True
        self.fields['firstband'].label='First Band'
        self.fields['secondband'].label='Second Band'
        self.fields['thirdband'].label='Multiplier'
        self.fields['fourthband'].label='Tolerance'
        self.fields['resistancevalue'].label='Resistance Value'
    