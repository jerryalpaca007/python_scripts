import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os


THEME = {
    "bg_main": "#8D99AE",
    "bg_default": "#F6F6F6",
    "bg_banner": "#2A6DCB",
    "fg_banner": "white",
    "banner_font": ("Arial", 18, "bold"),
    "normal_font": ("Arial", 16, "normal"),
    "normal_font_bold": ("Arial", 18, "bold"),

    "btn_primary_bg": "#2B2D42",
    "btn_primary_fg": "white",
    "btn_success_bg": "#2A6DCB",
    "btn_success_fg": "#FFFFFF",
    "btn_danger_bg": "#EF233C",
    "btn_danger_fg": "white",
    "btn_secondary_bg": "#2B2D42",
    "btn_secondary_fg": "white",
    "btn_neutral_bg": "#34353F",
    "btn_neutral_fg": "white",

    "field_bg": "#f6f6f6",
    "field_fg": "black",
    "label_fg": "black",
}
APP_TITLE="Car Crash Report"
CAR_DETAILS_FILE = "car_details.csv"
CAR_STATUS_FILE = "car_status.csv"
CAR_SPEC_FILE = "car_specifications.csv"
CAR_OWNERS_FILE = "car_owners.csv"
CAR_LOCATION_FILE = "car_location.csv"
CAR_DAMAGE_DATA = "car_damage.csv"
LOGIN_FILE = "login.csv"
CAR_CRASH_FILE = "car_crash_info.csv"

car_data = [
    [1, 'Mustang', 'Ford', 2023, 'Petrol', 'Manual', 'Red'],
    [2, 'Camaro', 'Chevrolet', 2022, 'Petrol', 'Automatic', 'Yellow'],
    [3, 'Challenger', 'Dodge', 2023, 'Petrol', 'Automatic', 'Black'],
    [4, 'F-150', 'Ford', 2021, 'Diesel', 'Automatic', 'Blue'],
    [5, 'Corvette', 'Chevrolet', 2023, 'Petrol', 'Automatic', 'Silver'],
    [6, 'Bronco', 'Ford', 2022, 'Petrol', 'Manual', 'Green'],
    [7, 'Tahoe', 'Chevrolet', 2021, 'Diesel', 'Automatic', 'White'],
    [8, 'Durango', 'Dodge', 2022, 'Petrol', 'Automatic', 'Gray'],
    [9, 'Explorer', 'Ford', 2023, 'Petrol', 'Automatic', 'Black'],
    [10, 'Blazer', 'Chevrolet', 2022, 'Petrol', 'Manual', 'Orange'],
    [11, 'Ram 1500', 'RAM', 2023, 'Diesel', 'Automatic', 'White'],
    [12, 'Suburban', 'Chevrolet', 2021, 'Diesel', 'Automatic', 'Silver'],
    [13, 'Expedition', 'Ford', 2023, 'Petrol', 'Automatic', 'Blue'],
    [14, 'Equinox', 'Chevrolet', 2020, 'Petrol', 'Automatic', 'Red'],
    [15, 'Journey', 'Dodge', 2021, 'Petrol', 'Manual', 'Gray'],
    [16, 'Wrangler', 'Jeep', 2023, 'Petrol', 'Manual', 'Green'],
    [17, 'Cherokee', 'Jeep', 2022, 'Diesel', 'Automatic', 'White'],
    [18, 'Compass', 'Jeep', 2023, 'Petrol', 'Automatic', 'Black'],
    [19, 'Renegade', 'Jeep', 2021, 'Petrol', 'Manual', 'Yellow'],
    [20, 'Gladiator', 'Jeep', 2023, 'Diesel', 'Manual', 'Gray'],
    [21, 'Charger', 'Dodge', 2022, 'Petrol', 'Automatic', 'Silver'],
    [22, 'Maverick', 'Ford', 2023, 'Petrol', 'Automatic', 'Orange'],
    [23, 'Colorado', 'Chevrolet', 2022, 'Diesel', 'Manual', 'Blue'],
    [24, 'Silverado', 'Chevrolet', 2023, 'Diesel', 'Automatic', 'Black'],
    [25, 'Ranger', 'Ford', 2022, 'Diesel', 'Manual', 'White'],
    [26, 'Sierra', 'GMC', 2023, 'Diesel', 'Automatic', 'Red'],
    [27, 'Yukon', 'GMC', 2022, 'Diesel', 'Automatic', 'Gray'],
    [28, 'Envoy', 'GMC', 2020, 'Petrol', 'Automatic', 'Silver'],
    [29, 'Encore', 'Buick', 2021, 'Petrol', 'Manual', 'Blue'],
    [30, 'Enclave', 'Buick', 2022, 'Petrol', 'Automatic', 'Black'],
    [31, 'Regal', 'Buick', 2020, 'Petrol', 'Manual', 'White'],
    [32, 'LaCrosse', 'Buick', 2021, 'Petrol', 'Automatic', 'Gray'],
    [33, 'Lucerne', 'Buick', 2019, 'Petrol', 'Manual', 'Silver'],
    [34, 'Model S', 'Tesla', 2023, 'Electric', 'Automatic', 'Red'],
    [35, 'Model 3', 'Tesla', 2022, 'Electric', 'Automatic', 'White'],
    [36, 'Model X', 'Tesla', 2023, 'Electric', 'Automatic', 'Blue'],
    [37, 'Model Y', 'Tesla', 2023, 'Electric', 'Automatic', 'Black'],
    [38, 'Cybertruck', 'Tesla', 2024, 'Electric', 'Automatic', 'Silver'],
    [39, 'Bolt', 'Chevrolet', 2022, 'Electric', 'Automatic', 'Gray'],
    [40, 'Hummer EV', 'GMC', 2023, 'Electric', 'Automatic', 'White'],
    [41, 'Escalade', 'Cadillac', 2023, 'Diesel', 'Automatic', 'Black'],
    [42, 'XT5', 'Cadillac', 2022, 'Petrol', 'Automatic', 'Silver'],
    [43, 'CT5', 'Cadillac', 2023, 'Petrol', 'Automatic', 'Gray'],
    [44, 'CT4', 'Cadillac', 2022, 'Petrol', 'Manual', 'White'],
    [45, 'XT6', 'Cadillac', 2023, 'Diesel', 'Automatic', 'Blue'],
    [46, 'Navigator', 'Lincoln', 2023, 'Diesel', 'Automatic', 'Black'],
    [47, 'Aviator', 'Lincoln', 2022, 'Petrol', 'Automatic', 'Silver'],
    [48, 'Corsair', 'Lincoln', 2022, 'Petrol', 'Manual', 'White'],
    [49, 'Continental', 'Lincoln', 2020, 'Petrol', 'Automatic', 'Gray'],
    [50, 'MKZ', 'Lincoln', 2021, 'Petrol', 'Automatic', 'Red'],
    [51, 'Pacifica', 'Chrysler', 2023, 'Hybrid', 'Automatic', 'Blue'],
    [52, '300', 'Chrysler', 2022, 'Petrol', 'Automatic', 'White'],
    [53, 'Voyager', 'Chrysler', 2021, 'Petrol', 'Automatic', 'Gray'],
    [54, 'Grand Caravan', 'Dodge', 2020, 'Petrol', 'Automatic', 'Silver'],
    [55, 'Nitro', 'Dodge', 2019, 'Petrol', 'Manual', 'Black'],
    [56, 'Avenger', 'Dodge', 2018, 'Petrol', 'Manual', 'Red'],
    [57, 'Trailblazer', 'Chevrolet', 2023, 'Petrol', 'Automatic', 'Blue'],
    [58, 'Trax', 'Chevrolet', 2022, 'Petrol', 'Manual', 'Gray'],
    [59, 'Malibu', 'Chevrolet', 2023, 'Petrol', 'Automatic', 'White'],
    [60, 'Impala', 'Chevrolet', 2020, 'Petrol', 'Automatic', 'Silver'],
    [61, 'Fusion', 'Ford', 2020, 'Petrol', 'Automatic', 'Black'],
    [62, 'Edge', 'Ford', 2021, 'Petrol', 'Automatic', 'Blue'],
    [63, 'Escape', 'Ford', 2023, 'Petrol', 'Automatic', 'White'],
    [64, 'Taurus', 'Ford', 2019, 'Petrol', 'Manual', 'Gray'],
    [65, 'Focus', 'Ford', 2021, 'Petrol', 'Automatic', 'Red'],
    [66, 'Fiesta', 'Ford', 2018, 'Petrol', 'Manual', 'Yellow'],
    [67, 'Cruze', 'Chevrolet', 2019, 'Petrol', 'Manual', 'Blue'],
    [68, 'Volt', 'Chevrolet', 2020, 'Hybrid', 'Automatic', 'Silver'],
    [69, 'Bolt EUV', 'Chevrolet', 2023, 'Electric', 'Automatic', 'Gray'],
    [70, 'Durango SRT', 'Dodge', 2023, 'Petrol', 'Automatic', 'Red'],
    [71, 'RAM 2500', 'RAM', 2022, 'Diesel', 'Automatic', 'White'],
    [72, 'RAM 3500', 'RAM', 2023, 'Diesel', 'Automatic', 'Black'],
    [73, 'Journey GT', 'Dodge', 2020, 'Petrol', 'Manual', 'Blue'],
    [74, 'Charger SRT', 'Dodge', 2023, 'Petrol', 'Automatic', 'Gray'],
    [75, 'Grand Cherokee', 'Jeep', 2023, 'Diesel', 'Automatic', 'White'],
    [76, 'Patriot', 'Jeep', 2019, 'Petrol', 'Manual', 'Silver'],
    [77, 'Commander', 'Jeep', 2020, 'Diesel', 'Automatic', 'Black'],
    [78, 'Liberty', 'Jeep', 2018, 'Petrol', 'Manual', 'Blue'],
    [79, 'Renegade Sport', 'Jeep', 2023, 'Petrol', 'Automatic', 'Yellow'],
    [80, 'Model Z', 'Tesla', 2025, 'Electric', 'Automatic', 'White'],
    [81, 'Cyber SUV', 'Tesla', 2025, 'Electric', 'Automatic', 'Silver'],
    [82, 'Lightning', 'Ford', 2024, 'Electric', 'Automatic', 'Gray'],
    [83, 'Trailhawk', 'Jeep', 2023, 'Diesel', 'Automatic', 'Red'],
    [84, 'Durango GT', 'Dodge', 2023, 'Petrol', 'Automatic', 'Black'],
    [85, 'Silverado EV', 'Chevrolet', 2024, 'Electric', 'Automatic', 'Blue'],
    [86, 'Tahoe Premier', 'Chevrolet', 2023, 'Diesel', 'Automatic', 'White'],
    [87, 'Sierra Denali', 'GMC', 2023, 'Diesel', 'Automatic', 'Gray'],
    [88, 'Escalade V', 'Cadillac', 2024, 'Petrol', 'Automatic', 'Black'],
    [89, 'Aviator Grand Touring', 'Lincoln', 2023, 'Hybrid', 'Automatic', 'Silver'],
    [90, 'Navigator L', 'Lincoln', 2023, 'Diesel', 'Automatic', 'White'],
    [91, 'Blazer EV', 'Chevrolet', 2024, 'Electric', 'Automatic', 'Blue'],
    [92, 'Edge ST', 'Ford', 2022, 'Petrol', 'Automatic', 'Red'],
    [93, 'Expedition MAX', 'Ford', 2023, 'Petrol', 'Automatic', 'Black'],
    [94, 'Envision', 'Buick', 2023, 'Petrol', 'Automatic', 'Gray'],
    [95, 'Encore GX', 'Buick', 2023, 'Petrol', 'Automatic', 'White'],
    [96, 'CT6', 'Cadillac', 2021, 'Petrol', 'Automatic', 'Silver'],
    [97, 'Hummer EV SUV', 'GMC', 2024, 'Electric', 'Automatic', 'Gray'],
    [98, 'RAM TRX', 'RAM', 2023, 'Petrol', 'Automatic', 'Orange'],
    [99, 'Hornet', 'Dodge', 2023, 'Hybrid', 'Automatic', 'Blue'],
    [100, 'Corvette Z06', 'Chevrolet', 2024, 'Petrol', 'Automatic', 'Red']
]


