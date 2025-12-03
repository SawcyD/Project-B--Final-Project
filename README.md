# Project B: Hybrid Forecasting and Sequential Intervention Assessment

## Project Overview

This project combines epidemiological forecasting with online change detection to assess the effectiveness of COVID-19 interventions (lockdowns, vaccination campaigns) in the United States. The project implements SARIMA models, state-space Poisson/Negative Binomial models for weekly incidence forecasting, applies CUSUM and Bayesian Online Change-Point Detection (BOCPD) methods on forecast residuals to detect structural changes, and conducts counterfactual analysis to quantify policy impacts.

## Objectives

- **Part 1**: Apply and compare forecasting models (SARIMA, Poisson State-Space, Negative Binomial State-Space)
- **Part 2**: Implement online change detection (CUSUM and BOCPD) on forecast residuals
- **Part 3**: Construct counterfactual forecasts and estimate avoided cases
- **Part 4**: Simulate policy scenarios (earlier vaccination vs. delayed lockdown)

## Data Sources

- **Primary Dataset**: Johns Hopkins University (JHU) CSSE COVID-19 Data Repository
  - USA Weekly COVID-19 Cases (January 2020 - March 2023)
  - Source: `https://github.com/CSSEGISandData/COVID-19`
  - Processing: Aggregated from daily cumulative cases to weekly incident cases

- **Secondary Dataset**: Maryland state-level data (available but not used in main analysis)

## Project Structure

```
project/
├── data/                          # Input data files
│   ├── maryland_weekly_cases.csv
│   └── usa_weekly_cases.csv
│
├── images/                        # All generated graphs and visualizations
│   ├── baseline_forecast.png
│   ├── bocpd_change_detection.png
│   ├── counterfactual_analysis.png
│   ├── cusum_change_detection.png
│   ├── forecast_model_comparison.png
│   ├── policy_scenario_simulations.png
│   ├── process_flow_diagram.png
│   ├── project_b_complete_overview.png
│   └── usa_baseline.png
│
├── results/                       # All generated CSV results and metrics
│   ├── baseline_metrics.csv
│   ├── change_point_detection_results.csv
│   ├── counterfactual_analysis.csv
│   ├── counterfactual_summary.csv
│   ├── forecast_comparison_metrics.csv
│   ├── policy_scenario_simulations.csv
│   └── scenario_comparison_table.csv
│
├── project.ipynb                  # Main analysis notebook (all 4 parts)
├── data.py                        # Data collection script for Maryland
└── README.md                      # This file
```

## Methodology

### Part 1: Forecasting Models

1. **SARIMA Model**: Seasonal Autoregressive Integrated Moving Average
   - Order: (1,1,1) × (1,1,1,52)
   - Best performing model (RMSE: 221,049, MAPE: 82.95%)

2. **State-Space Poisson Model**: Log-link state-space model with Poisson observation distribution

3. **State-Space Negative Binomial Model**: Extended model with dispersion parameter

**Validation Metrics**: RMSE, MAE, MAPE

### Part 2: Online Change Detection

1. **CUSUM Test**: Cumulative Sum test on SARIMA residuals
   - Detects structural changes when statistic exceeds threshold
   - Formula: $S_t = \max(0, S_{t-1} + (x_t - k))$

2. **BOCPD**: Bayesian Online Change-Point Detection
   - Probabilistic approach using recursive Bayesian updates
   - Identifies change points through run-length distribution

### Part 3: Counterfactual Analysis

- **No-Intervention Scenario**: Exponential growth model projected forward
- **Avoided Cases**: $\Delta y_t = \tilde{y}_t^{\text{no policy}} - y_t^{\text{observed}}$
- **Population Cap**: Counterfactual values capped at US population (335 million)

### Part 4: Policy Scenario Simulations

- **Scenario 1**: Earlier Vaccination (2 months earlier = October 2020)
- **Scenario 2**: Delayed Lockdown (2 months later = May 2020)
- **Impact Quantification**: Total cases, percentage change, peak cases

## Key Results

### Forecasting Performance

