#!/usr/bin/python3
"""Returns information about his/her to-do list progress."""
"""import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()

    completed = [todo for todo in todos if todo.get("completed") is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get("name"), len(completed), len(todos)))
    [print('\t {}'.format(c.get("title"))) for c in completed]
"""
import requests
import sys

def don_emp(employee_id):
    # Récupérer les données de l'employé
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_rep = requests.get(user_url)
    user_data = user_rep.json()
    nom_employe = user_data.get('name')

    # Récupérer la liste des tâches TODO de l'employé
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_rep = requests.get(todos_url)
    todos_data = todos_rep.json()

    # Filtrer les tâches terminées
    taches_terminees = [tache for tache in todos_data if tache.get('completed')]
    nb_taches_terminees = len(taches_terminees)
    nb_total_taches = len(todos_data)

    # Afficher les résultats
    print(f"Employee {nom_employe} is done with tasks({nb_taches_terminees}/{nb_total_taches}):")
    for tache in taches_terminees:
        print(f"\t {tache.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    don_emp(employee_id)
