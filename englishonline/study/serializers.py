from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.fields import FileField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from study.models import *
from django.contrib.auth.models import User, update_last_login


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('role',)
        read_only_fields = ('role',)


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'username', 'email', 'password', 'date_joined', 'userprofile',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BaseAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAudio
        fields = '__all__'


# _________ EGE _________

class Task1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task1
        fields = '__all__'


class EGETask2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task2
        fields = '__all__'


class EGETask3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task3
        exclude = ('question6',)


class EGETask4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task4
        exclude = ('pic3',)


class EGEVariantSerializer(serializers.ModelSerializer):
    creator = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = EGEVariant
        fields = '__all__'

    def create(self, validated_data):
        return EGEVariant.objects.create(**validated_data)


# _________ OGE _________


class OGETask2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task3
        fields = '__all__'


class OGETask3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task4
        exclude = ('pic1', 'pic2', 'pic3',)


class OGEVariantSerializer(serializers.ModelSerializer):
    creator = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = OGEVariant
        fields = '__all__'

    def create(self, validated_data):
        return OGEVariant.objects.create(**validated_data)


# _________ VPR _________


class VPRTask2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task4
        fields = '__all__'


class VPRVariantSerializer(serializers.ModelSerializer):
    creator = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = VPRVariant
        fields = '__all__'

    def create(self, validated_data):
        return VPRVariant.objects.create(**validated_data)


class EGEPopularitySerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    variant = EGEVariantSerializer(read_only=True)
    variant_id = serializers.PrimaryKeyRelatedField(queryset=EGEVariant.objects.all(), source='variant',
                                                    write_only=True)

    class Meta:
        model = EGEPopularity
        fields = '__all__'

    def create(self, validated_data):
        return EGEPopularity.objects.create(**validated_data)


class OGEPopularitySerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    variant = OGEVariantSerializer(read_only=True)
    variant_id = serializers.PrimaryKeyRelatedField(queryset=OGEVariant.objects.all(), source='variant',
                                                    write_only=True)

    class Meta:
        model = OGEPopularity
        fields = '__all__'

    def create(self, validated_data):
        return OGEPopularity.objects.create(**validated_data)


class VPRPopularitySerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())
    variant = VPRVariantSerializer(read_only=True)
    variant_id = serializers.PrimaryKeyRelatedField(queryset=VPRVariant.objects.all(), source='variant',
                                                    write_only=True)

    class Meta:
        model = VPRPopularity
        fields = '__all__'
