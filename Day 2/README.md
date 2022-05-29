# Day 2 - Problem Description

## Difficulty: Easy

Consider a CPU which is required to access a sequence of addresses from the **RAM**. In order to save time and avoid searching through the entire RAM every time, the CPU stores the addresses it has recently visited in a smaller, faster memory called **cache**, so that the same data can be found faster in subsequent requests. In case the CPU tries to access an address which is already in cache we have a **cache hit**; otherwise, we have a **cache miss**, and the requested address is loaded onto cache.

In this problem, we consider a cache memory of size _s_ (for _s_ strictly less than the RAM size) which works as follows: given an address _i_ from the RAM, the cache stores the contents of _i_ in position _i_ mod _s_. The task is to write an algorithm which takes as input the RAM size, the cache size and a sequence of addresses, and determines whether each request is a cache hit or a cache miss.

Example of a correct algorithm:

> Give RAM size:  
> 9  
> Give cache size (< RAM size):  
> 4  
> Give addresses (0-8):  
> 3  
> 0  
> 4  
> 3
>
> miss!  
> Cache: [X, X, X, 3]  
> miss!  
> Cache: [0, X, X, 3]  
> miss!  
> Cache: [4, X, X, 3]  
> hit!  
> Cache: [X, X, X, 3]
