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

import os.path
import random
from pygame import Rect, draw
from globals import get_window_dim, get_tile_size, get_zone_dim
from tile import StaticTile

class Zone:
    def __init__(self):
        '''(Zone) -> NoneType'''
        WIDTH, HEIGHT = get_zone_dim()
        TILE_SIZE = get_tile_size()
        NUM_TILES_W = int(WIDTH / TILE_SIZE) # Assumed to get integer in division
        NUM_TILES_H = int(HEIGHT / TILE_SIZE)

        self.rect = Rect(0, 0, WIDTH, HEIGHT)
        self.num_tiles_w = NUM_TILES_W
        self.num_tiles_h = NUM_TILES_H
        self.map = [[StaticTile(i * 50, j * 50) for j in range(NUM_TILES_H)] \
                for i in range(NUM_TILES_W)]

    def load(self, ZONE_N):
        '''(Zone, str) -> NoneType
        Loads Zone from Zone given in ZONE_N. Assumes success. Format for
        map files:

        min <int_value>
        max <int_value>
        img <index> <img_name>
        ...
        map
        XYZ ...
        ...
        
        min, max - optional entries to specific inclusive range for randomly
                   generated integers for tile values, which is used if given
                   a ? character
        img      - optional entry or entries to specify images for tiles
                   (images are not required by tiles). <img_name> is added to
                   a list, and <index> corresponds with the index in the list.
        map      - an array of tile entries, which are XYZ, separated by spaces.
                   X is the type of tile to be loaded: S for StaticTile. Y is
                   the img index to used, where 0 means no img. Z is the value
                   to be given to the tile, where ? means a random value
                   generated using min, max'''
        TILE_SIZE = get_tile_size()

        # Seed random in case random values are to be generated
        random.seed()

        PATH = os.path.join("data", "zone", ZONE_N)
        with open(PATH) as FILE:
            min = None
            max = None
            img_list = [None] # None there for use of 0 for no img

            line = FILE.readline()
            while line:
                data = line.split()
                if data[0] == "min":
                    min = int(data[1])
                elif data[0] == "max":
                    max = int(data[1])
                elif data[0] == "img":
                    img_list.append(data[2])
                elif data[0] == "map":
                    # Map is rest of file
                    line = FILE.readline()
                    for i in range(self.num_tiles_h): # Row number of data
                        data = line.split()
                        for j in range(self.num_tiles_w): # Column number of data
                            tile = data[j]
                            # Determine tile type
                            if tile[0] == "S":
                                tile_s = StaticTile(j * TILE_SIZE, i * TILE_SIZE)
                                img_index = int(tile[1])
                                if img_index:
                                    tile_s.load_img(img_list[img_index])
                                if tile[2] == "?":
                                    # Randomize value given by min, max
                                    tile_s.value = random.randint(min, max)
                                else:
                                    tile_s.value = int(tile[2])

                            self.map[j][i] = tile_s

                        line = FILE.readline()

                line = FILE.readline()

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Renders all Tiles in self.map.'''
        WHITE = (255, 255, 255)
        LINE_WIDTH = self.rect.w
        LINE_HEIGHT = self.rect.h
        TILE_SIZE = get_tile_size()

        # Draw tiles and lines defining tiles
        for i in range(self.num_tiles_w):
            # Draw the vertical line for these tiles
            draw.line(window, WHITE, (i * TILE_SIZE, 0), (i * TILE_SIZE, LINE_HEIGHT))
            for j in range(self.num_tiles_h):
                # Draw the horizontal line for these tiles
                draw.line(window, WHITE, (0, j * TILE_SIZE), (LINE_WIDTH, j * TILE_SIZE))
                # Draw the tile
                self.map[i][j].render(window)
