from django import forms
from .models import User,Topic
from django.forms import fields_for_model
TOPIC_CHOICES = (('general', 'General enquiry'), ('bug', 'Bug report'), ('suggestion', 'Suggestion'),)


#psf = form_for_model(Publisher)
class ContactForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user', 'comment',)




# TOPIC_CHOICES = (('general', 'General enquiry'), ('bug', 'Bug report'), ('suggestion', 'Suggestion'),)
#
#
# class ContactForm(forms.Form):
#     topic = forms.ChoiceField(choices=TOPIC_CHOICES)
#     message = forms.CharField(widget=forms.Textarea(), initial='Change it for your comment')
#     sender = forms.EmailField(required=False)
