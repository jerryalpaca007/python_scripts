# ==========================================================
#   CAR DEALERSHIP / ACCIDENT REPORT SYSTEM (CSV VERSION)
# ==========================================================

import tkinter as tk
from tkinter import ttk, messagebox
import csv, os
from test import open_update_car_screen

# ==========================================================
#   FILE PATHS
# ==========================================================
CAR_DETAILS_FILE = "car_details.csv"
CAR_STATUS_FILE = "car_status.csv"
CAR_SPEC_FILE = "car_specifications.csv"
LOGIN_FILE = "login_data.csv"
CAR_OWNERS_FILE = "car_owners.csv"
CAR_LOCATION_FILE = "car_location.csv"
CAR_DAMAGE_DATA = "car_damage.csv"


# ==========================================================
#   DEFAULT DATA
# ==========================================================
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

# ==========================================================
#   CSV HELPERS
# ==========================================================
def create_csv_file(file_path, headers, data):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
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

def get_car_damage(car_id):
    damages = read_csv_file(CAR_DAMAGE_DATA)
    for d in damages:
        if d["Car ID"] == str(car_id):
            return d
    return None

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

def start_app():
    if not os.path.exists(CAR_DETAILS_FILE):
        if messagebox.askyesno("Add Default Data?", "Do you want to add default car details?"):
            initialize_csvs()
    show_login_screen()

# ==========================================================
#   MAIN WINDOW
# ==========================================================
root = tk.Tk()
root.geometry("700x650")

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

# ==========================================================
#   LOGIN SCREEN
# ==========================================================
def show_login_screen():
    clear_root()
    root.title("Login")

    tk.Label(root, text="Car Dealership Login", font=("Arial", 18, "bold")).pack(pady=20)
    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(root, text="Username").pack()
    tk.Entry(root, textvariable=username).pack(pady=5)
    tk.Label(root, text="Password").pack()
    tk.Entry(root, textvariable=password, show="*").pack(pady=5)

    def login():
        users = read_csv_file(LOGIN_FILE)
        for user in users:
            if user["Username"] == username.get() and user["Password"] == password.get():
                messagebox.showinfo("Login Successful", f"Welcome, {username.get()}!")
                show_menu_screen()
                return
        messagebox.showerror("Error", "Invalid username or password.")

    def open_register_screen():
        clear_root()
        root.title("Register")

        tk.Label(root, text="Register New User", font=("Arial", 18, "bold")).pack(pady=20)
        new_user = tk.StringVar()
        new_pass = tk.StringVar()

        tk.Label(root, text="New Username").pack()
        tk.Entry(root, textvariable=new_user).pack(pady=5)
        tk.Label(root, text="New Password").pack()
        tk.Entry(root, textvariable=new_pass, show="*").pack(pady=5)

        def register_user():
            if not new_user.get() or not new_pass.get():
                messagebox.showwarning("Warning", "Please fill all fields.")
                return
            users = read_csv_file(LOGIN_FILE)
            for u in users:
                if u["Username"] == new_user.get():
                    messagebox.showerror("Error", "Username already exists.")
                    return
            append_to_csv(LOGIN_FILE, ["Username", "Password"],
                          {"Username": new_user.get(), "Password": new_pass.get()})
            messagebox.showinfo("Success", "User registered successfully!")
            show_login_screen()

        tk.Button(root, text="Register", bg="green", fg="white", width=15, command=register_user).pack(pady=10)
        tk.Button(root, text="Back", command=show_login_screen).pack()

    tk.Button(root, text="Login", bg="green", fg="white", width=15, command=login).pack(pady=10)
    tk.Button(root, text="Register", bg="blue", fg="white", width=15, command=open_register_screen).pack(pady=5)

# ==========================================================
#   MENU SCREEN
# ==========================================================


def show_menu_screen():
    clear_root()
    root.title("Main Menu")
    tk.Label(root, text="Car Dealership System", font=("Arial", 20, "bold")).pack(pady=20)

    tk.Button(root, text="Search Cars", bg="blue", fg="white", width=20, height=2,
              command=lambda: open_search_car_form(root)).pack(pady=10)
    
    tk.Button(root, text="Add New Car", bg="green", fg="white", width=20, height=2,
              command=open_add_car_screen).pack(pady=10)

    tk.Button(root, text="Update Car Details", bg="purple", fg="white", width=20, height=2,
              command=lambda: open_update_car_screen(root, show_menu_screen)).pack(pady=10)
    
    tk.Button(root, text="Logout", bg="red", fg="white", width=20, height=2,
              command=show_login_screen).pack(pady=10)


