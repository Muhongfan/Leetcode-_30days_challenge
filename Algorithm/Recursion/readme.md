Recurrence Relation

There are two important things that one needs to figure out before implementing a recursive function:

recurrence relation: the relationship between the result of a problem and the result of its subproblems.
base case: the case where one can compute the answer directly without any further recursion calls. Sometimes, the base cases are also called bottom cases, since they are often the cases where the problem has been reduced to the minimal scale, i.e. the bottom, if we consider that dividing the problem into subproblems is in a top-down manner.



Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. (Source: wikipedia)


Back to our Fibonacci function F(n). We could use a hash table to keep track of the result of each F(n) with n as the key. The hash table serves as a cache that saves us from duplicate calculations. The memoization technique is a good example that demonstrates how one can reduce compute time in exchange for some additional space.

Given a recursion algorithm, its time complexity {\mathcal{O}(T)}O(T) is typically the product of the number of recursion invocations (denoted as {R}R) and the time complexity of calculation (denoted as {\mathcal{O}(s)}O(s)) that incurs along with each recursion call:

{\mathcal{O}(T) = R * \mathcal{O}(s)}O(T)=R∗O(s)

Tail recursion is a recursion where the recursive call is the final instruction in the recursion function. And there should be only one recursive call in the function.

