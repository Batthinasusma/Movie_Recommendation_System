from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


movies = [
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "actor": "Leonardo DiCaprio",
        "director": "Christopher Nolan"
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "actor": "Matthew McConaughey",
        "director": "Christopher Nolan"
    },
    {
        "title": "The Matrix",
        "genre": "Sci-Fi",
        "actor": "Keanu Reeves",
        "director": "Lana Wachowski"
    },
    {
        "title": "Avatar",
        "genre": "Sci-Fi",
        "actor": "Sam Worthington",
        "director": "James Cameron"
    },
    {
        "title": "Titanic",
        "genre": "Romance",
        "actor": "Leonardo DiCaprio",
        "director": "James Cameron"
    },
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "actor": "Christian Bale",
        "director": "Christopher Nolan"
    },
    {
        "title": "The Prestige",
        "genre": "Drama",
        "actor": "Christian Bale",
        "director": "Christopher Nolan"
    },
    {
        "title": "The Notebook",
        "genre": "Romance",
        "actor": "Ryan Gosling",
        "director": "Nick Cassavetes"
    }
]


def create_movie(tx, movie):
    query = """
    MERGE (m:Movie {title: $title})
    MERGE (g:Genre {name: $genre})
    MERGE (a:Actor {name: $actor})
    MERGE (d:Director {name: $director})

    MERGE (m)-[:HAS_GENRE]->(g)
    MERGE (m)-[:HAS_ACTOR]->(a)
    MERGE (m)-[:DIRECTED_BY]->(d)
    """

    tx.run(
        query,
        title=movie["title"],
        genre=movie["genre"],
        actor=movie["actor"],
        director=movie["director"]
    )


with driver.session() as session:

    for movie in movies:
        session.execute_write(create_movie, movie)

print("Movie data successfully loaded into CognoDB.")

driver.close()