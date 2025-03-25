import pandas as pd

class CsvGenerator:
    def generate(self,data,filename):
        df = pd.DataFrame(data)
        df.to_csv(filename,index=False)
        print(f"CSV zapisany do {filename}")
