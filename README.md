# Movie_Recommendation_System
Movie Recommendation System is a web application that recommends movies based on relationships between movies and genres using a graph database.
A movie can belong to multiple genres, and many movies can share the same genres. A graph database represents these relationships
naturally as nodes and edges, making relationship-based recommendations easier to query.

(Movie) ──HAS_GENRE──> (Genre)
