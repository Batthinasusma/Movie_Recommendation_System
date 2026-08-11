# Movie Recommendation System


A graph-based Movie Recommendation System built using Python, Flask, and CognoDB.

## 1. Use Case

This application helps users discover movies related to a movie they already like.

The user selects a movie from the application and clicks the "Recommend Movies" button. The system finds other movies that share genres with the selected movie and displays them as recommendations.

## 2. Graph Database

A graph database is suitable for this application because the main information is based on relationships between movies and genres.

The data is represented as:

Movie -> HAS_GENRE -> Genre

For example:

Avatar -> HAS_GENRE -> Sci-Fi
Interstellar -> HAS_GENRE -> Sci-Fi

When a user selects a movie, the application can traverse:

Movie -> Genre -> Movie

This makes relationship-based movie recommendations natural to express using Cypher.

## 3. Graph Data Model

### Nodes

Movie

Properties:
- title

Genre

Properties:
- name

### Relationship

Movie -[HAS_GENRE]-> Genre

Example:

Avatar -[HAS_GENRE]-> Sci-Fi
Interstellar -[HAS_GENRE]-> Sci-Fi

## 4. Technology Stack

- Python
- Flask
- CognoDB
- Neo4j Python Driver
- Cypher
- HTML
- CSS
- python-dotenv

## 5. Project Structure

Movie_Recommendation_System/

- app.py
- seed.py
- requirements.txt
- README.md
- .gitignore
- queries/
  - queries.cypher
- templates/
  - index.html
- static/
  - style.css

## 6. Setup

Install the required Python packages:

```bash
pip install -r requirements.txt
