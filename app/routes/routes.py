from fastapi.routing import APIRouter

from app.service.calculate_service import CalculateInkService
from app.schema.room_schema import Measurements


router = APIRouter()


@router.post("",
        summary="Operação responsável por calcular a quantidade de tinta necessária")
def calculate_quantity_ink(infos: Measurements):
        calculate_ink_service = CalculateInkService()
        calculation = calculate_ink_service.calculate_quantity_ink(infos)

        if calculation:
                return calculation
        return {'Message': 'Error calculate quantity ink'}
