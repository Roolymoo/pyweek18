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

def get_window_dim():
    '''(NoneType) -> tuple
    Returns (WINDOW_W, WINDOW_H).'''
    # Just doing square window atm
    SIZE = get_tile_size() * 12
    return (SIZE, SIZE)

def get_tile_size():
    '''(NoneType) -> int
    Returns global tile size. Tiles are square.'''
    return 50