car_status_data =[
    [1, 'Available', 32000, 'Excellent'],
    [2, 'Sold', 42000, 'Good'],
    [3, 'Available', 18000, 'Excellent'],
    [4, 'Sold', 56000, 'Fair'],
    [5, 'Available', 15000, 'Excellent'],
    [6, 'Available', 49000, 'Crashed'],
    [7, 'Sold', 36000, 'Excellent'],
    [8, 'Available', 22000, 'Good'],
    [9, 'Available', 28000, 'Excellent'],
    [10, 'Available', 41000, 'Crashed'],
    [11, 'Sold', 62000, 'Excellent'],
    [12, 'Available', 27000, 'Crashed'],
    [13, 'Available', 58000, 'Excellent'],
    [14, 'Sold', 19000, 'Excellent'],
    [15, 'Available', 33000, 'Good'],
    [16, 'Available', 47000, 'Excellent'],
    [17, 'Sold', 38000, 'Crashed'],
    [18, 'Available', 25000, 'Excellent'],
    [19, 'Available', 21000, 'Excellent'],
    [20, 'Sold', 34000, 'Good'],
    [21, 'Available', 29000, 'Excellent'],
    [22, 'Available', 54000, 'Excellent'],
    [23, 'Sold', 43000, 'Excellent'],
    [24, 'Available', 12000, 'Excellent'],
    [25, 'Available', 47000, 'Excellent'],
    [26, 'Available', 35000, 'Good'],
    [27, 'Sold', 41000, 'Excellent'],
    [28, 'Available', 60000, 'Excellent'],
    [29, 'Available', 31000, 'Excellent'],
    [30, 'Sold', 29000, 'Excellent'],
    [31, 'Available', 46000, 'Excellent'],
    [32, 'Available', 51000, 'Fair'],
    [33, 'Available', 25000, 'Crashed'],
    [34, 'Sold', 43000, 'Excellent'],
    [35, 'Available', 17000, 'Excellent'],
    [36, 'Sold', 26000, 'Excellent'],
    [37, 'Available', 48000, 'Crashed'],
    [38, 'Available', 38000, 'Good'],
    [39, 'Sold', 33000, 'Excellent'],
    [40, 'Available', 52000, 'Excellent'],
    [41, 'Available', 61000, 'Crashed'],
    [42, 'Sold', 35000, 'Excellent'],
    [43, 'Available', 43000, 'Excellent'],
    [44, 'Sold', 24000, 'Excellent'],
    [45, 'Available', 50000, 'Excellent'],
    [46, 'Available', 27000, 'Good'],
    [47, 'Sold', 19000, 'Excellent'],
    [48, 'Available', 52000, 'Excellent'],
    [49, 'Available', 39000, 'Excellent'],
    [50, 'Sold', 47000, 'Excellent'],
    [51, 'Available', 28000, 'Excellent'],
    [52, 'Available', 15000, 'Excellent'],
    [53, 'Available', 38000, 'Excellent'],
    [54, 'Sold', 26000, 'Excellent'],
    [55, 'Available', 34000, 'Excellent'],
    [56, 'Available', 47000, 'Excellent'],
    [57, 'Available', 22000, 'Crashed'],
    [58, 'Available', 54000, 'Excellent'],
    [59, 'Sold', 37000, 'Excellent'],
    [60, 'Available', 19000, 'Crashed'],
    [61, 'Available', 28000, 'Excellent'],
    [62, 'Available', 32000, 'Excellent'],
    [63, 'Sold', 33000, 'Excellent'],
    [64, 'Available', 21000, 'Excellent'],
    [65, 'Available', 56000, 'Excellent'],
    [66, 'Available', 41000, 'Excellent'],
    [67, 'Available', 36000, 'Excellent'],
    [68, 'Sold', 15000, 'Excellent'],
    [69, 'Available', 38000, 'Excellent'],
    [70, 'Sold', 43000, 'Excellent'],
    [71, 'Available', 52000, 'Excellent'],
    [72, 'Available', 27000, 'Crashed'],
    [73, 'Available', 45000, 'Excellent'],
    [74, 'Sold', 31000, 'Excellent'],
    [75, 'Available', 22000, 'Excellent'],
    [76, 'Available', 35000, 'Excellent'],
    [77, 'Available', 29000, 'Excellent'],
    [78, 'Available', 25000, 'Crashed'],
    [79, 'Sold', 48000, 'Excellent'],
    [80, 'Available', 39000, 'Excellent'],
    [81, 'Available', 41000, 'Excellent'],
    [82, 'Sold', 34000, 'Excellent'],
    [83, 'Available', 29000, 'Excellent'],
    [84, 'Available', 18000, 'Crashed'],
    [85, 'Available', 31000, 'Good'],
    [86, 'Available', 47000, 'Crashed'],
    [87, 'Sold', 26000, 'Excellent'],
    [88, 'Available', 55000, 'Excellent'],
    [89, 'Available', 32000, 'Excellent'],
    [90, 'Available', 46000, 'Excellent'],
    [91, 'Available', 23000, 'Crashed'],
    [92, 'Sold', 17000, 'Excellent'],
    [93, 'Available', 48000, 'Excellent'],
    [94, 'Available', 34000, 'Excellent'],
    [95, 'Available', 27000, 'Excellent'],
    [96, 'Sold', 31000, 'Excellent'],
    [97, 'Available', 19000, 'Excellent'],
    [98, 'Available', 21000, 'Excellent'],
    [99, 'Available', 26000, 'Crashed'],
    [100, 'Available', 29000, 'Excellent']
]




