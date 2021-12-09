from __future__ import annotations

import unittest
import pandas as pd

from typing import (
    TYPE_CHECKING,
    Callable,
    Hashable,
    Sequence,
    cast,
)


from pandas._typing import (
    AggFuncType,
    AggFuncTypeBase,
    AggFuncTypeDict,
    IndexLabel,
)
from pandas.util._decorators import (
    Appender,
    Substitution,
)

from pandas.core.dtypes.cast import maybe_downcast_to_dtype
from pandas.core.dtypes.common import (
    is_integer_dtype,
    is_list_like,
    is_nested_list_like,
    is_scalar,
)
from pandas.core.dtypes.generic import (
    ABCDataFrame,
    ABCSeries,
)

import pandas.core.common as com
from pandas.core.frame import _shared_docs
from pandas.core.groupby import Grouper
from pandas.core.indexes.api import (
    Index,
    MultiIndex,
    get_objs_combined_axis,
)
from pandas.core.reshape.concat import concat
from pandas.core.reshape.util import cartesian_product
from pandas.core.series import Series

#if TYPE_CHECKING:
#    from pandas import DataFrame
#Reshape data (produce a “pivot” table) based on column values. Uses unique values from specified index / columns
# to form axes of the resulting DataFrame. This function does not support data aggregation, multiple values will
# result in a MultiIndex in the columns. See the User Guide for more on reshaping.
"""
Test the pandas.pivot(data, index=None, columns=None, values=None) 
function (https://pandas.pydata.org/docs/reference/api/pandas.pivot.html).

The pivot function createes a pivot table based on values given. The function will use
unique values from specified columns to form axes of the DataFram. 

Multiple values will result in a 'MultiIndex' which will not be tested.  
This function does not support data aggregation.

The parameters are the following:
Data (required) which is a DataFrame.
Index (optional)which can be a string or object or a list of strings.  This will be used to make the index of the new frame.
When not used, it will be the index of the current DataFrame.
Columns can be a string, object or a list of stirngs.  This is uesd to make the new frame's columns  
Values is an optional parameter. This will only be used as the default for these tests 

The return will be a pivoted DataFrame.
"""
#To test: empty frame

class test_pivot(unittest.TestCase):
    def setUp(self):
        self.nameArray = ["Alex", "Bob", "Henry", "Charles", "David"]
        self.emptyArray = []
        self.emptyDataFrame = pd.DataFrame(self.emptyArray)
        self.nameArrayDataFrame = pd.DataFrame({'Name': self.nameArray})
        self.df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                                'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                                'baz': [1, 2, 3, 4, 5, 6],
                                'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

        self.pivotDataTestOne = pd.DataFrame({
            'A': [1,4],
            'B': [2,5],
            'C': [3,6]
        }, index=['one', 'two'], columns=['A', 'B', 'C'])
        self.pivotDataTestTwo = pd.DataFrame({
            'A': ['x', 'q'],
            'B': ['y', 'w'],
            'C': ['z', 't']
        }, index=['one', 'two'], columns=['A', 'B', 'C'])
        self.pivotDataTestThree = pd.read_pickle("./pivot_test_three.pkl")
        self.pivotDataTestFour = pd.read_pickle("./pivot_test_four.pkl")
        self.pivotDataTestFive = pd.read_pickle("./pivot_test_five.pkl")
        self.pivotDataTestSix = pd.read_pickle("./pivot_test_six.pkl")

    def test_pivot_whitebox(self):

        #Test for correct data on two data columns
        testOne = pivot(data=self.df, index='foo', columns='bar', values='baz')
        testTwo = pivot(data=self.df, index='foo', columns='bar', values='zoo')
        testThree = pivot(data=self.df, index='foo', columns='bar', values=None)
        testFour = pivot(data=self.df, index=None, columns='bar', values='zoo')
        testFive = pivot(data=self.df, index=None, columns='bar', values=None)
        testSix  = pivot(data=self.df, index=None, columns='bar', values=['bar'])

        with self.assertRaises(TypeError):
            pivot(data=self.df, columns=None)

        self.assertTrue(testOne.equals(self.pivotDataTestOne))
        self.assertTrue(testTwo.equals(self.pivotDataTestTwo))
        self.assertTrue(testThree.equals(self.pivotDataTestThree))
        self.assertTrue(testFour.equals(self.pivotDataTestFour))
        self.assertTrue(testFive.equals(self.pivotDataTestFive))
        self.assertTrue(testSix.equals(self.pivotDataTestSix))

#empty DataFrame
        with self.assertRaises(TypeError):
            pivot()
        with self.assertRaises(TypeError):
            pivot(columns='names')
        with self.assertRaises(TypeError):
            pivot(columns=None)

def pivot(
    data: DataFrame,
    index: IndexLabel | None = None,
    columns: IndexLabel | None = None,
    values: IndexLabel | None = None,
) -> DataFrame:
    if columns is None:
        raise TypeError("pivot() missing 1 required argument: 'columns'")

    columns_listlike = com.convert_to_list_like(columns)

    if values is None:
        if index is not None:
            cols = com.convert_to_list_like(index)
        else:
            cols = []

        append = index is None
        # error: Unsupported operand types for + ("List[Any]" and "ExtensionArray")
        # error: Unsupported left operand type for + ("ExtensionArray")
        indexed = data.set_index(
            cols + columns_listlike, append=append  # type: ignore[operator]
        )
    else:
        if index is None:
            index_list = [Series(data.index, name=data.index.name)]
        else:
            index_list = [data[idx] for idx in com.convert_to_list_like(index)]

        data_columns = [data[col] for col in columns_listlike]
        index_list.extend(data_columns)
        multiindex = MultiIndex.from_arrays(index_list)

        if is_list_like(values) and not isinstance(values, tuple):
            # Exclude tuple because it is seen as a single column name
            values = cast(Sequence[Hashable], values)
            indexed = data._constructor(
                data[values]._values, index=multiindex, columns=values
            )
        else:
            indexed = data._constructor_sliced(data[values]._values, index=multiindex)
    return indexed.unstack(columns_listlike)

