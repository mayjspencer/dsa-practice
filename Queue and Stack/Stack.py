class Stack:
    def __init__(self):
        self.stacklist = []

    def push(self, item):
        self.stacklist.append(item)

    def pop(self):
        return self.stacklist.pop()

    def peek(self):
        return self.stacklist[-1]

    def is_empty(self):
        if len(self.stacklist) == 0:
            return True
        return False

    def size(self):
        return len(self.stacklist)


def reverse_string(s):
    """
    Use a stack to reverse the input string.
    Input: "hello"
    Output: "olleh"
    """
    stack = Stack()
    
    for char in s:
        stack.push(char)

    s2 = ''
    for char in s:
        s2 += stack.pop()
    # Your code here

    return s2  # Replace with actual reversed string


def is_balanced(expr):
    """
    Use a stack to check for balanced parentheses.
    Only checks (), but could be expanded to {}, [].
    
    Input: "(())" → True
           "(()"  → False
    """
    stack = Stack()

    for char in expr:
        if char == '(':
            stack.push('(')
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()

    if stack.is_empty():
        return True
    else:
        return False
    # Your code here


def evaluate_postfix(expr):
    stack = Stack()
    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            token = int(token)
            stack.push(token)
        else:
            right = stack.pop()
            stack.push(token)
            stack.push(right)

    # Final result should be on top of the stack
    return 0



if __name__ == "__main__":
    print("Reverse 'hello':", reverse_string("hello"))  # olleh
    print("Balanced '(()())':", is_balanced("(()())"))   # True
    print("Balanced '(()':", is_balanced("(()"))         # False
    print("Postfix '2 3 + 4 *':", evaluate_postfix("2 3 + 4 *"))  # 20

