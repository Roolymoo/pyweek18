pyweek18
========

Submission PyWeek challenge #18

[Repository on Github](https://github.com/5hassay/pyweek18)

Theme: "8-bit"

# How to Run the Game

## Using Python

Uses [Python v3.3.2](http://www.python.org/download/) and [Pygame v1.9.2](https://bitbucket.org/pygame/pygame/downloads)!

1. Download all the files. [Quick link to the zip (may autodownload)](https://github.com/5hassay/pyweek18/archive/master.zip).
2. Run `main.py` with Python, such as with one's console, and supply a level file name as an arguement. Choices are: `level1_easy.txt`, `level1_medium.txt`. For example, using a command-line: `python main.py level1_medium.txt`.

# How to Play the Game (Rules)

* Using the arrow keys, the goal is to take Bob to the stairs (exit)
* Almost all movement and actions will add or subtract from your SUM (right side of screen). If you go below -127, you "underflow" and lose. If you go above 126, you "overflow" and lose. (Think 8-bit integer.)
* Walking on normal tiles will add/subtract some amount for each time you walk on them.
* Walking on traps (fire, spikes, poop) will add/subtract some amount only once. Similarly for picking up keys or opening locks.

# Known Problems

1. None at this time.

# Notes on Source and Assets

* All Python code that is not an official python library or a pygame module was written from scratch by the authors Dickson Wong and Lucas Ashbury-Bridgwood. Images made by Dickson Wong.
* Image files were made by Dicksong Wong and Lucas Ashbury-Bridgwood.

# License

* This is released under the GNU GENERAL PUBLIC LICENSE Version 3. See the LICENSE file that was distributed with this game.
