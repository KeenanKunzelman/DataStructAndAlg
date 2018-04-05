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
def compute_average(n,how2append,howmany2appendby):
  """Perform n appends to an empty list and return average time elapsed."""
  data = dynamic_array.DynamicArray()
  start = time()                 # record the start time (in seconds)
  if how2append == 'append1':
      for k in range(n):
        data.append1(k,howmany2appendby)
  else:
      for k in range(n):
        data.append(k)
  end = time()                   # record the end time (in seconds)
  print(end)
  print(start)
  return (end - start) / n       # compute average per operation

def main():
    appends = int(input("input a value of appends to be executed "))
    first = compute_average(appends,'notladksjf;l',5)
    second = compute_average(appends, 'append1',1)
    third = compute_average(appends, 'append1',5)
    print("\n\nDoubling speed: " + str(first))
    print("Using append1 and incrementing by 1: " + str(second))
    print("Using append1 and incrementing by 5: " + str(third))
if __name__ == '__main__':
    main()
