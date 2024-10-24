# Social Network Search
This project implements a social network model allowing users to add friends and explore connections. It utilizes various algorithms for pathfinding and connection exploration.

## Features
- User management to add users and friendships
- Pathfinding using Breadth-First Search (BFS) for the shortest path
- Depth-First Search (DFS) to explore all connections from a user
- Iterative Deepening Search (IDS) for effective pathfinding with varying depths
- Complexity analysis for algorithm performance

## Execution Results
### Starting BFS...
**BFS Result:**
- Shortest path from User0 to User500: `User0 -> User389 -> User712 -> User105 -> User500`
- Steps taken: 970
- Time taken: 0.002284 seconds

### Starting DFS...
**DFS Result:**
- All connections from User0: 1000 connections found
- Time taken: 0.004874 seconds

### Starting IDS...
**IDS Result:**
- Path found from User0 to User500: `User0 -> User980 -> User572 -> User947 -> User508 -> User385 -> User474 -> User105 -> User500`
- Steps taken: 9
- Time taken: 0.003493 seconds

## Complexity Analysis
- **BFS Complexity:** O(V + E) - Visits each user and friendship once.
- **DFS Complexity:** O(V + E) - Similar to BFS, visits each user and friendship once.
- **DLS Complexity:** O(b^d) - Dependent on depth limit and branching factor.
- **IDS Complexity:** O(b^d) - Similar to DLS but better practical performance due to depth iterations.

## Usage
- Clone the repository
- Run the `socialnetworksearch.py` file
- The program will generate mock data with 1000 users and 5000 friendships
- Follow the printed output to see results of BFS, DFS, and IDS algorithms
