import wpf
import Bakend
import sys

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Library.xaml')
        books = Bakend.view_all()
        for t_book in books:
            l_book = list(t_book)
            book = str(l_book[0]) + "\t" + str(l_book[1]) + "\t" + str(l_book[2]) + "\t" + str(l_book[3]) + "\t" + str(l_book[4])
            self.List1.Items.Add(book)

    def clear(self):
        self.List1.Items.Clear()

    
    def view_command(self, books=None):
        if books == None:
            books = Bakend.view_all()
        self.clear()
        for t_book in books:
            l_book = list(t_book)
            book = str(l_book[0]) + "\t" + str(l_book[1]) + "\t" + str(l_book[2]) + "\t" + str(l_book[3]) + "\t" + str(l_book[4])
            self.List1.Items.Add(book)

    def remove(self):
        self.view_command()
        self.Title2.Text = ""
        self.Author2.Text = ""
        self.Year2.Text = ""
        self.ISBN2.Text = ""
    


    def ViewAll1_Click(self, sender, e):
        books = Bakend.view_all()
        self.view_command(books)

    
    def Close1_Click(self, sender, e):
        sys.exit()

    
    def SearchBooks1_Click(self, sender, e):
        title = self.Title2.Text
        writer = self.Author2.Text
        year = self.Year2.Text
        isbn = self.ISBN2.Text
        books = Bakend.search(title, writer, year, isbn)
        self.view_command(books)
        
    def AddBooks1_Click(self, sender, e):
        title = self.Title2.Text
        writer = self.Author2.Text
        year = int(self.Year2.Text)
        isbn = int(self.ISBN2.Text)
        books = Bakend.insert(title, writer, year, isbn)
        self.view_command()
        self.remove()

    
    def List1_PreviewMouseDoubleClick(self, sender, e):
        s_book = self.List1.SelectedItem.ToString()
        book = s_book.split("\t")
        global my_id
        my_id = int(book[0])
        self.Title2.Text = str(book[1])
        self.Author2.Text = str(book[2])
        self.Year2.Text = str(book[3])
        self.ISBN2.Text = str(book[4])

    
    def UpdateBook1_Click(self, sender, e):
        Bakend.update(my_id, self.Title2.Text, self.Author2.Text, int(self.Year2.Text), int(self.ISBN2.Text))
        self.view_command()
        
    def DeleteBook1_Click(self, sender, e):
        Bakend.delete(my_id)
        self.remove()        
    
    


if __name__ == '__main__':
    Application().Run(MyWindow())