| Model | RMSE | MAE | MAPE (%) |
|-------|------|-----|----------|
| **SARIMA** | **221,049** | **210,016** | **82.95%** |
| Poisson State-Space | 696,691 | 693,658 | 276.79% |
| Negative Binomial | 998,235 | 995,260 | 395.44% |

**Best Model**: SARIMA achieved lowest error across all metrics

### Policy Scenario Impact

| Scenario | Total Cases | Change vs Observed |
|----------|-------------|-------------------|
| Observed (Actual) | 103.8M | Baseline |
| **Earlier Vaccination** | **40.2M** | **-61.3%** |
| **Delayed Lockdown** | **144.2M** | **+57.3%** |

**Key Insight**: Earlier interventions = 61% reduction. Delayed interventions = 57% increase.

### Counterfactual Analysis

- Interventions prevented millions of cases
- Counterfactual capped at US population (335M)
- Peak reduction: 100%

## Installation & Setup

### Requirements

```bash
pip install -r requirements.txt
```

### Running the Project

1. **Data Collection** (optional - data files already included):
   ```bash
   python data.py  # Generates maryland_weekly_cases.csv
   ```

2. **Main Analysis**:
   - Open `project.ipynb` in Jupyter Notebook
   - Run all cells sequentially
   - All outputs will be saved to `images/` and `results/` folders

3. **View Results**:
   - Check `results/` folder for CSV files with metrics
   - Check `images/` folder for all graphs
   - Open `Project_B_Presentation.html` in browser for interactive slides

## Deliverables

### Code Files
- `project.ipynb`: Complete implementation of all 4 parts
- `data.py`: Data collection and preprocessing

### Data Files
- `data/usa_weekly_cases.csv`: Main dataset (USA weekly cases)
- `data/maryland_weekly_cases.csv`: State-level data

### Results Files
- `results/forecast_comparison_metrics.csv`: Model comparison
- `results/change_point_detection_results.csv`: CUSUM and BOCPD results
- `results/counterfactual_analysis.csv`: Full counterfactual data
- `results/counterfactual_summary.csv`: Summary statistics
- `results/policy_scenario_simulations.csv`: Scenario data
- `results/scenario_comparison_table.csv`: Policy comparison

### Visualizations
All graphs saved in `images/` folder:
- `forecast_model_comparison.png`: Part 1 results
- `cusum_change_detection.png`: CUSUM detection
- `bocpd_change_detection.png`: BOCPD detection
- `counterfactual_analysis.png`: Part 3 results
- `policy_scenario_simulations.png`: Part 4 results
- `process_flow_diagram.png`: Workflow diagram
- `project_b_complete_overview.png`: Comprehensive summary




## Key Findings Summary

1. **Forecasting**: SARIMA model provides best predictions (RMSE: 221K, MAPE: 83%)
2. **Change Detection**: CUSUM and BOCPD successfully identify intervention effects
3. **Intervention Impact**: Counterfactual analysis shows interventions prevented millions of cases
4. **Policy Timing**: Earlier vaccination reduces cases by 61%, delayed lockdown increases by 57%

## Technical Details

### Models Implemented
- SARIMA(1,1,1)×(1,1,1,52)
- State-Space Poisson with log-link
- State-Space Negative Binomial with dispersion parameter
- CUSUM change detection
- Bayesian Online Change-Point Detection (BOCPD)

### Evaluation Metrics
- **RMSE**: Root Mean Squared Error
- **MAE**: Mean Absolute Error
- **MAPE**: Mean Absolute Percentage Error
- **Change Point Detection**: Number of detected structural breaks

## References

1. Dong E, Du H, Gardner L. An interactive web-based dashboard to track COVID-19 in real time. *Lancet Inf Dis*. 2020;20(5):533-534.

2. Adams, R. P., & MacKay, D. J. (2007). Bayesian online changepoint detection. *arXiv preprint arXiv:0710.3742*.

3. Johns Hopkins University Center for Systems Science and Engineering. COVID-19 Data Repository. https://github.com/CSSEGISandData/COVID-19

4. Project B Specification: "Hybrid Forecasting and Sequential Intervention Assessment" 

