"""
This module contains additional test methods used to test AOC 2017 solution
code against example inputs. Test methods utilising pytest library.
"""

from src.solutions import day07


def test_day07_part1_ex01():
    """
    Test method for AOC 2017 Day 7 Part 1 using example input 1.
    """
    input_data = day07.process_input_file("./input/examples/day07_ex01.txt")
    solution = day07.solve_part1(input_data)
    assert solution == "tknk"


def test_day07_part2_ex01():
    """
    Test method for AOC 2017 Day 7 Part 1 using example input 1.
    """
    input_data = day07.process_input_file("./input/examples/day07_ex01.txt")
    solution = day07.solve_part2(input_data)
    assert solution == 60
