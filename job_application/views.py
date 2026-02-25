from django.shortcuts import render,redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.db.utils import IntegrityError
from django.core.mail import EmailMessage

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            try:

                Form.objects.create(first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    date=date,
                                    occupation=occupation)
                
                message_body = f"Thank you for submitting you application {first_name} \nwe will contact you soon"
                email = EmailMessage(subject='Form submission confirmation',
                                     body=message_body,
                                     to=[email])
                email.send()
                messages.success(request, "Form Submitted Successfully")
                redirect('home')
            except IntegrityError as I:
                print(I)
                messages.error(request, "Email Already Exists")

    return render(request,'home.html')