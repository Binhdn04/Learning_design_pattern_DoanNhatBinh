# Clients should not be forced to depend on interfaces they do not use
# Một class không nên phụ thuộc hoặc implement method mà nó không dùng 
# Chia interface lớn thành nhiều interface nhỏ, chuyên biệt
class Printer:
    def print(self):
        pass
class Scanner:
    def scan(self):
        pass
class Fax:
    def fax(self):
        pass

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

    def fax(self):
        print("Faxing ")

printer = MultiFunctionPrinter()
printer.print()