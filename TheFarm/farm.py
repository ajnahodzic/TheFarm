from Implement import Sprayer
from Implement import Mower
from Implement import Driller


class Farm:
    def __init__(self, name, farm_type, season,location, num_tractors):
        self.name = name
        self.farm_type = farm_type
        self.location = location
        self.num_tractors = num_tractors
        self.season = season
        self.tractors = []

    def get_working_tractors(self):
        working_tractors = [tractor for tractor in self.tractors if tractor.status == "Working"]
        return working_tractors

    def generate_farm_id(self):
        farm_id = f"{self.name}_{self.location}"
        print(farm_id)
        return farm_id

    def add_tractor(self, tractor):
        if len(self.tractors) < self.num_tractors:
            self.tractors.append(tractor)
            print(f"{tractor.tractor_type} tractor added to the farm.")
        else:
            print("Farm has reached the maximum capacity for tractors.")

    def remove_tractor(self, tractor_id):
        for tractor in self.tractors:
            if tractor.id == tractor_id:
                self.tractors.remove(tractor)
                print(f"{tractor.tractor_type} tractor removed from the farm.")
                return
        print("Tractor not found in the farm.")

    def get_seasonal_implement(self, season):
        if season == "summer":
            return Sprayer("water")
        elif season == "fall":
            return Mower()
        elif season == "winter":
            return Driller()
        elif season == "spring":
            return Sprayer("pesticides")
        else:
            return None

    def list_all_tractors_with_statuses(self):
        tractor_info = []
        for tractor in self.tractors:
            done_work_percentage = int(100-tractor.fuel_status)
            tractor_info.append({
                "Tractor Type": tractor.tractor_type,
                "Tractor Status": tractor.status,
                "Implement Type": tractor.implement_type.get_implement_type(),
                "Done Work Percentage": done_work_percentage
            })
        return tractor_info