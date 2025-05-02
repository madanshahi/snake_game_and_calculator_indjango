from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactform/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'contactform/contact.html', {'form': form})

def mysite(request):  # 🔧 'request' parameter अनिवार्य छ
    return render(request, 'contactform/welcome.html')  # 🔧 Corrected render syntax
