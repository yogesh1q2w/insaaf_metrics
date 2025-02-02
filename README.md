# ⚖️ Metrics from InSaAF paper
Minimal implementation of the metrics presented in the paper **InSaaF: Incorporating Safety through Accuracy and Fairness | Are LLMs ready for the Indian Legal Domain?** (JURIX 2024) [paper link](https://ebooks.iospress.nl/volumearticle/71031?_gl=1*go82z1*_up*MQ..*_ga*MTk2OTI4Njc3Mi4xNzM4NTAzMzI0*_ga_6N3Q0141SM*MTczODUwMzMyNC4xLjAuMTczODUwMzMyNC4wLjAuMA..)


## Includes all 3 metrics
1. Legal Safety Score ($\beta$-weighted)
2. Relative Fairness Score
3. $F_1$ score

## Steps to run the code and models
1. It is recommended to create a new python environment
```[bash]
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
2. Run the `compute_metrics.py` file to generate the metrics on sample dataset
```[bash]
python compute_metrics.py
```

You can change the dataset and the filters applied on the dataset in `compute_metrics.py`