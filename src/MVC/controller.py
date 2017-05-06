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

# @package: MVC
# @file: controller.py
# @description: Implementation of the Controller class.
# @date: 15-05-14
# @author: Victor Neville

import os
import time

class Controller:

	###########################################################################
    # @name: __getInteger
    # @description: Allows the user to enter an integer on the keyboard.
    # @inputs:
    # - self: the Controller object
    # - msg: the input message that has to be displayed
    # @returns: the integer chosen by the user
    def __getInteger(self, msg):            
        value = ''
        
        # loop while value is not a digit
        while not value.isdigit():
            os.system('clear')
            value = input(msg)

        return int(value)
    
    ###########################################################################
    # @name: __getStr
    # @description: Allows the user to enter a string on the keyboard.
    # @inputs:
    # - self: the Controller object
    # - msg: the input message that has to be displayed
    # - vals: values that can be accepted
    # @returns: the string chosen by the user
    def __getStr(self, msg, vals):
    
        # validate args
        if not isinstance(msg, str) or not hasattr(vals, '__iter__'):
            return None
    
        os.system('clear')
        value = input(msg).lower()
        
        # loop while the user value is not valid    
        while not value in vals:
            os.system('clear')
            value = input(msg).lower()
        return value
    
    ###########################################################################
    # @name: __getInput
    # @description: Allows the user to enter an input on the keyboard.
    # @inputs:
    # - self: the Controller object
    # - mode: the input mode
    # @returns: the input chosen by the user
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
    
    ###########################################################################
    # @name: __setModelSolution
    # @description: Computes basic arithmetic operations and sets the solution.
    # @inputs:
    # - self: the Controller object 
    # - first_oper: the first operand
    # - second_oper: the second operand
    # - operation: the arithmetic operation
    def __setModelSolution(self, first_oper, second_oper, operation):
        if operation == 'm':
            self.__model.setSolution(first_oper % second_oper)
        elif operation == 'a':
            self.__model.setSolution(first_oper + second_oper)
        elif operation == 's':
            self.__model.setSolution(first_oper - second_oper)
        elif operation == 'p':
            self.__model.setSolution(first_oper * second_oper)
        elif operation == 'd':
            self.__model.setSolution(first_oper / float(second_oper))
        else:
            self.__model.setSolution(None)
    
    ###########################################################################
    # @name: __init__
    # @description: The constructor of the Controller object.
    # @inputs:
    # - self: the Controller object 
    # - view: the View object
    # - model: the Model object
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
            
            if self.__getInput(mode='continue') == 'n': 
                done = True