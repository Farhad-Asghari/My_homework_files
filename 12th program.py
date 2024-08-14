#Creat a calss Book with private attributes title, author, and pages. Provide public methods to get and set these attributes.
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
        
    def get_title(self):
        return self.__title
    
    def set_title(self,new_title):
        self.__title = new_title
    
    def get_author(self):
        return self.__author
    
    def set_author(self, new_author):
        self.__author = new_author
    
    def get_pages(self): 
        return self.__pages 
    
    def set_pages(self, new_pages):
        self.__pages = new_pages

kitab = Book("yong man" ,"Tolastoi", 200 )
print(kitab.get_title())
kitab.set_pages(100)
print(kitab.get_pages())
kitab.set_title("The oldest human")
print(kitab.get_title())

    