from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI()

configuracoes_dispositivos: Dict[str, int] = {}

class ConfiguracaoVolume(BaseModel):
    placa: str = Field(..., example="ABC1234")
    volume_alerta: int = Field(..., ge=0, le=100, example=50)

@app.post("/api/dispositivos/configurar")
async def configurar_dispositivo(config: ConfiguracaoVolume):
    configuracoes_dispositivos[config.placa.upper()] = config.volume_alerta

    return {
        "mensagem": f"Configuração salva: {config.placa.upper()} com volume {config.volume_alerta}."
    }

@app.get("/api/dispositivos/configuracoes")
async def listar_configuracoes():
    return configuracoes_dispositivos