import pandas as pd
from psychopy import visual


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


def position_elements(win, elements):
    """Gets elements['data'], for ex: [[None, 'what', ..]]
    and creates the pictures for each of the elements with the right positioning.
    """

    pictures = {}
    for i, val in enumerate(elements['data']):
        for j, key in enumerate(val):
            if key is not None:
                image_location = 'materials/imgs/' + key + '.png'
                position = (
                    -0.28 + 0.14*j,
                    0.14 + (-0.14)*i + 0.01
                )
                pictures[key] = visual.ImageStim(
                    win=win,
                    name=key, 
                    image=image_location, mask=None,
                    ori=0.0, pos=position, size=(0.1, 0.1),
                    color=[1,1,1], colorSpace='rgb', opacity=None,
                    flipHoriz=False, flipVert=False,
                    texRes=128.0, interpolate=True, depth=-len(pictures)
                )
    return pictures