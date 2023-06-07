# Page Replacement Algorithm Comparison

## Project Summary

In this project, three page-replacement algorithms (FIFO, LRU, and OPT) were implemented in Python to generate page-reference strings, ranging from 0 to 9. The program recorded the number of page faults incurred by each algorithm using different configurations.

The Python project repository can be found [here](https://github.com/chambored/page-replacement-algorithms).

## Experiments

### Initial Test Strings

Three initial test strings of size 20 with 3 page frames were used to test the algorithms:

1. 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1
2. 8,1,0,7,3,0,3,4,5,3,5,2,0,6,8,4,8,1,5,3
3. 4,6,4,8,6,3,6,0,5,9,2,1,0,4,6,3,0,6,8,4

### Generated Random Strings

Random reference strings were generated for the following configurations: 

- Reference string sizes (rss): 10, 15, 20
- Number of page frames (npf): 3, 5, 7

A total of 27 configurations (3 per each of the 9 combinations) were tested.

## Results

[Program Output](output.txt)

## Discussion:

Three memory management strategies are compared: Optimal, Least Recently Used (LRU), and First-In-First-Out (FIFO). These strategies dictate how a computer chooses which 'pages' of data to store in its main memory and which to remove when space is needed for new data.

1. **Optimal**: This strategy possesses the ability to predict the future and knows precisely when a page will be needed again. The page not needed for the longest time next is always the one to be removed. Although this method offers superior performance, it's impractical since it assumes knowledge of future events.
2. **LRU**: The LRU strategy chooses the page that has not been accessed for the longest period. This approach makes an intelligent decision based on past usage but lacks the ability to foresee future requirements.
3. **FIFO**: The FIFO strategy follows a simple principle: the oldest page is always the first to be removed. This method doesn't consider the frequency or recency of page usage.

The number of page frames (slots in memory for storing pages) also plays a role. More page frames means more room for data, lessening the need for page replacement.

## Conclusion:

Based on this analysis, the Optimal strategy consistently outperforms the rest, owing to its theoretical ability to predict future requirements. The LRU and FIFO strategies perform satisfactorily, but they can't match the Optimal strategy's performance because their decision-making processes are less informed.

When the number of page frames increases, performance typically improves across all strategies. This improvement happens because more memory space decreases the need for page replacements.

However, these results rely on specific page reference sequences. In real-world situations, page reference patterns can vary greatly, which may alter the relative performance of these strategies. But it is still expected that the Optimal strategy will always perform at least as well as the other strategies, if not better.
