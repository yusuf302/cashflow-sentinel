# CashFlow Sentinel

An autonomous financial-diagnosis agent for small businesses in emerging markets.

CashFlow Sentinel reads a business's transaction ledger, builds a financial picture,
detects early-warning problems, investigates each problem by drilling into the ledger,
quantifies the impact, recommends operational actions, ranks priorities, and writes a
one-page management summary.

**Track:** Agentic Finance · **Audience:** African SMEs & founders (cash-first
businesses running on M-Pesa / bank transfers / cash).

## The agentic workflow

The agent runs a visible `READ → ANALYZE → DETECT → INVESTIGATE → QUANTIFY →
RECOMMEND → PRIORITIZE → SUMMARIZE` loop. Every step lands in a trace that the UI
renders live, so the autonomous decision-making is observable rather than hidden.

## Data

All data is **synthetic and generated locally** by `seed_data.py` — no real customer
data, no live bank feeds. The default dataset is a Nairobi bakery (Kenyan Shilling,
KES) with realistic, seeded financial problems.

## Stack

- Python 3 (standard library for data/analysis — no pandas)
- FastAPI + Uvicorn (API)
- HTML/CSS/vanilla JS + Chart.js (frontend, no build step)

## Run

```sh
py -3 -m pip install -r requirements.txt
py -3 seed_data.py                # generate data/bakery_ledger.csv
py -3 -m uvicorn main:app --port 8000
```

Then open http://localhost:8000/.

## Structure

```
app/          analysis, detection, investigation, prioritization, summarization
data/         generated ledger CSV (git-ignored)
static/       index.html, styles.css, app.js
tests/        automated tests for the financial engine
seed_data.py  synthetic ledger generator
main.py       FastAPI entry point
```
