from breezypythongui import EasyFrame


class HelloWorld(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Hello, World!", row=0, column=0)


if __name__ == "__main__":
    HelloWorld().mainloop()
