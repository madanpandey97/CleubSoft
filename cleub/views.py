from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForm,GetInTouchForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context

def index(request): 
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "cleub/thanks.html")
        else:
            raise Http404("No MyModel matches the given query.")
    form1 = GetInTouchForm()
    if request.method == 'POST':
            form1= GetInTouchForm(request.POST)
            if form1.is_valid():
                form1.save()
                return render(request, "cleub/thanks.html")
            else:
                raise Http404("No MyModel matches the given query.")
    context = {
        'form':form,
        'form1':form1,
    }
 
    return render(request, "index.html",context)


def thanks(request):
    context={
        'title':"Cleub Home Automation",
        'decription':"Home Automation Home Security Li-Fi",
    }
    return render(request, 'thanks.html',context)
def about(request):
    context={
        'title':"Cleub Home Automation",
        'decription':"Home Automation Home Security Li-Fi",
    }
    return render(request, 'about.html',context)

def services(request):

	return render(request, 'services.html')
def product(request):

	return render(request, 'product.html')

def contactus(request):

	form=ContactForm()
	if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "thanks.html")
            else:
                messages.error(request, "Error")
	return render(request, "contactus.html",{'form':form})