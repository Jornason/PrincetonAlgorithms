#!/usr/bin/env python

#************************************************************************
 #  Compilation:  javac MergeBU.java
 #  Execution:    java MergeBU < input.txt
 #  Dependencies: StdOut.java StdIn.java
 #  Data files:   http://algs4.cs.princeton.edu/22mergesort/tiny.txt
 #                http://algs4.cs.princeton.edu/22mergesort/words3.txt
 #   
 #  Sorts a sequence of strings from standard input using
 #  bottom-up mergesort.
 #   
 #  % more tiny.txt
 #  S O R T E X A M P L E
 #
 #  % java MergeBU < tiny.txt
 #  A E E L M O P R S T X                 [ one string per line ]
 #    
 #  % more words3.txt
 #  bed bug dad yes zoo ... all bad yet
 #  
 #  % java MergeBU < words3.txt
 #  all bad bed bug dad ... yes yet zoo    [ one string per line ]
 #
 #************************************************************************/

#*
 #  The <tt>MergeBU</tt> class provides static methods for sorting an
 #  array using bottom-up mergesort.
 #  <p>
 #  For additional documentation, see <a href="http://algs4.cs.princeton.edu/21elementary">Section 2.1</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/

#------------------------------------------------------------------------------
# 00:34 BOTTOM-UP MERGESORT: TRACE MERGE RESULTS FOR TOP-DOWN MERGESORT
# 
# BASIC PLAN:
#   * Pass through array, merging subarrays of size 1.
#   * Repeat for subarrays of size 2, 4, 8, 16, ...
#
# BOTTOM LINE: No recursion needed!
#   Bottom-up Mergesort gets the job done in lg N passes.
#   Each pass uses N compares
#   For a total cost of N lg N
#
#                                    a[]
#                                             1 1 1 1 1 1
#                         0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#                         -------------------------------
# a           lo      hi  M E R G E S O R T E X A M P L E
# size=1 
# b merge(a,  0,  0,  1)  E M   .       .               .
# c merge(a,  2,  2,  3)      G R       .               .
# e merge(a,  4,  4,  5)        . E S   .               .
# f merge(a,  6,  6,  7)        .     O R               .
# i merge(a,  8,  8,  9)        .       . E T           .
# j merge(a, 10, 10, 11)        .       .     A X       .
# m merge(a, 12, 12, 13)        .       .         M P   .
# n merge(a, 14, 14, 15)        .       .             E L
# size=2
# d merge(a,  0,  1,  3)  E G M R       .               .
# g merge(a,  4,  5,  7)          E O R S               .
# k merge(a,  8,  9, 11)                . A E T X
# o merge(a, 12, 13, 15)                .         E L M P
# sz=4: 2 sub-arrays sz 8
# h merge(a,  0,  3,  7)  E E G M O R R S               .
# p merge(a,  8, 11, 15)                . A E E L M P T X
# size=8
# q merge(a,  0,  7, 15)  A E E E E G L M M O P R R S T X


#------------------------------------------------------------------------------
# QUESTION: How many passes (over the input array) does bottom-up mergesort make in the worst-case?
# ANSWER: 


# stably merge a[lo..mid] with a[mid+1..hi] using aux[lo..hi]
# Same merge code as the original recursive Merge
def _merge(a, aux, lo, mid, hi):

    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]

    # merge back to a[]
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if   i > mid:               a[k] = aux[j]; j += 1 # this copying is unneccessary
        elif j > hi:                a[k] = aux[i]; i += 1
        elif _less(aux[j], aux[i]): a[k] = aux[j]; j += 1
        else:                       a[k] = aux[i]; i += 1


#*
 # Rearranges the array in ascending order, using the natural order.
 # @param a the array to be sorted
 #/
def Sort(a, array_history=None):
    N = len(a)
    aux = [None for i in range(N)]
    n = 1
    # First nested loop is "Size of the sub-array" executed only lg N times (lg N passes)
    while n < N: 
        i = 0
        while i < N-n:
            lo = i
            mi  = i+n-1
            hi = min(i+n+n-1, N-1)
            _merge(a, aux, lo, mi, hi)
            i += n+n
        # Outer Loop is executed lg N times because each time 
        # we double the size of the sub-array until we get to N
        n = n+n 
    assert _isSorted(a)

#**********************************************************************
#  Helper sorting functions
#**********************************************************************/

# is v < w ?
def _less(v, w): return v < w

# exchange a[i] and a[j]
def _exch(a, i, j):
    swap = a[i]
    a[i] = a[j]
    a[j] = swap


#**********************************************************************
#  Check if array is sorted - useful for debugging
#**********************************************************************/
def _isSorted(a):
    for i in range(1, len(a)):
        if _less(a[i], a[i-1]): return False
    return True

# Reads in a sequence of strings from standard input; mergesorts them;
# and prints them to standard output in ascending order.
def main():
  import InputArgs
  a = InputArgs.getStrArray("S O R T E X A M P L E")
  Sort(a)
  print ' '.join(map(str,a))

if __name__ == '__main__':
  main()

# Copyright (C) 2002-2010, Robert Sedgewick and Kevin Wayne. 
# Java version Last updated: Wed Dec 4 11:48:10 EST 2013.
