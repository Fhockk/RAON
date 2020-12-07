from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import ItemOffer


def home(request, category='auto'):
    offers = ItemOffer.objects.all()
    return render(request, 'browsing.html', {'category': category, 'offers': offers})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})


def offer(request, offer_uuid):
    item = get_object_or_404(ItemOffer, uuid=offer_uuid)
    return render(request, 'offer.html', {'offer': item})
