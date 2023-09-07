from django.contrib.auth import logout
from rest_framework import generics
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .models import *
from .serializers import *


# Create your views here.


def home(request):
    fl = Fuel.objects.all()
    ct = City.objects.all()
    print(ct)
    print(fl)
    return render(request, 'prime/home.html', {'fl': fl,
                                               'ct': ct})


def estimate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        car_model = request.POST.get('car_model')
        color = request.POST.get('color')
        gos_number = request.POST.get('gos_number')
        fuel_type = request.POST.get('fuel_type')
        volume = request.POST.get('volume')
        price = request.POST.get('price')
        payment = request.POST.get('payment')
        city = request.POST.get('city')
        address = request.POST.get('address')
        delivery_time = request.POST.get('delivery_time')

        element = Client(name=name,
                         phone_number=phone_number,
                         car_model=car_model,
                         color=color,
                         gos_number=gos_number,
                         fuel_type=fuel_type,
                         volume=volume,
                         price=price,
                         payment=payment,
                         city=city,
                         address=address,
                         delivery_time=delivery_time,
                         status=0,
                         )
        element.save()
        return render(request, 'prime/estimate.html', {'name': name,
                                                       'phone_number': phone_number,
                                                       'car_model': car_model,
                                                       'color': color,
                                                       'gos_number': gos_number,
                                                       'fuel_type': fuel_type,
                                                       'volume': volume,
                                                       'price': price,
                                                       'payment': payment,
                                                       'city': city,
                                                       'address': address,
                                                       'delivery_time': delivery_time,
                                                       })


def estimate_check(request):
    order = request.GET.get('check')
    spisok = Client.objects.filter(id=order)
    if len(spisok) > 0:
        return render(request, 'prime/estimate.html', {'name': spisok[0].name,
                                                        'phone_number': spisok[0].phone_number,
                                                        'car_model': spisok[0].car_model,
                                                        'color': spisok[0].color,
                                                        'gos_number': spisok[0].gos_number,
                                                        'fuel_type': spisok[0].fuel_type,
                                                        'volume': spisok[0].volume,
                                                        'price': spisok[0].price,
                                                        'payment': spisok[0].payment,
                                                        'city': spisok[0].city,
                                                        'address': spisok[0].address,
                                                        'delivery_time': spisok[0].delivery_time,
                                                        })
    else:
        return Http404


def add_client(request):
    if request.method == 'POST':
        form = newClientForm(request.POST)
        if form.is_valid():
            try:
                Client.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления заказа')

    else:
        form = newClientForm()
    return render(request, "prime/home.html", {'form': form})


def confidence(request):
    return render(request, 'prime/confidence.html')


def confirmation(request):
    return render(request, 'prime/confirmation.html')


def contacts(request):
    return render(request, 'prime/contacts.html')


def delivery(request):
    return render(request, 'prime/delivery.html')


def paymentMethods(request):
    return render(request, 'prime/paymentMethods.html')


class FuelAPIView(generics.ListAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer


class ClientAPIView(APIView):
    def get(self, request):
        c = Client.objects.all()
        return Response({'Clients': ClientSerializer(c, many=True).data})

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'Clients': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Client.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Client": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Client.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"Client": "deleted client" + str(pk)})
