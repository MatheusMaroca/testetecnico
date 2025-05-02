import requests
import asyncio
import aiohttp
import nest_asyncio

nest_asyncio.apply()

API_URL = "http://127.0.0.1:8000/api/dispositivos/configurar"

async def enviar_comando(placa, volume):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, json={"placa": placa, "volume_alerta": volume}) as response:
                print(f"{placa}: {response.status} - {await response.json()}")
    except Exception as e:
        print(f"Erro ao enviar para {placa}: {e}")

async def processar_veiculos_paralelamente(veiculos):
    tasks = [enviar_comando(v["placa"], v["volume"]) for v in veiculos]
    await asyncio.gather(*tasks)

veiculos = [
    {"placa": "ABC1234", "volume": 50},
    {"placa": "DEF5678", "volume": 30},
]

asyncio.run(processar_veiculos_paralelamente(veiculos))


def ajustar_volume_veiculo(placa: str, volume: int):

    
    if not placa.isalnum() or len(placa) != 7:
        print(f"Placa inválida: {placa}")
        return f"Placa inválida: {placa}"
    if not (0 <= volume <= 100):
        print(f"Volume fora do intervalo: {volume}")
        return f"Volume fora do intervalo: {volume}"

    payload = {
        "placa": placa.upper(),
        "volume_alerta": volume
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            return f"✅ {placa}: Volume ajustado para {volume}"
    except Exception as e:
        return f"❌ Erro de conexão: {str(e)}"
    

 
def enviar_comando(placa, volume): 
    
    if not placa.isalnum() or len(placa) != 7:
        print(f"Placa inválida: {placa}")
        return
    if not (0 <= volume <= 100):
        print(f"Volume inválido: {volume}")
        return
    try:
        response = requests.post(API_URL, json={"placa": placa, "volume_alerta": volume})
        print(f"{placa}: {response.status_code} - {response.json()}")
    except requests.RequestException as e:
        print(f"Erro ao enviar para {placa}: {e}")

def processar_veiculos(veiculos):
    for veiculo in veiculos:
        placa = veiculo["placa"].strip().upper()
        volume = veiculo["volume"]
        enviar_comando(placa, volume)


        
