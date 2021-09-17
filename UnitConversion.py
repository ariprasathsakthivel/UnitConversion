'''
@Author: Ariprasath
@Date: 2021-09-17 17:11:50
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-17
Title: convert the lengths from feet to inch
'''





class UnitConv():

    def feet_inch(self,length):
        '''
        Description:
            Converts the length from feet to inch
        Parameter:
            length(int): length in feet
        Return:
            length_inch(int): length in inch
        '''
        try:
            if length==None:
                return None
            elif length >=0:
                length_inch=length*12
                return length_inch
            else:
                raise Exception
        except Exception as e:
            print(e)