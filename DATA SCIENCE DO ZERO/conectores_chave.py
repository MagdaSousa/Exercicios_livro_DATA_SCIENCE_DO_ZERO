from __future__ import division

# Lista de ciêntistas de dados que atuam na empresa
# Objetivo: Descobrir quem são os conectores-chavee,
# ou seja os profissionais mais amigaveis, que tem bom relacionamento com mais funcionários
# resposta do pront neste ponto ao dar um print:

# [{'id': 0, 'name': 'Hero'},
# {'id': 1, 'name': 'Dunn'},
# {'id': 2, 'name': 'Sue'},
# {'id': 3, 'name': 'Chi'},
# {'id': 4, 'name': 'Thor'},
# {'id': 5, 'name': 'Clive'},
# {'id': 6, 'name': 'Hicks'},
# {'id': 7, 'name': 'Devin'},
# {'id': 8, 'name': 'Kate'},
# {'id': 9, 'name': 'Klein'}]

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# Lista com tuplas que mostram quem é amigo de quem na empresa
# (x,y) o x representa uma pessoa e o y o amigo dela
friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

for user in users:
    user["friends"] = []
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    # print(i,j)


# exemplo do resultado mostrado no terminal :[{'id': 0, 'name': 'Hero', 'friends': [{'id': 1, 'name': 'Dunn',
# 'friends': [{...},

# Agora queremos saber o número médio de conexões

def number_of_friends(user):
    """quantos amigos o usuário tem"""
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)  # total de conexões entre pessoas
# print(total_connections)

# print(total_connections)  # tamanho de todas as listas "friends" juntas

num_user = len(users)  # tamanho da lista de usuários
# print(num_user)
# print(num_user)
avg_connections = total_connections / num_user  # média de conexões
# print(avg_connections)
# print(avg_connections)

# criando uma lista, e ordenando em "muito amigos para "menos amigos"
num_friends_by_id = [(user["id"], number_of_friends(user))for user in users]

# ordenando os amigos de acordo com o número de usuários representado por x, e número de amigos
# representado por y(x,y)
print(sorted(num_friends_by_id, key=lambda it: it[1], reverse=True))
