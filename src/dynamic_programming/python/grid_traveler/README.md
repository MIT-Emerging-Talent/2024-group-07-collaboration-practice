# Grid Traveller Implementation

This project includes grid_traveler basic challenge realted to dynamic programming

## Contents

- [Introduction](#introduction)
- [Implementation](#implementation)
- [Behavior](#behavior)
- [Test Cases](#test-cases)
- [Running Tests](#running-tests)

## Introduction

In grid_traveler problem we are given the dimensions of a grid, represented by the number of rows x and the number of columns y, the task is to find the total number of unique paths that a traveller can take to go from the top left corner of the grid to the bottom right corner. The traveller can only move down or right at each step

## Implementation

This challenge is implemented in grid_traveler.py file and the name of the function is grid_traveller_basic. This function uses a recursive approach to count the unique number of paths from top left corner of the grid to reach the bottom right corner
## Behavior

The function recursively keeps the traveler to move right and bottom until the destination corner is reached. Once the destination is reached, the function recursively finds new paths to reach the same destination. The traveler can only move down the grid or towards the right of the grid.

## Test Cases

1) Input: num_rows=2, num_columns=2
   Output: 2

   Explanation: There are two paths the traveller can take: down-right and right-down.

|...S...|.......|

|.......|...E...|



2) Input: num_rows=3, num_columns=4
   Output: 10

   Explanation: There are 10 paths the traveller can take, for example down-down-right-right or down-right-down-right.

|...S...|.......|.......|.......|

|.......|.......|.......|........|

|.......|.......|.......|...E...|

## Running Tests

To verify the correctness of the implementation, a set of unit tests has been provided. These tests are located in the `test_grid_traveler.py` file. There are two more testcases which have been commented in this file as they are for the unimplemented functions. To run the tests, execute the following command in the terminal:


python test_grid_traveler.py