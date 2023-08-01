import time
import itertools
import logging

class Tractor:
    _ID = itertools.count()

    def __init__(self, tractor_type, fuel_status=20):
        self.id = next(self._ID)
        self.tractor_type = tractor_type
        self.fuel_status = fuel_status
        self.implement_type = None
        self.implement_type
        self.status = "On"

    def run(self):
        self.status = "Working"
        while self.status == "Working":
            if self.fuel_status > 10:
                self.fuel_status = self.fuel_status - 1
                print(f"Tractor {self.id} is running. Fuel status: {self.fuel_status}%")
                time.sleep(1)
                if self.fuel_status == 10:
                    logging.warning("Low fuel! The tractor will stop soon.")

            else:
                print(f"Tractor {self.id} has run out of fuel.")
                self.stop()
        return self.status

    def stop(self):
        if self.status == "Off" or self.status == "Stopped":
            print("Tractor is already stopped.")
        else:
            print("Stopping the tractor...")
            self.status = "Stopped"
            print("Tractor has stopped.")
    
    def attach_implement(self, implement):
        self.implement_type = implement

    def change_implement(self, new_implement):
        self.implement_type = new_implement

