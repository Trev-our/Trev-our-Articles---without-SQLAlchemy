# lib/debug.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.db.connection import get_connection
from lib.db.seed import seed_database
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def setup_database():
    conn = get_connection()
    try:
        schema_path = os.path.join(os.path.dirname(__file__), 'db/schema.sql')
        if not os.path.exists(schema_path):
            raise FileNotFoundError(f"Schema file not found at: {schema_path}")
        with open(schema_path, 'r') as file:
            schema = file.read()
        conn.executescript(schema)
        conn.commit()
        print("Database setup complete.")
    except Exception as e:
        print(f"Schema setup failed: {e}")
        raise
    finally:
        conn.close()

def authors_for_magazine(magazine_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT a.* FROM authors a
        JOIN articles art ON a.id = art.author_id
        WHERE art.magazine_id = ?
    """, (magazine_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def magazines_with_multiple_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.* FROM magazines m
        JOIN articles art ON m.id = art.magazine_id
        GROUP BY m.id
        HAVING COUNT(DISTINCT art.author_id) >= 2
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def article_count_per_magazine():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def most_prolific_author():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.* FROM authors a
        JOIN articles art ON a.id = art.author_id
        GROUP BY a.id
        ORDER BY COUNT(art.id) DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def debug():
    # Explicitly set up database before seeding
    setup_database()
    # Run seeding
    try:
        seed_database()
    except Exception as e:
        print(f"Seeding failed: {e}")
        return

    # Connect to database
    conn = get_connection()
    cursor = conn.cursor()

    # Print tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row['name'] for row in cursor.fetchall()]
    print("\nDatabase Tables:", tables)

    # Print authors
    cursor.execute("SELECT * FROM authors")
    authors = [dict(row) for row in cursor.fetchall()]
    print("\nAuthors:")
    for author in authors:
        print(f"ID: {author['id']}, Name: {author['name']}")

    # Print magazines
    cursor.execute("SELECT * FROM magazines")
    magazines = [dict(row) for row in cursor.fetchall()]
    print("\nMagazines:")
    for magazine in magazines:
        print(f"ID: {magazine['id']}, Name: {magazine['name']}, Category: {magazine['category']}")

    # Print articles
    cursor.execute("SELECT * FROM articles")
    articles = [dict(row) for row in cursor.fetchall()]
    print("\nArticles:")
    for article in articles:
        print(f"ID: {article['id']}, Title: {article['title']}, Author ID: {article['author_id']}, Magazine ID: {article['magazine_id']}")

    # Close database connection
    conn.close()

    # Run queries
    print("\nQuery Results:")
    print("Authors for magazine ID 1:", authors_for_magazine(1))
    print("Magazines with multiple authors:", magazines_with_multiple_authors())
    print("Article count per magazine:", article_count_per_magazine())
    print("Most prolific author:", most_prolific_author())

    # Test model interactions
    print("\nModel Interactions:")
    author = Author.find_by_id(1)
    if author:
        print(f"Author Name (ID 1): {author.name}")
        print(f"Articles by Author (ID 1): {author.articles()}")
        print(f"Magazines by Author (ID 1): {author.magazines()}")
    
    magazine = Magazine.find_by_id(1)
    if magazine:
        print(f"Magazine Name (ID 1): {magazine.name}")
        print(f"Article Titles for Magazine (ID 1): {magazine.article_titles()}")

if __name__ == "__main__":
    debug()