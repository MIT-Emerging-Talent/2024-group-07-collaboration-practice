# Selection Sort Implementation

This project includes can_sum basic challenge realted to dynamic programming

## Contents

- [Introduction](#introduction)
- [Implementation](#implementation)
- [Behavior](#behavior)
- [Test Cases](#test-cases)
- [Running Tests](#running-tests)

## Introduction

In can_sum problem we are given a target number target and a list of positive integers numbers, the goal is to determine if it is possible to sum the elements in numbers to reach the target.

## Implementation

This challenge is implemented in can_sum.py file and the name of the function is can_sum_basic. This function uses a recursive approach to check if it is possible to sum the elements in numbers to reach the target. 

## Behavior

The function starts by checking if the target is 0 (in which case it returns True) or if the target is negative (in which case it returns False). If neither of those conditions is met, it checks if any of the recursive calls to itself using the target minus one of the elements in numbers returns True.

## Test Cases

1) Input: target=7, numbers=[2, 3]
   Output: True

   Explanation: 2 + 2 + 3 = 7
2) Input: target=9, numbers=[2, 4, 8]
   Output: False

   Explanation: There is no combination of numbers that add up to 9


## Running Tests

To verify the correctness of the implementation, a set of unit tests has been provided. These tests are located in the `test_can_sum.py` file. There are two more testcases which have been commented in this file as they are for the unimplemented functions. To run the tests, execute the following command:


python test_can_sum.py


