#!/usr/bin/python3
"""Returns information about his/her to-do list progress."""
import requests
import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
		sys.exit(1)

	try:
		employee_id = int(sys.argv[1])
	except ValueError:
		print("L'ID de l'employé doit être un entier.")
		sys.exit(1)

	url = 'https://jsonplaceholder.typicode.com/'
	
	# Récupérer les données de l'utilisateur
	user_response = requests.get(f"{url}users/{employee_id}")
	if user_response.status_code != 200:
		print("Utilisateur non trouvé.")
		sys.exit(1)
	user = user_response.json()
	
	# Récupérer les tâches TODO de l'utilisateur
	todos_response = requests.get(f"{url}todos", params={"userId": employee_id})
	if todos_response.status_code != 200:
		print("Impossible de récupérer les tâches.")
		sys.exit(1)
	todos = todos_response.json()

	# Filtrer les tâches terminées
	completed = [todo for todo in todos if todo.get("completed") is True]
	print(f"Employee {user.get('name')} is done with tasks({len(completed)}/{len(todos)}):")
	for task in completed:
		print(f"\t {task.get('title')}")
