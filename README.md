# Barbeque Nation Agent System

## Hosted APIs
- Knowledge Base: http://localhost:8000/property-info/?city=delhi&question=timing

## Phone Number (if applicable)
+91-XXXXXXX (dummy)

## Post Call Analysis (Bonus)
TBD

## Chatbot Link (Bonus)
TBD
## 🔍 Knowledge Base API (800-token limit)

Base URL: http://localhost:8000

### GET /info/
- Description: Get relevant info based on query
- Params: `query` — e.g. `booking_policy`, `menu`, etc.

### GET /topics/
- Lists all available topics in the KB

### Sample:
GET /info/?query=menu

## Documentation
This repo contains a state machine chatbot for Barbeque Nation, powered by:
- FastAPI for Knowledge Base API
- Text-based Python State Machine
