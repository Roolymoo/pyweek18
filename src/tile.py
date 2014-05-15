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
    '''Base object for inheritance for tiles actually used in game.'''
    def __init__(self, X, Y):
        '''(Tile, int, int) -> NoneType
        (X,Y) top-left coordinate of tile.'''
        SIZE = get_tile_size()

        self.rect = Rect(X, Y, SIZE, SIZE)
        self.img = None
        self.value = None # In case text value should not be rendered
        self.obstacle = False

    def load_img(self, IMG_PATH):
        '''(Tile, str) -> NoneType
        Loads img given by IMG_PATH into self.img as Surface. Assumes
        IMG_PATH valid.'''
        self.img = image.load(IMG_PATH)


class StaticTile(Tile):
    '''For static entities, such as walls or floors.'''
    def __init__(self, X, Y):
        '''(Tile, int, int) -> NoneType
        (X,Y) top-left coordinate of tile.'''
        Tile.__init__(self, X, Y)

    def render(self, window):
        '''(StaticTile, Surface) -> NoneType
        Renders self.img if not None, then renders self.value in text on top
        if self.value is not None.'''
        PADDING_W = 20
        PADDING_H = 20
        FONT_SIZE = 20
        WHITE = (255, 255, 255)

        # Render img
        if self.img:
            window.blit(self.img, self.rect)

        # Prepare text for value
        if self.value != None:
            # Load the font into a Surface
            FONT = Font(None, FONT_SIZE) # Use default font
            SURFACE = FONT.render(str(self.value), False, WHITE)
            # Render the font
            window.blit(SURFACE, (self.rect.x + PADDING_W, self.rect.y + PADDING_H))
