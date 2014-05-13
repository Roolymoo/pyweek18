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
from zone import Tile, Zone


def get_test_zone():
    '''(NoneType) -> Zone'''
    test_zone = Zone()

    random.seed()

    MIN = -128
    MAX = 127

    for i in range(test_zone.width):
        for j in range(test_zone.height):
            test_zone.map[i][j].value = random.randint(MIN, MAX)

    return test_zone