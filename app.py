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
    """
    Endpoint POST para configurar o volume de um dispositivo (veículo).
    Recebe dados de placa e volume via JSON e armazena as configurações em memória.
    """
   
    configuracoes_dispositivos[config.placa.upper()] = config.volume_alerta

    return {
        "mensagem": f"Configuração salva: {config.placa.upper()} com volume {config.volume_alerta}."
    }

@app.get("/api/dispositivos/configuracoes")
async def listar_configuracoes():
    """
    Endpoint GET para listar todas as configurações de volume armazenadas.
    Retorna um dicionário com a placa como chave e o volume como valor.
    """
    return configuracoes_dispositivos