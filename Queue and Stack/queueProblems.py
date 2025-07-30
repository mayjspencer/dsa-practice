from collections import deque

# === Problem 1: Simulate a Task Queue ===
def simulate_task_queue(tasks):
    """
    Given a list of tasks (strings), enqueue them and process them in order.
    Print each task as it's processed.
    """
    # Your code here
    dq = deque()
    for task in tasks:
        dq.append(task)
        print(task)


# === Problem 2: First Non-Repeating Character in a Stream ===
def first_non_repeating(stream):
    result = []
    queue = deque()
    count = {}

    for char in stream:
        # Update character count
        count[char] = count.get(char, 0) + 1
        
        # Add to queue if it's the first time seeing this char
        if count[char] == 1:
            queue.append(char)

        # Remove characters from front of queue if they are repeating
        while queue and count[queue[0]] > 1:
            queue.popleft()

        # Determine current non-repeating char
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)

    return result


# === Problem 3: Reverse First K Elements of a Queue ===
def reverse_first_k(queue, k):
    """
    Reverse the first k elements of the queue, keeping the rest intact.
    Use a stack to help.

    Input: queue = deque([1, 2, 3, 4, 5]), k = 3
    Output: deque([3, 2, 1, 4, 5])
    """
    # Your code here
    stack = deque()
    
    for i in range(k):
        stack.append(queue.popleft())
    
    for i in range(k):
        queue.append(stack.pop())
    
    for i in range(len(queue) - k):
        queue.append(queue.popleft())
    
    return queue


# === Test Runner ===
if __name__ == "__main__":
    print("=== Task Queue ===")
    simulate_task_queue(["task1", "task2", "task3"])

    print("\n=== First Non-Repeating Characters ===")
    result = first_non_repeating("aabc")
    print(result)  # Expected: ['a', -1, 'b', 'b']

    print("\n=== Reverse First K Elements ===")
    q = deque([1, 2, 3, 4, 5])
    reverse_first_k(q, 3)
    print(q)  # Expected: deque([3, 2, 1, 4, 5])
