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
        self.ndays = ndays



        self.datetime_date = datetime.date(self.year, self.month, self.day)

        path = self.construct_path('http://goldsmr2.sci.gsfc.nasa.gov:80/opendap/MERRA/MAT1NXFLX.5.2.0', 'MERRA300.prod.assim.tavg1_2d_flx_Nx.', 0)

        dataset = open_url(path)
        self.native_lat = dataset['YDim'][:]
        self.native_lon = dataset['XDim'][:]


        self.lat_idx_native = np.where(np.min(np.abs(self.native_lat - lat)) == np.abs(self.native_lat - lat))[0][0]
        self.lon_idx_native = np.where(np.min(np.abs(self.native_lon - lon)) == np.abs(self.native_lon - lon))[0][0]


        self.lat_actual = self.native_lat[self.lat_idx_native]
        self.lon_actual = self.native_lon[self.lon_idx_native]

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

        #Get the sensible and latent heat fluxes
        lhf = np.array([], dtype=np.double)
        evap = np.array([], dtype=np.double)
        shf = np.array([], dtype=np.double)
        qlml = np.array([], dtype=np.double)
        tlml = np.array([], dtype=np.double)
        ulml = np.array([], dtype=np.double)
        vlml = np.array([], dtype=np.double)
        precip = np.array([], dtype=np.double)
        time = np.array([], dtype=np.double)


        for i in range(self.ndays):
            path = self.construct_path('http://goldsmr2.sci.gsfc.nasa.gov:80/opendap/MERRA/MAT1NXFLX.5.2.0',
                                       'MERRA300.prod.assim.tavg1_2d_flx_Nx.', i)
            dataset = open_url(path)


            #lhf = np.append(lhf, dataset['EFLUX'][:,self.lat_idx_native, self.lon_idx_native])
            #shf = np.append(shf, dataset['HFLUX'][:,self.lat_idx_native, self.lon_idx_native])
            #evap = np.append(evap, dataset['EVAP'][:,self.lat_idx_native, self.lon_idx_native])
            #ulml = np.append(ulml, dataset['ULML'][:, self.lat_idx_native, self.lon_idx_native])
            #vlml = np.append(vlml, dataset['VLML'][:, self.lat_idx_native, self.lon_idx_native])
            #qlml = np.append(qlml, dataset['QLML'][:, self.lat_idx_native, self.lon_idx_native])
            #tlml = np.append(tlml, dataset['TLML'][:, self.lat_idx_native, self.lon_idx_native])
            #precip = np.append(precip, dataset['PRECTOT'][:, self.lat_idx_native, self.lon_idx_native])

            #time = np.append(time, dataset['TIME'][:])

        #import pylab as plt
        #plt.plot(precip)
        #plt.show()


        return