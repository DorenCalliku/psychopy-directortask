import pandas as pd


def extract_experiment_steps(filename):
    clean_data = {}
    data = pd.read_excel(filename, sheet_name=None, header=None)  

    # clean the data
    for key, vals in data.items():

        # all data in sheet
        clean = vals.where(pd.notnull(vals), None).values.tolist()

        # grid condition
        grid = [j for i in clean[4:] for j in i if j != None]
        set_count = key.replace('set', '')

        clean_data[key] = {
            "data": clean[:4],
            "grid": grid[0] if grid != [] else None,
            "order": int(set_count) if set_count.isdigit() else None,
            "elements": [j for i in clean for j in i if j != None]
        }
    return clean_data
