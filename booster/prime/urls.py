from django.urls import path


from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('estimate/', estimate, name='estimate'),
    path('estimate_check/', estimate_check, name='estimate_check'),
    path('confidence/', confidence, name='confidence'),
    path('contacts/', contacts, name='contacts'),
    path('delivery/', delivery, name='delivery'),
    path('paymentMethods/', paymentMethods, name='paymentMethods'),
    path('confirmation/', confirmation, name='confirmation'),
    path('api/v1/fuellist', FuelAPIView.as_view(), name='fuellist'),
    path('api/v1/createclient', ClientAPIView.as_view(), name='createclient'),
    path('api/v1/createclient/<int:pk>/', ClientAPIView.as_view(), name='putclient'),
]
