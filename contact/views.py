from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.template import RequestContext
from django.core.context_processors import csrf

from contact.forms import NameForm, ContactForm

def get_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    message = form.cleaned_data['message']
		    sender = form.cleaned_data['sender']
		    cc_myself = form.cleaned_data['cc_myself']

		    recipients = ['mark.natividad@gmail.com']
		    if cc_myself:
		        recipients.append(sender)

		    send_mail(subject, message, sender, recipients)
		    return HttpResponseRedirect('thanks/')
	else:
		form = ContactForm()
		
	return render_to_response("contact/index.html",  {'form': form,  }, context_instance = RequestContext(request))

def thanks(request):
    return HttpResponse("Thank you for sending your message. Your feedback is important to us.")


