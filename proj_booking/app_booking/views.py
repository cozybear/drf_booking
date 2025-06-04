from django.shortcuts import render
from app_booking.models import SportsClub, Sport, Slot
from django.http import JsonResponse, HttpResponse
from django.template import loader  
from .serializers import ClubSerializer, SportSerializer, SlotSerializer
from rest_framework import response, request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import json, datetime
from .custom import AvailableSlots
# Create your views here.

class ClubAV(APIView):

    def get(self, request):
        clubs = SportsClub.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return response.Response(serializer.data)  

class SlotAV(APIView):
    
    def get(self, request):
        booked_slot_list = []
        sport_name = request.query_params.get('sport')
        club_name = request.query_params.get('club')
        input_date = request.query_params.get('date')

        if not input_date:
            return response.Response(data=f"Invalid Date", status=400)     
        else:
            # Check if the date is in correct format
            try:
                formatted_date = datetime.datetime.strptime(input_date, "%Y-%m-%d").strftime("%Y-%m-%d")
            except:
                return response.Response(data=f"Invalid Date", status=400)   

            if sport_name and club_name:
            
                clubs = SportsClub.objects.filter(name=club_name, sports_offered__name=sport_name)  
                clubs_serializer = ClubSerializer(clubs, many=True) 

                if not clubs_serializer.data: # Check if the relevant sports club offered select sport
                    return response.Response(data=f"""Sport {sport_name} is not available at {club_name}. Either sport name is incorrect or club name""")
                else:
                    slots = Slot.objects.filter(sport__name=sport_name, club__name=club_name, slot_date=formatted_date)
                    slots_serializer = SlotSerializer(slots, many=True)

                    if not slots_serializer.data:               # If not slots booked for the sport in sports club
                        available_slots = AvailableSlots().get_available_slots()
                        return response.Response(data=available_slots)
                
                    else:   # If any booked slot is found 
                        for entry in slots_serializer.data:
                            booked_slot_list.append(entry.get('slot_time'))
                        available_slots = AvailableSlots(booked_slot_list).get_available_slots()
                        return response.Response(data=available_slots)
                    
            elif sport_name and not club_name:  # This is when club name is not selected
            
                available_slots_by_clubs = {}
                clubs = SportsClub.objects.filter(sports_offered__name=sport_name)
                clubs_serializer = ClubSerializer(clubs, many=True)
                for data in clubs_serializer.data:
                    club_name = data.get('name')
                    slots = Slot.objects.filter(sport__name=sport_name, club__name=club_name)
                    slot_serializer = SlotSerializer(slots, many=True)
                    if slot_serializer.data:
                        for entry in slot_serializer.data:
                            booked_slot_list.append(entry.get('slot_time'))
                        available_slots = AvailableSlots(booked_slot_list).get_available_slots()
                        available_slots_by_clubs[club_name] = available_slots
                    else:
                        available_slots = AvailableSlots().get_available_slots()
                        available_slots_by_clubs[club_name] = available_slots
                return response.Response(data=available_slots_by_clubs)
            
            else:
                return response.Response(status=400, data="Bad Request")