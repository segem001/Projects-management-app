from rest_framework import serializers
from .models import Profile,Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'avatar','fullname','email')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','uploaded_by','landing_image','screen_one','screen_two','description','technologies','link','date')
