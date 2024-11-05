from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import uvicorn

# Carregar o modelo
try:
    model = tf.keras.models.load_model('modelo_fraude.h5')
    print("Modelo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o modelo: {str(e)}")
    print("Certifique-se de que o modelo está na pasta correta e no formato correto.")

app = FastAPI(
    title="API de Detecção de Fraudes",
    description="API para previsão de fraudes usando features temporais e fixas",
    version="1.0.0"
)

class PredictionInput(BaseModel):
    features_temporais: list
    features_fixas: list

    class Config:
        json_schema_extra = {
            "example":{
    "features_temporais": [[[0.1, 0.2, 0.3, 0.4, 0.5] * 5 + [0.6] for _ in range(7)]],
    "features_fixas": [[1.0, 0.5, 0.8, 0.2, 0.9]]
}
        }

@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        # Converter inputs para numpy arrays
        temp_features = np.array(input_data.features_temporais, dtype=np.float32)
        fixed_features = np.array(input_data.features_fixas, dtype=np.float32)
        
        # Log de debug para checar as formas dos arrays
        print(f"temp_features.shape: {temp_features.shape}")
        print(f"fixed_features.shape: {fixed_features.shape}")
        
        # Validar dimensões
        if temp_features.shape[1:] != (7, 26):
            raise HTTPException(
                status_code=400,
                detail=f"Features temporais devem ter formato (1, 7, 26), recebido {temp_features.shape}"
            )
        
        if fixed_features.shape[1:] != (5,):
            raise HTTPException(
                status_code=400,
                detail=f"Features fixas devem ter formato (1, 5), recebido {fixed_features.shape}"
            )

        # Fazer predição
        prediction = model.predict([temp_features, fixed_features])
        
        return {
            "prediction": float(prediction[0][0]),
            "fraud_probability": float(prediction[0][0]),
            "status": "success"
        }
    
    except Exception as e:
        print(f"Erro ao fazer predição: {str(e)}")  # Log de erro detalhado
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao fazer predição: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)