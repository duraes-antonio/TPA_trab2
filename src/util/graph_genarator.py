import pandas as pd
import glob

path = '../../resultados/heapsort' # use your path
all_files = glob.glob(path + "/*.csv")
all_files.sort()
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0, encoding='ISO-8859-1')
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(all_files)