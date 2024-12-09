from unittest.mock import AsyncMock, patch
import pytest
from httpx import AsyncClient
from app.server.app import app

@pytest.mark.asyncio
@patch("app.server.database.get_accounts_from_db", new_callable=AsyncMock)
async def test_get_accounts(mock_get_accounts_from_db):
    """Test avec une base de données simulée"""
    mock_get_accounts_from_db.return_value = [{"id": 1, "name": "Mocked Account"}]
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/accounts/")
    
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Mocked Account"}]