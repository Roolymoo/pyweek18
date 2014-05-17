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
from pygame import display, time, Rect
from pygame.font import Font
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from globals import get_window_dim, get_fps
from zone import Zone
from sumtracker import SumTracker
from keystracker import KeysTracker


def main():
    '''(NoneType) -> NoneType'''
    WINDOW_W, WINDOW_H = get_window_dim()

    pygame.init()

    fps_clock = time.Clock()
    FPS = get_fps()

    window = display.set_mode((WINDOW_W, WINDOW_H))

    # Set up arg parser to get the zone
    arg_parser = ArgumentParser()
    # Add the zone argument
    arg_parser.add_argument("zone", help="the zone to play, relative to data/zone")
    # Get the arg
    args = arg_parser.parse_args()

    ZONE = args.zone

    zone = Zone()
    zone.load(ZONE) # This loads the player

    sum_tracker = SumTracker(zone.player)
    keys_tracker = KeysTracker(zone.player, sum_tracker) # Put it below sum_tracker

    zone.render(window)
    sum_tracker.render(window)
    keys_tracker.render(window)

    display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            # Check for game over
            elif (zone.player.sum < -128) or (zone.player.sum > 127):
                # Game over
                # Render text to screen saying game is over
                FONT_SIZE = 50
                WHITE = (255, 255, 255)
                BLACK = (0, 0, 0)
                FONT = Font(None, FONT_SIZE)
                X1, Y1 = 50, 100
                X2, Y2 = 50, 150
                X3, Y3 = 50, 250
                # Check for underflow or overflow
                if zone.player.sum < -128:
                    status = "UNDERFLOW"
                else:
                    status = "OVERFLOW"
                FONT_S1 = FONT.render("GAMEOVER!", False, WHITE)
                FONT_S2 = FONT.render("YOU CREATED AN {}!".format(status), False, WHITE)
                FONT_S3 = FONT.render("Click to exit...", False, WHITE)
                # Black out window
                window.fill(BLACK)
                # Render text
                window.blit(FONT_S1, (X1, Y1))
                window.blit(FONT_S2, (X2, Y2))
                window.blit(FONT_S3, (X3, Y3))

                display.flip()

                # Wait for a click
                new_event = pygame.event.wait()
                while new_event.type != MOUSEBUTTONDOWN:
                    new_event = pygame.event.wait()

                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    zone.move_player("LEFT", window)
                elif event.key == pygame.K_RIGHT:
                    zone.move_player("RIGHT", window)
                elif event.key == pygame.K_UP:
                    zone.move_player("UP", window)
                elif event.key == pygame.K_DOWN:
                    zone.move_player("DOWN", window)
                # Update trackers
                sum_tracker.render(window)
                keys_tracker.render(window)

                display.flip()

        fps_clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
