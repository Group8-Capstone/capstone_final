from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import shutil

from services.fraud_service import FraudDetectionService

router = APIRouter()


@router.post('/api/predict/fraud')
async def predict_fraud(file: UploadFile = File(...)):

    temp_path = f'temp_{file.filename}'

    with open(temp_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    service = FraudDetectionService()

    result = service.predict(temp_path)

    return result