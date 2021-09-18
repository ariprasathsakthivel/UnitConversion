'''
@Author: Ariprasath
@Date: 2021-09-17 17:09:50
@Last Modified by: Ariprasath
@Last Modified time: 2021-09-18
Title: Test the unit conversion module using pytest
'''

import pytest
from UnitConversion import UnitConv



class TestUnitCOnversion():

    @pytest.fixture(scope="function")
    def obj(self):
        self.obj1=UnitConv()

    def test_feet_to_inch(self,obj):

        #Equality checks
        #Test case-1  Zero check
        assert self.obj1.feet_inch(0)==0

        #Test case-2 Null check
        assert self.obj1.feet_inch(None)==None

        #Test case-3  Reference check
        assert self.obj1.feet_inch(1)==12

        #Test case-4  Type check
        assert type(self.obj1.feet_inch(1))==int

        #Test case-5  Value check
        assert self.obj1.feet_inch(2)==24

        #Comparison check
        #Test case-6 
        assert self.obj1.feet_inch(1)!=1

        #Test case-7
        assert self.obj1.feet_inch(1)>1

        #Test case-8
        assert self.obj1.feet_inch(1)<13


        
    def test_feet_to_yard(self,obj):

        #Equality checks
        #Test case-1  Zero check
        assert self.obj1.feet_yard(0)==0

        #Test case-2 Null check
        assert self.obj1.feet_yard(None)==None

        #Test case-3  Reference check
        assert self.obj1.feet_yard(1)==0.33
        #Test case-4  Type check
        assert type(self.obj1.feet_yard(1))==float

        #Test case-5  Value check
        assert self.obj1.feet_yard(6)==2

        #Comparison check
        #Test case-6 
        assert self.obj1.feet_yard(1)!=1

        #Test case-7
        assert self.obj1.feet_yard(1)<1

        #Test case-8
        assert self.obj1.feet_yard(1)>0