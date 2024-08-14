# Creat a class Log with methods to write error messages to a log file.
class Log:
    def __init__(self, filename = "error_log.txt"):
        self.filename = filename
        
    def error(self, message):
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding = "utf-8") as f:
            f.write(f"{now} \nerror : {message}")

log = Log("myfile.txt")
log.error("we facing with some problems")