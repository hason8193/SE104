from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Hoadon,PhieuKB,Benhnhan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    name = forms.CharField(label="",max_length=100,widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class FormThemBN(forms.ModelForm):
    hoten = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Họ tên", "class": "form-control"}), label="")
    gioitinh = forms.ChoiceField(required=True, choices=[('M', 'Male'), ('F', 'Female')], widget=forms.Select(attrs={"class": "form-control"}), label="")
    namsinh = forms.IntegerField(required=True, widget=forms.TextInput(attrs={"placeholder": "Năm sinh", "class": "form-control"}), label="")
    diachi = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Địa chỉ", "class": "form-control"}), label="")
    ngaykham = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date", "class": "form-control","readonly": "readonly"}), label="")

    class Meta:
        model = Benhnhan
        exclude = ("patient",)


class FormPhieuKB(forms.ModelForm):
    hoten = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Họ tên", "class":"form-control"}), label="")
    ngaykham= forms.DateField(required=True, widget=forms.DateInput(attrs={"type":"date", "class":"form-control"}), label="")
    trieuchung = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"Symptoms", "class":"form-control"}), label="Symptoms")
    dudoan = forms.ChoiceField(required=True, widget=forms.Select(attrs={"class":"form-control"}), label="Prediction")
    
    class Meta:
        model = PhieuKB
        exclude = ("user",)

class FormthemThuoc(forms.ModelForm):
    tenThuoc = forms.CharField()
    giatheovien = forms.IntegerField()
    giatheochai = forms.IntegerField()
    sovienthem = forms.IntegerField()
    sochaithem = forms.IntegerField()


        
# class AddBill(forms.ModelForm):
#     name = forms.CharField(disabled=True,required=True, widget=forms.TextInput(attrs={"placeholder":"Name", "class":"form-control"}), label="")
#     date= forms.DateField(disabled=True,required=True, widget=forms.DateInput(attrs={"type":"date", "class":"form-control"}), label="")
#     cureCost = forms.IntegerField(initial=30000,disabled=True,required=True, widget=forms.TextInput(attrs={"placeholder":"cure cost","class":"form-control"}), label="")
#     medicineCost = forms.IntegerField(disabled=True,required=False, widget=forms.TextInput(attrs={"placeholder":"medicine cost","class":"form-control"}), label="")
#     class Meta:
#         model = Bill
#         exclude = ("user",)
#         model = MedicalExamination
#         exclude = ("user",)
