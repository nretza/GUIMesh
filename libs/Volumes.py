#########################################################################################################
#    GUIMesh v1                                                                                         #
#                                                                                                       #
#    Copyright (c) 2018  Marco Gui Alves Pinto mail:mgpinto11@gmail.com                                 #
#                                                                                                       #
#    This program is free software: you can redistribute it and/or modify                               #
#    it under the terms of the GNU General Public License as published by                               #
#    the Free Software Foundation, either version 3 of the License, or                                  #
#    (at your option) any later version.                                                                #
#                                                                                                       #
#    This program is distributed in the hope that it will be useful,                                    #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                                     #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                      #
#    GNU General Public License for more details.                                                       #
#                                                                                                       #
#    You should have received a copy of the GNU General Public License                                  #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>                              #
#                                                                                                       #
#########################################################################################################

class Volume():

    def __init__(self,myvolume,myMMD,myGDMLoption):

        self.VolumeCAD=myvolume
        self.VolumeMMD=myMMD
        self.VolumeGDMLoption=myGDMLoption
        self.setLabel()

    def setLabel(self):

        #get label
        label = str(self.VolumeCAD.Label)

        #can not contain special characters
        invalid_chars = [ ':', '@', '$', '%', '&', '/', '+', ',', ';', ' ', '.']

        for char in invalid_chars:
            label = label.replace(char, "_")

        # has to start with [a-zA-Z]
        if not label[0].isalpha():
            label = "a_" + label
        
        self.VolumeCAD.Label = label