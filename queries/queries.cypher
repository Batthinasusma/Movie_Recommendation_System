// 1. Get all movies

MATCH (m:Movie)
RETURN m.title AS title
ORDER BY title;


// 2. Get movie genres

MATCH (m:Movie)-[:HAS_GENRE]->(g:Genre)
RETURN m.title AS movie, g.name AS genre
ORDER BY movie;


// 3. Movie recommendation using a 2-hop graph traversal

MATCH (m:Movie {title: $title})
      -[:HAS_GENRE]->(g:Genre)
      <-[:HAS_GENRE]-(recommended:Movie)

WHERE recommended.title <> $title

RETURN DISTINCT
       recommended.title AS title,
       g.name AS genre
ORDER BY title;


// 4. Find movies connected through the same actor

MATCH (m:Movie {title: $title})
      -[:HAS_ACTOR]->(a:Actor)
      <-[:HAS_ACTOR]-(other:Movie)

WHERE other.title <> $title

RETURN DISTINCT other.title AS title,
       a.name AS actor;
