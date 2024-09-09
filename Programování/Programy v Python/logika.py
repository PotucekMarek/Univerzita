from kanren import Relation, facts

results = Relation()


facts(results,
    ("Anna", 1, 2),
    ("Anna", 2, 5),
    ("Bert", 1, 3),
    ("Bert", 2, 2),
    ("Cyril", 1, 2))

