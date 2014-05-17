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


if __name__ == "__main__":
    random.seed()

    MIN = -10
    MAX = 10
    NUM_TILES_W = 10
    NUM_TILES_H = 12

    FILE_N = "new.txt"
    with open(os.path.join("data", "zone", FILE_N), "w") as FILE:
        FILE.write("map\n")

        for i in range(NUM_TILES_H):
            for j in range(NUM_TILES_W):
                tile = "0,2,{},0  ".format(random.randint(MIN, MAX))

                FILE.write(tile)

            FILE.write("\n")
