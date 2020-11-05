from django.http import JsonResponse
from django.shortcuts import render
from pytz import unicode
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomerSerializer
from .models import Customer
from datetime import datetime


@api_view(http_method_names=['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def customers(request):

    params = request.query_params
    if params:

        ordering = params.get('ordering')

        if params.get("country"):
            country = params.get("country")
            if ordering:
                q = Customer.objects.filter(country=country).order_by('orderdate')
            else:
                q = Customer.objects.filter(country=country)
            ser = CustomerSerializer(q, many=True)
            return JsonResponse(ser.data, safe=False)

        elif params.get("start") and params.get("end"):
            # Date format: YYYY-MM-DD // but passing: DD.MM.YYYY
            start = datetime.strptime(params.get("start"), '%d.%m.%Y').strftime('%Y-%m-%d')
            end = datetime.strptime(params.get("end"), '%d.%m.%Y').strftime('%Y-%m-%d')
            if ordering:
                q = Customer.objects.filter(orderdate__gte=start).filter(orderdate__lte=end)\
                    .order_by('orderdate')
            else:
                q = Customer.objects.filter(orderdate__gte=start).filter(orderdate__lte=end)

            ser = CustomerSerializer(q, many=True)
            return JsonResponse(ser.data, safe=False)

        else:
            return JsonResponse(
                {
                    'request': params,
                    'user': unicode(request.user),
                    'auth': unicode(request.auth)
                }
            )

    else:
        return JsonResponse({})






