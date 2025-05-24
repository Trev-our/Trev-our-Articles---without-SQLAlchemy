from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    while True:
        print("\n1. List all authors")
        print("2. List all magazines")
        print("3. Find author by name")
        print("4. Find magazine by name")
        print("5. Find article by title")
        print("6. List magazines with multiple authors")
        print("7. List article counts per magazine")
        print("8. Find most prolific author")
        print("9. Find top publisher")
        print("10. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            print([dict(row) for row in cursor.fetchall()])
            conn.close()
        elif choice == "2":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines")
            print([dict(row) for row in cursor.fetchall()])
            conn.close()
        elif choice == "3":
            name = input("Enter author name: ")
            author = Author.find_by_name(name)
            print(dict(id=author.id, name=author.name) if author else "Author not found")
        elif choice == "4":
            name = input("Enter magazine name: ")
            magazine = Magazine.find_by_name(name)
            print(dict(id=magazine.id, name=magazine.name, category=magazine.category) if magazine else "Magazine not found")
        elif choice == "5":
            title = input("Enter article title: ")
            article = Article.find_by_title(title)
            if article:
                print({
                    "id": article.id,
                    "title": article.title,
                    "author": article.author.name,
                    "magazine": article.magazine.name
                })
            else:
                print("Article not found")
        elif choice == "6":
            magazines = Magazine.with_multiple_authors()
            print([{"id": m.id, "name": m.name, "category": m.category} for m in magazines])
        elif choice == "7":
            counts = Magazine.article_counts()
            print(counts)
        elif choice == "8":
            author = Author.most_prolific()
            print(dict(id=author.id, name=author.name) if author else "No authors found")
        elif choice == "9":
            magazine = Magazine.top_publisher()
            print(dict(id=magazine.id, name=magazine.name, category=magazine.category) if magazine else "No magazines found")
        elif choice == "10":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()