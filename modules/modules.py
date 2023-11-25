# ------ getting modules of an upper (parent) directory ------
import sys, os

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# getting the parent directory name where the current directory is present.
parent_dir = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent_dir)
# now we can import the modules in the parent directory.
from mini_projects.rps import rps
from mini_projects.guess_number import guess_number
from mini_projects.arcade import arcade

# using the module.
rock_paper_scissors = rps()
rock_paper_scissors()

guess_my_number = guess_number()
guess_my_number()

arcade()

# --------------- some examples ---------------
from math import pi

print(pi)

import random as rdm

for item in dir(rdm):
    print(item)

import kansas

print(kansas.capital)
kansas.randomfunfact()
print(__name__)  # __main__
print(kansas.__name__)  # kansas
