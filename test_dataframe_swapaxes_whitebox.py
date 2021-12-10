
import pandas as pd
import numpy as np
import unittest
import coverage

''' Here I am whitebox testing the swapaxes function and the goal is to get 100% statement coverage. So I have looked at the code
    and tried to get all lines executed.
    
    We get:

    Name                                  Stmts   Miss  Cover   Missing
    -------------------------------------------------------------------
    test_dataframe_swapaxes_whitebox.py      34      0   100%
    -------------------------------------------------------------------
    TOTAL                                    34      0   100%

    
'''

# Here is the function we are testing
def swap_axes(frame, axis1, axis2, copy=True):
    """
    Interchange axes and swap values axes appropriately.
    Returns
    -------
    y : same as input
    """
    i = frame._get_axis_number(axis1)
    j = frame._get_axis_number(axis2)

    if i == j:
        if copy:
            return frame.copy()
        return frame

    mapping = {i: j, j: i}

    new_axes = (frame._get_axis(mapping.get(k, k)) for k in range(frame._AXIS_LEN))
    new_values = frame.values.swapaxes(i, j)
    if copy:
        new_values = new_values.copy()

    # ignore needed because of NDFrame constructor is different than
    # DataFrame/Series constructors.
    return frame._constructor(
        # error: Argument 1 to "NDFrame" has incompatible type "ndarray"; expected
        # "Union[ArrayManager, BlockManager]"
        # error: Argument 2 to "NDFrame" has incompatible type "*Generator[Index,
        # None, None]"; expected "bool" [arg-type]
        # error: Argument 2 to "NDFrame" has incompatible type "*Generator[Index,
        # None, None]"; expected "Optional[Mapping[Hashable, Any]]"
        new_values,  # type: ignore[arg-type]
        *new_axes,  # type: ignore[arg-type]
    ).__finalize__(frame, method="swapaxes")




class TestUnique(unittest.TestCase):
    '''Functions for testing the unique in pandas index'''

    def setUp(self):
        #original
        self.df1 = pd.DataFrame({"A":[10, 11, 7, 8, 5],
                   "B":[21, 5, 32, 4, 6],
                   "C":[11, 21, 23, 7, 9],
                   "D":[1, 5, 3, 8, 6]}, 
                   index =["A1", "A2", "A3", "A4", "A5"])

        #swapped
        self.df2 = pd.DataFrame({"A1":[10, 21, 11, 1], 
                                 "A2":[11, 5, 21, 5], 
                                 "A3":[7, 32, 23, 3], 
                                 "A4":[8, 4, 7, 8], 
                                 "A5":[5, 6, 9, 6]},   
                   index =["A", "B", "C", "D"])

        self.df3 = pd.DataFrame({"A":[0]}, 
                        index =["A"])



    def test_unique_whitebox(self):

        #This first test gets most of the lines, except for lines 33-35.
        df1_swapped = swap_axes(self.df1,axis1="index", axis2="columns")
        # making array that is only True if all equal
        bool_arr = ((df1_swapped == self.df2).eq(True).all())
        self.assertTrue(bool_arr[0].all())

        #The two tests below cover lines 33-35.

        #giving same index. so if we want to swap something with itself, nothing should
        #change
        df3_swapped = swap_axes(self.df3,axis1="index", axis2="index")
        bool_arr = ((df3_swapped == self.df3).eq(True).all())
        self.assertTrue(bool_arr[0].all())

        #giving same index, without a copy.
        df3_swapped = swap_axes(self.df3,axis1="index", axis2="index",copy=False)
        bool_arr = ((df3_swapped == self.df3).eq(True).all())
        self.assertTrue(bool_arr[0].all())


if __name__ == '__main__':
    unittest.main()
