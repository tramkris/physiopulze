from physio.forms import ContactForm
from django.shortcuts import render, redirect, HttpResponse 
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def contact(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)

      print(form.errors)

      if form.is_valid(): 
         name = form.cleaned_data['name']
         email = form.cleaned_data['email']
         phone = form.cleaned_data['phone']
         subject = form.cleaned_data['subject']
         message = form.cleaned_data['message']

         body = "Patient Name    : " +  name + "\n\n" + "Phone Number   : " + phone + "\n\n" + "Email Address  : " +  email + "\n\n"+ "Message  : " + message

         EmailMessage(
              'Message From Patient {}'.format(name),
              body,
              email,
              [settings.EMAIL_HOST_USER]
          ).send()

         return redirect('success')
      else:
         return redirect('failure')

   else:
      form = ContactForm()
   return render(request,'contactus.html', {'form': form})

def success(request):
   return render(request,'success.html')
   
def failure(request):
   return render(request,'failure.html')

def home(request):
    return render(request,'home.html')

def contactus(request):
    return render(request,'contactus.html')

def treatmentsoffered(request):
    return render(request,'treatmentsoffered.html')

def aboutus(request):
   return render(request,'aboutus.html')

def backpain(request):
    return render(request,'treatments-offered/back-pain.html')

def jointpain(request):
    return render(request,'treatments-offered/joint-pain.html')

def neckpain(request):
    return render(request,'treatments-offered/neck-pain.html')

def headaches(request):
   return render(request,'treatments-offered/head-aches.html')

def strainssprains(request):
   return render(request,'treatments-offered/strains-sprains.html')

def sportsinjury(request):
   return render(request,'treatments-offered/sports-injury.html')

def orthorehabilitation(request):
   return render(request,'treatments-offered/ortho-rehabilitation.html')

def neurorehabilitation(request):
   return render(request,'treatments-offered/neuro-rehabilitation.html')