CREATE DATABASE IF NOT EXISTS GymPal;
SHOW DATABASES;
USE GymPal;

CREATE TABLE IF NOT EXISTS GymPal . GymManager (
    ManagerID int NOT NULL AUTO_INCREMENT,
    FirstName varchar(30) NOT NULL,
    LastName varchar(30) NOT NULL,
    PhoneNumber varchar(15) UNIQUE NOT NULL,
    Email varchar(30) UNIQUE NOT NULL,
    PRIMARY KEY (ManagerID)
);

CREATE TABLE IF NOT EXISTS Facilities (
    EquipmentID int NOT NULL AUTO_INCREMENT,
    PurchaseDate DATE NOT NULL,
    LastMaintenanceDate DATE NOT NULL,
    Name varchar(30) NOT NULL,
    Manufacturer varchar(30) NOT NULL,
    Condition varchar(30) NOT NULL,
    ManagerID int NOT NULL,
    PRIMARY KEY (EquipmentID),
    CONSTRAINT fk_01 FOREIGN KEY (ManagerID) REFERENCES GymManager(ManagerID)
        ON UPDATE CASCADE ON DELETE RESTRICT

);

CREATE TABLE IF NOT EXISTS Trainers (
    TrainerID int NOT NULL AUTO_INCREMENT,
    PhoneNumber varchar(30) UNIQUE NOT NULL,
    LastName varchar(30) NOT NULL,
    FirstName varchar(30) NOT NULL,
    Email varchar(30) UNIQUE NOT NULL,
    ManagerID int NOT NULL,
    PRIMARY KEY (TrainerID),
    CONSTRAINT fk_02 FOREIGN KEY (ManagerID) REFERENCES GymManager(ManagerID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS TrainerSchedule (
    Availability DATETIME NOT NULL,
    TrainerID int NOT NULL,
    CONSTRAINT fk_03 FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID)
    ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS TrainerResources (
    Workout varchar(30) NOT NULL,
    Duration varchar(30) NOT NULL,
    Intensity varchar(30) NOT NULL,
    TrainerID int NOT NULL,
    PRIMARY KEY (Workout),
    CONSTRAINT fk_04 FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Nutritionists (
    NutritionistID int NOT NULL,
    FirstName varchar(30) NOT NULL,
    LastName varchar(30) NOT NULL,
    PhoneNumber varchar(30) UNIQUE NOT NULL,
    Email varchar(30) UNIQUE NOT NULL,
    ManagerID int NOT NULL,
    PRIMARY KEY (NutritionistID),
    CONSTRAINT fk_05 FOREIGN KEY (ManagerID) REFERENCES GymManager(ManagerID)
        ON UPDATE CASCADE ON DELETE RESTRICT

);

CREATE TABLE IF NOT EXISTS NutritionistSchedule (
    Availability DATETIME NOT NULL,
    NutritionistID int NOT NULL,
    CONSTRAINT fk_06 FOREIGN KEY (NutritionistID) REFERENCES Nutritionists(NutritionistID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS NutritionistResources (
    Food varchar(30) NOT NULL,
    Calories int NOT NULL,
    Nutrients varchar(30) NOT NULL,
    Protein varchar(30) NOT NULL,
    Carbs varchar(30) NOT NULL,
    NutritionistID int,
    PRIMARY KEY (Food),
    CONSTRAINT fk_07 FOREIGN KEY (NutritionistID) REFERENCES Nutritionists(NutritionistID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Members (
    MemberID int NOT NULL AUTO_INCREMENT,
    FirstName varchar(30) NOT NULL,
    LastName varchar(30) NOT NULL,
    PhoneNumber varchar(30) UNIQUE NOT NULL,
    Email varchar(30) UNIQUE NOT NULL,
    Height float NOT NULL,
    Weight float NOT NULL,
    ManagerID int NOT NULL,
    PRIMARY KEY (MemberID),
    CONSTRAINT fk_08 FOREIGN KEY (ManagerID) REFERENCES GymManager(ManagerID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS NutritionPlan (
    Goals varchar(30) NOT NULL,
    DietRestrictions varchar(30) NOT NULL,
    MealPlan varchar(30) NOT NULL,
    DietType varchar(30) NOT NULL,
    MemberID int NOT NULL,
    CONSTRAINT fk_09 FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS WorkoutPlan (
    Goals varchar(30) NOT NULL,
    WorkoutType varchar(30) NOT NULL,
    MemberID int NOT NULL,
    CONSTRAINT fk_10 FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Progress (
    WorkoutName varchar(30) NOT NULL,
    Sets int NOT NULL,
    Reps int NOT NULL,
    Weight float NOT NULL,
    Time float NOT NULL,
    MemberID int NOT NULL,
    CONSTRAINT fk_11 FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Membership (
    MembershipID int AUTO_INCREMENT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    CreditCard varchar(30) NOT NULL,
    MemberID int NOT NULL,
    PRIMARY KEY (MembershipID),
    CONSTRAINT fk_12 FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS Classes (
    ClassID int NOT NULL,
    ClassName varchar(30) NOT NULL,
    SpotsAvailable int NOT NULL,
    StartTime DATETIME NOT NULL,
    MembershipID int NOT NULL,
    PRIMARY KEY (ClassID),
    CONSTRAINT fk_13 FOREIGN KEY (MembershipID) REFERENCES Membership(MembershipID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);
