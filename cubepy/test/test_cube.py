import unittest
import functools
import numpy as np

from cubepy import Index, Axis, Cube, stack, concatenate
from cubepy.exceptions import InvalidAxisLengthError, NonUniqueDimNamesError
from cubepy.utils import is_axis, is_indexed


def year_quarter_cube():
    """Creates a sample 2D cube with axes "year" and "quarter" with shape (3, 4)."""
    values = np.arange(12).reshape(3, 4)
    ax1 = Index("year", [2014, 2015, 2016])
    ax2 = Index("quarter", ["Q1", "Q2", "Q3", "Q4"])
    return Cube([ax1, ax2],values)


def year_quarter_weekday_cube():
    """Creates 3D cube with axes "year", "quarter", "weekday" with shape (3, 4, 7)."""
    values = np.arange(3 * 4 * 7).reshape(3, 4, 7)
    ax1 = Index("year", [2014, 2015, 2016])
    ax2 = Index("quarter", ["Q1", "Q2", "Q3", "Q4"])
    ax3 = Index("weekday", ["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
    return Cube([ax1, ax2, ax3],values)


class CubeTests(unittest.TestCase):

    def test_empty_cube(self):

        c = Cube(Axis("x", []),[] )
        self.assertEqual(c.ndim, 1)
        self.assertEqual(c.dims, ("x",))
        self.assertEqual(c.size, 0)

        c = Cube( [Axis("x", []), Axis("y", [])],np.empty((0, 0)))
        self.assertEqual(c.ndim, 2)
        self.assertEqual(c.dims, ("x", "y"))
        self.assertEqual(c.size, 0)

    def test_create_scalar(self):

        c = Cube(None,1 )
        self.assertEqual(c.ndim, 0)
        self.assertEqual(c.size, 1)

        c = Cube(None, None)
        self.assertEqual(c.ndim, 0)
        self.assertEqual(c.size, 1)

        c = Cube([],1)
        self.assertEqual(c.ndim, 0)
        self.assertEqual(c.size, 1)

    def test_create_cube(self):
    
        ax1 = Index("A", [10, 20, 30])
        ax2 = Index("B", ["a", "b", "c", "d"])
        ax3 = Index("C", [1.1, 1.2])

        # test Cube.zeros()
        a = Cube.zeros([ax1, ax3])
        self.assertTrue(np.array_equal(a.values, [[0, 0], [0, 0], [0, 0]]))

        # test Cube.ones()
        a = Cube.ones([ax1, ax3])
        self.assertTrue(np.array_equal(a.values, [[1, 1], [1, 1], [1, 1]]))

        # test Cube.full()
        a = Cube.full([ax1, ax3], np.inf)
        self.assertTrue(np.array_equal(a.values, [[np.inf, np.inf], [np.inf, np.inf], [np.inf, np.inf]]))

        # test Cube.full with NaNs
        # note: be careful because NaN != NaN so np.array_equal does not work
        a = Cube.full([ax1, ax3], np.nan)
        np.testing.assert_equal(a.values, [[np.nan, np.nan], [np.nan, np.nan], [np.nan, np.nan]])
        
        # create one-dimensional cube
        values = np.arange(3)
        try:
            Cube((ax1,),values)
            Cube(ax1,values)  # no need to pass axes as collection if there is only one axis
        except Exception:
            self.fail("raised exception unexpectedly")
        
        # two-dimensional cubes
        values = np.arange(12).reshape(3, 4)
        try:
            Cube((ax1, ax2),values)
            Cube([ax1, ax2],values)
        except Exception:
            self.fail("raised exception unexpectedly")


    def test_axes(self):
        """Counting axes, accessing axes by name or index, etc."""
        c = year_quarter_cube()

        # number of dimensions (axes)
        self.assertEqual(c.ndim, 2)
        self.assertEqual(c.dims, ("year", "quarter"))

        # get axis by index, by name and by axis object
        axis1 = c.axis(0)
        axis2 = c.axis("year")
        self.assertTrue( (axis1==axis2).any())
        axis3 = c.axis(-2)  # counting backwards
        self.assertTrue( (axis1==axis3).any())
        axis4 = c.axis(axis1)
        self.assertTrue( (axis1==axis4).any())

        # invalid axis identification raises LookupError
        self.assertRaises(LookupError, c.axis, "bad_axis")
        self.assertRaises(LookupError, c.axis, 3)
        self.assertRaises(LookupError, c.axis, Axis("bad_axis", []))

        # invalid argument types
        self.assertRaises(TypeError, c.axis, 1.0)
        self.assertRaises(TypeError, c.axis, None)

    def test_axis_index(self):
        c = year_quarter_cube()

        # get axis index by name
        self.assertEqual(c.axis_index("year"), 0)
        self.assertEqual(c.axis_index("quarter"), 1)

        # get axis index by Axis object
        self.assertEqual(c.axis_index(c.axis(0)), 0)
        self.assertEqual(c.axis_index(c.axis(1)), 1)

        # get axis index by index (negative turns to positive)
        self.assertEqual(c.axis_index(0), 0)
        self.assertEqual(c.axis_index(-2), 0)

        # invalid axes
        self.assertRaises(LookupError, c.axis_index, "bad_axis")
        self.assertRaises(LookupError, c.axis_index, Axis("bad_axis", []))
        self.assertRaises(LookupError, c.axis_index, 2)

        # invalid argument types
        self.assertRaises(TypeError, c.axis_index, 1.0)
        self.assertRaises(TypeError, c.axis_index, None)

    def test_has_axis(self):
        c = year_quarter_cube()

        # whether axis exists - by name
        self.assertTrue(c.has_axis("year"))
        self.assertFalse(c.has_axis("bad_axis"))

        # whether axis exists - by index (negative index means counting backwards)
        self.assertTrue(c.has_axis(1))
        self.assertFalse(c.has_axis(2))
        self.assertTrue(c.has_axis(-1))
        self.assertFalse(c.has_axis(-3))

        # whether axis exists - by Axis object
        ax1 = c.axis(0)
        self.assertTrue(c.has_axis(ax1))

        # invalid argument types
        self.assertRaises(TypeError, c.has_axis, 1.0)
        self.assertRaises(TypeError, c.has_axis, None)

    def test_getitem(self):
        """Getting items by row and column, slicing etc. using __getitem__(item)"""
        c = year_quarter_cube()

        d = c[0:2, 0:3]
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2], [4, 5, 6]]))
        self.assertEqual(d.ndim, 2)
        self.assertEqual(tuple(d.dims), ("year", "quarter"))
        
        # indexing - will collapse (i.e. remove) axis
        d = c[0]
        self.assertEqual(d.ndim, 1)
        self.assertEqual(d.axis(0).name, "quarter")
        self.assertTrue(np.array_equal(d.values, [0, 1, 2, 3]))

        d = c[:, 0]
        self.assertEqual(d.ndim, 1)
        self.assertEqual(d.axis(0).name, "year")
        self.assertTrue(np.array_equal(d.values, [0, 4, 8]))

        # slicing - will not collapse axis
        d = c[0:1]
        self.assertEqual(d.ndim, 2)
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))

        d = c[slice(0, 1)]
        self.assertEqual(d.ndim, 2)
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))

        d = c[:, 0:1]
        self.assertEqual(d.ndim, 2)
        self.assertTrue(np.array_equal(d.values, [[0], [4], [8]]))

        d = c[(slice(0, None), slice(0, 1))]
        self.assertEqual(d.ndim, 2)
        self.assertTrue(np.array_equal(d.values, [[0], [4], [8]]))

        # using negative indices
        self.assertTrue(np.array_equal(c[-1].values, [8, 9, 10, 11]))
        self.assertTrue(np.array_equal(c[:, -1].values, [3, 7, 11]))

        # wrong index
        self.assertRaises(IndexError, c.__getitem__, 5)
        # eq. C[0, 0, 0] raises IndexError: too many indices
        self.assertRaises(IndexError, c.__getitem__, (0, 0, 0))
        # wring number of slices
        self.assertRaises(IndexError, c.__getitem__, (slice(0, 2), slice(0, 2), slice(0, 2)))

        

    def test_filter(self):
        """Testing function Cube.filter()"""
        c = year_quarter_cube()

        d = c.filter("year", [2014, 2018])  # 2018 is ignored
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[0]).all())

        year_filter = Axis("year", range(2010, 2015))
        d = c.filter(year_filter)
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[0]).all())

        year_filter = Index("year", range(2010, 2015))
        d = c.filter(year_filter)
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[0]).all())

        country_filter = Axis("country", ["DE", "FR"])  # this axis is ignored

        # filter by two axis filters
        quarter_filter = Index("quarter", ["Q1", "Q3"])
        d = c.filter([quarter_filter, country_filter, year_filter])
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[[0, 0], [0, 2]]).all())

        # cube as a filter
        yq_cube_filter = Cube.ones([quarter_filter, year_filter, country_filter])
        d = c.filter(yq_cube_filter)
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[[0, 0], [0, 2]]).all())

        # a collection of cubes as a filter
        y_cube_filter = Cube.ones([year_filter, country_filter])
        q_cube_filter = Cube.ones([country_filter, quarter_filter])
        d = c.filter([y_cube_filter, q_cube_filter])
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[[0, 0], [0, 2]]).all())

    def test_exclude(self):
        """Testing function Cube.exclude()"""

        # TODO complete tests

        c = year_quarter_cube()

        d = c.exclude("year", [2015, 2016, 2018])  # 2018 is ignored
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[0]).all())

        # for large collections it is better for performance to pass the parameter as a set
        d = c.exclude("year", set(range(2015, 3000)))
        self.assertEqual(d.ndim, 2)
        self.assertTrue((d.values == c.values[0]).all())

    def test_apply(self):
        """Applies a function on each cube element."""
        c = year_quarter_weekday_cube()

        # apply vectorized function
        d = c.apply(np.sin)
        self.assertTrue(np.array_equal(np.sin(c.values), d.values))

        # apply non-vectorized function
        import math
        e = c.apply(math.sin)
        self.assertTrue((e == d).all())

        # apply lambda
        f = c.apply(lambda v: 1 if 6 <= v <= 8 else 0)
        self.assertTrue(f.sum(), 3)


        
    def test_squeeze(self):
        """Removes axes which have only one element."""
        ax1 = Index("A", [1])  # has only one element, thus can be collapsed
        ax2 = Index("B", [1, 2, 3])

        c = Cube([ax1, ax2],[[1, 2, 3]] )
        self.assertEqual(c.ndim, 2)
        d = c.squeeze()
        self.assertEqual(d.ndim, 1)
        self.assertEqual(d.axis(0).name, "B")

        c = Cube([ax2, ax1],[[1], [2], [3]])
        self.assertEqual(c.ndim, 2)
        d = c.squeeze()
        self.assertEqual(d.ndim, 1)
        self.assertEqual(d.axis(0).name, "B")

        ax3 = Index("C", [1])  # has only one element, thus can be collapsed
        c = Cube([ax1, ax3],[[1]])
        self.assertEqual(c.ndim, 2)
        d = c.squeeze()  # will collapse both axes
        self.assertEqual(d.ndim, 0)

    def test_transpose(self):
        c = year_quarter_weekday_cube()

        # transpose by axis indices
        d = c.transpose([1, 0, 2])

        self.assertEqual(d.shape, (4, 3, 7))
        self.assertEqual(d.dims, ("quarter", "year", "weekday"))

        # check that original cube has not been changed
        self.assertEqual(c.shape, (3, 4, 7))
        self.assertEqual(c.dims, ("year", "quarter", "weekday"))

        # compare with numpy transpose
        self.assertTrue(np.array_equal(d.values, c.values.transpose([1, 0, 2])))

        # transpose by axis names
        e = c.transpose(["quarter", "year", "weekday"])
        self.assertEqual(e.dims, ("quarter", "year", "weekday"))
        self.assertTrue(np.array_equal(d.values, e.values))
        
        # transpose axes specified by negative indices
        e = c.transpose([-2, -3, -1])
        self.assertTrue(np.array_equal(d.values, e.values))

        # specify 'front' argument (does not need to be specified explicitly)
        e = c.transpose(["quarter", "year"])
        self.assertTrue(np.array_equal(d.values, e.values))
        e = c.transpose([1, 0])
        self.assertTrue(np.array_equal(d.values, e.values))

        # specify 'back' argument
        e = c.transpose(back=["year", "weekday"])
        self.assertTrue(np.array_equal(d.values, e.values))
        e = c.transpose(back=[0, 2])
        self.assertTrue(np.array_equal(d.values, e.values))

        # specify 'front' and 'back' argument
        e = c.transpose(front="quarter", back="weekday")
        self.assertTrue(np.array_equal(d.values, e.values))

        # transpose with wrong axis indices
        self.assertRaises(LookupError, c.transpose, [3, 0, 2])
        self.assertRaises(LookupError, c.transpose, [-5, 0, 1])

        # transpose with wrong axis names
        self.assertRaises(LookupError, c.transpose, ["A", "B", "C"])

        # invalid axis identification raises LookupError
        self.assertRaises(LookupError, c.transpose, ["year", "weekday", "quarter", "A"])
        self.assertRaises(LookupError, c.transpose, [1, 0, 2, 3])

        # duplicate axes raise ValueError
        self.assertRaises(ValueError, c.transpose, [0, 0, 2])
        self.assertRaises(ValueError, c.transpose, ["year", "year", "quarter"])
        self.assertRaises(ValueError, c.transpose, front=["year", "weekday"], back=["year", "quarter"])
        self.assertRaises(ValueError, c.transpose, front=[1, 2], back=[0, 1])

        # invalid types
        self.assertRaises(TypeError, c.transpose, [1.1, 0, 2])
        self.assertRaises(TypeError, c.transpose, [None, "weekday", "year"])

    def test_operations(self):
        values = np.arange(12).reshape(3, 4)
        axc1 = Index("a", [10, 20, 30])
        axc2 = Index("b", ["a", "b", "c", "d"])
        c = Cube([axc1, axc2],values)

        axd1 = Index("a", [10, 20, 30])
        axd2 = Index("b", ["a", "b", "c", "d"])
        d = Cube([axd1, axd2],values)

        x = c * d
        self.assertTrue(np.array_equal(x.values, values * values))

        e = Cube([Index("a", [10, 20, 30])],[0, 1, 2])

        x2 = c * e
        self.assertTrue(np.array_equal(x2.values, values * np.array([[0], [1], [2]])))

        c3 = Cube([Index("b", ["a", "b", "c", "d"])],[0, 1, 2, 3])
        x3 = c * c3
        self.assertTrue(np.array_equal(x3.values, values * np.array([0, 1, 2, 3])))

        c3 = Cube([Index("b", ["b", "a", "c", "d"])],[0, 1, 2, 3])
        x3 = c * c3
        self.assertTrue(np.array_equal(x3.values, values * np.array([1, 0, 2, 3])))

        values_d = np.array([0, 1])
        d = Cube([Index("d", ["d1", "d2"])],values_d)
        x = c * d
        self.assertEqual(x.ndim, 3)
        self.assertEqual(x.axis(0).name, "a")
        self.assertEqual(x.axis(1).name, "b")
        self.assertEqual(x.axis(2).name, "d")

        self.assertTrue(np.array_equal(x.values, values.reshape(3, 4, 1) * values_d))

        # operations with scalar
        d = 10
        x = c * d
        self.assertTrue(np.array_equal(x.values, values * d))
        x = d * c
        self.assertTrue(np.array_equal(x.values, values * d))
        
        # operations with numpy.ndarray
        d = np.arange(4)
        x = c * d
        self.assertTrue(np.array_equal(x.values, values * d))
        x = d * c
        self.assertTrue(np.array_equal(x.values, values * d))
        
        d = np.arange(3).reshape(3, 1)
        x = c * d
        self.assertTrue(np.array_equal(x.values, values * d))
        x = d * c
        self.assertTrue(np.array_equal(x.values, values * d))
        
        # matching Index and Series
        values_d = np.array([0, 1])
        d = Cube(Axis("a", [10, 10]),values_d)
        x = c * d
        self.assertTrue(np.array_equal(x.values, values.take([0, 0], 0) * values_d[:, np.newaxis]))
        
        values_d = np.array([0, 1, 2, 3])
        d = Cube(Axis("b", ["d", "d", "c", "a"]),values_d)
        x = c * d
        self.assertTrue(np.array_equal(x.values, values.take([3, 3, 2, 0], 1) * values_d))

        # unary plus and minus
        c = year_quarter_cube()
        self.assertTrue(np.array_equal((+c).values, c.values))
        self.assertTrue(np.array_equal((-c).values, -c.values))

        c = year_quarter_cube() + 1  # +1 to prevent division by zero error
        import operator as op
        ops = [op.add, op.mul, op.floordiv, op.truediv, op.sub, op.pow, op.mod,  # arithmetics ops
               op.eq, op.ne, op.ge, op.le, op.gt, op.lt,  # comparison ops
               op.rshift, op.lshift]  # bitwise ops

        # operations with scalar
        d = 2
        for op in ops:
            self.assertTrue(np.array_equal(op(c, d).values, op(c.values, d)))
            self.assertTrue(np.array_equal(op(d, c).values, op(d, c.values)))

        # oprations with numpy array
        d = (np.arange(12).reshape(3, 4) / 6 + 1).astype(np.int)  # +1 to prevent division by zero error
        for op in ops:
            self.assertTrue(np.array_equal(op(c, d).values, op(c.values, d)))
            self.assertTrue(np.array_equal(op(d, c).values, op(d, c.values)))

    def test_group_by(self):
        values = np.arange(12).reshape(3, 4)
        ax1 = Axis("year", [2014, 2014, 2014])
        ax2 = Axis("month", ["jan", "jan", "feb", "feb"])
        c = Cube([ax1, ax2],values)
        
        d = c.reduce(np.mean, group=0)  # average by year
        self.assertTrue(np.array_equal(d.values, np.array([[4, 5, 6, 7]])))
        self.assertTrue(is_indexed(d.axis(0)))
        self.assertEqual(len(d.axis(0)), 1)
        self.assertEqual(d.values.shape, (1, 4))  # axes with length of 1 are not collapsed

        d = c.reduce(np.sum, group=ax2.name, sort_grp=False)  # sum by month
        self.assertTrue(np.array_equal(d.values, np.array([[1, 5], [9, 13], [17, 21]])))
        self.assertTrue(np.array_equal(d.axis(ax2.name).values, ["jan", "feb"]))

        d = c.reduce(np.sum, group=ax2.name)  # sum by month, sorted by default
        self.assertTrue(np.array_equal(d.values, np.array([[5, 1], [13, 9], [21, 17]])))
        self.assertTrue(np.array_equal(d.axis(ax2.name).values, ["feb", "jan"]))
        self.assertTrue(is_indexed(d.axis(ax2.name)))
        self.assertEqual(len(d.axis(ax2.name)), 2)
        self.assertEqual(d.values.shape, (3, 2))
        
        # testing various aggregation functions using direct calling, e.g. c.sum(group=0),
        # or indirect calling, e.g. reduce(func=np.sum, group=0)
        funcs_indirect = [np.sum, np.mean, np.median, np.min, np.max, np.prod]
        funcs_direct = [c.sum, c.mean, c.median, c.min, c.max, c.prod]
        for func_indirect, func_direct in zip(funcs_indirect, funcs_direct):
            result = np.apply_along_axis(func_indirect, 0, c.values)
            d = c.reduce(func_indirect, group=ax1.name)
            self.assertTrue(np.array_equiv(d.values, result))
            e = func_direct(group=ax1.name)
            self.assertTrue(np.array_equiv(e.values, result))

        # testing function with extra parameters which cannot be passed as *args
        third_quartile = functools.partial(np.percentile, q=75)
        d = c.reduce(third_quartile, group=ax1.name)
        self.assertTrue(np.array_equiv(d.values, np.apply_along_axis(third_quartile, 0, c.values)))

        # the same but using lambda - this is actually simpler and more powerful way
        third_quartile_lambda = lambda sample: np.percentile(sample, q=75)
        d = c.reduce(third_quartile_lambda, group=ax1.name)
        self.assertTrue(np.array_equiv(d.values, np.apply_along_axis(third_quartile_lambda, 0, c.values)))

    def test_rename_axis(self):
        c = year_quarter_cube()

        # axes by name
        d = c.rename_axis("year", "Y")
        d = d.rename_axis("quarter", "Q")
        self.assertEqual(tuple(d.dims), ("Y", "Q"))

        # axes by index
        d = c.rename_axis(0, "Y")
        d = d.rename_axis(1, "Q")
        self.assertEqual(tuple(d.dims), ("Y", "Q"))
        
        # axes with negative indices
        d = c.rename_axis(-2, "Y")
        d = d.rename_axis(-1, "Q")
        self.assertEqual(tuple(d.dims), ("Y", "Q"))

        # invalid new axis name type
        self.assertRaises(TypeError, c.rename_axis, 0, 0.0)
        self.assertRaises(TypeError, c.rename_axis, "year", None)

        # duplicate axes
        self.assertRaises(ValueError, c.rename_axis, 0, "quarter")
        self.assertRaises(ValueError, c.rename_axis, "year", "quarter")

        # non-existing axes
        self.assertRaises(LookupError, c.rename_axis, 2, "quarter")
        self.assertRaises(LookupError, c.rename_axis, "bad_axis", "quarter")

    def test_slice(self):
        c = year_quarter_weekday_cube()
        ax = 0
        d = c.slice(ax, None, None, 2)  # every even item
        self.assertTrue(np.array_equal(d.values, c.values[:, :, ::2]))
        self.assertTrue(np.array_equal(d.axis(ax).values, c.axis(ax).values[::2]))

    def test_first(self):
        c = year_quarter_weekday_cube()
        ax = "year"
        d = c.first(ax, 2)
        self.assertTrue(np.array_equal(d.values, c.values[0: 2]))
        self.assertTrue(np.array_equal(d.axis(ax).values, c.axis(ax).values[0: 2]))

    def test_last(self):
        c = year_quarter_weekday_cube()
        ax = "quarter"
        d = c.last(ax, 2)
        self.assertTrue(np.array_equal(d.values, c.values[:, -2:]))
        self.assertTrue(np.array_equal(d.axis(ax).values, c.axis(ax).values[-2:]))

    def test_reversed(self):
        c = year_quarter_weekday_cube()
        ax = "weekday"
        d = c.reversed(ax)
        self.assertTrue(np.array_equal(d.values, c.values[:, :, ::-1]))
        self.assertTrue(np.array_equal(d.axis(ax).values, c.axis(ax).values[::-1]))

    def test_diff(self):
        c = year_quarter_weekday_cube()
        d = c.diff("year")
        self.assertTrue(np.array_equal(d.values, np.diff(c.values, n=1, axis=0)))
        self.assertTrue(np.array_equal(d.axis("year").values, [2015, 2016]))

        d = c.diff("quarter", n=2)
        self.assertTrue(np.array_equal(d.values, np.diff(c.values, n=2, axis=1)))
        self.assertTrue(np.array_equal(d.axis("quarter").values, ["Q3", "Q4"]))

        d = c.diff("weekday", n=4, axis_shift=0)
        self.assertTrue(np.array_equal(d.values, np.diff(c.values, n=4, axis=2)))
        self.assertTrue(np.array_equal(d.axis("weekday").values, ["mon", "tue", "wed"]))

    def test_growth(self):
        c = year_quarter_cube() + 1  # to prevent division by zero

        d = c.growth("year")
        self.assertTrue(np.array_equal(d.values, c.values[1:, :] / c.values[:-1, :]))
        self.assertTrue(np.array_equal(d.axis("year").values, c.axis("year").values[1:]))

        d = c.growth(1)  # 1 = quarter axis
        self.assertTrue(np.array_equal(d.values, c.values[:, 1:] / c.values[:, :-1]))

        d = c.growth("year", axis_shift=0)
        self.assertTrue(np.array_equal(d.values, c.values[1:, :] / c.values[:-1, :]))
        self.assertTrue(np.array_equal(d.axis("year").values, c.axis("year").values[:-1]))

    def test_aggregate(self):
        c = year_quarter_cube()

        self.assertTrue((c.sum("quarter") == c.sum(1)).all())
        self.assertTrue((c.sum("quarter") == c.sum(-1)).all())
        self.assertTrue((c.sum("year") == c.sum(keep=1)).all())
        self.assertTrue((c.sum("year") == c.sum(keep=-1)).all())
        self.assertTrue((c.sum(["year"]) == c.sum(keep=[-1])).all())
        self.assertTrue((c.sum("quarter") == c.sum(keep="year")).all())

        year_ax = c.axis("year")
        quarter_ax = c.axis("quarter")
        self.assertTrue((c.sum(year_ax) == c.sum("year")).all())
        self.assertTrue((c.sum(year_ax) == c.sum(keep=quarter_ax)).all())
        self.assertTrue((c.sum(quarter_ax) == c.sum(1)).all())
        self.assertTrue((c.sum(quarter_ax) == c.sum(keep=0)).all())

        self.assertEqual(c.sum(None), c.sum())
        self.assertEqual(c.sum(), np.sum(c.values))
        self.assertEqual(c.mean(), np.mean(c.values))
        self.assertEqual(c.min(), np.min(c.values))
        self.assertEqual(c.max(), np.max(c.values))

        self.assertRaises(LookupError, c.sum, "bad_axis")
        self.assertRaises(LookupError, c.sum, 2)

        self.assertRaises(TypeError, c.sum, 1.0)

    def test_swap_axes(self):
        c = year_quarter_weekday_cube()
        self.assertEqual(c.shape, (3, 4, 7))

        # swap by name
        d = c.swap_axes("year", "quarter")
        self.assertEqual(tuple(d.dims), ("quarter", "year", "weekday"))
        self.assertEqual(d.shape, (4, 3, 7))

        # swap by index
        d = c.swap_axes(0, 2)
        self.assertEqual(tuple(d.dims), ("weekday", "quarter", "year"))
        self.assertEqual(d.shape, (7, 4, 3))
        
        # swap by index and name
        d = c.swap_axes(0, "quarter")
        self.assertEqual(tuple(d.dims), ("quarter", "year", "weekday"))
        self.assertEqual(d.shape, (4, 3, 7))
        
        # swap Axis instances
        year_axis = c.axis("year")
        quarter_axis = c.axis("quarter")
        d = c.swap_axes(year_axis, quarter_axis)
        self.assertEqual(tuple(d.dims), ("quarter", "year", "weekday"))
        self.assertEqual(d.shape, (4, 3, 7))
        
        # wrong axis results in LookupError
        self.assertRaises(LookupError, c.sum, "bad_axis")
        self.assertRaises(LookupError, c.sum, 3)
        
    def test_align_axis(self):
        c = year_quarter_cube()
        ax1 = Axis("year", [2015, 2015, 2014, 2014])
        ax2 = Index("quarter", ["Q1", "Q3"])
        
        d = c.align(ax1)
        d = d.align(ax2)

        # test identity of the new axis
        self.assertTrue(d.axis("year") is ax1)
        self.assertTrue(d.axis("quarter") is ax2)

        # test aligned values
        self.assertTrue(np.array_equal(d.values, [[4, 6], [4, 6], [0, 2], [0, 2]]))

    def test_concatenate(self):
        values = np.arange(12).reshape(3, 4)
        ax1 = Index("year", [2014, 2015, 2016])
        ax2 = Index("month", ["jan", "feb", "mar", "apr"])
        c = Cube([ax1, ax2],values)

        values = np.arange(12).reshape(4, 3)
        ax3 = Index("year", [2014, 2015, 2016])
        ax4 = Index("month", ["may", "jun", "jul", "aug"])
        d = Cube([ax4, ax3],values)

        e = concatenate([c, d], "month")
        self.assertEqual(e.ndim, 2)
        self.assertEqual(e.shape, (8, 3))  # the joined axis is always the first
        self.assertTrue(is_axis(e.axis("month")))

        e = concatenate([c, d], "month", as_index=True)
        self.assertEqual(e.ndim, 2)
        self.assertEqual(e.shape, (8, 3))
        self.assertTrue(is_indexed(e.axis("month")))

        # duplicate index values
        self.assertRaises(ValueError, concatenate, [c, c], "month", as_index=True)

        # broadcasting of an axis
        countries = Axis("country", ["DE", "FR"])
        f = d.insert_axis(countries)
        g = concatenate([c, f], "month", broadcast=True)
        self.assertEqual(g.ndim, 3)
        self.assertEqual(g.shape, (8, 3, 2))

        # if automatic broadcasting is not allowed
        self.assertRaises(LookupError, concatenate, [c, f], "month", broadcast=False)

    def test_stack(self):
        c = year_quarter_cube()
        d = year_quarter_cube()
        country_axis = Index("country", ["GB", "FR"])
        e = stack([c, d], country_axis)
        self.assertEqual(e.values.shape, (2, 3, 4))
        # the merged axis go first
        self.assertEqual(tuple(e.dims), ("country", "year", "quarter"))

        # axis with the same name already exists
        c = year_quarter_cube()
        d = year_quarter_cube()
        year_axis = Index("year", [2000, 2001])
        self.assertRaises(ValueError, stack, [c, d], year_axis)

        # different number of cubes and axis length
        c = year_quarter_cube()
        d = year_quarter_cube()
        country_axis = Index("country", ["GB", "FR", "DE"])
        self.assertRaises(ValueError, stack, [c, d], country_axis)

        # cubes do not have uniform shapes
        c = year_quarter_cube()
        d = year_quarter_weekday_cube()
        country_axis = Index("country", ["GB", "FR"])
        self.assertRaises(LookupError, stack, [c, d], country_axis)

        # the previous example if O, if automatic broadcasting is allowed
        e = stack([c, d], country_axis, broadcast=True)
        self.assertEqual(e.ndim, 4)
        # broadcast axes go last
        self.assertEqual(tuple(e.dims), ("country", "year", "quarter", "weekday"))
        

    def test_take(self):
        c = year_quarter_cube()

        # axis by name
        self.assertTrue(np.array_equal(c.take("year", [0, 1]).values, c.values.take([0, 1], 0)))
        self.assertTrue(np.array_equal(c.take("quarter", [0, 1]).values, c.values.take([0, 1], 1)))

        # axis by index
        self.assertTrue(np.array_equal(c.take(0, [0, 1]).values, c.values.take([0, 1], 0)))
        self.assertTrue(np.array_equal(c.take(1, [0, 1]).values, c.values.take([0, 1], 1)))

        # do not collapse dimension - a single int in a list or tuple
        d = c.take(0, [2])
        self.assertEqual(d.ndim, 2)
        self.assertTrue(np.array_equal(d.values, c.values.take([2], 0)))

        d = c.take(0, (2,))
        self.assertEqual(d.ndim, 2)
        self.assertTrue(np.array_equal(d.values, c.values.take([2], 0)))

        # collapse dimension - a single int
        d = c.take(0, 2)
        self.assertEqual(d.ndim, 1)
        self.assertTrue(np.array_equal(d.values, c.values.take(2, 0)))

        # negative index
        self.assertTrue(np.array_equal(c.take("year", [-3, -2]).values, c.values.take([0, 1], 0)))

        # wrong axes
        self.assertRaises(LookupError, c.take, "bad_axis", [0, 1])
        self.assertRaises(LookupError, c.take, 2, [0, 1])

        # wrong indices
        self.assertRaises(IndexError, c.take, "year", 4)
        self.assertRaises(IndexError, c.take, "year", [0, 4])
        self.assertRaises(ValueError, c.take, "year", ["X"])
        self.assertRaises(TypeError, c.take, "year", None)

    def test_slice(self):
        c = year_quarter_cube()

        d = c.slice("year", -1)  # except the last one
        self.assertTrue(np.array_equal(d.values, c.values[:-1, :]))

        d = c.slice(1, 0, 3, 2)  # 1 = quarter axis
        self.assertTrue(np.array_equal(d.values, c.values[:, 0: 3: 2]))

        # accepting a slice as an argument
        slc = slice(0, 3, 2)
        d = c.slice(1, slc)  # 1 = quarter axis
        self.assertTrue(np.array_equal(d.values, c.values[:, 0: 3: 2]))

    def test_compress(self):
        c = year_quarter_cube()

        d = c.compress(0, [True, False, False])
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))
        self.assertEqual(d.ndim, 2)
        self.assertEqual(tuple(d.dims), ("year", "quarter"))

        e = c.compress("quarter", [True, False, True, False])
        self.assertTrue(np.array_equal(e.values, [[0, 2], [4, 6], [8, 10]]))

        # using numpy array of bools
        e = c.compress("quarter", np.arange(1, 4) <= 1)
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))
        self.assertEqual(d.ndim, 2)
        self.assertEqual(d.dims, ("year", "quarter"))

        # ints instead of bools; 0 = False, other = True
        # similarly for other types; Python bool conversion is used
        d = c.compress(0, [1, 0, 0])
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))
        self.assertEqual(d.ndim, 2)
        self.assertEqual(d.dims, ("year", "quarter"))

        # wrong length of bool collection - too short ...
        d = c.compress(0, [True, False])  # unspecified means False
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))

        # ... and too long
        d = c.compress(0, [True, False, False, False])  # this is OK, the extra False is ignored
        self.assertTrue(np.array_equal(d.values, [[0, 1, 2, 3]]))
        self.assertRaises(IndexError, c.compress, 0, [True, False, False, True])  # but this is not OK

    def test_insert_axis(self):
        c = year_quarter_cube()
        countries = Axis("country", ["DE", "FR"])

        # insert as the first axis
        d = c.insert_axis(countries, 0)
        self.assertEqual(d.ndim, 3)
        self.assertEqual(tuple(d.dims), ("country", "year", "quarter"))
        self.assertEqual(d.shape, (2, 3, 4))
        # the values in each sub-cube must be equal to the original cube
        self.assertTrue((d.take("country", 0) == c).all())
        self.assertTrue((d.take("country", 1) == c).all())

        # append as the last axis
        d = c.insert_axis(countries, -1)
        self.assertEqual(d.ndim, 3)
        self.assertEqual(tuple(d.dims), ("year", "quarter", "country"))
        self.assertEqual(d.shape, (3, 4, 2))
        # the values in each sub-cube must be equal to the original cube
        self.assertTrue((d.take("country", 0) == c).all())
        self.assertTrue((d.take("country", 1) == c).all())

    def test_replace_axis(self):
        c = year_quarter_cube()
        self.assertEqual(c.dims, ("year", "quarter"))
        ax = Axis("Y", [2000, 2010, 2020])
        d = c.replace_axis("year", ax)
        e = c.replace_axis(0, ax)
        f = c.replace_axis(c.axis("year"), ax)
        self.assertEqual(d.dims, ("Y", "quarter"))
        self.assertEqual(d.dims, e.dims)
        self.assertEqual(d.dims, f.dims)
        self.assertRaises(NonUniqueDimNamesError, c.replace_axis, "year", Axis("quarter", [1, 2, 3]))
