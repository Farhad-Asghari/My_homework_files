# Creat a class Report that generates a report from data in a file. Provide methods to handle exceptions if the file does not exist or cannot be read.
class Report:
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self):
        try:
            with open(self.filename, "r", encoding = "utf-8") as f:
                data = f.read()
                print(f"report successfully generate from {self.filename}")
        except FileNotFoundError:
            print(f"error: {self.filename} is not found")
        except:
            print(f"error: {self.filename} has some probloms in reading")
                
report = Report("myfile.txt")
report.generate()

