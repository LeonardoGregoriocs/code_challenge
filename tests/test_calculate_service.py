from app.schema.room_schema import Measurements, RoomSchema
from app.service.calculate_service import CalculateInkService


def test_calculate_ink_service():

    room_schema = RoomSchema(
        wall_height = 5.0,
        wall_length = 3.0,
        amount_of_doors = 0,
        amount_of_windows = 0
    )

    measurements = Measurements(
        measurements = [room_schema, room_schema, room_schema, room_schema]
    )

    calculate_ink_service = CalculateInkService()
    result = calculate_ink_service.calculate_quantity_ink(measurements)

    expected = {
        'Total Measuarements': '60m2',
        'Gallon 0.5': 4.0,
        'Gallon 18': 0,
        'Gallon 2.5': 0,
        'Gallon 3.6': 3
    }

    assert result == expected

def test_calculate_ink_service_when_measurements_is_invalid():
    room_schema = RoomSchema(
        wall_height = 0.0,
        wall_length = 0.0,
        amount_of_doors = 0,
        amount_of_windows = 0
    )

    measurements = Measurements(
        measurements = [room_schema, room_schema, room_schema, room_schema]
    )

    calculate_ink_service = CalculateInkService()
    result = calculate_ink_service.calculate_quantity_ink(measurements)

    assert result == {'Message': 'Non-standard measurements'}
