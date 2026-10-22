from rest_framework import serializers
from app1.models.models import Customerr

class CustomerReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customerr
        fields = "__all__"

class CustomerResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customerr
        fields = "__all__"

class CustomerResponseSerializer(serializers.Serializer):
        id = serializers.UUIDField()
        cust_code = serializers.CharField(max_length=20)
        cust_name = serializers.CharField(max_length=100)
        cust_type = serializers.CharField()
    
        contact_person = serializers.CharField(max_length=100)
        email = serializers.EmailField()
        status = serializers.CharField()
        # phone = serializers.CharField(max_length=10)
        # address_line = serializers.CharField()
        city = serializers.CharField(max_length=100)
        state = serializers.CharField(max_length=100)
        # gst_number = serializers.CharField(max_length=15)
        # # payment_terms = serializers.CharField()
        # # status = serializers.CharField()
        # class Meta:
        #      model = Customerr
        #      fields = "__all__"

# class CustomerPutSerializer(serializers.Serializer):

