# Decision Log

## Why this file exists

Building a machine learning model involves dozens of decisions.

Some are small.

Some completely change the final result.

A few weeks later, it's surprisingly difficult to remember **why** you chose one approach over another. Without a written record, you'll often find yourself asking:

> "Why did I remove that feature?"
>
> "Why did I switch models?"
>
> "Didn't I already try this?"

Keeping a decision log solves that problem.

Think of it as an engineering notebook.

Instead of documenting *what* you did (Git already records that), you document **why** you did it.

---

## What belongs here?

Only decisions that affected your project.

Examples include:

- choosing one model instead of another;
- adding or removing features;
- changing the train/test split;
- handling missing values differently;
- detecting and removing target leakage;
- changing evaluation metrics;
- engineering new features;
- deciding not to use a particular approach after testing it.

You do **not** need to record every edit or bug fix.

Only decisions that someone reviewing your project would reasonably ask about.

---

## Why this matters

Imagine that six months from now someone asks:

> "Why aren't we using Linear Regression anymore?"

or

> "Why was this feature removed?"

Without documentation, the only honest answer is:

> "I don't remember."

With a decision log, you can point to the exact reasoning that led to the current solution.

This is also valuable when working in a team. Your teammates shouldn't have to reverse-engineer your thought process from Git commits or source code.

---

## How to write an entry

Each entry should answer three simple questions:

- **What decision did I make?**
- **Why did I make it?**
- **What trade-off did I accept?**

Keep entries short—usually one paragraph is enough.

The goal is to capture your reasoning while it's still fresh, not to write a detailed report.

---

## Example format

```text
2026-08-01 — Switched from Linear Regression to Random Forest

Decision:
Used Random Forest as the primary model.

Why:
The linear model consistently underfit the data, while Random Forest captured the non-linear relationships much better and significantly improved validation performance.

Trade-off accepted:
The model is less interpretable than a linear regression, but the increase in predictive performance justified the choice.
```
## Git records what changed. A Decision Log records why it changed.
---

## During your Capstone

Try to update this file **immediately after** making an important modeling decision.

Don't wait until the end of the project.

Your future self will thank you.
