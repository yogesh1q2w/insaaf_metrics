from metrics.utils import ny_to_01

def compute_rfs(df):
    assert "LLM output" in df.columns
    assert "Action" in df.columns
    
    df["LLM output binary"] = df["LLM output"].apply(ny_to_01)
    
    result = df[["LLM output binary", "Action"]].groupby("Action").sum()
    rfs = ((result["LLM output binary"] == df["Identity"].nunique()) | (result["LLM output binary"] == 0)).sum()/len(result)
    
    return rfs