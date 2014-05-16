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

import pygame
from pygame import display
from pygame.locals import QUIT
from globals import get_window_dim
from testzone import get_test_zone2


def main():
    '''(NoneType) -> int'''
    WINDOW_W, WINDOW_H = get_window_dim()

    pygame.init()

    window = display.set_mode((WINDOW_W, WINDOW_H))

    test_zone = get_test_zone2()
    test_zone.render(window)

    display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

    pygame.quit()

    return 0

if __name__ == "__main__":
    print(main()) # DEBUG ####################################################
