# AI Agenti - HW 2

## Setup

Start *n8n*:

```bash
podman pull docker.n8n.io/n8nio/n8n
podman network create n8n
podman volume create n8n_data

podman run --rm \
 --name n8n \
 -p 5678:5678 \
 --network n8n \
 --rm \
 -d \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

Start database:

```bash
podman volume create parking_db_data

podman run --rm \
 --name parking-db \
 --network n8n \
 --rm \
 -d \
 -e POSTGRES_DB=parking \
 -e POSTGRES_USER=parking \
 -e POSTGRES_PASSWORD=parkingpwd \
 -v parking_db_data:/var/lib/postgresql/data:Z \
 -v ${PWD}/hw-02/sql_inicialization/:/docker-entrypoint-initdb.d:Z \
 docker.io/library/postgres:latest
```

### Database examples

Connect to DB:

```bash
podman run -it --rm --network n8n -e PGPASSWORD=parkingpwd  docker.io/library/postgres:latest psql -h parking-db -U parking
```

```sql
-- Note: This table needs to be pre-populated with all 30-minute time slots for the days
-- you want to make available for booking.
-- Example to populate a single day:
INSERT INTO time_slots (slot_time)
WITH RECURSIVE slots AS (
    SELECT CAST('2025-09-15 00:00:00' AS TIMESTAMP) AS slot_union
    UNION ALL
    SELECT slot_union + INTERVAL '30 minute' FROM slots WHERE slot_union < '2025-09-15 23:30:00'
)
SELECT slot_union FROM slots;


-- ===== How to Book a Time Range =====

-- To make a reservation, you would update the rows for the desired time range.
-- For example, to book from 2:00 PM to 3:30 PM for 'Peter Pan':
UPDATE time_slots
SET
    is_reserved = TRUE,
    booking_name = 'Peter Pan'
WHERE
    slot_time >= '2025-09-14 14:00:00' AND slot_time < '2025-09-14 15:30:00';

-- Your application would first need to check if any of these slots are already reserved
-- and ensure the booking is for at least one hour (i.e., spans at least two time slots).


-- ===== Simplified Query to Find Available Time Slots =====

-- This query is now much simpler. It just finds all the slots for a given
-- day that are not marked as reserved.
SELECT
    slot_time
FROM
    time_slots
WHERE
    is_reserved = FALSE
    AND DATE(slot_time) = '2025-09-14'
ORDER BY
    slot_time;
```
