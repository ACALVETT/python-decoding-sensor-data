from house_info import HouseInfo
from datetime import date


class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2  # in watts
    ENERGY_BITS = 0x0F0

    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy & self.ENERGY_BITS  # mask ENERGY bits
        energy = energy >> 4  # shift right
        return energy

    def _convert_data(self, data):
        recs = []
        for rec in data:
            # Convert string of hex into actual integers based 10
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    def calculate_energy_usage(self, data):
        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
        return total_energy