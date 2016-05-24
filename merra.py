import datetime
import numpy as np
from pydap.client import open_url

class Merra():

    def __init__(self, day, month, year, lat, lon, ndays):

        self.day = day
        self.month = month
        self.year  = year
        self.lat = lat
        self.lon = lon



        self.datetime_date = datetime.date(self.year, self.month, self.day)

        path = self.construct_path('http://goldsmr2.sci.gsfc.nasa.gov:80/opendap/MERRA/MAT1NXFLX.5.2.0', 'MERRA300.prod.assim.tavg1_2d_flx_Nx.', 0)

        dataset = open_url(path)
        self.native_lat = dataset['YDim'][:]
        self.native_lon = dataset['XDim'][:]


        self.lat_idx_native = np.where(np.min(np.abs(self.native_lat - lat)) == np.abs(self.native_lat - lat))[0][0]
        self.lon_idx_native = np.where(np.min(np.abs(self.native_lon - lon)) == np.abs(self.native_lon - lon))[0][0]


        self.lat_actual = self.native_lat[self.lat_idx_native]
        self.lat_actual = self.

        return


    def construct_path(self, dataroot, filename, delta_day):

        date = self.datetime_date + datetime.timedelta(days=delta_day)
        date =  str(date.isoformat())
        day = date[8:10]
        month = date[5:7]
        year = date[:4]


        full_path =  dataroot + '/'  + str(year)+ '/'
        full_path += str(month) + '/'
        full_path += filename + year + month + day + '.hdf'


        return full_path


    def surface_fluxes(self):

        #First get latent heat flux




        return