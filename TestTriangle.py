# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Test 1
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right', '3,4,5 is a Right triangle')

    # Test 1a
#    def testRightTriangleB(self): 
#        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    # Test 2
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral', '1,1,1 should be equilateral')

    # Test 3
    def testLargerEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(48,48,48),'Equilateral', '48, 48, 48 should be equilateral')

    # Test 4
    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(6, 8, 8), 'Isoceles', '6, 8, 8 should be isoceles')

    # Test 5
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4, 6, 8), 'Scalene', '4, 6, 8 should be scalene')

    # Test 6
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(5, 7, 13), 'NotATriangle', '5, 7, 13 is not a valid triangle')

    # Test 7
    def testDecimalInput(self):
        self.assertEqual(classifyTriangle(3, 6, 9.2), 'InvalidInput')

    # Test 8
    def testStringInput(self):
        with self.assertRaises(TypeError):
            classifyTriangle(4, 'a', 11)

    # Test 9
    def testLargeInput(self):
        self.assertEqual(classifyTriangle(181, 140, 202), 'InvalidInput')

    # Test 10
    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(7, -9, -13), 'InvalidInput')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

