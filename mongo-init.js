db = db.getSiblingDB("cats_db");

db.createCollection("cats");

db.cats.insertMany([
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    },
    {
        "name": "murzik",
        "age": 5,
        "features": ["любить рибу", "грає з іграшками", "білий"]
    },
    {
        "name": "simba",
        "age": 2,
        "features": ["енергійний", "пустун", "спить в коробках"]
    }
]);

print("Database 'cats_db' initialized with collection 'cats' and sample records.");