from django import forms
from .models import Position, Employee, Applicant
# Create your models here.
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title', 'description', 'number_position']

'''class AnnounceUpdateForm(forms.ModelForm):
    class Meta:
        model = Announce
        fields = ['title', 'description', 'image']
'''
class EmployeeForm(forms.Form):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'seniority']

class ApplicantForm(forms.Form):
    class Meta:
        model = Applicant
        fields = ['name', 'last_name', 'email', 'angel_url', 'linkedin']
