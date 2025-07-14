signal = input("Entrez un signal corporel (ex: clignement d’œil, mouvement tête, etc.): ")

responses = {
    "clignement d’œil": "Vous voulez dire 'Oui'?",
    "secouer la tête": "Vous voulez dire 'Non'?",
    "lever la main": "Vous demandez de l'aide?",
}

print(responses.get(signal.lower(), "Signal non reconnu."))
