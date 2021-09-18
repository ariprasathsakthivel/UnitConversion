'''
@Author: Ariprasath
@Date: 2021-09-17 17:11:50
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-18
Title: convert the lengths from feet to inch and feet to yard
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

    def feet_yard(self,length):
        '''
        Description:
            Converts the length from feet to yard
        Parameter:
            length(int): length in feet
        Return:
            length_yard(float): length in inch with 2 decimal precision
        '''
        try:
            if length==None:
                return None
            elif length >=0:
                length_yard=length/3
                return round(length_yard,2)
            else:
                raise Exception
        except Exception as e:
            print(e)
