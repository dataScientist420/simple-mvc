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
# @file: view.py
# @description: Implementation of the View class.
# @date: 15-05-14
# @author: Victor Neville 

class View:

    ###########################################################################
    # @name: __init__
    # @description: The constructor of the View object.
    # @inputs: 
    # - self: the View object
    def __init__(self):
        pass

	###########################################################################
    # @name: printModel
    # @description: Displays the solution of the Model.
    # @inputs: 
    # - self: the View object
    # - model: the Model object
    def printModel(self, model):
        print('Result =', model.getSolution())
