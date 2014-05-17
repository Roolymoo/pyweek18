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

from argparse import ArgumentParser
import pygame
from pygame import display
from pygame.locals import QUIT
from globals import get_window_dim
from zone import Zone
from sumtracker import SumTracker


def main():
    '''(NoneType) -> int'''
    WINDOW_W, WINDOW_H = get_window_dim()

    pygame.init()

    window = display.set_mode((WINDOW_W, WINDOW_H))

    # Set up arg parser to get the zone
    arg_parser = ArgumentParser()
    # Add the zone argument
    arg_parser.add_argument("zone", help="the zone to play, relative to data/zone")
    # Get the arg
    args = arg_parser.parse_args()

    ZONE = args.zone

    test_zone = Zone()
    test_zone.load(ZONE) # This loads the player

    sum_tracker = SumTracker(test_zone.player)

    test_zone.render(window)
    sum_tracker.render(window)

    display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    test_zone.move_player("LEFT", window)
                elif event.key == pygame.K_RIGHT:
                    test_zone.move_player("RIGHT", window)
                elif event.key == pygame.K_UP:
                    test_zone.move_player("UP", window)
                elif event.key == pygame.K_DOWN:
                    test_zone.move_player("DOWN", window)
                # Update sum tracker
                sum_tracker.render(window)
                display.flip()
    pygame.quit()

    return 0

if __name__ == "__main__":
    print(main()) # DEBUG ####################################################
