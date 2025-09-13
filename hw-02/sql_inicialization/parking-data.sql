-- This table stores every possible 30-minute time slot for the parking spot.

CREATE TABLE time_slots (
    -- slot_id: A unique identifier for each 30-minute slot.
    -- In PostgreSQL, SERIAL is used for auto-incrementing integers.
    slot_id SERIAL PRIMARY KEY,

    -- slot_time: The start time of the 30-minute slot. This should be unique.
    -- In PostgreSQL, TIMESTAMP is the standard type for date and time.
    slot_time TIMESTAMP NOT NULL UNIQUE,

    -- is_reserved: A flag to indicate if the slot is booked.
    is_reserved BOOLEAN NOT NULL DEFAULT FALSE,

    -- booking_name: The name associated with the reservation, NULL if available.
    booking_name VARCHAR(100)
);
