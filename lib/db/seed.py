import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from lib.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Clear existing data
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")

        # Insert authors
        authors = [
            ("Trevour Ambia",),
            ("Alvin Mark",),
            ("Gloria Venus",)
        ]
        cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)

        # Insert magazines
        magazines = [
            ("Tech Trends", "Technology"),
            ("Health Weekly", "Health"),
            ("Science Digest", "Science")
        ]
        cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)

        # Insert articles
        cursor.execute("SELECT id FROM authors WHERE name = 'Trevour Ambia'")
        trevour_id = cursor.fetchone()['id']
        cursor.execute("SELECT id FROM authors WHERE name = 'Alvin Mark'")
        alvin_id = cursor.fetchone()['id']
        cursor.execute("SELECT id FROM authors WHERE name = 'Gloria Venus'")
        gloria_id = cursor.fetchone()['id']
        
        cursor.execute("SELECT id FROM magazines WHERE name = 'Tech Trends'")
        tech_id = cursor.fetchone()['id']
        cursor.execute("SELECT id FROM magazines WHERE name = 'Health Weekly'")
        health_id = cursor.fetchone()['id']
        
        articles = [
            ("AI Revolution", trevour_id, tech_id),
            ("Healthy Eating", alvin_id, health_id),
            ("Quantum Computing", trevour_id, tech_id),
            ("Fitness Tips", gloria_id, health_id)
        ]
        cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)

        conn.commit()
        print("Database seeded with test data.")
    except Exception as e:
        print(f"Seeding failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()