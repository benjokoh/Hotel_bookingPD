# Hotel_bookingPD
Core Entities:

# Room:
 Attributes:
        room_number (string): Unique identifier for each room.
        room_type (string): Type of the room (e.g., single, double, suite).
        capacity (integer): Maximum number of guests the room can accommodate.
        price_per_night (float): Cost of renting the room per night.
        is_available (boolean): Flag to indicate whether the room is available for booking or not.

# Guest:
 Attributes:
        guest_id (string): Unique identifier for each guest.
        name (string): Guest's full name.
        contact_number (string): Contact number of the guest.
        email (string): Email address of the guest.

# Reservation:
  Attributes:
        reservation_id (string): Unique identifier for each reservation.
        guest_id (string): Foreign key reference to the Guest who made the reservation.
        room_number (string): Foreign key reference to the Room that is being reserved.
        check_in_date (date): Date of check-in for the reservation.
        check_out_date (date): Date of check-out for the reservation.

# PickUpRequest:
  Attributes:
        request_id (string): Unique identifier for each pick-up request.
        guest_id (string): Foreign key reference to the Guest who made the request.
        pick_up_location (string): Location from where the guest needs to be picked up.
        pick_up_time (datetime): Date and time of the pick-up request.
        status (string): Status of the pick-up request (e.g., pending, completed).

# DropOffRequest:
  Attributes:
        request_id (string): Unique identifier for each drop-off request.
        guest_id (string): Foreign key reference to the Guest who made the request.
        drop_off_location (string): Location where the guest needs to be dropped off.
        drop_off_time (datetime): Date and time of the drop-off request.
        status (string): Status of the drop-off request (e.g., pending, completed).

# Relationships:
    A Room can have multiple Reservations (one-to-many relationship).
    A Guest can have multiple Reservations (one-to-many relationship).
    A Guest can make multiple PickUpRequests (one-to-many relationship).
    A Guest can make multiple DropOffRequests (one-to-many relationship).

# Database Schema:

If you choose to use a database for persistence, here's a simplified representation of the database schema:

# Rooms Table:
        room_number (Primary Key, String)
        room_type (String)
        capacity (Integer)
        price_per_night (Float)
        is_available (Boolean)

# Guests Table:
        guest_id (Primary Key, String)
        name (String)
        contact_number (String)
        email (String)

# Reservations Table:
        reservation_id (Primary Key, String)
        guest_id (Foreign Key, References Guests.guest_id)
        room_number (Foreign Key, References Rooms.room_number)
        check_in_date (Date)
        check_out_date (Date)

# PickUpRequests Table:
        request_id (Primary Key, String)
        guest_id (Foreign Key, References Guests.guest_id)
        pick_up_location (String)
        pick_up_time (DateTime)
        status (String)

# DropOffRequests Table:
        request_id (Primary Key, String)
        guest_id (Foreign Key, References Guests.guest_id)
        drop_off_location (String)
        drop_off_time (DateTime)
        status (String)

Keep in mind that this is a basic representation of the data model design. Depending on the specific requirements and features you want to implement, you may need to expand or modify the data model accordingly.
