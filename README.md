# Algorithm-and-Data-Structure-Python
```
       Algorithm	Time Complexity
                    Best	    Average	    Worst	
Selection Sort	    Ω(n^2)	    θ(n^2)	    O(n^2)
Bubble Sort	    Ω(n)	    θ(n^2)	    O(n^2)
Insertion Sort	    Ω(n)	    θ(n^2)	    O(n^2)
Heap Sort	    Ω(n log(n))	    θ(n log(n))	    O(n log(n))
Quick Sort	    Ω(n log(n))	    θ(n log(n))	    O(n^2)
Merge Sort	    Ω(n log(n))	    θ(n log(n))	    O(n log(n))
Bucket Sort	    Ω(n+k)	    θ(n+k)	    O(n^2)
Radix Sort	    Ω(nk)	    θ(nk)	    O(nk)
```
- **Linear. O(n)** - Most optimal algorithms run in linear time.  An easy way to identify this is to determine if you're visiting 
every node or item once and only once.  If you are, it is linear... it doesn't matter how many operations you're doing whether it's 1, 2, 3, or 4 lines of code you're executing per node.  Generally, you are still doing a constant amount of work per input.
- **Constant.  O(k)** - Constant time algorithms have a running time independent of the input size.  Mathematical formulas for instance have fixed running times and are considered constant time.
- **Logarithmic. O(log(n))** - Logarithmic algorithms are often seen in trees.  It's best to think of "logarithmic" as the "height of the tree."  So, a binary search, for instance, often includes traversing down the height of a tree and can be considered logarithmic in time.  (Although, it may still be more accurate to say that for an unbalanced tree, the runtime is in the worst case linear.)  
- **Superlinear. O(n*log(n))** -  Most sorts operate in "n log n" time.  This includes popular sorting algorithms like quicksort, mergesort, or heapsort.  (Actually, quicksort is O(n2) time in the worst-case scenario generally).
- **Quadratic or Cubic / Polynomial** - O(n2) or O(n3).  Brute force algorithms often run in O(n2) or O(n3) time where you may be looping within a loop.  It's easy to identify if you see a for-loop inside a for-loop, where for each element i you iterate through another element j, for instance.  A common scenario is, given two arrays, find the common elements in each array where you would simply go through each element and check whether it exists in the other array.  This would execute in O(n*m) time, where n and m are the sizes of each array.  It's still great to name these brute force algorithms if you can identify them.
- **Exponential. O(2n)** -  Exponential algorithms are quite terrible in running time.  A classic example is determining every permutation of a set of n bits (it would take 2n combinations).  Another example is computing the fibonacci sequence fib(n) = fib(n-1) + fib(n-2), where for each item, it requires the computation of two more subproblems.  
- **Factorial. O(n!)** -  These algorithms are the slowest and don't show up that often.  You might see this in combinatorial problems, or like a "traveling salesman" problem where given n nodes, you need to find the optimal path from start to finish.  In your first iteration, you have a selection of n cities to visit, then n-1 cities, then n-2 cities, n-3 cities, etc., until you reach the last city.   That runtime is n * (n -1 ) * (n - 2) * (n -3 ) ... 1 = O(n!).