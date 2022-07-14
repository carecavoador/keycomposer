import db
from pathlib import Path

DB = Path("dicionario.json")
dicionario = db.load_db(DB)
abreviacoes = dicionario["abreviacoes"]
