from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.conf import settings
from emailapp.forms import StudentForm
# Create your views here.

def stdform(request):
	form = StudentForm()
	if request.method == 'POST':
	    form = StudentForm(request.POST)
	    if form.is_valid():
		    form.save()
		    subject = 'Learning Software'
		    message = 'Dear candidate, \nWe are pleased to offer you an internship at our company'
		    receipient = form.cleaned_data.get('email')
		    send_mail(subject,message,settings.EMAIL_HOST_USER,[receipient],fail_silently=False)
	    return redirect('/')
	return render(request, 'home.html', {'form':form})