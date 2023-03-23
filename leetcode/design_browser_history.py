class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __get_node(self, index: int):
        if index < 0:
            return None
        node = self.head
        for _ in range(index):
            node = node.next_
        return node

    def get(self, index: int):
        node = self.__get_node(index)
        return node.value

    def insert(self, index, value):
        new_node = Node(value)
        if self.__is_empty():
            self.head = new_node
            self.tail = new_node
            return
        prev_node = self.__get_node(index - 1)
        if prev_node is None:
            raise IndexError
        if prev_node.next_ is None:
            self.tail.next_ = new_node
            self.tail = new_node
            return
        prev_node.next_ = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.__is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_ = new_node
        self.tail = new_node

    def __is_empty(self) -> bool:
        return self.head is None and self.tail is None

    def __str__(self):
        node = self.head
        if node is None:
            return "[]"
        values = str(node)
        while node.next_:
            node = node.next_
            values += ", " + str(node)
        return "[" + values + "]"


class BrowserHistory:

    def __init__(self, homepage: str):
        self.histories = LinkedList()
        self.histories.append(Node(homepage))
        self.current = 0
        self.size = 0
        print(f"homepage: {homepage} / {self.current}")

    def visit(self, url: str) -> None:
        self.current += 1
        self.size += 1
        if self.current == self.size:
            self.histories.append(url)
            print(f"visit1 {url} / {self.current} / {self.size}")
            return
        if self.size > self.current:
            self.size = self.current
        self.histories.insert(self.current, Node(url))
        print(f"visit2 {url} / {self.current} / {self.size}")

    def back(self, steps: int) -> str:
        self.current -= steps
        if self.current < 0:
            self.current = 0
        url = self.histories.get(self.current)
        print(f"back {steps} / {url} / {self.current} / {self.size}")
        return url

    def forward(self, steps: int) -> str:
        self.current += steps
        if self.current > self.size:
            self.current = self.size
        url = self.histories.get(self.current)
        print(f"forward {steps} / {url} / {self.current} / {self.size}")
        return url

    def __str__(self):
        return self.histories.__str__()


browser_history = BrowserHistory("esgriv.com")
browser_history.visit("cgrt.com")
browser_history.visit("tip.com")
browser_history.back(9)
browser_history.visit("kttzxgh.com")
browser_history.forward(7)
browser_history.visit("crqje.com")
browser_history.visit("iybch.com")
browser_history.forward(5)
browser_history.visit("uun.com")
browser_history.back(10)
browser_history.visit("hci.com")
browser_history.visit("whula.com")
browser_history.forward(10)
print(browser_history)
