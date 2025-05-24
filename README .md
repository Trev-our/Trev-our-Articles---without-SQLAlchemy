# Articles Code Challenge
A Python application modeling Authors, Articles, and Magazines with a SQLite database, using raw SQL queries.
Object Relations Code Challenge
Overview
This project is a Python-based Object Relations Code Challenge for Phase 3 of the Moringa School curriculum. It implements a database-driven application to manage authors, magazines, and articles, demonstrating object-oriented programming and SQLite database interactions. The application includes model classes (Author, Magazine, Article), a database schema, seeding scripts, and debugging tools to verify functionality.
Features

Database Schema: Defines tables for authors, magazines, and articles with foreign key relationships.
Model Classes: Author, Magazine, and Article classes with methods to query relationships (e.g., author.articles(), magazine.article_titles()).
Seeding: Populates the database with sample data for testing.
Debugging: A standalone debug.py script to verify database setup, seeding, queries, and model interactions by printing output.

Project Structure
code-challenge/
├── lib/
│   ├── __init__.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   ├── seed.py
│   │   └── utils.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   ├── controllers/
│   │   └── __init__.py
│   └── debug.py
├── scripts/
│   ├── setup_db.py
│   ├── run_queries.py
│   └── cli.py
├── articles.db
├── env/
├── .gitignore
├── README.md
└── requirements.txt


lib/db/schema.sql: Defines the SQLite database schema.
lib/db/seed.py: Seeds the database with sample data.
lib/db/connection.py: Manages SQLite database connections.
lib/models/*.py: Contains model classes for Author, Magazine, and Article.
lib/debug.py: Verifies the application by printing database contents, query results, and model interactions.
scripts/setup_db.py: Initializes the database schema.
scripts/run_queries.py: Runs sample SQL queries.
scripts/cli.py: (Optional) Interactive CLI for querying the database.

Prerequisites

Python 3.8+
Virtualenv
SQLite3

Setup Instructions

Clone the Repository:
git clone <repository-url>
cd code-challenge


Set Up Virtual Environment:
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


Install Dependencies:If requirements.txt exists, install dependencies:
pip install -r requirements.txt

Note: This project uses only the Python standard library (including sqlite3), so no external dependencies are required unless specified.

Verify Project Structure:Ensure all files listed in the project structure are present, especially lib/db/schema.sql and lib/debug.py.


Running the Application
To verify the application, use the lib/debug.py script, which sets up the database, seeds it with sample data, and prints verification output.

Clear Existing Database (optional, to start fresh):
rm articles.db


Run Debug Script:
source env/bin/activate
python lib/debug.py


Expected Output:The script will print:

Confirmation of database setup and seeding.
List of database tables (authors, magazines, articles).
Contents of authors, magazines, and articles tables.
Query results (e.g., authors for a magazine, article counts).
Model interactions (e.g., articles by an author, magazine titles).

Example output:
Database setup complete.
Database seeded with test data.

Database Tables: ['authors', 'magazines', 'articles']

Authors:
ID: 1, Name: Jane Doe
ID: 2, Name: John Smith
ID: 3, Name: Alice Johnson

Magazines:
ID: 1, Name: Tech Trends, Category: Technology
ID: 2, Name: Health Weekly, Category: Health
ID: 3, Name: Science Digest, Category: Science

Articles:
ID: 1, Title: AI Revolution, Author ID: 1, Magazine ID: 1
ID: 2, Title: Healthy Eating, Author ID: 2, Magazine ID: 2
ID: 3, Title: Quantum Computing, Author ID: 1, Magazine ID: 1
ID: 4, Title: Fitness Tips, Author ID: 3, Magazine ID: 2

Query Results:
Authors for magazine ID 1: [{'id': 1, 'name': 'Jane Doe'}]
Magazines with multiple authors: [{'id': 2, 'name': 'Health Weekly', 'category': 'Health'}]
Article count per magazine: [{'name': 'Tech Trends', 'article_count': 2}, {'name': 'Health Weekly', 'article_count': 2}, {'name': 'Science Digest', 'article_count': 0}]
Most prolific author: {'id': 1, 'name': 'Jane Doe'}

Model Interactions:
Author Name (ID 1): Jane Doe
Articles by Author (ID 1): [{'id': 1, 'title': 'AI Revolution', 'author_id': 1, 'magazine_id': 1}, {'id': 3, 'title': 'Quantum Computing', 'author_id': 1, 'magazine_id': 1}]
Magazines by Author (ID 1): [{'id': 1, 'name': 'Tech Trends', 'category': 'Technology'}]
Magazine Name (ID 1): Tech Trends
Article Titles for Magazine (ID 1): ['AI Revolution', 'Quantum Computing']



Troubleshooting

ModuleNotFoundError: No module named 'lib':Ensure all scripts (debug.py, seed.py, model files) include:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

Verify __init__.py files exist in lib/, lib/db/, and lib/models/.

No such table errors:Delete articles.db and re-run:
rm articles.db
python lib/debug.py

Ensure lib/db/schema.sql exists and contains the correct schema.

Schema file not found:Verify lib/db/schema.sql exists:
ls lib/db/schema.sql



Submission
To submit the project:

Commit changes:git add .
git commit -m "Complete Object Relations Code Challenge with debug verification"
git push origin main


Submit the repository link or required files as per Moringa School instructions.

Author
Trevour
License
This project is for educational purposes as part of Moringa School's Phase 3 curriculum.
