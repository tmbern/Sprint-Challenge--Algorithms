#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(n). As the input size grows, the runtime will grow at a constant rate.


b) Runtime is O(n log n). As the input size grows to very large numbers, it will take longer each time in the while loop. for example: when n = 1, the while loop will exit after the first iteration. when n = 2 the while loop will exit after the first iteration. But, when n = 3, the while loop will iterate 2x (j = 1, then 1*2 < 3, so we will need to iterate another time). So as input grows increasingly large, the amount of times to stay in the while loop will increase.  


c) Runtime is O(n). Because we are decreasing the input by 1 and using recursion till we hit the base case of input == 0. As input increases, we will run the recursive function that many times. 

## Exercise II

to sart we want to find the midpoint of the n-story building. 
the ceiling is the top floor and the base is the bottom floor. 
we would find the mid point of the building by taking the difference between the ceiling and base and dividing by 2

we would drop the egg from our midpoint.
if the egg broke then we know that we are too high and would need the first floor below the midpoint to be the new ceiling.
We would then re-drop the egg from the new midpoint. 

if the egg didnt break then we could be at the sweet spot but we also might be at any of the floors that are beneath the optimal floor.
We will need to set the floor above our current midpoint to the new floor.
We would then redrop our egg from the new midpoint.

We would continue dropping our egg untill there were no floors above or below our midpoint. That would be our optimal floor. 

The runtime of this would be o(log n). As the number of floors increase that would increase the runtime of the algorithm. However, because we are essentially eliminating half of the floors each pass, the algorithm doesn run for each input. So it would grow at a slower rate than a linear runtime.  
