from unittest.mock import patch, MagicMock
from scripts import ajustar_volume_veiculo

@patch("scripts.requests.post")
def test_placa_valida(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    resultado = ajustar_volume_veiculo("ABC1234", 40)

    assert "✅ ABC1234" in resultado