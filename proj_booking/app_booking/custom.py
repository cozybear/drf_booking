class AvailableSlots():
    def __init__(self, booked_slot=None):
        self.booked_slot = booked_slot
        # available_slot_list = []
        slot_dict = { 
                        '1': '08:00 - 09:00',
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
                        '12': '19:00 - 20:00'
                    }     
        self.slot_dict = slot_dict
        # self.available_slot_list = available_slot_list
        

    def get_available_slots(self):
        if self.booked_slot:
            if isinstance(self.booked_slot, list):
                for entry in self.booked_slot:
                    del self.slot_dict[entry]    
            else:
                del self.slot_dict[self.booked_slot]    
        else:
            pass
        # available_slot_list = list(self.slot_dict.keys())
        available_slot_list = self.slot_dict
        return available_slot_list

if __name__ in "__main__":
    available_slots_object = AvailableSlots("5")
    print(available_slots_object.get_available_slots())

