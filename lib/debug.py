from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database
from lib.db.utils import add_author_with_articles

if __name__ == "__main__":
    seed_database()
    print("Database seeded. Start debugging...")
    # Example usage
    author = Author.find_by_name("John Doe")
    print("John Doe's articles:", author.articles())
    print("John Doe's magazines:", author.magazines())
    print("John Doe's topic areas:", author.topic_areas())
    
    magazine = Magazine.find_by_name("Tech Weekly")
    print("Tech Weekly's articles:", magazine.articles())
    print("Tech Weekly's contributors:", magazine.contributors())
    print("Tech Weekly's article titles:", magazine.article_titles())
    
    # Test transaction
    articles_data = [
        {"title": "New Tech Article", "magazine_id": 1},
        {"title": "Another Article", "magazine_id": 2}
    ]
    success = add_author_with_articles("New Author", articles_data)
    print("Transaction success:", success)