# ==========================================================
#   ADD CAR SCREEN
# ==========================================================
def open_add_car_screen():
    clear_root()
    root.title("Add Car Details")

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)
    canvas = tk.Canvas(container)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    scroll_frame = tk.Frame(canvas, bg="#f5f5f5")
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * int(e.delta / 120), "units"))

    tk.Label(scroll_frame, text="Add New Car", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)
    entries = {}

    def section(title):
        tk.Label(scroll_frame, text=title, font=("Arial", 14, "bold"), bg="#e6f7ff").pack(fill="x", pady=10)

    def field(label, widget_type="entry", options=None):
        tk.Label(scroll_frame, text=label, bg="#f5f5f5").pack()
        if widget_type == "entry":
            e = tk.Entry(scroll_frame, width=40)
            e.pack(pady=3)
            entries[label] = e
        elif widget_type == "dropdown":
            var = tk.StringVar()
            dropdown = ttk.Combobox(scroll_frame, textvariable=var, values=options, state="readonly", width=38)
            dropdown.pack(pady=3)
            if options:
                dropdown.current(0)
            entries[label] = var

    all_cars = read_csv_file(CAR_DETAILS_FILE)
    next_car_id = max([int(c["Car ID"]) for c in all_cars], default=99) + 1

    section("1️⃣  Basic Car Information")
    tk.Label(scroll_frame, text=f"Car ID (Auto Assigned): {next_car_id}", font=("Arial", 12, "italic")).pack(pady=5)
    field("Car Name")
    field("Brand")
    field("Model Year")
    field("Fuel Type", widget_type="dropdown", options=["Petrol", "Diesel", "Electric", "Hybrid"])
    field("Transmission", widget_type="dropdown", options=["Manual", "Automatic"])
    field("Color")

    section("2️⃣  Status & Technical Details")
    for f in ["Availability", "Mileage", "Condition", "Engine CC", "Horsepower", "Torque", "Seating Capacity"]:
        field(f)

    section("3️⃣  Previous Owner Details")
    for f in ["Owner Name", "Phone", "Address", "Ownership Duration"]:
        field(f)

    section("4️⃣  Car Storage / Location Information")
    for f in ["Lot Number", "Storage Facility"]:
        field(f)

    def save_car():
        car_id = next_car_id

        # --- Car Details ---
        car_row = {k: entries[k].get() for k in ["Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"]}
        car_row["Car ID"] = car_id
        append_to_csv(
            CAR_DETAILS_FILE,
            ["Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color"],
            car_row
        )

        # --- Car Status ---
        status_row = {k: entries[k].get() for k in ["Availability", "Mileage", "Condition"]}
        status_row["Car ID"] = car_id
        append_to_csv(
            CAR_STATUS_FILE,
            ["Car ID", "Availability", "Mileage", "Condition"],
            status_row
        )

        # --- Car Specifications ---
        spec_row = {k: entries[k].get() for k in ["Engine CC", "Horsepower", "Torque", "Seating Capacity"]}
        spec_row["Car ID"] = car_id
        append_to_csv(
            CAR_SPEC_FILE,
            ["Car ID", "Engine CC", "Horsepower", "Torque", "Seating Capacity"],
            spec_row
        )

        # --- Car Owners ---
        owner_row = {k: entries[k].get() for k in ["Owner Name", "Phone", "Address", "Ownership Duration"]}
        owner_row["Car ID"] = car_id
        append_to_csv(
            CAR_OWNERS_FILE,
            ["Car ID", "Owner Name", "Phone", "Address", "Ownership Duration"],
            owner_row
        )

        # --- Car Location ---
        location_row = {k: entries[k].get() for k in ["Lot Number", "Storage Facility"]}
        location_row["Car ID"] = car_id
        append_to_csv(
            CAR_LOCATION_FILE,
            ["Car ID", "Lot Number", "Storage Facility"],
            location_row
        )

        messagebox.showinfo("Success", f"Car ID {car_id} added successfully!")
        show_menu_screen()

    tk.Button(scroll_frame, text="Save Car", bg="green", fg="white", width=15, command=save_car).pack(pady=15)
    tk.Button(scroll_frame, text="Back to Menu", command=show_menu_screen).pack(pady=5)

