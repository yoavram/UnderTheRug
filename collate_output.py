import os
import glob
import gzip
try:
    import ujson as json
except ImportError:
    import json

import pandas as pd
import click_spinner

def load_data(fname):
    try:
        with gzip.open(fname, 'rt') as f:
            data = json.load(f)
    except Exception as e:
        print("Failed loading {} due to {}".format(fname, e))
        return None
    else:
        if not fname.endswith(data['filename']):
            print("Problem in {}, not 'filename' field")
        if not 'n' in data:
            print("Problem in {}, not 'n' field")
        else:
            data.pop('n')
        return data


if __name__ == '__main__':
    with click_spinner.spinner():
        files = glob.glob(os.path.join("output", "*.json.gz"))
        data = (load_data(fname) for fname in files)
        df = pd.DataFrame(list((d for d in data if d)))
        df.to_csv("output.csv", index=False)
