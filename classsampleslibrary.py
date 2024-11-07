class Library:
    def __init__(self, book, author, availability):
        self.book = book
        self.author = author
        self.availability = availability
    
    def status(self):
        if self.availability == 0:
            print("Book is not available by the author "+self.author)
        else:
            print("Book is available by the author "+self.author)
            
    def set_availability(self, status):
        self.availability = status
    
    def show_author(self):
        print(f"Author: {self.author}")


x = Library("Book Name 1", "Author 1", 6)
y = Library("Book Name 2", "Author 2", 0)

x.status()  
y.status()

x.show_author()
y.show_author()