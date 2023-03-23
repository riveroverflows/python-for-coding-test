class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        if len(self.history) - 1 > self.current:
            self.history[self.current + 1:] = []
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current -= steps
        if self.current < 0:
            self.current = 0
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current += steps
        if self.current > len(self.history) - 1:
            self.current = len(self.history) - 1
        return self.history[self.current]


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
