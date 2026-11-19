"""Illustrative cross-category insurance catalog for the HKS portal prototype."""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HKS Insurance Advisory Plan Discovery API", version="1.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCTS = [
    {"id": "young-star", "name": "Young Star Health", "tagline": "A head start on a healthier future.", "category": "Health", "price": 612, "cover": 1_000_000, "cover_label": "₹10 lakh", "coverage_label": "Health cover up to", "features": ["Hospitalisation protection", "Wellness services", "Restoration options"], "accent": "blue", "badge": "POPULAR"},
    {"id": "family-health", "name": "Family Health Cover", "tagline": "One plan to explore for the whole family.", "category": "Health", "price": 984, "cover": 1_500_000, "cover_label": "₹15 lakh", "coverage_label": "Health cover up to", "features": ["Cover for family members", "Hospitalisation protection", "Preventive care options"], "accent": "teal", "badge": "FAMILY PICK"},
    {"id": "life-secure", "name": "Life Secure", "tagline": "Explore a financial safety net for loved ones.", "category": "Life", "price": 540, "cover": 5_000_000, "cover_label": "₹50 lakh", "coverage_label": "Life cover up to", "features": ["Life cover options", "Flexible policy terms", "Add-on choices available"], "accent": "purple", "badge": "LIFE COVER"},
    {"id": "motor-protect", "name": "Motor Protect", "tagline": "Cover options for the journeys you take.", "category": "Motor", "price": 790, "cover": 1_000_000, "cover_label": "₹10 lakh", "coverage_label": "Vehicle cover up to", "features": ["Own-damage cover options", "Third-party cover options", "Roadside assistance options"], "accent": "gold", "badge": "ON THE ROAD"},
    {"id": "travel-secure", "name": "Travel Secure", "tagline": "Explore protection for trips near and far.", "category": "Travel", "price": 320, "cover": 5_000_000, "cover_label": "₹50 lakh", "coverage_label": "Trip cover up to", "features": ["Emergency medical cover options", "Trip disruption options", "Baggage protection options"], "accent": "coral", "badge": "TRAVEL COVER"},
    {"id": "home-protect", "name": "Home Protect", "tagline": "Cover options for the place you call home.", "category": "Home", "price": 460, "cover": 7_500_000, "cover_label": "₹75 lakh", "coverage_label": "Home cover up to", "features": ["Structure protection options", "Contents cover options", "Natural event cover options"], "accent": "blue", "badge": "HOME COVER"},
]


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "hks-insurance-catalog"}


@app.get("/api/categories")
def categories():
    return ["All plans", *dict.fromkeys(product["category"] for product in PRODUCTS)]


@app.get("/api/products")
def products(
    category: str | None = Query(default=None),
    q: str | None = Query(default=None, min_length=1),
    sort: str = Query(default="recommended", pattern="^(recommended|price-low|cover-high)$"),
):
    """Browse and filter the illustrative multi-category catalog."""
    results = PRODUCTS
    if category and category != "All plans":
        results = [item for item in results if item["category"].lower() == category.lower()]
    if q:
        term = q.lower()
        results = [item for item in results if term in " ".join([item["name"], item["tagline"], item["category"], *item["features"]]).lower()]
    if sort == "price-low":
        results = sorted(results, key=lambda item: item["price"])
    elif sort == "cover-high":
        results = sorted(results, key=lambda item: item["cover"], reverse=True)
    return results


@app.get("/api/products/{product_id}")
def product_detail(product_id: str):
    for item in PRODUCTS:
        if item["id"] == product_id:
            return item
    raise HTTPException(status_code=404, detail="Plan not found")
