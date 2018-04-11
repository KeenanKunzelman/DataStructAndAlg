# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from time import time            # import time function from time module
import dynamic_array
def compute_average(n,version ,howmany2appendby):
  """Perform n appends to an empty list and return average time elapsed."""
  data = dynamic_array.DynamicArray()
  start = time()                 # record the start time (in seconds)
  if version == '2':
      for k in range(n):
        data.append1(k,howmany2appendby)
  elif version == '1':
      for k in range(n):
        data.append(k)
  end = time()                   # record the end time (in seconds)

  return (end - start) / n       # compute average per operation

def main():

    testCases = [10, 100, 1000, 10000]
    while True:
        cells_to_append = input("Enter a value for how many cells to append by ")
        for i in range(4):
            print("--------------------------------------------------")
            print("\nTesting for case n = " + str(testCases[i]))
            first = 1000000 * compute_average(testCases[i],'1',None)
            second = 1000000 * compute_average(testCases[i], '2', int(cells_to_append))


            print("\nDoubling speed: " + str(first) + " microseconds")
            print("Using append1 and incrementing by " + str(cells_to_append) + " cells: "  + str(second) + " microseconds")

if __name__ == '__main__':
    main()
