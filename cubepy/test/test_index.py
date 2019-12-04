import unittest
import numpy as np
import sys
import os

from cubepy import Index


class IndexTests(unittest.TestCase):

    def test_create_index(self):
        a = Index("A", [10, 20, 30])
        self.assertEqual(a.name, "A")
        self.assertEqual(len(a), 3)

        a = Index("Dim", ["a", "b", "c", "d"])
        self.assertEqual(a.name, "Dim")
        self.assertEqual(len(a), 4)

        # duplicate values
        self.assertRaises(ValueError, Index, "A", ["a", "b", "a"])
        self.assertRaises(ValueError, Index, "A", [0, 1, 1])

        # invalid Index name
        self.assertRaises(TypeError, Index, 1, [1, 2, 3])
        
    def test_index_take(self):
        a = Index("A", ["a", "b", "c", "d"])
        self.assertEqual(a.take([0, 2]).name, "A")  # keep name
        self.assertTrue(np.array_equal(a.take([0, 2]).values, ["a", "c"]))
        self.assertTrue(np.array_equal(a.take([2, 0]).values, ["c", "a"]))
        self.assertRaises(ValueError, a.take, [0, 2, 0])  # duplicate values in Index
        
    def test_compress(self):
        a = Index("A", ["a", "b", "c", "d"])
        selector = [True, False, True, False]
        b = a.compress(selector)
        c = a[np.array(selector)]
        self.assertTrue(np.array_equal(b.values, c.values))
        self.assertEqual(a.name, b.name)  # keep name
        self.assertTrue(np.array_equal(b.values, a.values.compress(selector)))

    def test_writeable(self):
        # once index has been created, its values cannot be changed in order not to break lookup function
        a = Index("A", [10, 20, 30])
        self.assertRaises(ValueError, a.values.__setitem__, 0, 40)
        self.assertRaises(ValueError, a.values.sort)

    def test_indexof(self):
        a = Index("A", [10, 20, 30])
        b = Index("Dim", ["ab", "bc", "cd", "de"])

        # a single value
        self.assertEqual(a.indexof(10), 0)
        self.assertEqual(b.indexof("cd"), 2)
        self.assertEqual(b.indexof(["cd"]), 2)

        # multiple values
        self.assertTrue(np.array_equal(a.indexof([10, 30]), [0, 2]))
        self.assertTrue(np.array_equal(b.indexof(["de", "cd"]), [3, 2]))

        # non-existent value raises KeyError (similar to dictionary lookup)
        self.assertRaises(KeyError, a.indexof, 0)
        self.assertRaises(KeyError, b.indexof, "ef")
        self.assertRaises(KeyError, b.indexof, None)
        self.assertRaises(KeyError, a.indexof, [0, 1])
        self.assertRaises(KeyError, b.indexof, ["de", "ef"])

    def test_operator_in(self):
        a = Index("A", [10, 20, 30])
        b = Index("B", ["ab", "bc", "cd", "de"])

        self.assertTrue(20 in a)
        self.assertFalse(40 in a)
        self.assertTrue("bc" in b)
        self.assertFalse("ef" in b)


    def test_contains(self):
        a = Index("A", [10, 20, 30])
        b = Index("B", ["ab", "bc", "cd", "de"])

        # a single value (in this case, operator 'in' is preferred)
        self.assertTrue(a.contains(20))
        self.assertFalse(a.contains(40))
        self.assertTrue(b.contains("bc"))
        self.assertFalse(b.contains("ef"))

        # multiple values returns one-dimensional numpy array of logical values
        self.assertTrue(np.array_equal(a.contains([0, 10, 20, 40]), [False, True, True, False]))
        self.assertTrue(np.array_equal(b.contains(["ab"]), [True]))
        self.assertTrue(np.array_equal(b.contains(["ab", "ef", "bc"]), [True, False, True]))
        self.assertTrue(np.array_equal(b.contains(("ab", "ef", "bc")), [True, False, True]))
