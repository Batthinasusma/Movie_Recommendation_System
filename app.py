from flask import Flask, render_template, request
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


def get_movies():
    query = """
    MATCH (m:Movie)
    RETURN m.title AS title
    ORDER BY title
    """

    with driver.session() as session:
        result = session.run(query)
        return [record["title"] for record in result]


def get_recommendations(movie_title):
    query = """
    MATCH (m:Movie {title: $title})
          -[:HAS_GENRE]->(g:Genre)
          <-[:HAS_GENRE]-(recommended:Movie)

    WHERE recommended.title <> $title

    RETURN DISTINCT recommended.title AS title,
           g.name AS genre
    ORDER BY title
    """

    with driver.session() as session:
        result = session.run(query, title=movie_title)

        return [
            {
                "title": record["title"],
                "genre": record["genre"]
            }
            for record in result
        ]


@app.route("/", methods=["GET", "POST"])
def home():

    movies = []
    recommendations = []
    selected_movie = None
    error = None

    try:
        movies = get_movies()

        if request.method == "POST":
            selected_movie = request.form.get("movie")

            if selected_movie:
                recommendations = get_recommendations(selected_movie)

    except Exception as e:
        print("Database error:", e)
        error = "Unable to connect to the movie database. Please try again later."

    return render_template(
        "index.html",
        movies=movies,
        recommendations=recommendations,
        selected_movie=selected_movie,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)