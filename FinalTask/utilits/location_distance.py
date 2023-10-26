from math import sin, cos, sqrt, atan2, radians


class LocationDistance:
    def __init__(self):
        """Initialize a LocationDistance instance with the approximate radius of Earth."""
        self.R = 6373.0

    def location_meter(self, latitude_from, longitude_from, latitude_to, longitude_to):
        """Calculate the distance in kilometers between two locations using the Haversine formula.

        Args:
            latitude_from (float): Latitude of the starting location.
            longitude_from (float): Longitude of the starting location.
            latitude_to (float): Latitude of the destination location.
            longitude_to (float): Longitude of the destination location.

        Returns:
        float: The distance between the two locations in kilometers.
        """
        lat1 = radians(float(latitude_from))
        lon1 = radians(float(longitude_from))
        lat2 = radians(float(latitude_to))
        lon2 = radians(float(longitude_to))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        # haversine formula used for measuring distance between two locations
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = self.R * c

        return distance
