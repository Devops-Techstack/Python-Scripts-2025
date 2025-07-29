 
 #"You have the string 'accgbiy'. Your task is to sort its characters 
 #alphabetically using a Python script. While Python offers built-in sorting capabilities, 
 #for this exercise, we will specifically apply the logic of the Bubble Sort algorithm 
 #to achieve the sorted output of 'abccgiy'."
 

def sort_string_bubble_sort(s):
   """
   Sorts a string alphabetically using a basic Bubble Sort algorithm.
   (Less efficient than built-in methods, for demonstration purposes).
 
   Args:
     s: The input string.
 
   Returns:
     The sorted string.
   """
 
   #char_list = list(s): Our sorting machine can't easily move individual 
   # letters around when they're stuck together in a word. So, this line 
   # takes your input word (like "accgbiy") and breaks it into a list of individual 
   # letters:
   char_list = list(s)
   print(char_list)
   n = len(char_list)
   
   for i in range(n - 1):
     # Last i elements are already in place
     for j in range(0, n - i - 1):
       # Traverse the list from 0 to n-i-1
       # Swap if the element found is greater than the next element
       if char_list[j] > char_list[j + 1]:
         char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
 
   return "".join(char_list)
 
my_string = "accgbiy"
sorted_result_bubble = sort_string_bubble_sort(my_string)
print(f"Sorted string (Bubble Sort): {sorted_result_bubble}")
 
 
""" 
 Imagine our list of letters is
 ['a', 'c', 'c', 'g', 'b', 'i', 'y']
 
 The length n is 7.
 
 The Outer Loop: for i in range(n - 1):
 This loop controls how many full passes we make through the list.
 
 n - 1 is 7 - 1 = 6. So, this loop will run i for values
 0, 1, 2, 3, 4, 5
 
 .
 Think of i as the number of elements already sorted and placed at the end of the list.
 Why n - 1 passes?
 Because after each pass, at least one element (the largest unsorted one) is guaranteed to be in its correct final position at the end. If you have 7 items, you only need to make 6 passes to ensure the first 6 are in place, because if they are, the 7th one must also be in place.
 
 The Inner Loop:
 for j in range(0, n - i - 1):
 
 This loop is where the actual comparisons and swaps happen in each pass.
 
 j represents the current position we are looking at in the list.
 n - i - 1 is the limit for j. This tells us how far we need to go in the current pass.
 Let's trace it with our example
 ['a', 'c', 'c', 'g', 'b', 'i', 'y']
 
 :
 
 Pass 1: i = 0
 
 Outer loop: i is 0. This means 0 elements are sorted at the end.
 
 Inner loop: j will go from 0 up to n - i - 1 = 7 - 0 - 1 = 6. So j will be
 0, 1, 2, 3, 4, 5
 
 .
 
 j = 0: Compare char_list[0] ('a') and char_list[1] ('c'). 'a' is not greater than 'c'. No swap.
 List:
 ['a', 'c', 'c', 'g', 'b', 'i', 'y']
 
 j = 1: Compare char_list[1] ('c') and char_list[2] ('c'). 'c' is not greater than 'c'. No swap.
 List:
 ['a', 'c', 'c', 'g', 'b', 'i', 'y']
 
 j = 2: Compare char_list[2] ('c') and char_list[3] ('g'). 'c' is not greater than 'g'. No swap.
 List:
 ['a', 'c', 'c', 'g', 'b', 'i', 'y']
 
 j = 3: Compare char_list[3] ('g') and char_list[4] ('b'). 'g' IS greater than 'b'. SWAP!
 List becomes:
 ['a', 'c', 'c', 'b', 'g', 'i', 'y']
 
 (notice 'b' and 'g' swapped)
 j = 4: Compare char_list[4] ('g') and char_list[5] ('i'). 'g' is not greater than 'i'. No swap.
 List:
 ['a', 'c', 'c', 'b', 'g', 'i', 'y']
 
 j = 5: Compare char_list[5] ('i') and char_list[6] ('y'). 'i' is not greater than 'y'. No swap.
 List:
 ['a', 'c', 'c', 'b', 'g', 'i', 'y']
 
 End of Pass 1. Notice that 'y' (the largest letter) is now at the very end. It has "bubbled up" to its correct final position.
 
 Pass 2: i = 1
 
 Outer loop: i is 1. This means 1 element ('y') is now sorted at the end.
 
 Inner loop: j will go from 0 up to n - i - 1 = 7 - 1 - 1 = 5. So j will be
 0, 1, 2, 3, 4
 
 .
 
 Crucially: We don't need to check char_list[6] ('y') anymore because we know it's in place. The loop for j stops before reaching it.
 
 j = 0: Compare char_list[0] ('a') and char_list[1] ('c'). No swap.
 
 List:
 ['a', 'c', 'c', 'b', 'g', 'i', 'y']
 
 j = 1: Compare char_list[1] ('c') and char_list[2] ('c'). No swap.
 
 List:
 ['a', 'c', 'c', 'b', 'g', 'i', 'y']
 
 j = 2: Compare char_list[2] ('c') and char_list[3] ('b'). 'c' IS greater than 'b'. SWAP!
 
 List becomes:
 ['a', 'c', 'b', 'c', 'g', 'i', 'y']
 
 j = 3: Compare char_list[3] ('c') and char_list[4] ('g'). No swap.
 
 List:
 ['a', 'c', 'b', 'c', 'g', 'i', 'y']
 
 j = 4: Compare char_list[4] ('g') and char_list[5] ('i'). No swap.
 
 List:
 ['a', 'c', 'b', 'c', 'g', 'i', 'y']
 
 End of Pass 2. Now 'i' (the second largest unsorted letter) is in its correct final position.
 
 Pass 3: i = 2
 
 Outer loop: i is 2. This means 2 elements ('y', 'i') are sorted at the end.
 
 Inner loop: j will go from 0 up to n - i - 1 = 7 - 2 - 1 = 4. So j will be
 0, 1, 2, 3
 
 .
 
 We are now only comparing elements up to char_list[4].
 
 j = 0: Compare char_list[0] ('a') and char_list[1] ('c'). No swap.
 
 List:
 ['a', 'c', 'b', 'c', 'g', 'i', 'y']
 
 j = 1: Compare char_list[1] ('c') and char_list[2] ('b'). 'c' IS greater than 'b'. SWAP!
 
 List becomes:
 ['a', 'b', 'c', 'c', 'g', 'i', 'y']
 
 j = 2: Compare char_list[2] ('c') and char_list[3] ('c'). No swap.
 
 List:
 ['a', 'b', 'c', 'c', 'g', 'i', 'y']
 
 j = 3: Compare char_list[3] ('c') and char_list[4] ('g'). No swap.
 
 List:
 ['a', 'b', 'c', 'c', 'g', 'i', 'y']
 
 End of Pass 3. 'g' is now in place. """
