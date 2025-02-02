import pandas as pd
from tqdm import tqdm

from metrics.f1 import compute_f1
from metrics.rfs import compute_rfs
from metrics.lss import compute_lss

DATASET_PATH = "dataset/sample.csv"
BETA=1

dataset = pd.read_csv(DATASET_PATH)

# apply some filter on dataset to get crime/identity type specific metrics

dataset_specific = dataset[dataset["Crime"] == "Robbery"]

f1 = compute_f1(dataset_specific)
rfs = compute_rfs(dataset_specific)
lss = compute_lss(dataset_specific, beta=BETA)

print(f"F1 score = {round(f1, 4)}\nRFS = {round(rfs, 4)}\nLSS (beta={BETA}) = {round(lss, 4)}")