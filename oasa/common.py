# Copyright (C) 2003-2008 Beda Kosata <beda@zirael.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>



def gen_combinations_of_series(series):
    """series is a list of lists (tuples), the generator yields
    lists by combining each element of each list with each other"""
    counter = len(series) * [0]
    end = [i-1 for i in map(len, series)]
    counter[0] = -1  # dirty trick
    while counter != end:
        for i, e in enumerate(end):
            if counter[i] < e:
                counter[i] += 1
                for j in range(i):
                    counter[j] = 0
                break
        yield [s[counter[j]] for j, s in enumerate(series)]


def is_uniquely_sorted(series, sorting_function=None):
    """Take a *sorted* series and tell if all the items are unique.

    """
    if sorting_function is None:
        for i in range(len(series) - 1):
            if series[i] == series[i+1]:
                return False
    else:
        for i in range(len(series) - 1):
            if sorting_function(series[i], series[i+1]) == 0:
                return False
    return True


def least_common_item(series):
    d = {}
    for i in series:
        d[i] = d.get(i, 0) + 1
    return list(d.keys())[list(d.values()).index(min(d.values()))]
