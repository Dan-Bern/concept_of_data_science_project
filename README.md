# Concepts of Data Science Project

## Tenary search tree implementation  

Hasselt University 1st Year Master of Statistics and Data Science 

Contributors: Edwin Dzoro Mwazuma (2469499) and Daniel Mutwiri Benard (2469288) 

## Project Overview
This project implements a Ternary Search Tree (TST) in Python, a data structure that combines the efficiency of a binary search tree with the ability to store and retrieve strings efficiently. TSTs are especially useful in applications involving auto-completion, spell checking, and dictionary word searches.

## Key Features
Insert: Efficiently adds strings to the TST.

Search: Quickly checks for the existence of a given word.

Performance Comparison: Includes benchmarking against a B-tree implementation using BTrees.OOBTree.

## Implementation on the HPC Infrastructure
The script used to run is available under the file name project_script.slurm

## Benchmarking
We benchmark the TST's performance on insertion and search operations across increasing word volumes and compare it with a B-Tree wrapper to analyze time complexity trends. This was done in the HPC infrastructure and the output file is under the file name performance_58227431.out.

## Dependencies
Python 3.10.4

## Conclusion
The benchmarking results showed that the Ternary Search Tree (TST), while functional and capable of handling increasing volumes of data, is significantly slower than the B-Tree implementation in both insertion and search operations.

TST Performance: Insertion time increased approximately linearly with the number of words, reaching ~0.10 seconds for 10,000 words. Search times also grew steadily but remained under 0.01 seconds.

B-Tree Performance: Insertion and search times remained extremely low throughout, with insertion times under 0.005 seconds and search times nearly constant below 0.0006 seconds even at 10,000 words.

These results suggest that while TSTs are useful for string-heavy applications (like prefix-based lookups or auto-completion), they may not be optimal for high-performance requirements where speed is critical, especially when compared to a B-Tree structure optimized for rapid insert/search operations.
