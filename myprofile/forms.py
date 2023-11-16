from .models import client_info
from django.forms import ModelForm

# class UserEditForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = '__all__' 

class UserProfileForm(ModelForm):
    class Meta:
        model = client_info
        fields = '__all__'