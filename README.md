# Retail Demand Forecasting

A small end-to-end machine learning project forecasting next-week product demand from recent sales history.

The goal is to compare simple statistical and tree-based models against a naive persistence baseline, while using a leakage-safe chronological evaluation setup.

## Dataset

The project uses the UCI Machine Learning Repository's
**Online Retail** dataset:
https://archive.ics.uci.edu/dataset/352/online+retail

It contains transaction-level data from a UK-based online retailer
between December 2010 and December 2011..

The raw data contains approximately 540,000 transactions.

Our analysis:
- keeps UK transactions only;
- removes cancellations, non-positive quantities and prices, and obvious non-product administrative codes;
- aggregates transactions into weekly product-level demand;
- removes partial boundary weeks;
- constructs a complete product-week panel, treating missing product-week sales as zero observed demand.

## Forecasting setup

The target is current-week product demand.

The predictors are the previous four weeks of demand:

- `lag_1`
- `lag_2`
- `lag_3`
- `lag_4`

The data is split chronologically into:
- training period;
- validation period;
- test period.

The product universe is selected using training-period information only and then frozen, avoiding selection leakage.

## Models

The following models are compared:

- Naive persistence baseline: predict next week using last week's demand;
- Ordinary Least Squares (OLS) regression;
- Ridge regression;
- Random Forest regression.

Hyperparameters are selected using validation RMSE only. Final model choices are then frozen before evaluation on the untouched test set.

## Test results

| Model | RMSE | MAE |
|---|---:|---:|
| Persistence | 159.40 | 51.86 |
| OLS | **132.32** | 46.88 |
| Ridge | 132.52 | 46.99 |
| Random Forest | 135.67 | **45.22** |

All learned models substantially outperform the persistence baseline.

OLS achieves the best test RMSE, while Random Forest achieves the best test MAE.

Further error analysis shows that Random Forest performs better on low- and medium-demand observations, while OLS handles some of the most extreme high-demand misses better. A small number of large demand spikes dominate RMSE.

## Interpretation

The results suggest that recent demand history contains substantial predictive signal beyond a naive last-week forecast.

Ridge performs almost identically to OLS, suggesting that regularization provides little practical benefit in this setting.

Random Forest captures some additional nonlinear structure and improves typical absolute-error performance, but extreme demand spikes remain difficult to predict.

Overall, the project does not identify one universally superior model:
- OLS performs better under a metric that strongly penalizes extreme errors;
- Random Forest performs better on the typical magnitude of forecasting error.

## Limitations

Important limitations include:
- observed sales are used as a proxy for true demand;
- stockouts may therefore lead to censored demand;
- only lagged demand features are used;
- no price, promotion, holiday, or refined product information is included;
- the dataset covers approximately one year;
- the analysis uses a simple chronological train/validation/test split;
- the model is pooled across products;
- extreme demand spikes remain poorly predicted.

## Possible extensions

Potential extensions include:
- richer features such as price, promotions, seasonality, and product metadata;
- modelling products separately by demand scale or demand regime;
- longer historical data.

## Repository

The main analysis is contained in:

`retail_demand_forecasting.ipynb`

The notebook includes the full data preparation, feature construction, model selection, test evaluation, and error analysis.

## Tools

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- Jupyter
- Git