## Rola flask_app

### Dodaj secrety

Dodaj secrety dla danej chmury w dedykowanym pliu w `roles/flask_app/secrets/`.
Przykład dla chmury AWS w `roles/flask_app/secrets/secrets_aws.yaml`.

```
db_user: "admin"
db_password: "Secret123"
db_host: "tfmaestro-mysql-db.c5coc8si4khk.us-east-1.rds.amazonaws.com"
db_name: "tfmaestro-mysql-database"

```

### Zaszyfruj plik z secretami

Jeśli pierwszy raz szyfrujesz secrety znajdujące się w `roles/flask_app/secrets/` wystarczy, że skorzystasz z poniższej komendy do zaszyfrowania konkretnego pliku. 

Przejdź do folderu `ansible` i z tego miejsca zaszyfruj konkretny plik, dla chmury z która pracujesz. 
Przykład dla chmury GCP:

```
ansible-vault encrypt roles/flask_app/secrets/secrets_gcp.yaml
```

W efekcie zostaniesz zapytany/a o podanie hasła, dzięki któremu dane zostaną zaszyfrowane. 
To hasło będzie następnie wykorzystywane przy każdym deployu. 
Zapisz je w bezpiecznym miejscu, np. w secret managerze.

Teraz możesz wykonywać deploy Ansible, ale za każdym razem dodaj `--ask-vault-pass` do komendy.


### Dodaj certyfikat dla bazy w Azure

Upewnij się, że masz dodany certyfikat wymagany do połączenia z bazą danych. 
Plik powinien się znajdować w `roles/flask_app/files/`.

Wykonaj deploy. Przykład dla chmury GCP:
```
ansible-playbook -i inventory.ini playbook.yaml -t app_deploy --limit gcp --ask-vault-pass
```
