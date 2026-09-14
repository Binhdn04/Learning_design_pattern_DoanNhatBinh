# Tree data structure, xu ly mot object va 1 nhom object cung 1 cach
class File:
    def show(self):
        print("File")

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)

    def show(self):
        print(f"{self.name}")
        for child in self.children:
            child.show()

# Client
root = Folder("Documents")

root.add(File())
root.add(File())

projects = Folder("Projects")
projects.add(File())
projects.add(File())

root.add(projects)

root.show()