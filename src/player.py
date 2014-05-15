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
from globals import get_tile_size


class Player:
    def __init__(self, X, Y):
        '''(Player, int, int) -> NoneType
        (X,Y) are the coordinates (in tiles) of the player
        '''
        SIZE = get_tile_size()

        self.x = X;
        self.y = Y;
        self.rect = Rect(X, Y, SIZE, SIZE)
        self.img = None
        self.value = 0;

    def load_img(self, IMG_PATH):
        '''(Tile, str) -> NoneType
        Loads img given by IMG_PATH into self.img as Surface. Assumes
        IMG_PATH valid.
        '''
        self.img = image.load(IMG_PATH)

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Draws the player image onto the Surface window.  Assumes coordinates
        of the player are valid.
        '''
        PADDING_W = 20
        PADDING_H = 20
        WHITE = (255, 255, 255)

        # Render img if there is one - there better be one
        if self.img:
            window.blit(self.img, self.rect)
        # Render value text
        self.rect = Rect(X, Y, SIZE, SIZE)
        window.blit(SURFACE, (self.rect.x + PADDING_W, self.rect.y + PADDING_H))

    def move(self, direction, zone, window):
        '''(Zone, str, Zone, Surface) -> NoneType
        Attempts to move the player in the direction given (in Zone) and then
        redraws player if necessary.
        '''
        new_x = self.x
        new_y = self.y

        #find the new coordinates
        if (direction == "LEFT"):
            new_x -= 1
        elif (direction == "RIGHT"):
            new_x += 1
        elif (direction == "UP"):
            new_y -= 1
        elif (direction == "DOWN"):
            new_y += 1
        else:
            return

        new_tile = zone.map[new_x][new_y]

        #in the case of an obstacle, no need for further action
        if (new_tile.obstacle):
            return

        elif (new_tile.trap):
            self.value += new_tile.value

            #Remove the trap and it is now a normal floor tile
            new_tile.trap = False
            new_tile.trapimg = None

        else:
            self.x = new_x
            self.y = new_y

        new_tile.render(window)
        self.render(window)

