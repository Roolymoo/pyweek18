##############################################################################
# Copyright (C) 2013 Dickson Wong, Lucas Ashbury-Bridgwood
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##############################################################################

import random
import os.path
from zone import Tile, Zone


def get_test_zone():
    '''(NoneType) -> Zone'''
    test_zone = Zone()

    random.seed()

    MIN = -20
    MAX = 20

    for i in range(test_zone.num_tiles_w):
        for j in range(test_zone.num_tiles_h):
            test_zone.map[i][j].value = random.randint(MIN, MAX)

    # Make some tiles walls
    WALL_PATH = os.path.join("art", "Stone.png")
    WALL_V_DISPLACEMENT = int(test_zone.num_tiles_h / 3)
    for i in range(int(test_zone.num_tiles_w / 2)):
        test_zone.map[i][WALL_V_DISPLACEMENT].load_img(WALL_PATH)
        test_zone.map[i][WALL_V_DISPLACEMENT * 2].load_img(WALL_PATH)
    j = WALL_V_DISPLACEMENT
    while j <= WALL_V_DISPLACEMENT * 2:
        # Use last used i
        test_zone.map[i][j].load_img(WALL_PATH)
        j += 1

    return test_zone
