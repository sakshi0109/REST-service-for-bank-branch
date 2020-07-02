from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework_jwt.settings import api_settings

from tickets.serializers import BanksSerializer
from tickets.models import Banks

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


from .models import Banks
from .serializers import BanksSerializer


# Create your views here.

# ViewSets define the view behavior.
class BanksView2(generics.ListCreateAPIView):
	"""
	GET api/bank_name/city
	"""
	#print("im in banks view2")
	queryset = Banks.objects.all()
	serializer_class = BanksSerializer
	def get(self, request, bank_name, city):
		try:
			branch_qset = Banks.objects.filter(
				city__iexact=city, bank__name__icontains=bankname)
			
			serializer = BanksSerializer(branch_qset, many=True)
			return Response(serializer.data, safe=False)
		except Banks.DoesNotExist:
			return Response(
				data={
				"message": "Bank in city: {} with name {} does not exist".format(city, bank_name)
				},
				status=status.HTTP_404_NOT_FOUND
			)
			
class ListBanksView(generics.ListCreateAPIView):
	"""
	GET banks/
	"""
	queryset = 	Banks.objects.all().filter
	serializer_class = BanksSerializer	 


class BanksViewSet(generics.ListCreateAPIView):
	"""
	GET api/ifsc/
	"""
	#print("im in banks viewset")
	queryset = Banks.objects.all()
	serializer_class = BanksSerializer
	def get(self, request, *args, **kwargs):
		try:
			a_bank = self.queryset.get(ifsc=kwargs["ifsc"])
			return Response(BanksSerializer(a_bank).data)
		except Banks.DoesNotExist:
			return Response(
				data={
				"message": "Bank with ifsc: {} does not exist".format(kwargs["ifsc"])
				},
				status=status.HTTP_404_NOT_FOUND
			)

# city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(), widget = CheckboxSelectMultiple)
# trade_type = django_filters.ModelMultipleChoiceFilter(queryset=Trade.objects.all(), widget = CheckboxSelectMultiple)

	'''

	def get(self, request, *args, **kwargs):
        try:
            #queryset=Banks.objects.filter(bank_name=kwargs["bank_name"] and city=kwargs["city"])
			a_bank=self.queryset.getall()
			return Response(BanksSerializer(queryset).data)
        except Banks.DoesNotExist:
            return Response(
                data={
                    "message": "Bank in city: {} with bank name:{} does not exist".format(kwargs["city"], kwargs["bank_name"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

	'''