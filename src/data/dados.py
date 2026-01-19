import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.json"


def carregar_dados():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