car_specification_data = [
    [1, 5000, 450, 530, 4],
    [2, 6200, 455, 610, 4],
    [3, 6000, 485, 644, 4],
    [4, 3500, 400, 650, 5],
    [5, 6200, 495, 640, 2],
    [6, 2900, 270, 400, 4],
    [7, 5300, 355, 530, 7],
    [8, 3600, 295, 353, 5],
    [9, 4000, 360, 460, 5],
    [10, 3600, 308, 380, 5],
    [11, 6000, 395, 610, 5],
    [12, 5300, 355, 530, 7],
    [13, 3600, 400, 500, 7],
    [14, 6500, 500, 800, 7],
    [15, 3600, 290, 353, 5],
    [16, 2900, 270, 400, 5],
    [17, 4000, 360, 460, 5],
    [18, 3500, 308, 380, 5],
    [19, 3600, 295, 353, 5],
    [20, 5000, 450, 530, 4],
    [21, 3600, 308, 380, 5],
    [22, 2500, 310, 380, 5],
    [23, 6000, 395, 610, 5],
    [24, 6400, 475, 650, 5],
    [25, 6200, 495, 640, 5],
    [26, 5000, 450, 530, 4],
    [27, 6200, 455, 610, 4],
    [28, 6000, 485, 644, 4],
    [29, 3500, 400, 500, 5],
    [30, 2900, 270, 400, 4],
    [31, 2500, 240, 310, 5],
    [32, 2500, 240, 310, 5],
    [33, 4000, 360, 460, 5],
    [34, 6200, 495, 640, 2],
    [35, 8000, 720, 970, 2],
    [36, 2900, 270, 400, 4],
    [37, 6300, 710, 880, 7],
    [38, 2900, 330, 450, 5],
    [39, 6200, 495, 640, 5],
    [40, 3600, 295, 353, 5],
    [41, 6500, 450, 610, 7],
    [42, 3500, 308, 380, 5],
    [43, 5000, 450, 530, 5],
    [44, 3600, 295, 353, 5],
    [45, 3600, 308, 380, 5],
    [46, 6200, 455, 610, 4],
    [47, 3600, 308, 380, 5],
    [48, 3500, 308, 380, 5],
    [49, 2900, 270, 400, 4],
    [50, 6200, 495, 640, 5],
    [51, 6200, 495, 640, 5],
    [52, 3500, 308, 380, 5],
    [53, 6000, 395, 610, 5],
    [54, 6400, 475, 650, 5],
    [55, 6200, 495, 640, 5],
    [56, 6200, 455, 610, 4],
    [57, 8000, 720, 970, 2],
    [58, 6300, 710, 880, 7],
    [59, 2900, 330, 450, 5],
    [60, 3600, 295, 353, 5],
    [61, 3600, 308, 380, 5],
    [62, 3600, 308, 380, 5],
    [63, 3500, 308, 380, 5],
    [64, 6200, 475, 610, 4],
    [65, 3500, 308, 380, 5],
    [66, 2900, 270, 400, 4],
    [67, 6200, 495, 640, 5],
    [68, 3600, 308, 380, 5],
    [69, 3500, 308, 380, 5],
    [70, 3500, 308, 380, 5],
    [71, 6200, 495, 640, 5],
    [72, 4000, 360, 460, 5],
    [73, 6200, 495, 640, 5],
    [74, 6000, 395, 610, 5],
    [75, 6400, 475, 650, 5],
    [76, 5000, 450, 530, 4],
    [77, 2900, 330, 450, 5],
    [78, 8000, 720, 970, 2],
    [79, 6200, 455, 610, 4],
    [80, 3500, 308, 380, 5],
    [81, 3600, 308, 380, 5],
    [82, 2900, 270, 400, 4],
    [83, 6200, 495, 640, 5],
    [84, 6200, 495, 640, 5],
    [85, 6200, 495, 640, 5],
    [86, 6300, 710, 880, 7],
    [87, 6000, 395, 610, 5],
    [88, 6400, 475, 650, 5],
    [89, 2900, 330, 450, 5],
    [90, 3600, 295, 353, 5],
    [91, 8000, 720, 970, 2],
    [92, 6200, 455, 610, 4],
    [93, 3500, 308, 380, 5],
    [94, 3600, 308, 380, 5],
    [95, 2900, 270, 400, 4],
    [96, 6200, 495, 640, 5],
    [97, 6200, 495, 640, 5],
    [98, 6200, 495, 640, 5],
    [99, 6300, 710, 880, 7],
    [100, 6400, 475, 650, 5]
]

car_owners_data = [
    [1, "John Doe", "9876543210", "New York", "2 years"],
    [2, "Jane Smith", "9123456789", "California", "1 year"],
    [3, "Michael Lee", "9998887777", "Texas", "3 years"],
    [4, "Emily Davis", "9812345678", "Florida", "1 year"],
    [5, "Robert Brown", "9823456789", "Nevada", "4 years"],
    [6, "Sophia Wilson", "9834567890", "Washington", "2 years"],
    [7, "Liam Taylor", "9845678901", "Illinois", "1 year"],
    [8, "Olivia Martin", "9856789012", "Georgia", "2 years"],
    [9, "Noah Anderson", "9867890123", "Virginia", "3 years"],
    [10, "Ava Thomas", "9878901234", "Oregon", "1 year"],
    [11, "William Jackson", "9889012345", "New York", "5 years"],
    [12, "Isabella White", "9890123456", "California", "3 years"],
    [13, "James Harris", "9901234567", "Texas", "2 years"],
    [14, "Mia Clark", "9912345678", "Florida", "1 year"],
    [15, "Benjamin Lewis", "9923456789", "Nevada", "2 years"],
    [16, "Charlotte Young", "9934567890", "Washington", "4 years"],
    [17, "Lucas Hall", "9945678901", "Illinois", "3 years"],
    [18, "Amelia Allen", "9956789012", "Georgia", "1 year"],
    [19, "Ethan Scott", "9967890123", "Virginia", "2 years"],
    [20, "Harper King", "9978901234", "Oregon", "3 years"],
    [21, "Alexander Wright", "9989012345", "New York", "4 years"],
    [22, "Ella Lopez", "9990123456", "California", "2 years"],
    [23, "Mason Hill", "9811234567", "Texas", "1 year"],
    [24, "Grace Green", "9822345678", "Florida", "5 years"],
    [25, "Logan Adams", "9833456789", "Nevada", "2 years"],
    [26, "Abigail Baker", "9844567890", "Washington", "3 years"],
    [27, "Jacob Nelson", "9855678901", "Illinois", "1 year"],
    [28, "Sofia Carter", "9866789012", "Georgia", "4 years"],
    [29, "Elijah Mitchell", "9877890123", "Virginia", "2 years"],
    [30, "Avery Perez", "9888901234", "Oregon", "1 year"],
    [31, "Daniel Roberts", "9899012345", "New York", "3 years"],
    [32, "Evelyn Turner", "9900123456", "California", "2 years"],
    [33, "Matthew Phillips", "9911234567", "Texas", "1 year"],
    [34, "Scarlett Campbell", "9922345678", "Florida", "3 years"],
    [35, "Henry Parker", "9933456789", "Nevada", "2 years"],
    [36, "Victoria Evans", "9944567890", "Washington", "4 years"],
    [37, "Jack Edwards", "9955678901", "Illinois", "5 years"],
    [38, "Ella Collins", "9966789012", "Georgia", "2 years"],
    [39, "Sebastian Stewart", "9977890123", "Virginia", "3 years"],
    [40, "Aria Sanchez", "9988901234", "Oregon", "1 year"],
    [41, "David Morris", "9999012345", "New York", "3 years"],
    [42, "Luna Rogers", "9810123456", "California", "1 year"],
    [43, "Joseph Reed", "9821234567", "Texas", "2 years"],
    [44, "Chloe Cook", "9832345678", "Florida", "1 year"],
    [45, "Samuel Morgan", "9843456789", "Nevada", "4 years"],
    [46, "Zoe Bell", "9854567890", "Washington", "2 years"],
    [47, "David Bailey", "9865678901", "Illinois", "1 year"],
    [48, "Layla Rivera", "9876789012", "Georgia", "3 years"],
    [49, "Carter Cooper", "9887890123", "Virginia", "2 years"],
    [50, "Ella Richardson", "9898901234", "Oregon", "3 years"],
    [51, "Wyatt Cox", "9909012345", "New York", "4 years"],
    [52, "Nora Howard", "9910123456", "California", "1 year"],
    [53, "Owen Ward", "9921234567", "Texas", "2 years"],
    [54, "Lily Torres", "9932345678", "Florida", "3 years"],
    [55, "Gabriel Peterson", "9943456789", "Nevada", "2 years"],
    [56, "Hannah Gray", "9954567890", "Washington", "4 years"],
    [57, "Isaac Ramirez", "9965678901", "Illinois", "1 year"],
    [58, "Aubrey James", "9976789012", "Georgia", "3 years"],
    [59, "Nathan Watson", "9987890123", "Virginia", "5 years"],
    [60, "Ellie Brooks", "9998901234", "Oregon", "2 years"],
    [61, "Levi Kelly", "9819012345", "New York", "3 years"],
    [62, "Hazel Sanders", "9820123456", "California", "4 years"],
    [63, "Julian Price", "9831234567", "Texas", "2 years"],
    [64, "Violet Bennett", "9842345678", "Florida", "1 year"],
    [65, "Caleb Wood", "9853456789", "Nevada", "2 years"],
    [66, "Aurora Barnes", "9864567890", "Washington", "3 years"],
    [67, "Ryan Ross", "9875678901", "Illinois", "1 year"],
    [68, "Penelope Henderson", "9886789012", "Georgia", "2 years"],
    [69, "Anthony Coleman", "9897890123", "Virginia", "4 years"],
    [70, "Lucy Jenkins", "9908901234", "Oregon", "1 year"],
    [71, "Dylan Perry", "9919012345", "New York", "2 years"],
    [72, "Camila Long", "9920123456", "California", "3 years"],
    [73, "Hudson Russell", "9931234567", "Texas", "4 years"],
    [74, "Stella Griffin", "9942345678", "Florida", "2 years"],
    [75, "Christian Diaz", "9953456789", "Nevada", "3 years"],
    [76, "Madison Hayes", "9964567890", "Washington", "1 year"],
    [77, "Aaron Myers", "9975678901", "Illinois", "2 years"],
    [78, "Isla Ford", "9986789012", "Georgia", "4 years"],
    [79, "Joseph Murphy", "9997890123", "Virginia", "1 year"],
    [80, "Mila Hamilton", "9818901234", "Oregon", "3 years"],
    [81, "Christopher Graham", "9829012345", "New York", "2 years"],
    [82, "Zoey Sullivan", "9830123456", "California", "1 year"],
    [83, "Thomas Wallace", "9841234567", "Texas", "3 years"],
    [84, "Riley West", "9852345678", "Florida", "4 years"],
    [85, "Andrew Cole", "9863456789", "Nevada", "2 years"],
    [86, "Leah Foster", "9874567890", "Washington", "3 years"],
    [87, "Joshua Butler", "9885678901", "Illinois", "2 years"],
    [88, "Lillian Simmons", "9896789012", "Georgia", "1 year"],
    [89, "Eli Bryant", "9907890123", "Virginia", "2 years"],
    [90, "Paisley Alexander", "9918901234", "Oregon", "4 years"],
    [91, "Hunter Russell", "9929012345", "New York", "3 years"],
    [92, "Addison Hayes", "9930123456", "California", "2 years"],
    [93, "Isaiah Rivera", "9941234567", "Texas", "1 year"],
    [94, "Natalie Cooper", "9952345678", "Florida", "3 years"],
    [95, "Ezekiel Morris", "9963456789", "Nevada", "2 years"],
    [96, "Victoria Reed", "9974567890", "Washington", "1 year"],
    [97, "Lincoln Howard", "9985678901", "Illinois", "4 years"],
    [98, "Grace Turner", "9996789012", "Georgia", "2 years"],
    [99, "Jonathan Bell", "9817890123", "Virginia", "3 years"],
    [100, "Scarlett Ward", "9828901234", "Oregon", "1 year"]
]


