Array has to be sorted for the lower bound to be implemented.
lower bound:Smallest index such that arr[index]>=n
arr[]= [3,5,8,15,19]
n=8
lower bound= 2

n=16
lower bound= 4

n=20
lower bound(hypothetical)= 5

Use binary search. If middle element satisfies condition (>= target), store it and move left to find earlier valid index. Otherwise, move right.

The core intuition behind lower/upper bound binary search.
Why do we do high = mid - 1 when condition is satisfied?
Main Idea

When arr[mid] satisfies the condition:

It might be the answer
But there may be an earlier valid index on the left side
So we save mid, then search left.
That’s why:

`ans = mid
high = mid - 1`

Lower Bound Example

Find first index where:

arr[i] >= 4

Array:

[1, 2, 4, 4, 5]

Indexes:
0  1  2  3  4
Step 1
low=0, high=4
mid=2
arr[2]=4

Condition true:

4 >= 4

So index 2 could be the answer.

But maybe there is another 4 before index 2?
Maybe at index 1 or 0?

So:

ans = 2
high = 1

Now search left half only.

Why Not Return Immediately?

Because binary search for bounds is not just “find any match”.

We need the first valid index.

Visual Rule

When condition is true:

arr[mid] >= target

Then all possibilities are:

mid
some index left of mid

Never need right side for first occurrence.

So discard right side.

Why high = mid - 1, not high = mid

Because mid is already checked.

If you do:

high = mid

You may get infinite loop.

Need to move boundary past mid:

high = mid - 1

🔹 Opposite Case

If condition is false:

arr[mid] < target

Then:

mid cannot be answer
everything left of mid also too small

So move right:

low = mid + 1
One-Line Intuition
If mid works:

Search left for better answer.

If mid fails:

Search right for possible answer.

**Same for Upper Bound**

Condition:

arr[mid] > target

If true:

mid may be answer
maybe earlier answer exists on left.

So

`ans = mid
high = mid - 1`


**Generic Binary Search for Bounds**

`if condition(mid):
    ans = mid
    high = mid - 1
else:
    low = mid + 1`

Used in:

* lower bound
* upper bound
* first true
* minimum valid answer
* search on answer

When mid satisfies the condition, I store it as a potential answer and continue searching left because I want the earliest valid index.

The time complexity of both Lower Bound and Upper Bound is:
Time Complexity: O(log n).

Because both use binary search.

Why O(log n)?

In every step, search space becomes half.