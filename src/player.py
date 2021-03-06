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
from pygame import Rect, image
from globals import get_tile_size
from img import load_img


class Player:
    def __init__(self, X, Y):
        '''(Player, int, int) -> NoneType
        (X,Y) are the coordinates (in tiles) of the player
        '''
        self.x = X
        self.y = Y
        self.rect = None
        self.update_rect()
        self.img = load_img("Bob.png")
        self.sum = 0
        self.keys = 0 # Number of keys in inventory
        self.win = False # Wins when reaches exit

    def load_img(self, IMG_N):
        '''(Tile, str) -> NoneType
        Loads img given by IMG_N into self.img as Surface. Assumes
        IMG_N valid.
        '''
        self.img = load_img(IMG_N)

    def render(self, window):
        '''(Zone, Surface) -> NoneType
        Draws the player image onto the Surface window.  Assumes coordinates
        of the player are valid.
        '''
        # Render img if there is one - there better be one
        if self.img:
            window.blit(self.img, self.rect)

    def change_sum(self, val, zone, window):
        '''(Player, int, Zone, window) -> NoneType
        Attempts to change self.sum; if the player goes over 155 or under -156,
        the game is over.
        '''
        self.sum += val
        if (self.sum > 127) or (self.sum < -128):
            #you die hereg
            return

    def update_rect(self):
        '''(Player) -> NoneType
        Updates the location of self.rect.
        '''
        SIZE = get_tile_size()
        self.rect = Rect(self.x * SIZE, self.y * SIZE, SIZE, SIZE)

    def move(self, direction, zone, window):
        '''(Player, str, Zone, Surface) -> NoneType
        Attempts to move the player in the direction given (in Zone) and then
        redraws player if necessary.
        '''
        new_x = self.x
        new_y = self.y

        #find the new coordinates
        if (direction == "LEFT"):
            if new_x != 0:
                new_x -= 1
        elif (direction == "RIGHT"):
            if new_x != zone.num_tiles_w - 1:
                new_x += 1
        elif (direction == "UP"):
            if new_y != 0:
                new_y -= 1
        elif (direction == "DOWN"):
            if new_y != zone.num_tiles_h - 1:
                new_y += 1
        else:
            return

        new_tile = zone.map[new_x][new_y]

        #in the case of an obstacle (wall, lock with no key), no need for further action
        if new_tile.wall:
            return
        elif new_tile.lock and (self.keys == 0):
            return

        #otherwise, erase the current space and move to new space
        zone.map[self.x][self.y].render(window)
        new_value = new_tile.value # For updating (eg traps, keys)
        if (new_tile.trap):
            #Remove the trap and it is now a normal floor tile
            new_tile.trap = False
            new_tile.trapimg = None
            new_value = 0
        elif new_tile.key:
            # Remove the key, give it to player
            self.keys += 1
            new_tile.key = False
            new_tile.key_img = None
            new_value = 0
        elif new_tile.lock:
            # Player has > 0 keys because already checked if only 0
            # Use a key to open the lock
            self.keys -= 1
            # Remove the lock
            new_tile.lock = False
            new_tile.lock_img = None
        elif new_tile.exit:
            self.win = True

        if (new_x == self.x) and (new_y == self.y):
            # Dont update value
            update_value = False
        else:
            update_value = True

        self.x = new_x
        self.y = new_y
        new_tile.render(window)

        self.update_rect()
        self.render(window)
        if update_value:
            self.change_sum(new_tile.value, zone, window)
        # Update value
        new_tile.value = new_value
