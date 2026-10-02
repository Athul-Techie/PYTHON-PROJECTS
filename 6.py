import pandas as pd
import numpy as np
ser=pd.Series(np.arange(10,31,2))
print(ser)
print()
print(ser[6:])
print()
print(ser.tail(5))
