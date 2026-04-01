# LandScout Intelligence  
**AI-Orchestrated Land Investment Analysis System**

LandScout Intelligence is a hybrid AI system that compresses multi-hour land analysis into seconds by orchestrating LLM-based feature extraction with a deterministic multi-factor decision engine.

---

## MoJo Outcome

- **Input:** Street address (~30 seconds)  
- **Output:** Structured investment analysis (scoring + insights)  
- **Manual Equivalent:** ~2 hours of research  
- **System Runtime:** ~5 seconds  

**MoJo Score:** ~1,440x (Output / Human Time)

---

## System Architecture

The system is built on a core principle:

> **Delegate ambiguity to AI, and precision to deterministic systems**

### Pipeline Overview                    
                    
                    
                    ┌──────────────────────────────┐
                    │        User Input            │
                    │     (Street Address)         │
                    └──────────────┬───────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   LLM Extraction Layer       │
                    │ (Claude - Feature Parsing)   │
                    └──────────────┬───────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │  Structured Parcel Features  │
                    │  (Normalized Inputs)         │
                    └──────────────┬───────────────┘
                                   ↓
        ┌─────────────────────────────────────────────────────┐
        │        Deterministic Scoring Engine                 │
        │                                                     │
        │  ┌──────────────┐  ┌──────────────┐                │
        │  │ Growth       │  │ Infrastructure│               │
        │  └──────────────┘  └──────────────┘                │
        │  ┌──────────────┐  ┌──────────────┐                │
        │  │ Zoning       │  │ Market       │                │
        │  └──────────────┘  └──────────────┘                │
        │            ┌──────────────┐                        │
        │            │ Risk (Inverted)│                      │
        │            └──────────────┘                        │
        └────────────────────┬──────────────────────────────┘
                             ↓
                    ┌──────────────────────────────┐
                    │ Weighted Aggregation         │
                    │ + Confidence Estimation      │
                    └──────────────┬───────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │ Final Output                 │
                    │ Score + Breakdown + Tier     │
                    └──────────────────────────────┘


---

## Orchestration Design

### 1. LLM Extraction Layer (Ambiguity Handling)
- Processes unstructured address input  
- Extracts normalized parcel-level features  
- Handles incomplete or noisy data  

---

### 2. Deterministic Reasoning Engine (Core Intelligence)

Located in:  
`landscout/backend/app/services/scoring_engine.py`

This module serves as the **core decision system**.

#### Key Characteristics:

- **Multi-factor modeling (20+ signals):**
  - Growth (30%)
  - Infrastructure (25%)
  - Zoning & regulatory (20%)
  - Market dynamics (15%)
  - Risk factors (10%)

- **Non-linear transformations:**
  - Exponential decay (distance effects)
  - Logarithmic scaling (land scarcity)
  - Diminishing returns (income impact)

- **Risk-aware scoring:**
  - Explicit inversion of negative factors

- **Confidence estimation:**
  - Output reliability based on data completeness

- **Calibrated weights:**
  - Based on large-scale historical patterns
  - Designed to align with real-world investment outcomes

---

### 3. API Orchestration Layer

- Built with FastAPI (async)
- Coordinates extraction → scoring → response
- End-to-end latency: <5 seconds

---

## Example Output

```json
{
  "total_score": 78.4,
  "growth_score": 82.1,
  "infrastructure_score": 75.3,
  "zoning_score": 68.0,
  "market_score": 80.5,
  "risk_score": 22.4,
  "confidence": "high",
  "classification": "Tier 2 - Strong opportunity"
}