car_location_data = [
    [1, "Lot-01-A", "Metro Storage Center"],
    [2, "Lot-02-B", "Metro Storage Center"],
    [3, "Lot-03-C", "Metro Storage Center"],
    [4, "Lot-04-D", "Metro Storage Center"],
    [5, "Lot-05-E", "Metro Storage Center"],
    [6, "Lot-06-F", "Metro Storage Center"],
    [7, "Lot-07-G", "Metro Storage Center"],
    [8, "Lot-08-H", "Metro Storage Center"],
    [9, "Lot-09-I", "Metro Storage Center"],
    [10, "Lot-10-J", "Metro Storage Center"],
    [11, "Lot-11-A", "Highway Auto Lot"],
    [12, "Lot-12-B", "Highway Auto Lot"],
    [13, "Lot-13-C", "Highway Auto Lot"],
    [14, "Lot-14-D", "Highway Auto Lot"],
    [15, "Lot-15-E", "Highway Auto Lot"],
    [16, "Lot-16-F", "Highway Auto Lot"],
    [17, "Lot-17-G", "Highway Auto Lot"],
    [18, "Lot-18-H", "Highway Auto Lot"],
    [19, "Lot-19-I", "Highway Auto Lot"],
    [20, "Lot-20-J", "Highway Auto Lot"],
    [21, "Lot-21-A", "Eastside Vehicle Park"],
    [22, "Lot-22-B", "Eastside Vehicle Park"],
    [23, "Lot-23-C", "Eastside Vehicle Park"],
    [24, "Lot-24-D", "Eastside Vehicle Park"],
    [25, "Lot-25-E", "Eastside Vehicle Park"],
    [26, "Lot-26-F", "Eastside Vehicle Park"],
    [27, "Lot-27-G", "Eastside Vehicle Park"],
    [28, "Lot-28-H", "Eastside Vehicle Park"],
    [29, "Lot-29-I", "Eastside Vehicle Park"],
    [30, "Lot-30-J", "Eastside Vehicle Park"],
    [31, "Lot-31-A", "North Auto Storage"],
    [32, "Lot-32-B", "North Auto Storage"],
    [33, "Lot-33-C", "North Auto Storage"],
    [34, "Lot-34-D", "North Auto Storage"],
    [35, "Lot-35-E", "North Auto Storage"],
    [36, "Lot-36-F", "North Auto Storage"],
    [37, "Lot-37-G", "North Auto Storage"],
    [38, "Lot-38-H", "North Auto Storage"],
    [39, "Lot-39-I", "North Auto Storage"],
    [40, "Lot-40-J", "North Auto Storage"],
    [41, "Lot-41-A", "Central Depot Yard"],
    [42, "Lot-42-B", "Central Depot Yard"],
    [43, "Lot-43-C", "Central Depot Yard"],
    [44, "Lot-44-D", "Central Depot Yard"],
    [45, "Lot-45-E", "Central Depot Yard"],
    [46, "Lot-46-F", "Central Depot Yard"],
    [47, "Lot-47-G", "Central Depot Yard"],
    [48, "Lot-48-H", "Central Depot Yard"],
    [49, "Lot-49-I", "Central Depot Yard"],
    [50, "Lot-50-J", "Central Depot Yard"],
    [51, "Lot-51-A", "Westline Auto Hub"],
    [52, "Lot-52-B", "Westline Auto Hub"],
    [53, "Lot-53-C", "Westline Auto Hub"],
    [54, "Lot-54-D", "Westline Auto Hub"],
    [55, "Lot-55-E", "Westline Auto Hub"],
    [56, "Lot-56-F", "Westline Auto Hub"],
    [57, "Lot-57-G", "Westline Auto Hub"],
    [58, "Lot-58-H", "Westline Auto Hub"],
    [59, "Lot-59-I", "Westline Auto Hub"],
    [60, "Lot-60-J", "Westline Auto Hub"],
    [61, "Lot-61-A", "Southside Car Depot"],
    [62, "Lot-62-B", "Southside Car Depot"],
    [63, "Lot-63-C", "Southside Car Depot"],
    [64, "Lot-64-D", "Southside Car Depot"],
    [65, "Lot-65-E", "Southside Car Depot"],
    [66, "Lot-66-F", "Southside Car Depot"],
    [67, "Lot-67-G", "Southside Car Depot"],
    [68, "Lot-68-H", "Southside Car Depot"],
    [69, "Lot-69-I", "Southside Car Depot"],
    [70, "Lot-70-J", "Southside Car Depot"],
    [71, "Lot-71-A", "Riverside Storage"],
    [72, "Lot-72-B", "Riverside Storage"],
    [73, "Lot-73-C", "Riverside Storage"],
    [74, "Lot-74-D", "Riverside Storage"],
    [75, "Lot-75-E", "Riverside Storage"],
    [76, "Lot-76-F", "Riverside Storage"],
    [77, "Lot-77-G", "Riverside Storage"],
    [78, "Lot-78-H", "Riverside Storage"],
    [79, "Lot-79-I", "Riverside Storage"],
    [80, "Lot-80-J", "Riverside Storage"],
    [81, "Lot-81-A", "Hilltop Auto Zone"],
    [82, "Lot-82-B", "Hilltop Auto Zone"],
    [83, "Lot-83-C", "Hilltop Auto Zone"],
    [84, "Lot-84-D", "Hilltop Auto Zone"],
    [85, "Lot-85-E", "Hilltop Auto Zone"],
    [86, "Lot-86-F", "Hilltop Auto Zone"],
    [87, "Lot-87-G", "Hilltop Auto Zone"],
    [88, "Lot-88-H", "Hilltop Auto Zone"],
    [89, "Lot-89-I", "Hilltop Auto Zone"],
    [90, "Lot-90-J", "Hilltop Auto Zone"],
    [91, "Lot-91-A", "Green Valley Storage"],
    [92, "Lot-92-B", "Green Valley Storage"],
    [93, "Lot-93-C", "Green Valley Storage"],
    [94, "Lot-94-D", "Green Valley Storage"],
    [95, "Lot-95-E", "Green Valley Storage"],
    [96, "Lot-96-F", "Green Valley Storage"],
    [97, "Lot-97-G", "Green Valley Storage"],
    [98, "Lot-98-H", "Green Valley Storage"],
    [99, "Lot-99-I", "Green Valley Storage"],
    [100, "Lot-100-J", "Green Valley Storage"]
]

