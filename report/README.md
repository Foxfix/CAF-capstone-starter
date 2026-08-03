# Business Report

## Why this folder exists

By this point, you've built a machine learning model that can make predictions.

That's a major milestone-but it is **not** the end of a Data Science project.

In industry, a model is only one part of the final deliverable. Before anyone decides to use it, someone needs to understand what it does, how reliable it is, where it should (and shouldn't) be used, and what value it provides. That audience is rarely another data scientist. It is much more likely to be a product manager, business owner, client, engineer, or executive.

Those people usually don't care which algorithm you trained or how you tuned its hyperparameters.

Instead, they ask questions like:

- What problem does this solve?
- How accurate is it?
- When should we trust it?
- When should we **not** trust it?
- What should we actually do with it?

Being able to answer those questions clearly is one of the most valuable skills a data scientist can develop.

A technically excellent model with a poor explanation often never gets adopted. A simpler model that stakeholders understand and trust is much more likely to create real value.

This report exists to help you practice communicating your work-not just building it.

---

## Your Task

Imagine you've spent several weeks building your Capstone project.

Now your manager walks over and says:

> **"Can you explain what you've built in five minutes? I don't need the code-I need to know whether we should use it."**

This report is your answer.

You'll first write the content here, then turn it into a short presentation.

The goal is **not** to explain machine learning.

The goal is to explain **your solution**.

---

# Presentation Structure

## Slide 1 - The Problem

Start with the problem your project solves.

Describe it from a business perspective, not a technical one.

Your audience should understand **why this project exists** before they hear anything about models or algorithms.

**Good**

> "The goal is to estimate house prices before a property is listed so agents can produce an initial valuation within seconds."

**Avoid**

> "We trained a Random Forest model."

A model is not the problem-the business problem comes first.

---

## Slide 2 - The Solution

Briefly explain how your project approaches the problem.

Keep this high level.

Your audience should understand:

- what data you used,
- what information the model learns from,
- how predictions are produced.

Avoid implementation details unless they are important to understanding the solution.

---

## Slide 3 - The Results

Now answer the question everyone will ask:

> **"Does it actually work?"**

Include your evaluation metrics, but always explain what they mean in plain English.

Instead of writing:

```
MAE = 16,099
```

write something like:

> "On average, the model's predictions differ from the true sale price by about $16,000."

Most stakeholders understand that explanation immediately.

Whenever possible, connect your metrics back to the original business problem.

---

## Slide 4 - Limitations

Every model has limitations.

Being honest about them is not a weakness-it demonstrates that you understand your solution and know where it can be trusted.

Examples include:

- limited training data,
- missing features,
- small dataset,
- geographic limitations,
- changing market conditions,
- class imbalance,
- possible bias,
- performance outside the observed data range.

A model is only useful when people understand both its strengths **and** its boundaries.

---

## Slide 5 - Recommendation

Finish by answering the most important question:

> **"What should we do with this model?"**

Don't repeat your evaluation metrics.

Instead, provide a recommendation.

For example:

- deploy the model internally,
- use it as a decision-support tool,
- require manual review for certain cases,
- collect additional training data,
- retrain periodically,
- avoid using it outside the training distribution.

This is where your project becomes a business solution instead of just a machine learning exercise.

---

# Build the Presentation

Once you've completed this document:

1. Create a slide deck using PowerPoint, Google Slides, Keynote, or another presentation tool.
2. Use **one slide for each section** above.
3. Keep the slides clean and concise.
4. Include visuals where they improve understanding (charts, screenshots, diagrams, sample predictions, etc.).
5. Export the finished presentation as:

```
report/presentation.pdf
```

---

# What We're Evaluating

This assignment is **not** about graphic design.

We're evaluating whether you can communicate your project clearly to someone who is **not** a machine learning engineer.

A strong presentation answers three questions:

- **What did you build?**
- **How well does it work?**
- **Should someone actually use it?**

If your audience can confidently answer those three questions after your presentation, you've done your job.

Remember:

> **Building the model demonstrates your technical skills. Explaining the model demonstrates your professional skills. A successful Data Science project requires both.**
