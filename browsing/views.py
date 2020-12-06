from django.shortcuts import render
from .models import ItemOffer


def home(request, category='auto'):
    offers = ItemOffer.objects.all()
    return render(request, 'browsing.html', {'category': category, 'offers': offers})


def profile(request, user_id=None):
    return render(request, 'profile.html')


def offer(request, offer_uuid=None):
    item = ItemOffer.objects.get(uuid=offer_uuid)
    return render(request, 'offer.html', {'offer': item})
