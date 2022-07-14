import json
from pathlib import Path


def load_db(arquivo_db: Path) -> dict:
    """Carrega um arquivo .JSON e retorna um dicionário."""
    try:
        return json.load(open(arquivo_db, "r", encoding="utf-8"))
    except FileNotFoundError:
        print(f"Não foi possível abrir o arquivo {arquivo_db}.")
