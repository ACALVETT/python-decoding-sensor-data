from house_info import HouseInfo

class TemperatureData(HouseInfo)

    def _convert_data(self,data):
        recs = []

        for rec in data:
            recs.append(int(rec,base=10))

        recs

        def get_data_by_area(self,rec_area = 0):
            recs = super(get_data_by_area("temperature",rec_area))