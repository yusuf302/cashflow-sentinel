# CashFlow Sentinel

**Agentic SME Financial Risk Monitor**

CashFlow Sentinel is a lightweight financial-risk monitoring MVP built for the **Global AI Hackathon — Powered by Mel** in the **Agentic Finance** track.

It turns transaction-level SME data into a concise management view: key cash-flow metrics, prioritized financial risks, numerical evidence, and practical operational actions.

> **Demo scenario:** a synthetic Nairobi bakery operating in Kenyan Shillings (KES) across M-Pesa, bank, and cash transactions.

## Why this matters

Many small businesses have transaction records but no dedicated finance team to continuously interpret them. Problems such as rising costs, customer concentration, and short-term cash deficits can therefore become serious before management acts.

CashFlow Sentinel is designed to shorten that gap between **data** and **decision**.

## What the MVP does

The dashboard provides:

- Total inflows and total outflows
- Net cash flow
- Revenue concentration
- Recent expense growth
- Monthly cash-flow trend
- Three prioritized financial risks (`P0`, `P1`, `P2`)
- Numerical evidence for each flagged risk
- One practical management action per risk
- A concise management summary

The final demo currently identifies risks such as an **inventory-cost surge**, **revenue concentration**, and a **monthly cash deficit**.

## Agentic workflow

CashFlow Sentinel demonstrates the following financial-triage loop:

`READ → DETECT → INVESTIGATE → RANK → RECOMMEND`

1. **Read** transaction-level business data.
2. **Detect** unusual or decision-relevant financial signals.
3. **Investigate** the underlying metrics and monthly patterns.
4. **Rank** the most important issues as P0, P1, and P2.
5. **Recommend** an operational response supported by numerical evidence.

The current hackathon MVP deliberately uses **deterministic analysis logic** rather than an external LLM API. This keeps the demo fast, reproducible, inexpensive, and reliable while still making the decision workflow visible to the user.

## Demo design

The application is a single-page fintech dashboard with:

- A light, minimalist executive interface
- KPI cards for rapid financial-health scanning
- A Chart.js monthly cash-flow visualization
- Color-coded priority cards for P0/P1/P2 risks
- A management brief designed for a non-finance founder or SME manager

## Data

All data is **synthetic**. No real customer or bank data is used.

`seed_data.py` generates a reproducible 12-month bakery ledger using a fixed random seed. The synthetic ledger contains:

- M-Pesa, bank, and cash transactions
- Retail and wholesale sales
- Inventory, rent, utilities, and miscellaneous expenses
- A large wholesale customer early in the year
- Gradually rising inventory costs
- A deliberately weak seasonal month

The generated CSV is written to:

```text
data/bakery_ledger.csv
