"""Hotel room containing the room number,the type of room (single or double), 
its capacity, availability and a price per night."""
class Room:
    def __init__(self, room_number, room_type, capacity, price_per_night, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_available = is_available

class Guest:
    def __init__(self, guest_id, name, contact_number, email):
        self.guest_id = guest_id
        self.name = name
        self.contact_number = contact_number
        self.email = email

class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

class PickUpRequest:
    def __init__(self, request_id, guest, pick_up_location, pick_up_time, status='pending'):
        self.request_id = request_id
        self.guest = guest
        self.pick_up_location = pick_up_location
        self.pick_up_time = pick_up_time
        self.status = status

class DropOffRequest:
    def __init__(self, request_id, guest, drop_off_location, drop_off_time, status='pending'):
        self.request_id = request_id
        self.guest = guest
        self.drop_off_location = drop_off_location
        self.drop_off_time = drop_off_time
        self.status = status

# Example Usage
if __name__ == "__main__":
    room1 = Room("101", "single", 1, 100)
    guest1 = Guest("G001", "John Doe", "123-456-7890", "john@example.com")
    reservation1 = Reservation("R001", guest1, room1, "2023-08-01", "2023-08-05")
    pickup_request1 = PickUpRequest("P001", guest1, "Airport", "2023-08-01 10:00:00")
    dropoff_request1 = DropOffRequest("D001", guest1, "Hotel", "2023-08-05 14:00:00")

    room2  = Room("201", "Double", 2, 250)
    guest2 = Guest("A02762450","Benson Okoh","+86-186-240-77395","besomn@gmail.com")

    print(f"Room Number: {room1.room_number}")
    print(f"Guest Name: {guest1.name}")
    print(f"Reservation Check-In Date: {reservation1.check_in_date}")
    print(f"Pick-Up Location: {pickup_request1.pick_up_location}")
    print(f"Drop-Off Time: {dropoff_request1.drop_off_time}")

    