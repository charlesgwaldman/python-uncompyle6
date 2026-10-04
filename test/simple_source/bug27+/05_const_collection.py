# Constant collections of 5+ elements go through the BUILD_CONST_LIST /
# BUILD_CONST_SET optimization and were rendered by n_const_list() from the
# co_consts *index* (elem.attr) instead of the value (elem.pattr); after the
# index was fixed for lists, string elements were still emitted unquoted.
# See https://github.com/rocky/python-uncompyle6/issues/527
# RUNNABLE!

"""This program is self-checking!"""

ints = [239, 168, 254, 54, 235, 128]
assert ints == [239, 168, 254, 54, 235, 128]
assert ints[0] == 239

strs = ["aa", "bb", "cc", "dd", "ee"]
assert strs == ["aa", "bb", "cc", "dd", "ee"]
assert strs[2] == "cc"

floats = [1.5, 2.5, 3.5, 4.5, 5.5]
assert sum(floats) == 17.5

mixed = [1, "two", 3.0, "four", 5, "six"]
assert mixed[1] == "two"
assert mixed[2] == 3.0

nested = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
assert nested[4] == (9, 10)

const_set = {10, 20, 30, 40, 50}
assert 30 in const_set
assert len(const_set) == 5
