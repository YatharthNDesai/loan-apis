from rest_framework.generics import ListAPIView,CreateAPIView


from loan_apps.serializers import LoanApplicationSerializer,AddressSerializer,BusinessSerializer
from loan_apps.models import LoanApplication,Business,Address

class LoanApplicationListById(ListAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return LoanApplication.objects.filter(id=id)

class LoanApplicationList(ListAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer


class AddressCreate(CreateAPIView):
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request,*args,**kwargs)

class BusinessCreate(CreateAPIView):
    serializer_class = BusinessSerializer

    def create(self,request,*args,**kwargs):
        return super().create(request,*args,**kwargs)

class LoanApplicationCreate(CreateAPIView):
    serializer_class = LoanApplicationSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request,*args,**kwargs)

class AddressList(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class BusinessList(ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer