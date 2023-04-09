import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 944932368

def solution(x: np.array) -> bool: 
    alpha = 0.08
    pvalue = ztest(x, value=300, alternative='smaller')[1]
    return pvalue < alpha 
