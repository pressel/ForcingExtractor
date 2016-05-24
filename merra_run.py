from merra import Merra
def main():

    lat = -20
    lon = 250.0 - 360.0

    md = Merra(1, 6, 2014, lat, lon)

    return


if __name__ == '__main__':
    main()

