# 🏙️ MetroPulse

## Real Estate Investment & Yield Analytics Dashboard

## 📌 Project Overview

**MetroPulse** is an end-to-end real estate investment analytics platform designed to help investors, analysts, and advisory firms identify high-potential real estate micro-markets within major Indian cities.

The platform integrates **time-series data analysis, feature engineering, explainable investment scoring, unsupervised market clustering, backtesting, and interactive dashboards** to enable **data-driven and risk-aware investment decisions**.

## 🎯 Business Problem

Real estate investment decisions are often based on:
-   Static reports
-   Broker opinions
-   Limited historical analysis
-   Lack of risk awareness
    
This leads to:
-   Mispriced investments
-   Overexposure to speculative markets
-   Poor yield vs growth trade-offs
    

### The core challenge:

> **How can investors systematically identify micro-markets that offer the best balance between rental income, capital appreciation, infrastructure strength, and risk?**

## 🧱 Data Architecture

### Datasets Used

| Dataset Name | Description |
|-------------|------------|
| property_prices.csv | Time-series property price & rent data |
| infrastructure_scores.csv | Infrastructure indicators by market |
| market_metadata.csv | Market classification & risk profile |
| master_dataset.csv | Unified analytical dataset |

## 🔧 Synthetic Data Generation

Since real granular micro-market data is difficult to obtain, **synthetic data** was generated using realistic economic assumptions:

Value(t)=Base_Market_Value+f(Time)+NoiseValue(t) = Base\_Market\_Value + f(Time) + NoiseValue(t)=Base_Market_Value+f(Time)+Noise

This approach ensures:

-   Gradual price appreciation  
-   Infrastructure-driven growth
-   Market-specific behavior
-   Realistic volatility and liquidity patterns


## 🧠 Feature Engineering

Raw data was transformed into **investment-relevant features** to convert prices, rent, and infrastructure signals into actionable analytics.

### Feature Engineering Flow


### Engineered Features

| Feature | Description |
|--------|------------|
| `rental_yield_pct` | Annual rental income relative to property price |
| `yoy_price_growth` | Year-over-year capital appreciation |
| `infra_score` | Composite infrastructure strength |
| `infra_momentum` | Rate of infrastructure improvement over time |
| `liquidity_score` | Ease of buying and selling properties |
| `price_volatility` | Market risk indicator based on price fluctuations |


## 🧮 Investment Scoring Framework

A **rule-based, explainable investment score** was designed to rank micro-markets:

Investment Score = Rental Yield + Capital Appreciation + Infrastructure Strength + Liquidity + Risk (Volatility)

### Why scoring?

-   Converts multi-dimensional data into a single decision metric
-   Enables ranking and comparison
-   Maintains transparency and business trust

## 🧠 Market Segmentation (Clustering)

### Models Used

-   **HDBSCAN** → final production model
    
### Why HDBSCAN?

-   Automatically detects natural market groupings
-   Identifies speculative/outlier markets
-   Handles uneven market densities
    

### Resulting Market Segments

-   Balanced Markets
-   Yield-Focused Markets
-   Growth-Driven Markets
-   Speculative / Outlier Markets

## 🔗 Hybrid Intelligence: Clusters Inside Investment Score

To improve robustness, cluster insights were incorporated into the investment score using **confidence multipliers**:
Final Investment Score = Base Investment Score × Cluster Confidence Factor

This:
-   Rewards structurally stable markets
-   Penalizes speculative outliers
-   Combines rule-based logic with ML insights

## 🔮 Backtesting & Validation

### Objective

Validate whether **high investment scores actually led to higher future returns**.

### Methodology
-   Score markets at time `t`
-   Measure price growth at `t + 12 months`
-   Compare performance across score quantiles
    

### Result

Markets with higher investment scores consistently demonstrated **stronger future price appreciation**, validating the model.

----------

## 🎯 Confidence Bands (Risk Awareness)

To account for uncertainty, **confidence scores** were added based on:

-   Price volatility
-   Market liquidity
### Confidence Levels
-   **High Confidence** → Stable, reliable markets
-   **Medium Confidence** → Moderate risk
-   **Low Confidence** → Speculative markets
    

This enables **risk-adjusted decision-making**.

----------

## 📊 Visualization & Dashboards
### Power BI Dashboard

-   Executive KPI view
    
-   Interactive slicers
    
-   Target vs actual comparisons
    
-   Client-ready presentation
    
----------

## 🛠️ Tech Stack

-   **Python**: Pandas, NumPy, Scikit-learn
    
-   **ML**: HDBSCAN
    
-   **Visualization**: Matplotlib
    
-   **Dashboards**: Power BI
    
-   **Data Modeling**: Time-series analysis, feature engineering, EDA
    
