#!/usr/bin/env python 

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

# package: MVC
# file: controller.py
# date: 15-05-14
# author: Victor Neville

import os
import time

class Controller:

    # Function that allows the user to enter an integer on the keyboard.
    def __getInteger(self, msg):
        if not isinstance(msg, str):
            return
            
        value = ''
        
        # loop while value is a string
        while isinstance(value, str):
            os.system('clear')
            value = input(msg)
            try:
                value = int(value)
            except:
                print('The value must be an integer.')
        return value
    
    # Function that allows the user to enter a string on the keyboard.
    def __getStr(self, msg, vals):
        
        # validate args
        if not isinstance(msg, str) or not isinstance(vals, tuple):
            return
    
        os.system('clear')
        value = input(msg).lower()
        
        # loop while the user value is not valid    
        while not value in vals:
            os.system('clear')
            value = input(msg).lower()
        return value

    # Function that allows the user to enter an input on the keyboard.
    def __getInput(self, mode=None):
        value = None
        
        if mode == 'first operand':
            value = self.__getInteger('Enter first operand: ')
        
        elif mode == 'second operand':
            value = self.__getInteger('Enter second operand: ')
        
        elif mode == 'operation':
            msg = 'Enter the operation:\n- addition\t(a)\n- substraction' + \
                  '\t(s)\n- product\t(p)\n- division\t(d)\n- modulo\t(m)\n'
              
            value = self.__getStr(msg, ('a', 's', 'p', 'd', 'm'))
   
        elif mode == 'continue':
            msg = 'Continue yes(y) or no(n) ? '
            value = self.__getStr(msg, ('y', 'n'))
        return value

    # Function that computes the operation and sets the solution.
    def __setModelSolution(self, first_oper, second_oper, operation):
        
        # validate args
        if not isinstance(first_oper, int) or   \
            not isinstance(second_oper, int) or \
            not isinstance(operation, str):
            return
        
        if operation == 'm':
            self.__model.setSolution(first_oper % second_oper)
        elif operation == 'a':
            self.__model.setSolution(first_oper + second_oper)
        elif operation == 's':
            self.__model.setSolution(first_oper - second_oper)
        elif operation == 'p':
            self.__model.setSolution(first_oper * second_oper)
        else:
            self.__model.setSolution(first_oper / float(second_oper))
    
    # Constructor
    def __init__(self, view, model):
        self.__view = view
        self.__model = model
       
        done = False
           
        while not done:
            first_oper = self.__getInput(mode='first operand')
            second_oper = self.__getInput(mode='second operand')
            operation = self.__getInput(mode='operation')
                                                          
            self.__setModelSolution(first_oper, second_oper, operation)
            view.printModel(model)
            time.sleep(2)
            
            if self.__getInput(mode='cotinue') == 'n': 
                done = True
