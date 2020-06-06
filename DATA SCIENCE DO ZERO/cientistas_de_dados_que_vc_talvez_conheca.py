# Desenvolva sugestões de amigos que vc conheça..
from conectores_chave import users
from collections import Counter


# Agora o chefe quer que  vc de sugestões de novas amizades, então foi sugerido que os amigos identificados no
# exercício anterior conheçam os amigos dos amigos: - Para cada amigo do usuário, itera sobre os amigos daquela
# pessoa, e coleta todos os dados
def friends_of_friends_ids_bad(user):
    # foaf abreviação de friends of a friends
    return [foaf["id"]
            for friend in user["friends"]  # para cada amigo do usuário
            for foaf in friend["friends"]]  # pega cada _their_friends


# print(friends_of_friends_ids_bad(users[0]))
# # resultado:[0, 2, 3, 0, 1, 3] Analisando-->  O resultado Faz referencia ao Data Science Hero do exercício do livro,
# # onde  ele mesmo representado pelo digito 0, aparece duas vezes pois ele tem amizade, com os colegas diretos 1 e 2,
# # e o colega indireto número 3, aparece duas vezes, pois pode ser acionado atravéz de seus dois colegas mais
# # próximos.Ex: 0 (Hero)---> 2(Sue) --> 3(chi)| 0 (Hero)---> 1(Dunn) --> 3(chi)
# print(friends_of_friends_ids_bad(users[1]))  # resultado:[1, 2, 0, 1, 3, 1, 2, 4]
# print(friends_of_friends_ids_bad(users[2]))  # resultado:[1, 2, 0, 2, 3, 1, 2, 4]
# print(friends_of_friends_ids_bad(users[3]))  # resultado:[0, 2, 3, 0, 1, 3, 3, 5]
# print(friends_of_friends_ids_bad(users[4]))  # resultado:[1, 2, 4, 4, 6, 7]
# print(friends_of_friends_ids_bad(users[5]))  # resultado:[3, 5, 5, 8, 5, 8]
# print(friends_of_friends_ids_bad(users[6]))  # resultado:[4, 6, 7, 6, 7, 9]
# print(friends_of_friends_ids_bad(users[7]))  # resultado:[4, 6, 7, 6, 7, 9]
# print(friends_of_friends_ids_bad(users[8]))  # resultado:[5, 8, 5, 8, 8]
# print(friends_of_friends_ids_bad(users[9]))  # resultado:[6, 7, 9]


print([friend["id"] for friend in users[0]["friends"]])  # neste caso ele vai retornar os amigos diretos do usuário de

# índice 0


""" Agora construiremos uma função de ajuda, para exlcuir as
pessoas que já são amigas do usuário, e deixar apenas os
amigos novos em potencial, ou seja, amigos em comum"""


def not_the_same(user, other_user):
    """ dois usuários não podem ser os mesmos se possuem ids diferentes"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """ other_user não é um amigo se não estiver em user["friends]; isso é, se é not_the_same com todas as pessoas
    em user["friends]"""
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))


print(friends_of_friend_ids(users[3]))
# resposta --->Counter({0: 2, 5: 1}) quer dizer que chi(3) tem dois amigos em comum com Hero(0), e um amigo em comum com
# Clive(5)
