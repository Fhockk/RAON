from django.shortcuts import render
from .models import ItemOffer


def home(request, category='auto'):
    offers = ItemOffer.objects.all()
    return render(request, 'browsing.html', {'category': category, 'offers': offers})


def profile(request, user_id=None):
    return render(request, 'profile.html')


def item(request, item_id=None):
    return render(request, 'item.html')
