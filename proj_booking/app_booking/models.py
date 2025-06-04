from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

SLOT_DICT = {"1":  '08:00 - 09:00', 
             '2': '09:00 - 10:00', 
             '3': '10:00 - 11:00', 
             '4': '11:00 - 12:00', 
             '5': '12:00 - 13:00', 
             '6': '13:00 - 14:00', 
             '7': '14:00 - 15:00', 
             '8': '15:00 - 16:00', 
             '9': '16:00 - 17:00', 
             '10': '17:00 - 18:00', 
             '11': '18:00 - 19:00', 
             '12': '19:00 - 20:00'}

class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return self.name

class SportsClub(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sports_offered = models.ManyToManyField(Sport, related_name="clubs")

    def __str__(self):
        return self.name
    
class Slot(models.Model):
    club = models.ForeignKey(SportsClub, on_delete=models.CASCADE, related_name='slots')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    slot_time = models.TextField(choices=SLOT_DICT)
    book_time = models.DateTimeField(auto_now_add=True)

    def clean(self):
    #     if (self.end_time - self.start_time).total_seconds() < 3600:
    #         raise ValidationError("Minimum booking hour should be one hour")
        
        if self.sport not in self.club.sports_offered.all():
            raise ValidationError(f"{self.club} doesn't offer {self.sport.name}")

    def __str__(self):
        return f" Slot booked {self.slot_time} {self.sport.name} at {self.club.name} "


# class Customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=50)
#     contact = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class SportsClub(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100,blank=True)
#     is_available = models.BooleanField()
   
#     def __str__(self):
#         return self.name
    


