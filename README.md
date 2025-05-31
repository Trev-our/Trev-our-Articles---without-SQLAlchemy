
### OBJECTS RELATION

Welcome to the Object Relations Code Challenge! This project showcases object-oriented programming and database interactions using Python and SQLite. It models relationships between Authors, Magazines, and Articles, enabling you to manage and query publication data efficiently.

 ### 🚀 FEATURES

🗄️ SQLite database with tables for authors, magazines, and articles.
🧑‍💻 Object-oriented models (Author, Magazine, Article) with relationship methods.
📊 Query scripts to analyze publication data (e.g., most prolific author, article counts).
🛠️ Debug script to verify database setup, seeding, and model functionality.
🌱 Seed script to populate the database with test data.


#### 📋TOOLS USED

🐍 Python 3.8+ (tested with Python 3.8.13)
🗄️ SQLite3 (included with Python)
💻 Virtualenv (recommended for dependency management)

### 🛠️ INSTALLATION

Clone the Repository
git clone https://github.com/Marciahpeach/Articles---without-SQLAlchemy.git
cd code-challenge


### SETUP VIRTUAL ENVIRONMENT
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


### INSTALLING DEPENDENCIES
pip install pytest

Expected: lib/  scripts/  tests/  .gitignore  README.md 

### 🚀 USAGE
The primary way to verify the project is by running the debug script, which sets up the database, seeds test data, and prints verification output.

### RUN THE DEBUG
python lib/debug.py


### EXPECTED OUTPUT
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

 ### PROJECT STRUCTURE 

code-challenge/
├── .gitignore              
├── .venv/                
├── README.md               
├── lib/                    
│   ├── __init__.py
│   ├── db/                
│   │   ├── __init__.py
│   │   ├── connection.py  
│   │   ├── schema.sql   
│   │   └── seed.py       
│   ├── models/           
│   │   ├── __init__.py
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   └── debug.py         
├── scripts/             
│   ├── setup_db.py      
│   └── run_queries.py    

### 🤝 Contributing
Contributions are welcome! To contribute:

### Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit changes (git commit -m 'Add YourFeature').
Push to the branch (git push origin feature/YourFeature).
Open a Pull Request.

Please ensure code follows PEP 8 and includes tests if applicable.
### 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
🌟 Happy Coding!
