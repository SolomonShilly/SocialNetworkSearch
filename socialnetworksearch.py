import time
from collections import deque

# Define a class to represent the social network
class SocialNetwork:
    def __init__(self):
        self.network = {}  # Initialize the network as an empty dictionary

    def add_user(self, user):
        if user not in self.network:
            self.network[user] = []  # Create an empty list for the user's friends

    def add_friendship(self, user1, user2):
        if user1 in self.network and user2 in self.network:
            self.network[user1].append(user2)  # Add user2 to user1's list of friends
            self.network[user2].append(user1)  # Add user1 to user2's list of friends

# Function to perform BFS to find the shortest path between two users
def bfs_shortest_path(social_network, startUser, targetUser):
    queue = deque([[startUser]])  # Start with the initial path containing the start user
    visited = {startUser}  # Set to keep track of visited users
    steps = 0  # Initialize step count

    while queue:
        path = queue.popleft()  # Get the first path from the queue
        user = path[-1]  # Get the last user in the current path
        steps += 1  # Increment step count

        if user == targetUser:
            return path, steps  # Return the shortest path found and step count

        for friend in social_network.network.get(user, []):
            if friend not in visited:  # Only explore unvisited friends
                visited.add(friend)  # Mark this friend as visited
                queue.append(path + [friend])  # Create a new path to the friend and add it to the queue

    return None, steps  # Return None if no path is found and step count

# Function to perform DFS to explore all connections from a user
def dfs_explore(social_network, user, visited=None):
    if visited is None:
        visited = set()  # Use a set to keep track of visited users

    visited.add(user)  # Mark the current user as visited
    connections = [user]  # Start with the current user in the list of connections

    for friend in social_network.network.get(user, []):
        if friend not in visited:  # Only explore unvisited friends
            connections.extend(dfs_explore(social_network, friend, visited))  # Add new connections

    return connections  # Return all explored connections

# Function for Depth-Limited Search (DLS)
def dls(social_network, user, targetUser, depth, visited=None):
    if visited is None:
        visited = set()

    visited.add(user)  # Mark the current user as visited

    if user == targetUser:
        return [user], 1  # Return the path and step count if the target user is found

    if depth <= 0:
        return None, 1  # Return None and step count if the depth limit is reached

    for friend in social_network.network.get(user, []):
        if friend not in visited:  # Only explore unvisited friends
            path, steps = dls(social_network, friend, targetUser, depth - 1, visited)
            if path:  # If a path is found, prepend the current user to the path and return it
                return [user] + path, steps + 1  # Return the path and total steps

    return None, 1  # Return None and step count if no path is found

# Function for Iterative Deepening Search (IDS)
def ids(social_network, startUser, targetUser):
    depth = 0
    while True:
        path, steps = dls(social_network, startUser, targetUser, depth)
        if path:
            return path, steps  # Return the path and step count if found
        depth += 1  # Increase the depth limit for the next iteration

# Main function to drive the program
def main():
    # Create a new social network instance
    socialNetwork = SocialNetwork()

    # Mock data: Expand user base significantly
    users = [f"User{i}" for i in range(1000)]  # Adding 1000 users
    for user in users:
        socialNetwork.add_user(user)  # Add each user to the network

    # Mock data: Add a larger set of friendships (randomly connect users)
    import random
    for _ in range(5000):  # Adding 5000 friendships
        user1, user2 = random.sample(users, 2)  # Ensure unique users
        socialNetwork.add_friendship(user1, user2)  # Create each friendship

    # Track time for BFS
    print("\nStarting BFS...")
    start_time = time.time()  # Record the start time
    path, bfs_steps = bfs_shortest_path(socialNetwork, "User0", "User500")
    bfs_time = time.time() - start_time  # Calculate time taken for BFS

    # Display the shortest path result and time taken for BFS
    print("\nBFS Result:")
    if path:
        print(f"Shortest path from User0 to User500: {' -> '.join(path)}")
    else:
        print("No path found from User0 to User500.")
    print(f"Steps taken: {bfs_steps}, Time taken: {bfs_time:.6f} seconds.")

    # Track time for DFS
    print("\nStarting DFS...")
    start_time = time.time()  # Record the start time
    connections = dfs_explore(socialNetwork, "User0")  # Get all connections using DFS
    dfs_time = time.time() - start_time  # Calculate time taken for DFS
    print("\nDFS Result:")
    print(f"All connections from User0: {len(connections)} connections found.")
    print(f"Time taken: {dfs_time:.6f} seconds.")

    # Track time for IDS
    print("\nStarting IDS...")
    start_time = time.time()  # Record the start time
    ids_path, ids_steps = ids(socialNetwork, "User0", "User500")
    ids_time = time.time() - start_time  # Calculate time taken for IDS

    print("\nIDS Result:")
    if ids_path:
        print(f"Path found from User0 to User500: {' -> '.join(ids_path)}")
    else:
        print("No path found from User0 to User500.")
    print(f"Steps taken: {ids_steps}, Time taken: {ids_time:.6f} seconds.")

    # Complexity notes
    print("\nComplexity Analysis:")
    print("BFS Complexity: O(V + E) - Visits each user and friendship once.")
    print("DFS Complexity: O(V + E) - Similar to BFS, visits each user and friendship once.")
    print("DLS Complexity: O(b^d) - Dependent on depth limit and branching factor.")
    print("IDS Complexity: O(b^d) - Similar to DLS but better practical performance due to depth iterations.")

# Main Function
if __name__ == "__main__":
    main()