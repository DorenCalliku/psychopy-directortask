from psychopy import visual, core

# Setup stimulus
win = visual.Window([400, 400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5,
    name='gabor', autoLog=False)
fixation = visual.GratingStim(win, tex=None, mask='gauss', sf=0, size=0.02,
    name='fixation', autoLog=False)

# Let's draw a stimulus for 200 frames, drifting for frames 50:100
for frameN in range(200):   # For exactly 200 frames
    if 10 <= frameN < 150:  # Present fixation for a subset of frames
        fixation.draw()
    if 50 <= frameN < 100:  # Present stim for a different subset
        gabor.phase += 0.1  # Increment by 10th of cycle
        gabor.draw()
    win.flip()
