from lib.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.execute("BEGIN TRANSACTION")
        # Clear existing data
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")

        # Insert authors
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Doe",))
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Smith",))
        cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Alice Johnson",))

        # Insert magazines
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Digest", "Health"))
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Science Monthly", "Science"))

        # Insert articles
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                      ("Tech Trends 2025", 1, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                      ("AI Revolution", 1, 1))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                      ("Healthy Living", 2, 2))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                      ("Quantum Physics", 3, 3))
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                      ("Tech Gadgets", 2, 1))

        conn.commit()
        print("Database seeded successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Seeding failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()