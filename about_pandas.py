import numpy as np
import pandas as pd

data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 11, 'b': 22, 'c': 33}]
df = pd.DataFrame(data, index=range(2))

print df