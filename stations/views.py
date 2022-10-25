from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

with open(r'C:\Users\User\PycharmProjects\Django\1.2-requests-templates\pagination\data-398-2018-08-30.csv',
          encoding='UTF-8') as f:
    stan = []
    DictReader_obj = csv.DictReader(f)
    for item in DictReader_obj:
        stan.append(item)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(stan, 15)
    stans = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': stans,
        'page': page_number,
    }
    return render(request, 'stations/index.html', context)
