# Capstone Starter: House Price Estimator

A working, end-to-end Data Science project template. It trains a `RandomForestRegressor` on a housing dataset, evaluates it honestly on held-out data, and serves live predictions through a Streamlit web app. It runs immediately on a built-in demo dataset - your job is to swap that demo dataset for your own Capstone problem and carry the same pipeline through.

## What this project does, as it stands right now
Given a property's square footage, bedroom count, bathroom count, and neighborhood, it predicts a sale price. On its demo data, it reaches Test MAE ≈ $16,000 and Test R² ≈ 0.985. This is a **demo dataset** (synthetic, generated in `train_model.py`) - the numbers exist to prove the pipeline works, not to represent a real market.

## What's in this repo
```
capstone-starter/
├── README.md                    - this file
├── requirements.txt              - pinned dependencies
├── train_model.py                - loads data, engineers features, trains, saves model.pkl
├── app.py                        - Streamlit interface that loads model.pkl and serves predictions
├── model.pkl                      - pre-trained on the demo dataset, included so app.py works immediately
├── data/
│   └── README.md                  - where your own dataset goes
├── notebooks/
│   └── capstone_starter.ipynb      - exploratory notebook (EDA, feature checks), separate from production code
├── src/
│   └── features.py                  - reusable feature engineering functions, imported by both train_model.py and app.py
├── decision_log.md                  - dated log of modeling decisions, with two real example entries
└── report/
    └── README.md                     - business report template with worked examples, backs your 5-slide presentation
```

---

## Your Assignment

This repo is a working example built on a demo dataset. Your task is to carry the same pipeline through on your own Capstone problem from Section 7.1. Follow these steps in order - each one tells you what to run and what you should see if it worked. Don't skip ahead; later steps assume earlier ones are done.

### Part 1 - Get This Project Running As-Is

**Step 1: Download the project and put it under version control**

Unzip `capstone-starter.zip`. Open a terminal and navigate into the folder:
```bash
cd path/to/capstone-starter
```
Create a new empty repository on GitHub (Section 1.2), then connect this folder to it:
```bash
git init
git add .
git commit -m "Initial commit from starter template"
git remote add origin <your-repo-url>
git push -u origin main
```

**Step 2: Set up your environment**
```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
```
You'll know it worked if your terminal prompt now shows `(venv)`.

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
```
**Checkpoint:** run `pip list` and confirm `streamlit`, `scikit-learn`, and `pandas` appear. If `pip install` errors, check `TROUBLESHOOTING.md` from Section 1 before continuing.

**Step 4: Train the baseline model**
```bash
python train_model.py
```
**Checkpoint:** you should see:
```
Test MAE: 16,099
Test R^2: 0.985
Saved model.pkl
```
A `model.pkl` file now exists in the project folder.

**Step 5: Run the app**
```bash
streamlit run app.py
```
Your browser opens to `http://localhost:8501`. Enter some values and click **"Estimate price."** You should see a predicted price. Stop the app with `Ctrl + C` when done.

**Step 6: Explore the notebook**
```bash
jupyter notebook notebooks/capstone_starter.ipynb
```
Run every cell top to bottom (**Shift + Enter**). You should see a scatter plot render, and the leakage-check cell should print `Flagged as possibly leaky: none`.

**Step 7: Read the code before changing anything**
Open and read `src/features.py`, `train_model.py`, and `app.py`.

□ Write one sentence for each file, in your own words, describing what it's responsible for - confirm you understand the pipeline before modifying it.

---

### Part 2 - Adapt This Project to Your Own Capstone Dataset

**Step 8:** Place your real dataset (e.g., `my_data.csv`) inside `data/`.

**Step 9:** In `train_model.py`, replace the `load_data()` function body:
```python
def load_data():
    return pd.read_csv("data/my_data.csv")
```
Delete the synthetic-data generation code (the `rng.integers(...)` lines).

**Step 10:** Update the feature list in `train_model.py`:
```python
numeric_cols = ["your", "numeric", "columns", "here"]
X = df.drop(columns=["your_target_column"])
y = df["your_target_column"]
```
Update `encode_categorical(df, columns=[...])` to match your own categorical columns.

□ In `src/features.py`, replace the example logic in `add_derived_features()` (`rooms_total`, `sqft_per_bedroom`) with 1–2 derived features that make sense for your dataset, using your Section 4.6 work as a guide.

**Step 11:** Re-run `python train_model.py`.
**Checkpoint:** a suspiciously perfect R² (above 0.99) is a signal to re-run `check_target_leakage()` and check for a leaky feature, per Section 3 and 4.6.

**Step 12:** In `app.py`, update the `st.number_input(...)` / `st.selectbox(...)` fields and the `input_df = pd.DataFrame([{...}])` block to match your real dataset's column names. Re-run `streamlit run app.py` and confirm it still works end to end.

---

### Part 3 - Document and Present

**Step 13:** In `decision_log.md`, delete the two housing-price example entries. Add a new dated entry immediately each time you make a real modeling decision. Minimum: 3 real entries.

**Step 14:** Rewrite this README's **"What this project does"** and **"Repository"** sections above to describe your own project instead of the House Price Estimator demo - real title, real problem statement, real dataset source, real results.

**Step 15:** In `report/README.md`, fill in each of the five slide sections with your project's real numbers, following the worked examples already there as your guide to expected detail. Build an actual 5-slide deck and export it as `report/presentation.pdf`.

**Step 16:**
```bash
git add .
git commit -m "Add real dataset, retrain model, update app and docs"
git push
```

---

### Part 4 - Deploy

**Step 17:** Confirm your GitHub repo is accessible and `model.pkl` is committed (unless your data is sensitive - see `.gitignore`).

**Step 18:** Go to **share.streamlit.io**, sign in with GitHub, click **"New app,"** select your repo/branch/`app.py`, click **"Deploy."**
**Checkpoint:** open the live URL and test the form, same as Step 5.

**Step 19:** Paste your live Streamlit URL into this README's **Live Demo** section below.

## Live Demo
*Not yet deployed - see Step 19.*

---

## Final Checklist
□ `train_model.py` runs on my real dataset with no errors
□ `model.pkl` reflects the real, retrained model
□ `app.py` form matches my dataset's actual features
□ `decision_log.md` has at least 3 real, dated entries
□ This README describes my actual project, not the House Price Estimator demo
□ `report/presentation.pdf` exists and states a real limitation, not a generic one
□ Project is pushed to GitHub
□ App is deployed and the live URL works
□ Live URL is pasted into this README
