import unittest

import numpy as np
import pandas as pd
from pandas._libs import lib
from pandas._libs.tslibs.timedeltas import parse_timedelta_unit
from pandas.core.dtypes.generic import ABCSeries, ABCIndex
from pandas.core.dtypes.inference import is_list_like
from pandas.core.tools.timedeltas import _convert_listlike, _coerce_scalar_to_timedelta_type


class TestToTimedelta(unittest.TestCase):
    """
    White box test for the pandas.to_timedelta function.
    This tests for coverage.
    Complete coverage was not possible due to requiring the types ABCSeries and ABCIndex, but these seem to be completely
    internal and lack documentation.
    """

    def setUp(self):
        self.td_1a = to_timedelta(1, 'D')
        self.td_1b = to_timedelta('1 days')

        self.td_2a = to_timedelta(None)
        self.td_2b = None

        self.td_3a = to_timedelta(np.array(1))
        self.td_3b = to_timedelta(np.array(1))

        self.td_4a = to_timedelta(['1 D', '2 D'])
        self.td_4b = to_timedelta(['1 days', '2 days'])

    def test_to_timedelta(self):
        self.assertEqual(self.td_1a, self.td_1b)
        self.assertEqual(self.td_2a, self.td_2b)
        self.assertEqual(self.td_3a, self.td_3b)
        self.assertTrue(self.td_4a.equals(self.td_4b))

        self.assertRaises(ValueError, to_timedelta, '1 D', None, 'asdf')
        self.assertRaises(ValueError, to_timedelta, 1, 'Y')
        self.assertRaises(TypeError, to_timedelta, pd.DataFrame([]))
        self.assertRaises(ValueError, to_timedelta, '1 D', 'D')


def to_timedelta(arg, unit=None, errors="raise"):
    if unit is not None:
        unit = parse_timedelta_unit(unit)

    if errors not in ("ignore", "raise", "coerce"):
        raise ValueError("errors must be one of 'ignore', 'raise', or 'coerce'.")

    if unit in {"Y", "y", "M"}:
        raise ValueError(
            "Units 'M', 'Y', and 'y' are no longer supported, as they do not "
            "represent unambiguous timedelta values durations."
        )

    if arg is None:
        return arg
    elif isinstance(arg, ABCSeries):
        values = _convert_listlike(arg._values, unit=unit, errors=errors)
        return arg._constructor(values, index=arg.index, name=arg.name)
    elif isinstance(arg, ABCIndex):
        return _convert_listlike(arg, unit=unit, errors=errors, name=arg.name)
    elif isinstance(arg, np.ndarray) and arg.ndim == 0:
        # extract array scalar and process below
        arg = lib.item_from_zerodim(arg)
    elif is_list_like(arg) and getattr(arg, "ndim", 1) == 1:
        return _convert_listlike(arg, unit=unit, errors=errors)
    elif getattr(arg, "ndim", 1) > 1:
        raise TypeError(
            "arg must be a string, timedelta, list, tuple, 1-d array, or Series"
        )

    if isinstance(arg, str) and unit is not None:
        raise ValueError("unit must not be specified if the input is/contains a str")

    # ...so it must be a scalar value. Return scalar.
    return _coerce_scalar_to_timedelta_type(arg, unit=unit, errors=errors)


if __name__ == '__main__':
    unittest.main()
