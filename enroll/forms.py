from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address'}))
    email = forms.EmailField(max_length=70, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'@gmail.com'}))
    message = forms.CharField(widget= forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your message here'}))
    