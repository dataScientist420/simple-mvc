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
# @file: model.py
# @description: Implementation of the Model class.
# @date: 15-05-14
# @author: Victor Neville

class Model:

    ###########################################################################
    # @name: __init__
    # @description: The constructor of the Model object.
    # @inputs: 
    # - self: the Model object
    def __init__(self):
        self.__solution = None

    ###########################################################################
    # @name: setSolution
    # @description: Setter of the solution.
    # @inputs: 
    # - self: the Model object
    # - solution: the solution value
    def setSolution(self, solution):
        self.__solution = solution
    
    ###########################################################################
    # @name: getSolution
    # @description: Getter of the solution.
    # @inputs: 
    # - self: the Model object
    # @return: the solution value    
    def getSolution(self):
        return self.__solution
