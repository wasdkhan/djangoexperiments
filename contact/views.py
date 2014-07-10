from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from contact.forms import NameForm, ContactForm

def get_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['Bobbyjoe500@gmail.com']

			if cc_myself: 
				recipient.append(sender)

			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('thanks/')
	else:
		form = ContactForm()
		
	return render(request, 'contact/index.html', {'form' : form})

def thanks(request):
    return HttpResponse("Thank you for sending your message. Your feedback is important to us.")


