from fastapi import APIRouter
import requests
from app.database import authenticate, ODOO_URL

router = APIRouter()

@router.get("/clientes")
def obtener_clientes():
    """Consulta la lista de clientes desde Odoo"""
    cookies = authenticate()
    if not cookies:
        return {"error": "Autenticación fallida en Odoo"}

    url = f"{ODOO_URL}/web/dataset/call_kw/res.partner/search_read"
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "model": "res.partner",
            "method": "search_read",
            "args": [[]],
            "kwargs": {"fields": ["id",
