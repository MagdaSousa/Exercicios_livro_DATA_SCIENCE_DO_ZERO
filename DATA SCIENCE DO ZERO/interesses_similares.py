from conectores_chave import users
from collections import defaultdict

# Encontrar usuários com interesses comuns
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSql"), (1, "MongoDB"), (1, "Cassandra"), (1, "Hbase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "Scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "Pandas"), (3, "R"), (3, "python"),
    (3, "statistics"), (3, "Regression"), (3, "Probabily"),
    (4, "machine learning"), (4, "regression"), (4, "decison trees"),
    (4, "libsvm"), (5, "python"), (5, "R"), (5, "java"), (5, "C++"),
    (5, "haskell"), (5, "programing languages"), (6, "Statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "big data"), (8, "artificial intelligence"), (9, "hadoop"),
    (9, "java"), (9, "MapReduce"), (9, "big data"),

]


# construir uma função que encontrem usuários com o mesmo interesse

def data_scientists_who_like(target_interest):
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]


# As chaves são os interesses, os valores são as listas de user_ids com interests

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
interests_by_user_id = defaultdict(list)
for  user_id,interest in interests:
    interests_by_user_id[user_id].append(interest)
#resposta: [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]