from unittest.mock import patch, MagicMock

from scripts import enviar_comando

@patch("scripts.requests.post")
def test_enviar_comando_valido(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"mensagem": "Configuração salva: ABC1234 com volume 50."}
    mock_post.return_value = mock_response

   
    enviar_comando("ABC1234", 50)
    
    mock_post.assert_called_once_with(
        "http://127.0.0.1:8000/api/dispositivos/configurar",
        json={"placa": "ABC1234", "volume_alerta": 50}
    )