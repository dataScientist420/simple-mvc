#!/usr/bin/env python 

#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# package: MVC
# file: model.py
# date: 15-05-14
# author: Victor Neville
#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *

class Model:
    def __init__(self):
        self.__solution = 0

    def calculate(self, a, b, oper):
        if oper is 'm':
            self.__solution = a % b
        elif oper is 'a':
            self.__solution = a + b
        elif oper is 's':
            self.__solution = a - b
        elif oper is 'p':
            self.__solution = a * b
        else:
            self.__solution = a / float(b)

    def get_solution(self):
        return self.__solution
