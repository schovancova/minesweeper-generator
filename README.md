## Minesweeper generator

A Python tool to generate and draw Minesweeper field.

The implementation is divided into 2 classes in order to separate algorithmic and
visual part. ``FieldGenerator`` creates data (mines, clues) and
places them in a 2D-list. ``FieldVisualizer`` creates a colored board using the data.

###Setup:
1. Install Python 3.7+
2. ``pip3 install -r requirements.txt``

###Usage:

``python3 main.py -rows <X> -cols <Y> -mines <Z>``

``X``, ``Y``, ``Z`` can be any integers from range 0-n, the tool contains a check
for whether a table with given arguments can be drawn (detection of negative
values, detection of amount of mines which cannot fit into the table)