import asyncio
from unittest.mock import patch, MagicMock

from scripts import processar_veiculos_paralelamente

@patch("scripts.aiohttp.ClientSession.post")
async def test_processar_veiculos_paralelamente(mock_post):
    mock_response = MagicMock()
    mock_response.status = 200
    mock_response.json.return_value = {"mensagem": "Configuração salva: ABC1234 com volume 50."}
    mock_post.return_value.__aenter__.return_value = mock_response

    veiculos = [
        {"placa": "ABC1234", "volume": 50},
        {"placa": "DEF5678", "volume": 30},
    ]

    await processar_veiculos_paralelamente(veiculos)

    mock_post.call_count==2
