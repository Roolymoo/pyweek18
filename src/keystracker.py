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


class KeysTracker:
    def __init__(self, player, sum_tracker):
        '''(KeysTracker, Player, SumTracker) -> NoneType'''
        PADDING_H = 20
        # Put it PADDING_H below sum_tracker with same dim
        X = sum_tracker.rect.x
        Y = PADDING_H + sum_tracker.rect.y
        WIDTH = sum_tracker.rect.w
        HEIGHT = sum_tracker.rect.h

        self.rect = Rect(X, Y, WIDTH, HEIGHT)
        self.text = "KEYS"
        self.player = player

    def render(self, window):
        '''(KeysTracker, Surface) -> NoneType
        Renders self.player.keys as text, with width, height given by
        generated font.'''
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        FONT_SIZE = 20

        # Load the font into a Surface
        FONT = Font(None, FONT_SIZE) # Use default font
        SURFACE = FONT.render("{}: {}".format(self.text, self.player.keys), False, WHITE)

        # Clear old sum
        window.fill(BLACK, self.rect)

        # Render the font
        window.blit(SURFACE, self.rect)
