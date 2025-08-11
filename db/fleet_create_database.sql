-- SQL script to create the MySQL database named 'fleet'

CREATE DATABASE IF NOT EXISTS fleet;
USE fleet;

-- You can add table creation statements here once you provide the schema details.

CREATE TABLE IF NOT EXISTS customer (
    CusID INT PRIMARY KEY,
    CusName VARCHAR(50),
    MobileNo INT,
    Email VARCHAR(50),
    Address VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Remainder (
    RemainderID INT PRIMARY KEY,
    VehicleID INT,
    RemDate DATE,
    Message VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS vehicle (
    VehicleID INT PRIMARY KEY,
    VehicleRegNo INT UNIQUE,
    Name VARCHAR(100),
    Type VARCHAR(100),
    RegistrationExpDate DATE,
    VehicleGroup VARCHAR(255),
    VehicleColour VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS driver (
    DriverID INT PRIMARY KEY,
    Name VARCHAR(255),
    MobileNo INT,
    LicenseNo VARCHAR(255),
    LicenseExpDate DATE,
    DateOfJoining DATE,
    TotalExperience INT,
    Address VARCHAR(255),
    Status ENUM('Active', 'Inactive')
);

CREATE TABLE IF NOT EXISTS bookings (
    BookId INT PRIMARY KEY,
    CusID INT,
    VehicleID INT,
    DriverID INT,
    TripType VARCHAR(255),
    StartLocation VARCHAR(255),
    EndLocation VARCHAR(255),
    ApproxKM INT,
    StartDate DATE,
    EndDate DATE,
    TotalAmount INT,
    Status ENUM('Active', 'Inactive'),
    FOREIGN KEY (CusID) REFERENCES customer(CusID),
    FOREIGN KEY (VehicleID) REFERENCES vehicle(VehicleID),
    FOREIGN KEY (DriverID) REFERENCES driver(DriverID)
);
