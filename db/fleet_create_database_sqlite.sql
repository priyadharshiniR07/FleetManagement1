-- SQLite script to create the database schema for 'fleet'

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS customer (
    CusID INTEGER PRIMARY KEY,
    CusName TEXT,
    MobileNo INTEGER,
    Email TEXT,
    Address TEXT
);

CREATE TABLE IF NOT EXISTS Remainder (
    RemainderID INTEGER PRIMARY KEY,
    VehicleID INTEGER,
    RemDate TEXT,
    Message TEXT,
    FOREIGN KEY (VehicleID) REFERENCES vehicle(VehicleID)
);

CREATE TABLE IF NOT EXISTS vehicle (
    VehicleID INTEGER PRIMARY KEY,
    VehicleRegNo INTEGER UNIQUE,
    Name TEXT,
    Type TEXT,
    RegistrationExpDate TEXT,
    VehicleGroup TEXT,
    VehicleColour TEXT
);

CREATE TABLE IF NOT EXISTS driver (
    DriverID INTEGER PRIMARY KEY,
    Name TEXT,
    MobileNo INTEGER,
    LicenseNo TEXT,
    LicenseExpDate TEXT,
    DateOfJoining TEXT,
    TotalExperience INTEGER,
    Address TEXT,
    Status TEXT CHECK(Status IN ('Active', 'Inactive'))
);

CREATE TABLE IF NOT EXISTS bookings (
    BookId INTEGER PRIMARY KEY,
    CusID INTEGER,
    VehicleID INTEGER,
    DriverID INTEGER,
    TripType TEXT,
    StartLocation TEXT,
    EndLocation TEXT,
    ApproxKM INTEGER,
    StartDate TEXT,
    EndDate TEXT,
    TotalAmount INTEGER,
    Status TEXT CHECK(Status IN ('Active', 'Inactive')),
    FOREIGN KEY (CusID) REFERENCES customer(CusID),
    FOREIGN KEY (VehicleID) REFERENCES vehicle(VehicleID),
    FOREIGN KEY (DriverID) REFERENCES driver(DriverID)
);
