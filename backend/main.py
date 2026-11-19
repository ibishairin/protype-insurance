"""Demo plan catalog API for the HKS Insurance Advisory portal prototype."""
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HKS Insurance Advisory Plan Discovery API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCTS = [
    {"id": "young-star", "name": "Young Star", "tagline": "A head start on a healthier future.", "category": "Young adults", "price": 612, "cover": 1_000_000, "cover_label": "₹10 lakh", "highlight": "Built for your next chapter", "features": ["Automatic restoration of cover", "Wellness rewards", "No claim bonus"], "accent": "blue", "badge": "POPULAR"},
    {"id": "family-health", "name": "Family Health Optima", "tagline": "One plan that looks after everyone.", "category": "Families", "price": 984, "cover": 1_500_000, "cover_label": "₹15 lakh", "highlight": "Made for the whole family", "features": ["Shared family cover", "Automatic restoration", "Annual health check-up"], "accent": "teal", "badge": "FAMILY PICK"},
    {"id": "red-carpet", "name": "Senior Citizens Red Carpet", "tagline": "Thoughtful cover for your golden years.", "category": "Senior care", "price": 1280, "cover": 1_000_000, "cover_label": "₹10 lakh", "highlight": "Care that grows with you", "features": ["Designed for seniors", "Hospitalisation cover", "Optional co-pay choices"], "accent": "purple", "badge": "SENIOR CARE"},
    {"id": "comprehensive", "name": "Comprehensive Health", "tagline": "Everyday cover with room to grow.", "category": "Individuals", "price": 758, "cover": 2_000_000, "cover_label": "₹20 lakh", "highlight": "More cover, more confidence", "features": ["In-patient hospitalisation", "Day-care procedures", "Recharge benefit"], "accent": "gold", "badge": "WIDE COVER"},
    {"id": "assure", "name": "Star Assure", "tagline": "Flexible protection for changing needs.", "category": "Families", "price": 1125, "cover": 2_500_000, "cover_label": "₹25 lakh", "highlight": "Flexible family protection", "features": ["Multiple cover options", "Restore benefit", "Wellness services"], "accent": "coral", "badge": "FLEXIBLE"},
    {"id": "young-star-neo", "name": "Young Star Neo", "tagline": "More health. More dreams. A brighter tomorrow.", "category": "Young adults", "price": 699, "cover": 1_500_000, "cover_label": "₹15 lakh", "highlight": "Designed for tomorrow’s achievers", "features": ["Freeze your age option", "Future Shield benefit", "Star THRIVE wellness"], "accent": "blue", "badge": "NEW GENERATION"},
]


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "star-health-plan-catalog"}


@app.get("/api/categories")
def categories():
    return ["All plans", *dict.fromkeys(product["category"] for product in PRODUCTS)]


@app.get("/api/products")
def products(
    category: str | None = Query(default=None),
    q: str | None = Query(default=None, min_length=1),
    sort: str = Query(default="recommended", pattern="^(recommended|price-low|cover-high)$"),
):
    """Browse and filter the illustrative insurance plan catalog."""
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
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Plan not found")
