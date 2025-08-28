# Placeholder: simple baseline that clusters by lat/lng bins.
import pandas as pd

def load_data(path='training_data.csv'):
    return pd.read_csv(path)

def simple_bin_predict(df, lat, lng, precision=2):
    df['bin_lat'] = df['lat'].round(precision)
    df['bin_lng'] = df['lng'].round(precision)
    counts = df.groupby(['bin_lat','bin_lng']).size().reset_index(name='count')
    return counts.sort_values('count', ascending=False).head(50)

if __name__ == "__main__":
    df = load_data()
    print(simple_bin_predict(df, 9.0, 8.0))
