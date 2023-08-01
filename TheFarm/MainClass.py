from farm import Farm
from tractor import Tractor
import threading

class MainClass:
    def __init__(self):
        self.farm = None
        self.farm_name = "farm"
        self.season = ""
        self.num_dedicated_tractors = 0
        self.farm_location = (0, 0, 0, 0)
        self.farm_type = ""

    def input_data(self):
        self.farm_name = input("Enter the name of the farm: ")
        self.farm_type = input("Enter the type of the farm (Apples, Citrus, Grapes): ")
        self.season = input("Enter the season (winter, fall, summer, spring): ")
        self.num_dedicated_tractors = int(input("Enter the number of dedicated tractors (should be more than 3): "))
        x, y, h, w = [int(x) for x in input("Enter the location in map (x, y), height and width: ").split()]
        self.farm_location = (x, y, h, w)

    def assign_new_tractors(self):
       self.farm = Farm(self.farm_name, self.farm_type, self.season, self.farm_location, self.num_dedicated_tractors)
       for all in range(self.num_dedicated_tractors):
            tractor_type = input("Enter tractor type (John Deere or New Holland): ")
            fuel_status = int(input("Enter fuel status (0-100%): "))
            #fuel_status = 100
            #tractor_type = "John Deere"
            tractor = Tractor(tractor_type, fuel_status)
            self.farm.add_tractor(tractor)

    def run_tractors(self):
        threads = []
        running_tractors = self.farm.tractors[:3]

        # create thread for each running tractor
        for tractor in running_tractors:
            implement = self.farm.get_seasonal_implement(self.farm.season)
            tractor.attach_implement(implement)
            thread = threading.Thread(target=tractor.run)
            threads.append(thread)
            thread.start()

        # check if tractor has finished
        while True:
            for tractor in self.farm.tractors:
                if tractor.status == "Stopped":
                    free_implement = tractor.implement_type
                    next_ready_tractor = next(tractor for tractor in self.farm.tractors if tractor.fuel_status > 10)
                    next_ready_tractor.attach_implement(free_implement)
                    thread = threading.Thread(target=next_ready_tractor.run)
                    threads.append(thread)
                    thread.start()
                    thread.join()

    def stop_tractors(self):
        for tractor in self.farm.tractors:
            tractor.status = "Off"

    def start(self):
        self.input_data()
        self.assign_new_tractors()
        self.run_tractors()
        self.stop_tractors()

# Example usage:
main_instance = MainClass()
main_instance.start()
