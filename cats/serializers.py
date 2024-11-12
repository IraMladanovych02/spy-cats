import requests

from rest_framework import serializers

from cats.models import SpyCat, Mission, Target


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = "__all__"

    def validate_breed(self, value):
        """Validate that the breed exists in TheCatAPI."""
        api_url = f"https://api.thecatapi.com/v1/breeds?name={value.lower()}"
        response = requests.get(api_url)

        if response.status_code != 200:
            raise serializers.ValidationError("Error fetching breed data.")

        breeds = response.json()
        if not breeds:
            raise serializers.ValidationError(f"The breed '{value}' is not recognized.")

        return value


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = "__all__"

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission
