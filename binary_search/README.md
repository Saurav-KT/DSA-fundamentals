Binary search reduces time from O(n) to O(log n) by eliminating half of the 
remaining possibilities at every step, which is only possible when the problem has a 
monotonic structure.
Binary search works because every comparison eliminates half of the search space.

Linear Search → O(n)
Imagine a sorted list of 16 numbers:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]

Searching for 27 using linear search:
1 → 3 → 5 → 7 → 9 → ... → 27

Worst case:
You check all 16 elements
Time complexity = O(n)

Binary Search → O(log n)
Same list, but now:

Step 1
Check the middle element:

Middle = 15

Is 27 > 15?

Yes → ignore the left half (8 elements)

Step 2
Remaining:
[17, 19, 21, 23, 25, 27, 29, 31]

Middle = 23
Is 27 > 23?
✔ Yes → ignore half again (4 elements)

Step 3
Remaining:
[25, 27, 29, 31]
Middle = 27 → found

Result
Elements checked: 3
Instead of 16 → 3
That’s the power of halving

Why Is This O(log n)?
Each step:
Reduces the search space by ½

**Mathematically:**
“How many times do I divide n by 2 until I reach 1?”
That number is: log₂(n)
Time complexity = O(log n)

Find mid?
mid= (low+ high)//2
or
mid= low+ (high-low)//2

**Key Requirement:**

Monotonic Property
Binary search only works if the search space has this property:
Once a condition becomes true (or false), it stays that way.

**Examples:**

Sorted array
First failing test
Minimum capacity that works
Earliest valid timestamp
Without this, you can’t safely discard half.