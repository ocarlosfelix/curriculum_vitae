# Carlos Felix — Curriculum Vitae

Senior full-stack CV served with **Flask + Jinja**.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

If `ensurepip` is missing on the host, use [uv](https://github.com/astral-sh/uv):

```bash
uv venv .venv
uv pip install -r requirements.txt --python .venv/bin/python
```

## Run

Default (debug **off**):

```bash
python app.py
# → http://127.0.0.1:5000/
```

Or with the Flask CLI:

```bash
export FLASK_APP=app.py
flask run
# → http://127.0.0.1:5000/
```

### Preview / bind all interfaces

```bash
export FLASK_RUN_HOST=0.0.0.0
export PORT=5000          # or FLASK_RUN_PORT
python app.py
```

### Local debug (optional)

```bash
export FLASK_DEBUG=1
python app.py
```

`debug` is **off by default**. Never force `debug=True` in preview or production.

## Smoke checklist

1. Open `/` — expect HTTP 200 and the name **Carlos Felix**.
2. Confirm sections: Summary, Skills, Experience (K-12 assessment, industrial simulation, Limpei, Earlier), Recommendation, Education.
3. Mailto, GitHub, and LinkedIn links resolve.
4. Phone is **not** shown. Alura course titles are **not** listed.
5. Static CSS loads (reset, then styles); no broken `../static/...` paths.
6. Footer year is **2026** or later.

## Structure contract (Pacote B)

Semantic classes owned by Pacote A for visual polish:

| Class | Role |
|-------|------|
| `.header` | Identity + contact |
| `.summary` | Senior headline + short summary |
| `.skills` | Skills emphasis |
| `.experience` | Product engagements |
| `.recommendation-quote` | Ray pull-quote |
| `.recommendation` | Full recommendation letter |
| `.education` | De-emphasized certs / languages |
| `.footer` | Footer (year ≥ 2026) |

Do **not** invent metrics, employers, or titles. Evidence used for the current copy:

- Product titles use the plain language Ray asked for on 2026-11-02. “Eddo Learning” stays as the employer on the role line and on the letter, not as the name of the product.
- K-12 assessment dates follow Carlos’s commits in the product repo (Aug 2025–present). Bullets describe outcomes. Tool names sit on the tech line.
- Industrial simulation dates follow Carlos’s commits on `eddo-ai/ffl-project` (24 Nov 2025–20 Apr 2026) and `eddo-ai/oemffl-roleplay-agent`. The page does not use the internal name. The “spinoff CEO” line stays off. Nothing in the letter or the repos supports it.
- Limpei follows the store repo (first commit Aug 2026; catalog, register, service orders, electronic invoices).
- The letter is Ray’s Slack text, in his three paragraphs. Title on the role line is “Full-stack engineer”; “Senior” is the headline.
- `static/certificados.json` stays in the repo as the cert archive and is not rendered. Intro course titles read as junior on a senior CV.

## Secrets

No secrets belong in this repo. Keep env-only configuration for host/port/debug.
