import json
import os
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

_CERTS_PATH = Path(__file__).resolve().parent / "static" / "certificados.json"


def _load_certificates():
    """Curated cert list for the de-emphasized education section."""
    try:
        with _CERTS_PATH.open(encoding="utf-8") as fh:
            certs = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return []
    # Prefer formation + core language certs; keep the list short for recruiters.
    preferred = {
        "Formação HTML e CSS",
        "Javascript: explorando a linguagem",
        "Python: avançando na linguagem",
        "Python: Avançando na orientação a objetos",
        "React Native: Criando um app",
        "CSS: Dispondo elementos com Flexbox e Grid",
    }
    curated = [c for c in certs if c.get("nome_curso") in preferred]
    return curated or certs[:6]


@app.route("/")
def homepage():
    return render_template("homepage.html", certificates=_load_certificates())


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0").lower() in {"1", "true", "yes"}
    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("PORT") or os.environ.get("FLASK_RUN_PORT") or "5000")
    app.run(host=host, port=port, debug=debug)
