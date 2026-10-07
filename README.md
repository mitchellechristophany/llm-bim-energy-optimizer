# 🏢 LLM Building Energy & BIM Performance Optimizer

An AI-driven API architecture combining Random Forest regression with LLM-inspired rule evaluation to analyze Building Information Modeling (BIM) structural configurations and generate energy optimization insights.

## 📌 Features
- **Energy Load Prediction:** ML model trained on structural attributes (floor area, wall insulation R-values, window-to-wall ratios).
- **Automated Advisory Engine:** Evaluates physical building parameters to produce targeted decarbonization and efficiency recommendations.
- **REST API Architecture:** FastAPI framework designed for seamless integration into CAD software, Revit plugins, or web dashboards.

## 📐 Architecture Overview
```text
[ BIM Metadata / Input JSON ]
            │
            ▼
┌─────────────────────────┐
│ FastAPI Request Handler │
└───────────┬─────────────┘
            │
    ┌───────┴────────┐
    ▼                ▼
[ ML Model ]   [ Rule/LLM Engine ]
(Energy kWh)   (Actionable Insights)
    │                │
    └───────┬────────┘
            ▼
 [ API Response Output ]
