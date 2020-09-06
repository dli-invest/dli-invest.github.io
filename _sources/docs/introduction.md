---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: myst
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    name: python3
---

% Link all references to use them in other directories

# Summary

```{note}
As an investor, I decided to document my journal from a software engineer to yoloing the market like in `/r/wallstreetbets`.

Since I am a prudent person, I will not disclose actually dollar amount, but will leave all the helpful code snippets I developed in here. The main programming languages at the moment are python, some deno scripts, rust/go (for speed) and ipynb notebooks.
```

> \"Stocks only go up.\" -- /r/wallstreetbets


## Learning Sources

### Books

* TODO ADD CONTENT

### Sources of Information
* iex
* yahoo finance
* trading view
* discord (for notifications)
* emails

Signing up for newsletters and never forget wallstreetbets


### Github Projects
* cad_tickers
* stock_screener
* ytube_nlp - automatically getting youtube investing videos and analyzing them, 
while making it easy to jump to points of interest. With AWS DyanmioDB, I'll
be able to search text.

### Code Tools

## Courses
```{warning}
MOVE this into a new file once it grows large enough and I am familar enough with jupyter notebook.
Sphinx 3 and 1.0.0 release.
```

### Introduction to Trading, Machine Learning & GCP
My notes for {cite}`coursera:ml-trading` are open source and available for anyone. As someone who has benefited greatly from open source, I do not really care, but from experience, I doubt anyone will read this. The corresponding tutorials for this course are at {cite}`github:gcp-da`.

```{note}

Github source code references available at 
[ai-for-finance](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/ai-for-finance)
```


Modern approaches use Machine Learning to model fluid market behaviours
and complexity.

-   Financial markets are a dynamic, evolving collection of behaviours

-   Use historical data to train a model and adjusts features and
    loadings to improve predictive power

-   Integrate the model into an order-execution strategy

-   Retrain and retest continually with new data to capture the market's
    current state.

Market moves with many human factors that are difficult to measure.

Exogenous and endogenous factors both drive changes in share prices.
Technical strategies tend to focus on endogenous factors and
event-driven strategies focus on exogenous factors.

```{bibliography} ../_bibliography/references.bib
:style: unsrt
:filter: docname in docnames
```
