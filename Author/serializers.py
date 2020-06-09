from rest_framework import serializers
from .models import Author
from django_countries import Countries
from django.utils.encoding import force_text


# class SerializableCountryField(serializers.ChoiceField):
#     def to_representation(self, value):
#         if value in ('', None):
#             return ''  # instead of `value` as Country(u'') is not serializable
#         return super(SerializableCountryField, self).to_representation(value)

# class CustomerSerializerV2(serializers.ModelSerializer):
#     country = SerializableCountryField(allow_blank=True, choices=Countries())


class AuthorSerializer(serializers.ModelSerializer):

    # nationallity = SerializableCountryField(allow_blank=True, choices=Countries())

    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['id', 'name', 'email']