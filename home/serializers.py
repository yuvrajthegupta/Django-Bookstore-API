from rest_framework import serializers
from .models import *



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields=['name','age']
        # exclude = ['id']
        fields='__all__'

    def validate(self,data):
        if 'age' in data and data['age']<18:
            raise serializers.ValidationError({'error':"age cannot be not less than 18"})
        # if data['name']:
        #     for n in data['name']:
        #         if n.isdigit():
        #             raise serializers.ValidationError({'error':"name cant be numeric"})
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category_name']

class BookSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Book
        fields='__all__'
        # depth=1