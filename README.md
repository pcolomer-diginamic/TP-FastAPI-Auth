- Pour les besoins du TP, un seul endpoit est actif => /docs#classes

- Pour ajouter des utilisateur dans la table user, décommenter le code situé dans .src.conf.session.py
        """pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        u_user = User(user_id="admin@fastapi.io", passwd=pwd_context.hash("testapi"), role="ADMIN")
        session.add(u_user)
        session.commit()
        pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        u_user = User(user_id="lambda@fastapi.io", passwd=pwd_context.hash("test"), role="USER")
        session.add(u_user)
        session.commit()"""

- Pour visualiser le fichier de log de l'application => docker compose exec -it fastapi cat app.log
