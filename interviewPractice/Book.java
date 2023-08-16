import java.util.ArrayList;






/*
online cloud reading application
kinda like kindle (short stories)
help designing the code to implement online cloud reading




*  users have a library of books that they can add or remove

* can set a book as active

*the application remembers where a user left off in a given book

* the reading application only displays a page of text at a time in the active book

 - all books in library
 - remember active book
 - remember last pages in all books
 - display page in active book



 - Class -->> Book:
        - title
        - pages/content in the book
        - last page user looked at

  - Class -->> library (collection of books)
        - active book
*/
public class Book {

    private String title;
    private String[] pages;
    private int lastPage;
    private int id;

    public Book(String title, String[] pages, int id ){

        this.title = title;
        this.pages = pages;
        this.id = id;
        lastPage = 0;
    }

    public String display(){
        return pages[lastPage];
    }

    public void turnPageRight(){
       if (lastPage < pages.length){
           id += 1;
           display();

       }
       else{
           System.out.println("congrats You have finsihed the book");

       }

    }

    public void turnPageleft(){
        if (lastPage > 0){
            id -= 1;
            display();

        }
        else{
            System.out.println("The book has just started");

        }

    }









}
