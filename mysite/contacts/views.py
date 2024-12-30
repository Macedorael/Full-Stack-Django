from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.decorators import permission_required



from .forms import NameForm, ContactForm


@permission_required('contacts.add_contact')
def create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return HttpResponseRedirect(reverse('contacts:thanks', args=(name,)))
    else:
        form = ContactForm()
    return render(request, 'contacts/create.html', {'form': form})

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return HttpResponseRedirect(reverse('contacts:thanks', args=(name,)))
        
    else:
        form = NameForm()   
    
    return render(request, 'contacts/name.html', {'form': form})


def thanks(request, name):
    
    return HttpResponse(f'Obrigado { name }!')
# Create your views here.
