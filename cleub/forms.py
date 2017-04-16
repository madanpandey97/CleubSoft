from django import forms


from .models import Contact,GetInTouch


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['Name', 'Email', 'Message']


class GetInTouchForm(forms.ModelForm):

    class Meta:
        model = GetInTouch
        fields = ['Email']
