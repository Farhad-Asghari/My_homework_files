# Creat a class FileManager with methods to read from and write to a file.
class FileManger:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        try:
            with open(self.filename, "r", encoding = "utf-8") as f:
                content = f.read()
                return content
        except FileNotFoundError:
            return "file is not found"
    
    def  write(self, text):
        try:
            with open(self.filename, "w", encoding = "utf-8") as f:
                f.write(text)
                print("The text is  wrote successfully in", self.filename)
        except FileNotFoundError:
            print(self.filename, "is not found")

file_manager = FileManger("myfile.txt")
file_manager.write("hello world")
print(file_manager.read())
