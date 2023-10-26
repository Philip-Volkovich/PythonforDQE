from utilits.db_connection import DBConnection
from utilits.location_distance import LocationDistance


class AppRunner:
    def __init__(self):
        """Initialize an AppRunner instance."""
        pass

    def console_runner(self):
        """Run the console-based news feed application."""

        while True:
            print("\nThis app allows to calculate distance in km between two cities based om their "
                  "coordinates (latitude, longitude)")
            print("Select number to continue:")
            print("1. Calculate distance between two cities")
            print("2. Exit")
            main_choice = input("Enter your choice: ")

            if main_choice == '1':
                city_from = input("Enter the name of the first city (e.g. 'Minsk'): ")
                city_to = input("Enter the name of the second city (e.g.'Borisov'): ")

                db_record = DBConnection()
                db_record.db_create()
                if db_record.db_select_city_record(f'{city_from}') != 'None':
                    latitude_from = db_record.db_select_city_record(f'{city_from}', 'latitude')
                    longitude_from = db_record.db_select_city_record(f'{city_from}', 'longitude')
                else:
                    print(f"Requested city:{city_from} has not been found. Please add latitude and longitude")
                    latitude_from = input(f"Enter the latitude for {city_from} (format: dd.dddddd, e.g. 59.565857): ")
                    longitude_from = input(f"Enter the longitude for {city_from} (format: dd.dddddd, e.g. 59.565857): ")
                    db_record.db_insert('city,latitude,longitude', f"'{city_from}', {latitude_from}, "
                                                                   f"{longitude_from}")

                if db_record.db_select_city_record(f'{city_to}') != 'None':
                    latitude_to = db_record.db_select_city_record(f'{city_to}', 'latitude')
                    longitude_to = db_record.db_select_city_record(f'{city_to}', 'longitude')
                else:
                    print(f"Requested city:{city_to} has not been found. Please add latitude and longitude")
                    latitude_to = input(f"Enter the latitude for {city_to} (format: dd.dddddd, e.g. 59.565857): ")
                    longitude_to = input(f"Enter the longitude for {city_to} (format: dd.dddddd, e.g. 59.565857): ")
                    db_record.db_insert('city,latitude,longitude', f"'{city_to}', {latitude_to}, "
                                                                   f"{longitude_to}")

                new_distance = LocationDistance()
                result = round(new_distance.location_meter(latitude_from, longitude_from, latitude_to, longitude_to), 2)

                print(f"Distance between {city_from} and {city_to}: {result} km")

            elif main_choice == '2':
                print('Exiting the program')
                break

            else:
                print('Not valid choice. Please choose 1 or 2')


if __name__ == "__main__":
    run_app = AppRunner()
    run_app.console_runner()
