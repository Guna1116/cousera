-- little_lemon_schema.sql
CREATE DATABASE LittleLemon;

USE LittleLemon;

CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    BookingDate DATE,
    NumberOfGuests INT,
    SpecialRequests TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT PRIMARY KEY,
    ItemName VARCHAR(100),
    Price DECIMAL(10, 2),
    QuantityAvailable INT
);