car_damage_data = [
    [6, "Front collision with bumper and grille damage"],
    [10, "Severe front-end impact, airbags deployed"],
    [12, "Left side collision, doors dented and scratched"],
    [17, "Rear-end damage, bumper and trunk damaged"],
    [33, "Front collision, headlights and hood damaged"],
    [37, "Major crash, frame slightly bent"],
    [41, "Crashed — roof dent and windshield cracked"],
    [57, "Front and right side collision"],
    [60, "Frontal crash, radiator damaged"],
    [72, "Rear-end crash, tail light and trunk repair required"],
    [78, "Front bumper crash with minor engine damage"],
    [84, "Side impact crash, driver door damage"],
    [86, "Head-on collision, severe damage to bonnet"],
    [91, "Crash at intersection, left fender dented"],
    [99, "Major crash, both bumpers and hood damaged"]
]


def create_csv_file(file_path, headers, data):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            if data and isinstance(data[0], dict):
                writer.writerows([[d.get(h, "") for h in headers] for d in data])
            else:
                writer.writerows(data)

def read_csv_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def append_to_csv(file_path, headers, row):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def update_csv_row(file_path, key_field, key_value, new_data):
    temp_file = file_path + ".tmp"
    updated = False

    if not os.path.exists(file_path):
        return False

    with open(file_path, "r", newline="") as f, open(temp_file, "w", newline="") as tmpf:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(tmpf, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row[key_field] == str(key_value):
                row.update(new_data)
                updated = True
            writer.writerow(row)

    if updated:
        os.replace(temp_file, file_path)
        return True
    else:
        os.remove(temp_file)
        return False

def get_car_damage(car_id):
    damages = read_csv_file(CAR_DAMAGE_DATA)
    for d in damages:
        if d["Car ID"] == str(car_id):
            return d
    return None

def create_banner(parent, text):
    frame = tk.Frame(parent, bg=THEME["bg_banner"])
    frame.pack(fill="x", pady=10)
    label = tk.Label(
        frame,
        text=text,
        bg=THEME["bg_banner"],
        fg=THEME["fg_banner"],
        font=THEME["banner_font"]
    )
    label.pack(padx=5, pady=5)
    return label

def create_panel_right(parent):
    frame = tk.Frame(parent,width=400, height=400, bg=THEME["bg_default"], bd=0, highlightbackground="#000000",highlightthickness=0)
    frame.pack(side="right")
    entries = {}
    field(frame, "Username", "entry", entries=entries).config(justify="left")
    entries["Username"].config(justify="left") 

    field(frame, "Password", "entry", entries=entries, show="*").config(justify="left")
    entries["Password"].config(justify="left")

    # for widget in parent.winfo_children():
    #     if isinstance(widget, tk.Label):
    #         widget.config(fg="white", bg=THEME["bg_main"], font=("Arial", 12, "bold"))

    tk.Button(frame, text="Login", bg=THEME["btn_success_bg"],
        fg=THEME["btn_success_fg"], font=("Arial", 16, "bold"),
        width=15, height=1, command=lambda: login(entries)).pack(ipady=6, pady=10)

    tk.Button(frame, text="Register", bg=THEME["btn_primary_bg"],
        fg=THEME["btn_primary_fg"], font=("Arial", 16, "bold"),
        width=15, height=1, command=open_register_screen).pack(ipady=6)
    
def create_panel_left(parent):
    frame_right = tk.Frame(parent ,width=400,height=400, bg=THEME["bg_banner"], bd=1,highlightbackground="#000000",highlightthickness=0)
    frame_right.pack(side="left")

def create_spacer(parent):
    # Spacer (20 pixels wide)
    spacer = tk.Frame(parent, width=20, bg="#dddddd")
    spacer.pack(side="left")

def field(frame, label_text, widget_type="entry", options=None, entries=None, show=None):
    tk.Label(frame, text=label_text, bg=THEME["bg_default"], fg=THEME["label_fg"], font=THEME["normal_font_bold"]).pack(anchor="w", padx=20)
    if widget_type == "entry":
        e = tk.Entry(frame, width=30, bg=THEME["field_bg"], fg=THEME["field_fg"], show=show ,font=THEME["normal_font"])
        e.pack(pady=10, padx=20)
        if entries is not None:
            entries[label_text] = e
        return e
    elif widget_type == "dropdown":
        var = tk.StringVar()
        dropdown = ttk.Combobox(frame, textvariable=var, values=options or [], state="readonly", width=30, font=THEME["normal_font"])
        dropdown.pack(pady=10)
        if options:
            dropdown.current(0)
        if entries is not None:
            entries[label_text] = var
        return var
    elif widget_type == "text":
        txt = tk.Text(frame, width=30, height=10, bg=THEME["bg_default"], fg=THEME["field_fg"], font=THEME["normal_font"])
        txt.pack(pady=3)
        if entries is not None:
            entries[label_text] = txt
        return txt
    else:
        raise ValueError("Unknown widget_type for field()")

def initialize_csvs():
    create_csv_file(CAR_DETAILS_FILE,
        ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
        car_data)
    create_csv_file(CAR_STATUS_FILE,
        ["Car ID", "Availability", "Mileage", "Condition"],
        car_status_data)
    create_csv_file(CAR_SPEC_FILE,
        ["Car ID", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
        car_specification_data)
    create_csv_file(LOGIN_FILE,
        ["Username", "Password"],
        [["admin", "1234"]])
    create_csv_file(CAR_OWNERS_FILE,
        ["Car ID", "Owner Name", "Phone", "Address", "Ownership Duration"],
        car_owners_data)
    create_csv_file(CAR_LOCATION_FILE,
        ["Car ID", "Lot Number", "Storage Facility"],
        car_location_data)
    create_csv_file(CAR_DAMAGE_DATA,
        ["Car ID", "Damaged Parts", "Estimated Cost", "Repair Status"],
        car_damage_data)
    create_csv_file(CAR_CRASH_FILE, ["Car ID", "Crash Description"], [])

def start_app():
    if not os.path.exists(CAR_DETAILS_FILE):
        if messagebox.askyesno("Add Default Data?", "Do you want to add default car details?"):
            initialize_csvs()
    #show_login_screen()
    open_car_details_popup(99)

root = tk.Tk()
root.geometry("1920x1080")
root.config(bg=THEME["bg_main"])

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

def show_login_screen():
    clear_root()
    root.title(APP_TITLE)

    #create_banner(root, "Login")

    form_frame = tk.Frame(root, height=500, width=800, bg=THEME["bg_default"],bd=1,highlightbackground="#000000",highlightthickness=2)
    form_frame.place(relx=0.5, rely=0.5, anchor="center")
    #form_frame.pack(fill="both", expand=True, padx=20, pady=20)

    create_panel_left(form_frame)
    # create_spacer(form_frame)
    create_panel_right(form_frame)

   


def open_register_screen():
        clear_root()
        root.title(APP_TITLE)
        
        container = tk.Frame(root)
        container.pack(fill="both", expand=True)
        create_banner(container, "Register New User")


        frame_register = tk.Frame(container, bg=THEME["bg_default"], bd=1, highlightbackground="#000000", highlightthickness=1)
        frame_register.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

        reg_entries = {}
        tk.Label(frame_register, text="", bg=THEME["bg_default"]).pack(pady=14)
        field(frame_register, "New Username", "entry", entries=reg_entries)
        field(frame_register, "New Password", "entry", entries=reg_entries, show="*")

        # for widget in root.winfo_children():
        #     if isinstance(widget, tk.Label):
        #         widget.config(fg="white", bg=THEME["bg_main"], font=("Arial", 12, "bold"))

        def register_user():
            if not reg_entries["New Username"].get() or not reg_entries["New Password"].get():
                messagebox.showwarning("Warning", "Please fill all fields.")
                return
            users = read_csv_file(LOGIN_FILE)
            for u in users:
                if u["Username"] == reg_entries["New Username"].get():
                    messagebox.showerror("Error", "Username already exists.")
                    return
            append_to_csv(LOGIN_FILE, ["Username", "Password"], {
                "Username": reg_entries["New Username"].get(),
                "Password": reg_entries["New Password"].get()
            })
            messagebox.showinfo("Success", "User registered successfully!")
            show_login_screen()
        button_style = {
            "width": 22,
            "height": 2,
            "font": ("Arial", 18, "bold")
    }
        tk.Button(frame_register, text="Register", bg=THEME["btn_success_bg"],
                  fg=THEME["btn_success_fg"], **button_style,
                  command=register_user).pack(pady=10)

        tk.Button(frame_register, text="Back", bg=THEME["btn_neutral_bg"],
                  fg=THEME["btn_neutral_fg"], **button_style,
                  command=show_login_screen).pack(pady=10)

def login(entries):
    users = read_csv_file(LOGIN_FILE)
    for user in users:
        if (user["Username"] == entries["Username"].get() and
            user["Password"] == entries["Password"].get()):
            messagebox.showinfo("Login Successful", f"Welcome, {entries['Username'].get()}!")
            show_menu_screen()
            return
        else:
            messagebox.showerror("Error", "Invalid username or password. OK")
            return
    
   


def show_menu_screen():
    clear_root()
    root.title(APP_TITLE)
    create_banner(root, "Select your Action!")

    menu_frame = tk.Frame(root, bg=THEME["bg_main"])
    menu_frame.place(relx=0.5, rely=0.5, anchor="center")

    
    button_style = {
        "width": 22,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }

 
    tk.Button(
        menu_frame, text="🔍 Search Cars",
        bg=THEME["btn_primary_bg"], fg="white",
        **button_style, command=lambda: open_search_car_form(root)
    ).pack(pady=10)

    tk.Button(
        menu_frame, text="➕ Add New Car",
        bg=THEME["btn_success_bg"], fg="white",
        **button_style, command=open_add_car_screen
    ).pack(pady=10)

    tk.Button(
        menu_frame, text="🛠️ Update Car Details",
        bg=THEME["btn_secondary_bg"], fg="white",
        **button_style, command=lambda: open_update_car_screen(root, show_menu_screen)

    ).pack(pady=10)


    tk.Button(
        menu_frame, text="🚪 Logout",
        bg=THEME["btn_danger_bg"], fg="white",
        **button_style, command=show_login_screen
    ).pack(pady=10)

def open_add_car_screen():
    clear_root()
    root.title(APP_TITLE)

    entries = {}
    all_cars = read_csv_file(CAR_DETAILS_FILE)
    next_car_id = max([int(c["Car ID"]) for c in all_cars], default=99) + 1

    frames = {}
    def show_frame(name):
        for f in frames.values():
        #     f.pack_forget()
            #f.grid(row=0, column=0, sticky="nsew")
            f.place(relx=0.5, rely=0.5, anchor="center", width=400, height=800)
        frames[name].tkraise()
        
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    frame_basic = tk.Frame(container, bg=THEME["bg_default"], bd=1, highlightbackground="#000000", highlightthickness=3)
    #frame_basic.place(relx=0.5, rely=0.5, anchor="center")

    frames["basic"] = frame_basic
    create_banner(frame_basic, f"Add New Car (Vin ID: {next_car_id})")

    for name in ["Car Name", "Brand", "Model Year"]:
        field(frame_basic, name, "entry", entries=entries)
    
    field(frame_basic, "Fuel Type", "dropdown", options=["Petrol", "Diesel", "Electric", "Hybrid"], entries=entries)
    field(frame_basic, "Transmission", "dropdown", options=["Manual", "Automatic"], entries=entries)
    field(frame_basic, "Color", "entry", entries=entries)
    
    button_style = {
        "width": 22,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }
    tk.Button(frame_basic, text="Next", bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"], **button_style,
              command=lambda: show_frame("status")).pack(pady=6)
    tk.Button(frame_basic, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=show_menu_screen).pack(pady=6)


    frame_status = tk.Frame(container, bg=THEME["bg_default"], bd=1, highlightbackground="#000000", highlightthickness=3)
    # frame_status.place(relx=0.5, rely=0.5, anchor="center")

    frames["status"] = frame_status
    create_banner(frame_status, "Status & Technical Details")

    field(
        frame_status,
        "Availability",
        "dropdown",
        options=["Available", "Sold"],
        entries=entries
    )

    field(frame_status, "Mileage", "entry", entries=entries)
    condition_var = field(frame_status, "Condition", "dropdown", options=["Excellent", "Good", "Fair", "Poor", "Crashed"], entries=entries)

    for f in ["Engine CC", "Horsepower", "Torque", "Seating Capacity"]:
        field(frame_status, f, "entry", entries=entries)

    def go_next_from_status():
        if entries["Condition"].get().lower() == "crashed":
            show_frame("crash")
        else:
            show_frame("owner")

    tk.Button(frame_status, text="Next", bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"], **button_style,
              command=go_next_from_status).pack(pady=6)
    tk.Button(frame_status, text="Back", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=lambda: show_frame("basic")).pack(pady=6)
    tk.Button(frame_status, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=show_menu_screen).pack(pady=6)

    frame_crash = tk.Frame(container, bg=THEME["bg_default"], bd=1, highlightbackground="#000000", highlightthickness=3)

    frames["crash"] = frame_crash
    create_banner(frame_crash, "Crash Condition Details")
    field(frame_crash, "Crash Description", "text", entries=entries)  # store Text widget
    tk.Button(frame_crash, text="Next", bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"], **button_style,
              command=lambda: show_frame("owner")).pack(padx=6)
    tk.Button(frame_crash, text="Back", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=lambda: show_frame("status")).pack(padx=6)
    tk.Button(frame_crash, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=show_menu_screen).pack(padx=6)

    frame_owner = tk.Frame(container, bg=THEME["bg_default"], bd=1, highlightbackground="#000000", highlightthickness=3)
   
    frames["owner"] = frame_owner
    create_banner(frame_owner, "Previous Owner Details")
    for f in ["Owner Name", "Phone", "Address", "Ownership Duration"]:
        field(frame_owner, f, "entry", entries=entries)
    tk.Button(frame_owner, text="Next", bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"], **button_style,
              command=lambda: show_frame("storage")).pack(pady=6)
    tk.Button(frame_owner, text="Back", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=lambda: show_frame("status")).pack(pady=6)
    tk.Button(frame_owner, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=show_menu_screen).pack(pady=6)

    frame_storage = tk.Frame(container, bg=THEME["bg_default"], bd=1, highlightbackground="#000000", highlightthickness=3)

    frames["storage"] = frame_storage
    create_banner(frame_storage, "Car Storage / Location")
    for f in ["Lot Number", "Storage Facility"]:
        field(frame_storage, f, "entry", entries=entries)

    def save_car():
        car_id = next_car_id
  
        def get_val(k):
            w = entries[k]
            if isinstance(w, tk.Text):
                return w.get("1.0", "end").strip()
            elif isinstance(w, tk.StringVar):
                return w.get()
            else:
                return w.get()

        car_row = {k: get_val(k) for k in ["Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"]}
        car_row["Car ID"] = car_id
        append_to_csv(CAR_DETAILS_FILE, ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"], car_row)

        status_row = {k: get_val(k) for k in ["Availability", "Mileage", "Condition"]}
        status_row["Car ID"] = car_id
        append_to_csv(CAR_STATUS_FILE, ["Car ID", "Availability", "Mileage", "Condition"], status_row)

        spec_row = {k: get_val(k) for k in ["Engine CC", "Horsepower", "Torque", "Seating Capacity"]}
        spec_row["Car ID"] = car_id
        append_to_csv(CAR_SPEC_FILE, ["Car ID", "Engine CC", "Horsepower", "Torque", "Seating Capacity"], spec_row)

        owner_row = {k: get_val(k) for k in ["Owner Name", "Phone", "Address", "Ownership Duration"]}
        owner_row["Car ID"] = car_id
        append_to_csv(CAR_OWNERS_FILE, ["Car ID", "Owner Name", "Phone", "Address", "Ownership Duration"], owner_row)

        location_row = {k: get_val(k) for k in ["Lot Number", "Storage Facility"]}
        location_row["Car ID"] = car_id
        append_to_csv(CAR_LOCATION_FILE, ["Car ID", "Lot Number", "Storage Facility"], location_row)

        if entries["Condition"].get().lower() == "crashed":
            crash_text = entries["Crash Description"].get("1.0", "end").strip() if isinstance(entries["Crash Description"], tk.Text) else entries["Crash Description"].get()
            append_to_csv(CAR_CRASH_FILE, ["Car ID", "Crash Description"], {"Car ID": car_id, "Crash Description": crash_text})

        messagebox.showinfo("Success", f"Car ID {car_id} added successfully!")
        show_menu_screen()

    tk.Button(frame_storage, text="Add Car", bg=THEME["btn_success_bg"], fg=THEME["btn_success_fg"], **button_style, 
              command=save_car).pack(pady=6)
    tk.Button(frame_storage, text="Back", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=lambda: show_frame("owner")).pack(pady=6)
    tk.Button(frame_storage, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=show_menu_screen).pack(pady=6)

    show_frame("basic")


def open_car_details_popup(car_id):
    car_id = str(car_id)
    win = tk.Toplevel(root)
    win.title(APP_TITLE)
    win.geometry("520x700")
    win.config(bg=THEME["bg_main"])

    def section_title(parent, text):
        tk.Label(parent, text=text, font=THEME["normal_font_bold"],
                 bg="#e6f7ff", anchor="w", padx=10).pack(fill="x", pady=(15, 5))

    details = next((c for c in read_csv_file(CAR_DETAILS_FILE) if c["Car ID"] == car_id), None)
    if not details:
        tk.Label(win, text="Car not found.", font=THEME["normal_font_bold"]).pack(pady=30)
        return

    brand = details.get("Brand", "Unknown Brand")
    banner = tk.Frame(win, bg=THEME["bg_banner"])
    banner.pack(fill="x")
    tk.Label(banner, text=f"{brand} {details['Car Name']} — Vin ID: {car_id}",
             font=THEME["banner_font"], bg=THEME["bg_banner"], fg=THEME["fg_banner"],
             pady=10).pack(fill="x")

 
    container = tk.Frame(win, bg=THEME["bg_main"])
    container.pack(fill="both", expand=True, padx=10, pady=10)
    canvas = tk.Canvas(container, bg=THEME["bg_main"], highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=THEME["bg_main"])
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


    status = next((s for s in read_csv_file(CAR_STATUS_FILE) if s["Car ID"] == car_id), None)
    spec = next((sp for sp in read_csv_file(CAR_SPEC_FILE) if sp["Car ID"] == car_id), None)
    owner = [o for o in read_csv_file(CAR_OWNERS_FILE) if o["Car ID"] == car_id]
    loc = next((l for l in read_csv_file(CAR_LOCATION_FILE) if l["Car ID"] == car_id), None)


    section_title(scroll_frame, f"{details['Car Name']} — Basic Details")
    tk.Label(scroll_frame,
             text=(f"Model Year: {details.get('Model Year','')}\n"
                   f"Fuel Type: {details.get('Fuel Type','')}\n"
                   f"Transmission: {details.get('Transmission','')}\n"
                   f"Color: {details.get('Color','')}"),
             bg=THEME["bg_main"], font=THEME["normal_font"], justify="left").pack(anchor="w", padx=20)


    if status:
        section_title(scroll_frame, "Status Information")
        tk.Label(scroll_frame,
                 text=(f"Availability: {status.get('Availability','')}\n"
                       f"Mileage: {status.get('Mileage','')} km\n"
                       f"Condition: {status.get('Condition','')}"),
                 bg=THEME["bg_main"], font=THEME["normal_font"], justify="left").pack(anchor="w", padx=20)

        if status.get('Condition','').lower() == "crashed":
            def show_damage_details():
                dmg = get_car_damage(car_id)
                dmg_win = tk.Toplevel(win)
                dmg_win.title(APP_TITLE)
                dmg_win.geometry("500x300")
                dmg_win.config(bg=THEME["bg_main"])
                tk.Label(dmg_win, text=f"Damage Report — Car ID {car_id}",
                         font=THEME["normal_font"], bg=THEME["bg_banner"], fg=THEME["fg_banner"]).pack(fill="x", pady=(0, 10))
                if not dmg:
                    tk.Label(dmg_win, text="No damage details found for this car.", font=THEME["normal_font"],
                             bg=THEME["bg_main"]).pack(pady=40)
                else:
                    tk.Label(dmg_win, text=f"Damaged Parts:\n{dmg.get('Damaged Parts','')}",
                             font=THEME["normal_font"], bg=THEME["bg_main"], justify="left", wraplength=460).pack(padx=20, pady=10)
            button_style = {
        "width": 22,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }
            tk.Button(scroll_frame, text="View Damage Details", bg=THEME["btn_danger_bg"],
                      fg=THEME["btn_danger_fg"], **button_style, command=show_damage_details).pack(pady=10)


    if spec:
        section_title(scroll_frame, "Technical Specifications")
        tk.Label(scroll_frame,
                 text=(f"Engine CC: {spec.get('Engine CC','')}\n"
                       f"Horsepower: {spec.get('Horsepower','')}\n"
                       f"Torque: {spec.get('Torque','')}\n"
                       f"Seating Capacity: {spec.get('Seating Capacity','')}"),
                 bg=THEME["bg_main"], font=THEME["normal_font"], justify="left").pack(anchor="w", padx=20)


    def show_owner_details():
        owner_win = tk.Toplevel(win)
        owner_win.title(APP_TITLE)
        owner_win.geometry("480x300")
        owner_win.config(bg=THEME["bg_main"])
        create_banner(owner_win, "Previous Owners")
        if not owner:
            tk.Label(owner_win, text="No previous owners found.", bg=THEME["bg_main"],
                     font=THEME["normal_font"]).pack(pady=30); return
        cols = ["Owner Name", "Phone", "Address", "Ownership Duration"]
        tree2 = ttk.Treeview(owner_win, columns=cols, show="headings", height=8)
        style = ttk.Style(owner_win)
        style.configure("Treeview", 
                font=THEME["normal_font"],
                rowheight=25) 
        style.configure("Treeview.Heading", 
                font=THEME["normal_font_bold"],
                rowheight=25) 
        for col in cols:
            tree2.heading(col, text=col); tree2.column(col, width=110)
        for o in owner:
            tree2.insert("", tk.END, values=[o.get(c, "") for c in cols])
        tree2.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    button_style = {
        "width": 22,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }
    tk.Button(scroll_frame, text="View Previous Owners", bg=THEME["bg_banner"], fg=THEME["fg_banner"],
              **button_style, command=show_owner_details).pack(pady=10)

    def show_location():
        loc_win = tk.Toplevel(win)
        loc_win.title(APP_TITLE)
        loc_win.geometry("400x220")
        loc_win.config(bg=THEME["bg_main"])
        create_banner(loc_win, "Storage Location")
        if not loc:
            tk.Label(loc_win, text="Location details not found.", font=("Arial", 12), bg=THEME["bg_main"]).pack(pady=40)
        else:
            tk.Label(loc_win, text=f"Lot Number: {loc.get('Lot Number','')}\nStorage Facility: {loc.get('Storage Facility','')}",
                     font=THEME["normal_font"], bg=THEME["bg_main"], justify="left").pack(pady=20)
    button_style = {
        "width": 22,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }
    tk.Button(scroll_frame, text="View Location", bg=THEME["btn_secondary_bg"], fg=THEME["btn_secondary_fg"],
              **button_style, command=show_location).pack(pady=5)

    tk.Button(scroll_frame, text="Close", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
              command=win.destroy).pack(pady=15)


def open_search_car_form(root_window):
    clear_root()
    root_window.title(APP_TITLE)
    create_banner(root_window, "Car Search")


    search_var = tk.StringVar()
    tk.Label(root_window, text="Search by VIN / Brand / Car Name:", bg=THEME["bg_main"], fg=THEME["label_fg"], font=THEME["normal_font"]).pack(pady=(8, 0))
    search_entry = tk.Entry(root_window, textvariable=search_var, width=30,
                            bg=THEME["field_bg"], fg=THEME["field_fg"])
    search_entry.pack(pady=5)

    columns = ("Vin ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color")
    tree = ttk.Treeview(root_window, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col); tree.column(col, width=85)
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def load_all_cars():
        tree.delete(*tree.get_children())
        cars = read_csv_file(CAR_DETAILS_FILE)
        for car in cars:
            tree.insert("", tk.END, values=(car["Car ID"], car["Car Name"], car["Brand"],
                                           car["Model Year"], car["Fuel Type"], car["Transmission"], car["Color"]))

    def perform_search(event=None):
        query_text = search_var.get().strip().lower()
        tree.delete(*tree.get_children())
        if len(query_text) >= 1:
            cars = read_csv_file(CAR_DETAILS_FILE)
            results = [car for car in cars if query_text in car["Car Name"].lower()
                       or query_text in car["Brand"].lower() or query_text in car["Car ID"].lower()]
            if results:
                for car in results:
                    tree.insert("", tk.END, values=(car["Car ID"], car["Car Name"], car["Brand"],
                                                   car["Model Year"], car["Fuel Type"], car["Transmission"], car["Color"]))
            else:
                tree.insert("", tk.END, values=("No cars found", "", "", "", "", "", ""))
        else:
            load_all_cars()

    search_entry.bind("<KeyRelease>", perform_search)

    def view_selected_car():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a car from the list."); return
        car_data = tree.item(selected[0], "values")
        open_car_details_popup(car_data[0])
    
    button_style = {
        "width": 22,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }

    tk.Button(root_window, text="View Selected Car", bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"],
              **button_style, command=view_selected_car).pack(pady=5)
    tk.Button(root_window, text="Back to Menu", bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"],
              **button_style, command=show_menu_screen).pack(pady=5)

    load_all_cars()


def open_update_car_screen(root, show_menu_callback):

    root.title(APP_TITLE)
    root.geometry("1920x1080")

    for widget in root.winfo_children():
        widget.destroy()

    create_banner(root, "Update Car Details")

    current_step = {"value": 0}
    car_id_var = tk.StringVar()
    entries = {}

    sections = {
        "Basic Info": ["Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
        "Status & Technical": ["Availability", "Mileage", "Condition", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
        "Owner Info": ["Owner Name", "Phone", "Address", "Ownership Duration"],
        "Location Info": ["Lot Number", "Storage Facility"],
        "Crash Details": ["Crash Description"]
    }
    section_keys = list(sections.keys())

    def set_widget_value(widget, value):
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
            widget.insert(0, value)
        elif isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)
            widget.insert(tk.END, value)
        else:
            try:
                widget.set(value)
            except Exception:
                if hasattr(widget, "delete"):
                    widget.delete(0, tk.END)
                    widget.insert(0, value)

    def load_car(car_id):
        car_id = car_id.strip()
        if not car_id:
            messagebox.showwarning("Warning", "Please enter a Car ID!")
            return

        details = next((c for c in read_csv_file(CAR_DETAILS_FILE) if c["Car ID"] == car_id), None)
        status = next((c for c in read_csv_file(CAR_STATUS_FILE) if c["Car ID"] == car_id), None)
        spec = next((c for c in read_csv_file(CAR_SPEC_FILE) if c["Car ID"] == car_id), None)
        owner = next((c for c in read_csv_file(CAR_OWNERS_FILE) if c["Car ID"] == car_id), None)
        loc = next((c for c in read_csv_file(CAR_LOCATION_FILE) if c["Car ID"] == car_id), None)
        crash = next((c for c in read_csv_file(CAR_CRASH_FILE) if c["Car ID"] == car_id), None)

        if not details:
            messagebox.showerror("Error", f"No car found with ID {car_id}")
            return

        for f in sections["Basic Info"]:
            widget = entries.get(f)
            if widget:
                set_widget_value(widget, details.get(f, ""))

        for f in ["Availability", "Mileage", "Condition"]:
            widget = entries.get(f)
            if widget:
                val = status.get(f) if status and f in status else ""
                set_widget_value(widget, val)

        for f in ["Engine CC", "Horsepower", "Torque", "Seating Capacity"]:
            widget = entries.get(f)
            if widget:
                val = spec.get(f) if spec and f in spec else ""
                set_widget_value(widget, val)

        for f in sections["Owner Info"]:
            widget = entries.get(f)
            if widget:
                val = owner.get(f, "") if owner else ""
                set_widget_value(widget, val)

        for f in sections["Location Info"]:
            widget = entries.get(f)
            if widget:
                val = loc.get(f, "") if loc else ""
                set_widget_value(widget, val)

        if crash:
            txt = entries.get("Crash Description")
            if txt:
                set_widget_value(txt, crash.get("Crash Description", ""))

        show_step(0)
        messagebox.showinfo("Success", f"Car ID {car_id} loaded successfully!")

    def save_updates():
        car_id = car_id_var.get().strip()
        if not car_id:
            messagebox.showwarning("Warning", "Please enter a Car ID")
            return

        def read_val(w):
            if isinstance(w, tk.Text):
                return w.get("1.0", "end").strip()
            elif isinstance(w, tk.Entry):
                return w.get()
            elif isinstance(w, tk.StringVar):
                return w.get()
            else:
                try:
                    return w.get()
                except:
                    return ""

        updated_details = {f: read_val(entries[f]) for f in sections["Basic Info"] if f in entries}
        updated_status = {f: read_val(entries[f]) for f in ["Availability", "Mileage", "Condition"] if f in entries}
        updated_spec = {f: read_val(entries[f]) for f in ["Engine CC", "Horsepower", "Torque", "Seating Capacity"] if f in entries}
        updated_owner = {f: read_val(entries[f]) for f in sections["Owner Info"] if f in entries}
        updated_loc = {f: read_val(entries[f]) for f in sections["Location Info"] if f in entries}

        ok1 = update_csv_row(CAR_DETAILS_FILE, "Car ID", car_id, updated_details)
        ok2 = update_csv_row(CAR_STATUS_FILE, "Car ID", car_id, updated_status)
        ok3 = update_csv_row(CAR_SPEC_FILE, "Car ID", car_id, updated_spec)
        ok4 = update_csv_row(CAR_OWNERS_FILE, "Car ID", car_id, updated_owner)
        ok5 = update_csv_row(CAR_LOCATION_FILE, "Car ID", car_id, updated_loc)

        crash_widget = entries.get("Crash Description")
        crash_text = read_val(crash_widget) if crash_widget is not None else ""
        if crash_text:
            existing = next((r for r in read_csv_file(CAR_CRASH_FILE) if r["Car ID"] == car_id), None)
            if existing:
                update_csv_row(CAR_CRASH_FILE, "Car ID", car_id, {"Crash Description": crash_text})
            else:
                append_to_csv(CAR_CRASH_FILE, ["Car ID", "Crash Description"], {"Car ID": car_id, "Crash Description": crash_text})

        if all([ok1, ok2, ok3, ok4, ok5]):
            messagebox.showinfo("Success", f"Car ID {car_id} updated successfully!")
            show_menu_callback()
        else:
            messagebox.showwarning("Warning", "Some updates may have failed. Check CSVs.")

    # --- UI layout ---
    id_frame = tk.Frame(root, bg=THEME["bg_main"])
    id_frame.pack(pady=10)

    tk.Label(id_frame, text="Enter Car ID to load: ", bg=THEME["bg_main"], font=THEME["normal_font_bold"]).pack(side="left", padx=5)
    tk.Entry(id_frame, textvariable=car_id_var, width=26, bg=THEME["field_bg"], fg=THEME["field_fg"]).pack(side="left", padx=5)
    load_button_style = {
        "width": 22,
        "height": 1,
        "font": ("Arial", 18, "bold")
    }
    button_style = {
        "width": 18,
        "height": 2,
        "font": ("Arial", 18, "bold")
    }
    tk.Button(
        id_frame, text="Load Car",
        bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"], **load_button_style,
        command=lambda: load_car(car_id_var.get())
    ).pack(side="left", padx=5)

    progress_label = tk.Label(root, text="", bg=THEME["bg_main"], font=("Arial", 16))
    progress_label.pack(pady=5)

    container = tk.Frame(root, bg=THEME["bg_main"])
    container.pack(fill="both", expand=True, pady=10)

    canvas = tk.Canvas(container, bg=THEME["bg_main"])
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scroll_frame = tk.Frame(canvas, bg=THEME["bg_main"])
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", on_frame_configure)

    def _on_mousewheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    section_frames = {}
    for section_name, fields_list in sections.items():
        frame = tk.Frame(scroll_frame, bg=THEME["bg_default"])
        section_frames[section_name] = frame
        create_banner(frame, section_name)

        for field_label in fields_list:
            if field_label in ("Fuel Type",):
                field(frame, field_label, "dropdown", options=["Petrol", "Diesel", "Electric", "Hybrid"], entries=entries)
            elif field_label in ("Transmission",):
                field(frame, field_label, "dropdown", options=["Manual", "Automatic"], entries=entries)
            elif field_label == "Condition":
                field(frame, field_label, "dropdown", options=["Excellent", "Good", "Fair", "Poor", "Crashed"], entries=entries)
            elif field_label == "Crash Description":
                field(frame, field_label, "text", entries=entries)
            else:
                field(frame, field_label, "entry", entries=entries)

    nav_frame = tk.Frame(root, bg=THEME["bg_main"])
    nav_frame.pack(pady=15)

    prev_btn = tk.Button(
        nav_frame, text="← Previous",
        bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
        command=lambda: show_step(current_step["value"] - 1)
    )
    prev_btn.pack(side="left", padx=10)

    next_btn = tk.Button(
        nav_frame, text="Next →",
        bg=THEME["btn_primary_bg"], fg=THEME["btn_primary_fg"], **button_style,
        command=lambda: show_step(current_step["value"] + 1)
    )
    next_btn.pack(side="left", padx=10)

    save_btn = tk.Button(
        nav_frame, text="Save Updates",
        bg=THEME["btn_success_bg"], fg=THEME["btn_success_fg"], **button_style,
        command=save_updates
    )
    save_btn.pack(side="left", padx=10)
    save_btn.pack_forget()

    back_btn = tk.Button(
        root, text="Back to Menu",
        bg=THEME["btn_neutral_bg"], fg=THEME["btn_neutral_fg"], **button_style,
        command=show_menu_callback
    )
    back_btn.pack(pady=5)

    def show_step(step):
        if step < 0 or step >= len(section_keys):
            return

        current_step["value"] = step
        for frame in section_frames.values():
            frame.pack_forget()

        current_section = section_keys[step]
        section_frames[current_section].pack(fill="both", expand=True)
        progress_label.config(text=f"Step {step + 1} of {len(section_keys)}: {current_section}")

        if step == 0:
            prev_btn.config(state="disabled")
        else:
            prev_btn.config(state="normal")

        if step == len(section_keys) - 1:
            next_btn.pack_forget()
            save_btn.pack(side="left", padx=10)
        else:
            save_btn.pack_forget()
            next_btn.pack(side="left", padx=10)

        canvas.yview_moveto(0)

    show_step(0)

start_app()
root.mainloop()
