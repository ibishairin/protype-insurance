# HKS Insurance Advisory plan discovery portal prototype

A responsive React and FastAPI prototype for people exploring health insurance options with HKS Insurance Advisory. It is a public plan discovery experience, not a policyholder account or administration system.

## Frontend

```powershell
npm install
npm run dev
```

Open the Vite URL (usually `http://localhost:5173`). Visitors can browse plans by audience, search plan names and benefits, sort by starting premium or cover, open plan details, shortlist plans, compare up to three options, and open a callback enquiry popup.

## API

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
uvicorn backend.main:app --reload --port 8000
```

The API provides `GET /api/health`, `GET /api/categories`, `GET /api/products`, and `GET /api/products/{product_id}`. The products endpoint supports `category`, `q`, and `sort` query parameters. Example: `/api/products?category=Families&sort=price-low`.

## Prototype data

Product names, benefits, and premium figures are illustrative UI data and should not be treated as policy terms, quotes, or an offer of insurance. Replace these samples with approved product catalog and pricing data before publishing. The callback popup validates contact details in the browser but does not transmit or store them. Social icons currently link to the general Instagram, WhatsApp, and Facebook home pages; replace those URLs with HKS account links when available.
