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

if __name__ == '__main__':
    main()

