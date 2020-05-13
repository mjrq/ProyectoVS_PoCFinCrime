from django import forms 
from AppVS_PoCFinCrime.models import CUSTOMERS 
  
  
# creating a form 
class ClientesForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = CUSTOMERS 
  
        # specify fields to be used 
        fields = [ 
            "CUSTOMER_SOURCE_UNIQUE_ID", 
            "first_name",
            "last_name",
        ] 
