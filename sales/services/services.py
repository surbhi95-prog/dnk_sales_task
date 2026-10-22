from sales.models.models import Customerr
from rest_framework.exceptions import NotFound
class CustomerService:

    @staticmethod
    def create_user(validated_data):
        # data = validated_data.copy()
        # id = data.pop("id")
        # cust= Customerr.objects.exists(id=id)
        # if not cust:
        cust = Customerr.objects.create(**validated_data)
        return cust

    @staticmethod
    def list_all_cust():
        return Customerr.objects.all()

    @staticmethod
    def get_by_id(id):
        return Customerr.objects.get(id=id)


    @staticmethod
    def update_cust(validated_data,id):
        try:
            cust = Customerr.objects.get(id=id)
        except Customerr.DoesNotExist:
            raise NotFound("Customer with this ID does not exist")
        for fields,val in validated_data.items():
            setattr(cust,fields,val)
        cust.save()
        return cust
    # def update_cust(id,validated_data):
    #     try:
    #         cust = Customerr.objects.get(id=id)
    #     except Customerr.DoesNotExist:
    #         raise NotFound("Customer Not Found")

    #     for field,value in validated_data.items():
    #         setattr(cust,field,value)

    #     cust.save()

    #     return cust


    @staticmethod
    def patch_cust(validated_data,id):
        try:
            cust = Customerr.objects.get(id=id)
        except Customerr.DoesNotExist:
            raise NotFound("Id not found")
        for fields, vals in validated_data.items():
            setattr(cust,fields,vals)

        cust.save()
        return cust

    # def patch_cust(id,validated_data):

    #     try:
    #         cust = Customerr.objects.get(id=id)

    #     except Customerr.DoesNotExist:
    #         raise NotFound("Cust with this code does not exist")

    #     for field,val in validated_data.items():
    #         setattr(cust,field,val)

    #     cust.save()
    #     return cust

    @staticmethod
    def delete_by_id(id):
         try:
            emp = Customerr.objects.get(cust_code=id)
         except Customerr.DoesNotExist:
             raise NotFound("This cust code does not exist")

         emp.delete()

    @staticmethod
    def delete_all():
        cust = Customerr.objects.all()

        cust.delete()