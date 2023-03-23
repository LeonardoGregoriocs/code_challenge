from math import ceil
from fastapi.responses import PlainTextResponse

from app.schema.room_schema import Measurements
from utils.constants import MAXIMUM_SIZE, MINIMUM_SIZE, WINDOWN, DOOR, GALLON_EIGHTEN, GALLON_THREE_POINT_SIX, GALLON_TWO_POINT_FIVE, GALLON_ZERO_POINT_FIVE


class CalculateInkService():
    def __init__(self) -> None:
        pass

    def calculate_quantity_ink(self, infos: Measurements):
        try:
            measurements_obj = infos.dict()
            measurements = []

            for measurement in measurements_obj['measurements']:
                square_meter = self.get_square_meter_from_the_wall(measurement)

                if type(square_meter) is tuple:
                    return square_meter[1]

                measurements.append(square_meter)

            if not len(measurements) == 4:
                return PlainTextResponse(str('Invalid data'), status_code=400)

            quantity_ink_obj = self.calculate_quantity_of_gallons(measurements)

            return quantity_ink_obj

        except Exception as err:
            print(f'Error the calculate quantity ink: {err}')

    def get_square_meter_from_the_wall(self, measurement):
        try:
            square_meter = measurement['wall_height'] * measurement['wall_length']

            square_meter_obj = self.discount_from_the_doors_and_windows(square_meter, measurement)

            if type(square_meter_obj) is tuple:
                return square_meter_obj

            if square_meter_obj > MINIMUM_SIZE and square_meter_obj < MAXIMUM_SIZE:
                return square_meter_obj
            else:
                return None, {'Message': 'Non-standard measurements'}

        except Exception as err:
            print(f'Error the get square meter from the wall: {err}')

    def discount_from_the_doors_and_windows(self, square_meter_obj, measurement):
        try:
            quantity_doors = measurement['amount_of_doors']
            quantity_windows = measurement['amount_of_windows']

            quantity_doors_obj = quantity_doors * DOOR
            quantity_windows_obj = quantity_windows * WINDOWN

            square_meter = square_meter_obj - quantity_doors_obj - quantity_windows_obj

            total_meter_from_the_doors_and_windows = quantity_doors_obj + quantity_windows_obj

            if total_meter_from_the_doors_and_windows > (square_meter / 2):
                return None, {'Message': 'The total area of the doors and windows must be a maximum of 50 percentage of the wall area'}

            if quantity_doors >= 1:
                if measurement['wall_height'] < 2.20:
                    return None, {'Message': 'The height of walls with a door must be at least 30 centimeters greater than the height of the door.'}

            return square_meter

        except Exception as err:
            print(f'Error discount from the doors and windows: {err}')

    def calculate_quantity_of_gallons(self, measurements):
        total_measurements = (sum(measurements) / 5)

        gallon_eighteen = int(total_measurements / GALLON_EIGHTEN)
        rest = total_measurements - (gallon_eighteen * GALLON_EIGHTEN)

        gallon_three_point_six = int(rest / GALLON_THREE_POINT_SIX)
        rest = rest - (gallon_three_point_six * GALLON_THREE_POINT_SIX)

        gallon_two_point_five = int(rest / GALLON_TWO_POINT_FIVE)
        rest = rest - (gallon_two_point_five * GALLON_TWO_POINT_FIVE)

        gallon_zero_point_five = (ceil(rest) / GALLON_ZERO_POINT_FIVE)

        quantity_ink_obj = {
            'Total Measuarements': f'{sum(measurements).__round__()}m2',
            'Gallon 18': gallon_eighteen,
            'Gallon 3.6': gallon_three_point_six,
            'Gallon 2.5': gallon_two_point_five,
            'Gallon 0.5': gallon_zero_point_five
        }

        return quantity_ink_obj
