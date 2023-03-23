class Node:
    def __init__(self, value, prev=None, next_=None) -> None:
        self.value = value
        self.prev = prev
        self.next_ = next_


class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next_ = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev
        return self.current.value

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next_ is None:
                break
            self.current = self.current.next_
        return self.current.value


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
