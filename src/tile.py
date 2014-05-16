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
from img import load_img

class Tile:
    def __init__(self, X, Y):
        '''(Tile, int, int) -> NoneType
        (X,Y) top-left coordinate of tile.'''
        SIZE = get_tile_size()

        self.rect = Rect(X, Y, SIZE, SIZE)
        self.img = None
        self.value = None # In case text value should not be rendered
        self.obstacle = False
        self.trap = False
        self.trapimg = None

    #---------------------------------------obsolete
    def set_trap(self, type):
        '''(StaticTile, Surface) -> NoneType
        '''
        self.trap = True

        if (type == "FIRE"):
            self.trapimg = load_img("Fire2.png")
        elif (type == "SPIKE"):
            self.trapimg = load_img("Spike.png")
        elif (type == "POOP"):
            self.trapimg = load_img("Poop.png")
        else:
            self.trapimg = load_img("Poop.png")
    #---------------------------------------------------

    def load_img(self, IMG_N):
        '''(Tile, str) -> NoneType
        Loads img given by IMG_N into self.img as Surface. Assumes
        IMG_N valid.'''
        self.img = load_img(IMG_N)

    def load_trapimg(self, IMG):
        '''(Tile, str) -> NoneType
        Load IMG into self.trapimg. Assumes we want a trap here.
        '''
        self.trapimg = load_img(IMG)

    def render(self, window):
        '''(StaticTile, Surface) -> NoneType
        Renders self.img if not None, then renders the trap img if not None,
        then renders self.value in text on top if self.value is not None.'''
        PADDING_W = 20
        PADDING_H = 20
        FONT_SIZE = 20
        WHITE = (255, 255, 255)

        # Render img
        if self.img:
            window.blit(self.img, self.rect)

        # Then render the trap
        if self.trap:
            window.blit(self.trapimg, self.rect)

        # Prepare text for value
        if self.value != None:
            # Load the font into a Surface
            FONT = Font(None, FONT_SIZE) # Use default font
            SURFACE = FONT.render(str(self.value), False, WHITE)
            # Render the font
            window.blit(SURFACE, (self.rect.x + PADDING_W, self.rect.y + PADDING_H))

