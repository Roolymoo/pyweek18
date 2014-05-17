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
from globals import get_zone_dim


class SumTracker:
    def __init__(self, player):
        '''(SumTracker, Player) -> NoneType'''
        ZONE_W, ZONE_H = get_zone_dim()
        PADDING_W = 20
        PADDING_H = 20

        self.x = ZONE_W + PADDING_W
        self.y = PADDING_H
        self.text = "SUM"
        self.player = player

    def render(self, window):
        '''(SumTracker, Surface) -> NoneType
        Renders self.player.sum as text, with width, height given by
        generated font.'''
        WHITE = (255, 255, 255)
        FONT_SIZE = 20

        # Load the font into a Surface
        FONT = Font(None, FONT_SIZE) # Use default font
        SURFACE = FONT.render("{}: {}".format(self.text, self.player.sum), False, WHITE)
        # Render the font
        window.blit(SURFACE, (self.x, self.y))
