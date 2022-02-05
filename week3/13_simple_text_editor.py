# Enter your code here. Read input from STDIN. Print output to STDOUT


class S:
    """
    We use lists as stacks (you can only append and pop)
    Two alternative strategies.
    Either you:
        a) Save a history of operations
            Advantage: memory-light.
            Inconvenient: more compute (you need to re-compute operations).
        b) Save a history of strings
            Advantage: no compute overhead.
            Inconvenient: memory-heavy (needs copies)
    To pass the tests, you need to pick solution b.
    """

    def __init__(self, s: str = "") -> None:
        self.s = list(s)
        self.history = [self.s.copy()]

    def append(self, w: str) -> None:
        self.s += list(w)
        self.history.append(self.s.copy())

    def delete(self, k: int) -> None:
        for i in range(k):
            self.s.pop()
        self.history.append(self.s.copy())

    def undo(self) -> None:
        self.history.pop()
        if self.history:
            self.s = self.history[-1].copy()

    def print(self, k):
        print(self.s[k - 1])


nb_queries = input()
s = S()
while True:
    try:
        in_ = input()
        query_type = int(in_.split(" ")[0])
        if query_type in [1, 2, 3]:
            argument = in_.split(" ")[1]
            if query_type == 1:
                s.append(w=argument)
            elif query_type == 2:
                s.delete(k=int(argument))
            else:  # query_type == 3
                s.print(k=int(argument))
        else:  # query_type == 4
            s.undo()
    except EOFError:
        break
