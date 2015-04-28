from django import forms
from feedback.views import WebDevSeminar2Feedback
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
import re


class FeedbackForm(forms.ModelForm):
    
    class Meta:
       model = WebDevSeminar2Feedback
    
    def clean(self):
       phone = re.compile(r'^\d{10}$')
       if phone.match(self.cleaned_data.get('contact')) == None:
          raise ValidationError("Invalid Mobile Number, Your mobile number must be of 10digits and contain only digits from 0-9 without any characters")
       
       elif (WebDevSeminar2Feedback.objects.filter(email = self.cleaned_data.get('email'))):
             raise ValidationError("Email already used to fill the form. Please use a unique email id")
       
       elif (WebDevSeminar2Feedback.objects.filter(contact = self.cleaned_data.get('contact'))):
            raise ValidationError("Contact Number already used once. Please use a unique contact no.")
       
       else:
             return self.cleaned_data
    
