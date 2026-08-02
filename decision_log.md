# Decision Log

Log every meaningful modeling decision here, as you make it — not reconstructed afterward from memory. Two real example entries below to show the expected level of detail; delete them once you start your own.

---

### 2026-08-01 — Chose RandomForestRegressor over LinearRegression as baseline
**Decision:** Started with `RandomForestRegressor` instead of linear regression.
**Why:** Initial EDA showed a non-linear relationship between `sqft` and `price` (diminishing returns above ~3000 sqft). Linear regression underfit this in a quick test (R² = 0.71 vs. 0.985 for the forest).
**Trade-off accepted:** Random Forest is harder to interpret than a linear model's coefficients. Documented feature importances separately to partially offset this for the business presentation.

---

### 2026-08-01 — Flagged and dropped a leaky feature
**Decision:** Ran `check_target_leakage()` from `src/features.py` before finalizing features.
**Finding:** A column named `assessed_value` correlated with `price` at 0.99 — almost certainly derived from the sale price itself, not available at prediction time in a real workflow.
**Action:** Dropped the column. Re-ran evaluation; R² dropped from 0.998 to 0.985, which is the honest number.

---

### [Your date] — [Decision title]
**Decision:**
**Why:**
**Trade-off accepted:**
