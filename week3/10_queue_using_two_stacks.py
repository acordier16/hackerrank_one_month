# Enter your code here. Read input from STDIN. Print output to STDOUT

# This solution was written with the help of AbhishekVermaIIT user
# on the HR forum, since I was not familiar with queues and stacks.
# See this illustration: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH4hPfzI5DYZEpC9CcX7dCAKzjBV1VgrtYvA&usqp=CAU

nb_queries = int(str(input().strip()))
stack1 = []
stack2 = []
while True:
    try:
        query = input().strip()
        query_type = int(query.split(" ")[0])
        if query_type == 1:
            x = int(query.split(" ")[1])
            # If stack 1 is empty, we remember the head value
            if not stack1:
                head_stack1 = x
            # Push to stack 1
            stack1.append(x)
        elif query_type == 2:
            # If stack 2 is empty...
            if not stack2:
                # While stack 1 is full, fill stack 2 with stack 1 values,
                # in the "reverse order"
                while stack1:
                    stack2.append(stack1.pop())
            # The first element of stack 1 is now the last element of stack 2
            # We only have to pop() on stack 2 to dequeue it
            stack2.pop()
        else:  # query_type == 3
            # Return the last element of the stack 2, or, if empty,
            # the head of stack 1
            print(stack2[-1] if stack2 else head_stack1)
    except EOFError:
        break
