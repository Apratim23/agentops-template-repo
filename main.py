# main.py
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

knowledge_base = {
    "delhi": {
        "address": "Connaught Place, Delhi",
        "phone": "+91-1234567890",
        "faq": {
            "timing": "Open 12pm - 11pm",
            "menu": "Buffet includes veg/non-veg items, desserts, live counters"
        }
    },
    "bangalore": {
        "address": "Indiranagar, Bangalore",
        "phone": "+91-9876543210",
        "faq": {
            "timing": "Open 1pm - 10:30pm",
            "menu": "Buffet includes South Indian specialties"
        }
    }
}

@app.get("/property-info/")
def get_info(city: str, question: Optional[str] = None):
    city_data = knowledge_base.get(city.lower())
    if not city_data:
        return {"error": "City not found"}
    
    if question:
        answer = city_data["faq"].get(question.lower(), "FAQ not found.")
        return {"answer": answer}
    
    return city_data