# ==========================================================
#   SEARCH + CAR DETAILS POPUP (with location)
# ==========================================================
def open_search_car_form(root_window):
    clear_root()
    root_window.title("Search Car Details")
    tk.Label(root_window, text="Search Car Details", font=("Arial", 16, "bold")).pack(pady=10)
    search_var = tk.StringVar()
    search_entry = tk.Entry(root_window, textvariable=search_var, width=40)
    search_entry.pack(pady=5)

    columns = ("Car ID", "Car Name", "Brand", "Model Year", "Fuel Type", "Transmission", "Color")
    tree = ttk.Treeview(root_window, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=85)
    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def load_all_cars():
        tree.delete(*tree.get_children())
        cars = read_csv_file(CAR_DETAILS_FILE)
        for car in cars:
            tree.insert("", tk.END, values=(car["Car ID"], car["Car Name"], car["Brand"], car["Model Year"], car["Fuel Type"], car["Transmission"], car["Color"]))

    def perform_search(event=None):
        query_text = search_var.get().strip().lower()
        tree.delete(*tree.get_children())
        if len(query_text) >= 1:
            cars = read_csv_file(CAR_DETAILS_FILE)
            results = [car for car in cars if query_text in car["Car Name"].lower() or query_text in car["Brand"].lower() or query_text in car["Car ID"].lower()]
            if results:
                for car in results:
                    tree.insert("", tk.END, values=(car["Car ID"], car["Car Name"], car["Brand"], car["Model Year"], car["Fuel Type"], car["Transmission"], car["Color"]))
            else:
                tree.insert("", tk.END, values=("No cars found", "", "", "", "", "", ""))
        else:
            load_all_cars()

    search_entry.bind("<KeyRelease>", perform_search)

    def view_selected_car():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a car from the list.")
            return
        car_data = tree.item(selected[0], 'values')
        open_car_details_popup(car_data[0])

    tk.Button(root_window, text="View Selected Car", bg="orange", fg="white", command=view_selected_car).pack(pady=5)
    tk.Button(root_window, text="Back to Menu", command=show_menu_screen).pack(pady=5)
    load_all_cars()

# ==========================================================
#   CAR DETAILS POPUP
# ==========================================================
def open_car_details_popup(car_id):
    car_id = str(car_id)
    win = tk.Toplevel(root)
    win.title("Car Details")
    win.geometry("500x600")

    details = next((c for c in read_csv_file(CAR_DETAILS_FILE) if c["Car ID"] == car_id), None)
    status = next((s for s in read_csv_file(CAR_STATUS_FILE) if s["Car ID"] == car_id), None)
    spec = next((sp for sp in read_csv_file(CAR_SPEC_FILE) if sp["Car ID"] == car_id), None)
    owner = [o for o in read_csv_file(CAR_OWNERS_FILE) if o["Car ID"] == car_id]
    loc = next((l for l in read_csv_file(CAR_LOCATION_FILE) if l["Car ID"] == car_id), None)

    if not details:
        tk.Label(win, text="Car not found.").pack()
        return

    tk.Label(win, text=f"{details['Car Name']} ({details['Brand']})", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(win, text=f"Year: {details['Model Year']}\nFuel: {details['Fuel Type']}\nTransmission: {details['Transmission']}\nColor: {details['Color']}", justify="left").pack(pady=5)

    if status:
        tk.Label(win, text=f"\nStatus:\nAvailability: {status['Availability']}\nMileage: {status['Mileage']} km\nCondition: {status['Condition']}", justify="left").pack(pady=5)
    
    if status and status['Condition'].lower() == 'crashed':
        def show_damage_details():
            dmg = get_car_damage(car_id)
            dmg_win = tk.Toplevel(win)
            dmg_win.title("Damage Details")
            dmg_win.geometry("600x250")
            if not dmg:
                tk.Label(dmg_win, text="No damage details found for this car.", font=("Arial", 12)).pack(pady=30)
                return
            tk.Label(dmg_win, text=f"Damaged Parts: {dmg['Damaged Parts']}", font=("Arial", 12), justify="left").pack(pady=10)
        tk.Button(win, text="View Damage Details", bg="red", fg="white", command=show_damage_details).pack(pady=10)

    if spec:
        tk.Label(win, text=f"\nSpecifications:\nEngine CC: {spec['Engine CC']}\nHorsepower: {spec['Horsepower']}\nTorque: {spec['Torque']}\nSeating: {spec['Seating Capacity']}", justify="left").pack(pady=5)

    def show_owner_details():
        owner_win = tk.Toplevel(win)
        owner_win.title("Previous Owners")
        owner_win.geometry("480x250")
        if not owner:
            tk.Label(owner_win, text="No previous owners found.", font=("Arial", 12)).pack(pady=20)
            return
        cols = ["Owner Name", "Phone", "Address", "Ownership Duration"]
        tree = ttk.Treeview(owner_win, columns=cols, show="headings", height=8)
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=110)
        for o in owner:
            tree.insert("", tk.END, values=[o[c] for c in cols])
        tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def show_location():
        loc_win = tk.Toplevel(win)
        loc_win.title("Car Location")
        loc_win.geometry("400x200")
        if not loc:
            tk.Label(loc_win, text="Location details not found.").pack(pady=20)
        else:
            tk.Label(loc_win, text=f"Lot: {loc['Lot Number']}\nStorage Facility: {loc['Storage Facility']}", font=("Arial", 12), justify="left").pack(pady=30)

    tk.Button(win, text="View Previous Owners", bg="blue", fg="white", command=show_owner_details).pack(pady=5)
    tk.Button(win, text="View Location", bg="purple", fg="white", command=show_location).pack(pady=5)
    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)

# ==========================================================
#   APP START
# ==========================================================
start_app()
root.mainloop()