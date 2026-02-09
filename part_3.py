user_input = input("Enter motor speed")
try:
    motor_speed = int(user_input)
    print(f"Motor speed set to {motor_speed}")
except ValueError:
    print("Error: Corrupted Signal. Maintining current speed.")

def get_coordinates():
    while True:
        try:
            x = float(input("Enter X coordinate: "))
            y = float(input("Enter Y coordinate: "))
            return x, y
        except ValueError:
            print("Error: Corrupted Signal. Please enter valid coordinates.")
    