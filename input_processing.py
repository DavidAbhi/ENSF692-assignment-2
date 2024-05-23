# input_processing.py
# ABHIJITH DAVID, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.


# ENSF 692 Car Vision Detector Processing Program

# Sensor class was defined with the attributes traffic light, pedestrian & vehicle.

class Sensor:
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian_detected = "no"
        self.vehicle_detected = "no"

    def update_traffic_light(self, color):
        if color in ["green", "yellow", "red"]:
            self.traffic_light = color
        else:
            print("Invalid traffic light color.")

    def update_pedestrian_status(self, status):
        if status in ["yes", "no"]:
            self.pedestrian_detected = status
        else:
            print("Invalid pedestrian status.")

    def update_vehicle_status(self, status):
        if status in ["yes", "no"]:
            self.vehicle_detected = status
        else:
            print("Invalid vehicle status.")

    def get_status(self):
        return {
            "traffic_light": self.traffic_light,
            "pedestrian_detected": self.pedestrian_detected,
            "vehicle_detected": self.vehicle_detected
        }

def user_input(sensor):
    while True:

        # Prompting the user for input

        print("Select an option:")
        print("1 to update the detected traffic light colour")
        print("2 to update whether a pedestrian is detected")
        print("3 to update whether a vehicle is detected")
        print("0 to end the program")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Program ended.")
                break
            elif choice == 1:
                color = input("Enter the traffic light color (green, yellow, red): ")
                sensor.update_traffic_light(color)
            elif choice == 2:
                pedestrian_status = input("Is a pedestrian detected? (yes or no): ")
                sensor.update_pedestrian_status(pedestrian_status)
            elif choice == 3:
                vehicle_status = input("Is a vehicle detected? (yes or no): ")
                sensor.update_vehicle_status(vehicle_status)
            else:
                print("Invalid option. Please try again.")
                continue

            # Determining the status from the user inputs retrieved

            status = sensor.get_status()
            if status['traffic_light'] == "red" or status['pedestrian_detected'] == "yes" or status['vehicle_detected'] == "yes":
                action_message = "STOP"
            elif status['traffic_light'] == "green" and status['pedestrian_detected'] == "no" and status['vehicle_detected'] == "no":
                action_message = "Proceed"
            elif status['traffic_light'] == "yellow" and status['pedestrian_detected'] == "no" and status['vehicle_detected'] == "no":
                action_message = "Caution"
            else:
                action_message = "STOP"

            # Printing the action message and the current status
            print(f"\n {action_message}\n")
            print(f"\n Traffic Light: {status['traffic_light']}, Pedestrian: {status['pedestrian_detected']}, Vehicle: {status['vehicle_detected']}\n")

        except ValueError:
            print("Invalid input. Please enter a number from 0 to 3.")

def main():
    sensor = Sensor()
    user_input(sensor)

if __name__ == '__main__':
    main()

