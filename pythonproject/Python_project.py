#Car accident report database

import mysql.connector
import tkinter
import csv
import pickle
from tkinter import PhotoImage
sql=mysql.connector.connect(host='localhost',username='root',password='helloworld')
cur=sql.cursor()
try:
    cur.execute('create database car_inventory')
except:
     pass
try:
    cur.execute('create database customer_data')
except:
     pass
sql1=mysql.connector.connect(host='localhost',username='root',password='helloworld',database='car_inventory')
sql2=mysql.connector.connect(host='localhost',username='root',password='helloworld',database='customer_data')
cur1=sql1.cursor()
cur2=sql2.cursor()
try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_details (
        car_id INT AUTO_INCREMENT PRIMARY KEY,
        car_name VARCHAR(50),
        brand VARCHAR(50),
        model_year INT,
        fuel_type VARCHAR(20),
        transmission VARCHAR(20),
        color VARCHAR(20)
    );
    """)
except Exception as e:
    print("Error creating Car_details table:", e)

try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_status (
        status_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        availability VARCHAR(20),
        mileage INT,
        condition_status VARCHAR(20),
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_status table:", e)


try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_specification (
        spec_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        engine_cc INT,
        horsepower INT,
        torque INT,
        seating_capacity INT,
        color VARCHAR(20),
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_specification table:", e)

try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_price (
        price_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        onroad_price INT,
        currency VARCHAR(10),
        listing_price INT,
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_price table:", e)

try:
    cur1.execute("""
    CREATE TABLE IF NOT EXISTS Car_owner_history (
        owner_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        previous_owners INT,
        last_owner_name VARCHAR(100),
        ownership_type VARCHAR(20),
        ownership_hand VARCHAR(30),
        FOREIGN KEY (car_id) REFERENCES Car_details(car_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """)
except Exception as e:
    print("Error creating Car_owner_history table:", e)

try:
    cur2.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        phone VARCHAR(15),
        city VARCHAR(50),
        country VARCHAR(50)
    );
    """)
except Exception as e:
    print("Error creating Customers table:", e)

try:
    cur2.execute("""
    CREATE TABLE IF NOT EXISTS Customer_login (
        login_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_id INT,
        username VARCHAR(50),
        password_hash VARCHAR(255),
        last_login DATETIME,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );
    """)
except Exception as e:
    print("Error creating Customer_login table:", e)

try:
    cur2.execute("""
    CREATE TABLE IF NOT EXISTS Customer_purchase_history (
        purchase_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_id INT,
        car_id INT,
        purchase_date DATE,
        purchase_type VARCHAR(20),
        price_paid DECIMAL(10,2),
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );
    """)
except Exception as e:
    print("Error creating Customer_purchase_history table:", e)