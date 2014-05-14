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

from pygame import draw
from globals import get_window_dim, get_tile_size
from tile import Tile

class Zone:
    def __init__(self):
        '''(Zone) -> NoneType'''
        WINDOW_W, WINDOW_H = get_window_dim()
        TILE_SIZE = get_tile_size()
        NUM_TILES_W = int(WINDOW_W / TILE_SIZE) # Assumed to get integer in division
        NUM_TILES_H = int(WINDOW_H / TILE_SIZE)

        self.num_tiles_w = NUM_TILES_W
        self.num_tiles_h = NUM_TILES_H
        self.map = [[Tile(i * 50, j * 50) for j in range(NUM_TILES_H)] for i in range(NUM_TILES_W)]

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Renders all Tiles in self.map.'''
        WHITE = (255, 255, 255)
        LINE_WIDTH, LINE_HEIGHT = get_window_dim()
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
