from django.shortcuts import render,redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.db.utils import IntegrityError

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

                messages.success(request, "Form Submitted Successfully")
                redirect('home')
            except IntegrityError as I:
                print(I)
                messages.error(request, "Email Already Exists")

    return render(request,'home.html')