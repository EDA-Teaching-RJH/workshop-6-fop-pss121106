rover_status = ["Battery: 100%", "Heater: Off", "Camera: On"]
current_status = rover_status[0]
print(current_status)

print("The rover is moving and conditions are changing.")
rover_status[0] = "Battery: 85%"
print(rover_status[0])
rover_status[1] = "Heater: On"
print(rover_status[1])
rover_status[2] = "Camera: Off"
rover_status.append("Speed: 5")
print("Here is the updated rover status:" , current_status)

mission_log = [{"site": "Site Crater A", "radiator": "Radiator: Low", "water": "Water: False"}, {"site": "Site B", "radiator": "Radiator: High", "water": "Water: True"}]

for site in mission_log:
    print(f"Site: {site['site']}, Radiation: {site['radiator']}")