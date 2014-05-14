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

from pygame import Rect, image
from pygame.font import Font
from globals import get_tile_size


class Tile:
    def __init__(self, X, Y):
        '''(Tile, int, int) -> NoneType
        (X,Y) top-left coordinate of tile.'''
        SIZE = get_tile_size()

        self.rect = Rect(X, Y, SIZE, SIZE)
        self.img = None
        self.value = 0

    def load_img(self, IMG_PATH):
        '''(Tile, str) -> NoneType
        Loads img given by IMG_PATH into self.img as Surface. Assumes
        IMG_PATH valid.'''
        self.img = image.load(IMG_PATH)

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Draws self.value is a number with padding given below within self.rect
        relative to window.'''
        PADDING_W = 20
        PADDING_H = 20
        FONT_SIZE = 20
        WHITE = (255, 255, 255)

        # Prepare text for value
        FONT = Font(None, FONT_SIZE) # Use default font
        SURFACE = FONT.render(str(self.value), False, WHITE)

        # Render img if there is one
        if self.img:
            window.blit(self.img, self.rect)
        # Render value text
        window.blit(SURFACE, (self.rect.x + PADDING_W, self.rect.y + PADDING_H))
