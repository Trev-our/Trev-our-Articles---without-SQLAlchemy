import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self._id = id
        self._name = None
        self._category = None
        self.name = name  # Use setter for validation
        self.category = category  # Use setter for validation
        if id is None:
            self._save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def _save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self._id = cursor.lastrowid
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Failed to save magazine: {e}")
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None

    @classmethod
    def with_multiple_authors(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            HAVING COUNT(DISTINCT a.author_id) >= 2
        """)
        magazines = [cls(row['name'], row['category'], row['id']) for row in cursor.fetchall()]
        conn.close()
        return magazines

    @classmethod
    def article_counts(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.name, COUNT(a.id) as article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
        """)
        counts = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return counts

    @classmethod
    def top_publisher(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            ORDER BY COUNT(a.id) DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['category'], row['id']) if row else None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return [dict(article) for article in articles]

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles art ON a.id = art.author_id
            WHERE art.magazine_id = ?
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [dict(author) for author in authors]

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        titles = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return titles

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.* FROM authors a
            JOIN articles art ON a.id = art.author_id
            WHERE art.magazine_id = ?
            GROUP BY a.id
            HAVING COUNT(art.id) > 2
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return [dict(author) for author in authors]