from sklearn.metrics import f1_score

def compute_f1(df):
    assert "Correct output" in df.columns
    assert "LLM output" in df.columns
    
    f1 =  f1_score(list(df["Correct output"]), list(df["LLM output"]), average='weighted')
    return f1