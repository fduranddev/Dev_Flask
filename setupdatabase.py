from basic import app, db, Puppy

with app.app_context():

    # Création du fichier data.sqlite et la table puppies
    db.create_all()

    sam = Puppy("Sammy", 3)
    frank = Puppy("Frankie", 4)

    # Les objets ne sont pas encore enregistrés
    print(sam.id)
    print(frank.id)

    # Ajout des objets à la session
    db.session.add_all([sam, frank])

    # Enregistrement dans la base de données
    db.session.commit()

    # Les identifiants sont maintenant attribués
    print(sam.id)
    print(frank.id)
