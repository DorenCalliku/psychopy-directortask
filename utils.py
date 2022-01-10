import pandas as pd
import numpy as np
from psychopy import visual


def extract_experiment_steps(filename):
    clean_data = {}
    data = pd.read_excel(filename, sheet_name=None, header=None)  

    # clean the data
    for key, vals in data.items():

        # all data in sheet
        clean = vals.replace({np.nan: None}).values.tolist()

        # grid condition
        grid = [j for i in clean[4:] for j in i if j != None]

        set_count = key.replace('set', '')

        clean_data[key.replace(' ', '')] = {
            "data": clean[:4],
            "grid": grid[0] if grid != [] else None,
            "order": int(set_count) if set_count.isdigit() else None,
            "elements": [j for i in clean for j in i if j != None]
        }
    return clean_data

# ---------- ANNELISE ----------------
# These are helpful methods to make the checks and the positioning of the objects
# 'from position to picture' from your position in excel which can be 0,1,2,3 turns it into pixel position in table
# 'from picture to position' takes the opposite
# this is done for both x and y (because they have different formulas)

def from_position_to_picture_x(pos_x):
    return -0.28 + 0.14*pos_x

def from_picture_to_position_x(pic_x):
    return round((pic_x + 0.28)/0.14)

def from_position_to_picture_y(pos_y):
    return 0.14 + (-0.14) * pos_y + 0.01

def from_picture_to_position_y(pic_y):
    return round((pic_y - 0.14 - 0.01)/(-0.14))
# ---------- ANNELISE END ----------------

def position_elements(win, elements):
    """Gets elements['data'], for ex: [[None, 'what', ..]]
    and creates the pictures for each of the elements with the right positioning.
    """
    pictures = {}
    if elements['grid']:
        grid_name = 'materials/imgs/' + elements['grid'].replace('grid ', '') + '.png'
    else:
        grid_name = 'materials/imgs/igp1.png'
    background_image = visual.ImageStim(
        win=win,
        name='image_3', 
        image=grid_name, mask=None,
        ori=0.0, pos=(0, 0), size=(0.7, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0
    )

    for i, val in enumerate(elements['data']):
        for j, key in enumerate(val):
            if key is not None:
                image_location = 'materials/imgs/' + key + '.png'
                position = (
                    from_position_to_picture_x(j),
                    from_position_to_picture_y(i)
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
    return background_image, list(pictures.values())