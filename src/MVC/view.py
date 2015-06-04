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
# file: view.py
# date: 15-05-14
# author: Victor Neville
#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *

# Constant strings
MSG = ("Enter the operation:\n- addition\t(a)\n- substraction", 
       "\t(s)\n- product\t(p)\n- division\t(d)\n- modulo\t(m)\n") 

class View:
    def __init__(self):
        self.__first_num = self.__sol = None
        self.__scnd_num = self.__oper = None

    def getInput(self, mode=None):
        val=None
        while True:
            if mode == 1:
                val = raw_input("Enter the first number: ")
                if val.isdigit():
                    self.__first_num = val = int(val)
                    break 
            elif mode == 2:
                val = raw_input("Enter the second number: ")
                if val.isdigit():
                    self.__scnd_num = val = int(val)
                    break
            elif mode == 'continue':
                val = raw_input("Continue (y or n): ").lower()
                if val == 'y' or val == 'n': break
            elif mode == 'oper': 
                val = raw_input(MSG[0] + MSG[1])
                if val == 'a' or val == 's' or val == 'p' or val == 'd' or val == 'm': 
                    self.__oper = val
                    break
            else: break
        return val

    def setSolution(self, sol):
        self.__sol = sol
        print 'Result =', self.__sol
