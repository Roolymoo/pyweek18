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

from pygame import Rect
from pygame.font import Font
from globals import get_window_dim, get_tile_size


class Tile:
    def __init__(self, X, Y):
        '''(Tile, int, int) -> NoneType
        (X,Y) top-left coordinate of tile.'''
        SIZE = get_tile_size()

        self.rect = Rect(X, Y, SIZE, SIZE)
        self.value = 0

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Draws self.value is a number with padding given below within self.rect
        relative to window.'''
        PADDING_W = 20
        PADDING_H = 20
        FONT_SIZE = 20
        COLOUR = (255, 255, 255)

        FONT = Font(None, FONT_SIZE) # Use default font
        SURFACE = FONT.render(str(self.value), False, COLOUR)
        window.blit(SURFACE, (self.rect.x + PADDING_W, self.rect.y + PADDING_H))


class Zone:
    def __init__(self):
        '''(Zone) -> NoneType'''
        WINDOW_W, WINDOW_H = get_window_dim()
        NUM_TILES_W = int(WINDOW_W / get_tile_size()) # Assumed to get integer
        NUM_TILES_H = int(WINDOW_H / get_tile_size())

        self.width = NUM_TILES_W
        self.height = NUM_TILES_H
        self.map = [[Tile(i * 50, j * 50) for j in range(NUM_TILES_H)] for i in range(NUM_TILES_W)]

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Renders all Tiles in self.map.'''
        for i in range(self.width):
            for j in range(self.height):
                self.map[i][j].render(window)
