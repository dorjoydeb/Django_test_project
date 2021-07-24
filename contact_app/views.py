from django.shortcuts import render
from layout_app.models import Footar
from .models import *

contact_page = 'contact.html'


def home(request):
    Social_data = Footar.objects.all()
    Contact_Top_data = Contact_top_bar.objects.all()
    Contact_body_data = Contact_body_section.objects.all()
    Email_data = Contact_email_section

    super = {
        'social': Social_data,
        'c_t_data': Contact_Top_data,
        'c_b_data': Contact_body_data,
    }

    return render(request, contact_page, super)

# Create your views here.