from django import forms
from .models import Position, Employee, Applicant
# Create your models here.

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title', 'description', 'number_position','position_skills']

'''class AnnounceUpdateForm(forms.ModelForm):
    class Meta:
        model = Announce
        fields = ['title', 'description', 'image']
'''
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'seniority','employee_skills']

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'last_name', 'email', 'angel_url', 'linkedin','apllicant_skills']
