from rest_framework import serializers
from .models import SportsClub, Sport, Slot

class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields ="__all__"

class ClubSerializer(serializers.ModelSerializer):
    sports_offered = SportSerializer(read_only=True, many=True)

    class Meta:
        model = SportsClub
        fields = ["id", "name", "location", "sports_offered"]

class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slot
        fields = "__all__"
