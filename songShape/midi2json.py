import py_midicsv
import numpy
import json
import csv

mc = py_midicsv.midi_to_csv("songs/mary.mid")
m_head = mc[0]
mx = csv.DictReader(mc)
mj = open('mary.json','w')

for row in mx:
    json.dump(row,mj)
    mj.write('\n')

# with open('mary.json','w') as outfile:
#     json.dump(mary,outfile)
# print slayer

# write midi file to json, with tick being x axis, and figuring out "data" to be note and duration.
# floor()
# octave # will be radius - floor of (number divided by 12)
# numpy.floor(midi{NoteOnEvent}.data)
# note will be angle - (remainder of (number divided by 12)) multiplied by the variable
# note_angle = {'angles':[
#     {0,{'note':'C','angle':0}},
#     {7,{'note':'G','angle':30}},
#     {2,{'note':'D','angle':60}},
#     {9,{'note':'A','angle':90}},
#     {4,{'note':'E','angle':120}},
#     {11,{'note':'B','angle':150}},
#     {6,{'note':'F#','angle':180}},
#     {1,{'note':'C#','angle':210}},
#     {8,{'note':'G#','angle':240}},
#     {3,{'note':'D#','angle':270}},
#     {10,{'note':'A#','angle':300}},
#     {5,{'note':'F','angle':330}}
#     ]}

# https://math.stackexchange.com/questions/260096/find-the-coordinates-of-a-point-on-a-circle
# https://www.midimountain.com/midi/midi_note_numbers.html
print('ding!')