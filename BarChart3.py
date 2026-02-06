import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label3 = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label3)), height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label3)), table['NAMA KELURAHAN'], rotation=90)

plt.xlabel('Kelurahan di Jakarta Pusat')
plt.ylabel('Jumlah Penduduk Laki - laki')
plt.title('Persebaran Jumlah Penduduk Laki - laki DI Jakarta Pusat')
plt.show()