import mysql.connector

# Connect to the MySQL database
def connect_to_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="LittleLemon"
    )
    return conn

# Example connection
try:
    conn = connect_to_database()
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    conn.close()


def get_max_quantity(cursor):
    query = "SELECT MAX(QuantityAvailable) AS MaxQuantity FROM MenuItems;"
    cursor.execute(query)
    result = cursor.fetchone()
    print(f"Max Quantity Available: {result['MaxQuantity']}")


def manage_booking(cursor, booking_id, new_date):
    query = """
    UPDATE Bookings
    SET BookingDate = %s
    WHERE BookingID = %s;
    """
    cursor.execute(query, (new_date, booking_id))
    print(f"Booking {booking_id} updated to {new_date}")


def update_booking(cursor, booking_id, special_requests):
    query = """
    UPDATE Bookings
    SET SpecialRequests = %s
    WHERE BookingID = %s;
    """
    cursor.execute(query, (special_requests, booking_id))
    print(f"Booking {booking_id} updated with special requests: {special_requests}")


def add_booking(cursor, customer_id, booking_date, guests, requests):
    query = """
    INSERT INTO Bookings (CustomerID, BookingDate, NumberOfGuests, SpecialRequests)
    VALUES (%s, %s, %s, %s);
    """
    cursor.execute(query, (customer_id, booking_date, guests, requests))
    print("Booking added successfully!")


def cancel_booking(cursor, booking_id):
    query = "DELETE FROM Bookings WHERE BookingID = %s;"
    cursor.execute(query, (booking_id,))
    print(f"Booking {booking_id} canceled successfully!")


import pandas as pd

def export_to_csv(cursor, query, filename):
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

query = "SELECT * FROM Bookings;"
export_to_csv(cursor, query, "bookings.csv")
