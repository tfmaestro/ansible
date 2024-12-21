## Ansible

### Skonfiguruj ansible.cfg

Dodaj domyślnego użytkownika i domyślną ścieżkę do klucza prywatnego w pliku ansible.cfg.

```
[defaults]
host_key_checking = False
private_key_file = ~/.ssh/<ŚCIEżKA_DO_KLUCZA_PRYWATNEGO>
ansible_ssh_user = <NAZWA_USERA_NA_VM>
[privilege_escalation]
become_flags=-H -S

```

### Skonfiguruj inventory.ini

Dodaj publiczne adresy IP w pliku inventory.ini, a także zdefiniuj nazwę użytkownika i ścieżkę do klucza prywatnego.

```
[gcp]
<PUBLICZNE_IP_VM>
<PUBLICZNE_IP_VM>

[aws]
<PUBLICZNE_IP_VM> ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/.ssh/<ŚCIEżKA_DO_KLUCZA_PRYWATNEGO>
<PUBLICZNE_IP_VM> ansible_ssh_user=ubuntu ansible_ssh_private_key_file=~/.ssh/<ŚCIEżKA_DO_KLUCZA_PRYWATNEGO>

[azure]
<PUBLICZNE_IP_VM>
<PUBLICZNE_IP_VM>

[webapp:vars]
ansible_ssh_user=<NAZWA_USERA_NA_VM>
ansible_python_interpreter=/usr/bin/python3

```

### Wykonaj deploy

Przetestuj deploy konfiguracji dla wybranej chmury w tzw. dry mode. Możesz też użyć opcji —-limit i podać adres IP jednej z maszyn, jeśli nie chcesz testować zmian od razu na wszystkich maszynach dla dalej chmury.
```
ansible-playbook -i inventory.ini playbook.yaml --check -vv --limit <nazwa_chmury>
```

Przykład testu na maszynach w GCP:
```
ansible-playbook -i inventory.ini playbook.yaml --check -vv --limit gcp
```

Wykonaj deploy na wszystkich maszynach:
```
ansible-playbook -i inventory.ini playbook.yaml --limit <tag_roli>
```

Przykład deployu roli base_server_configuration:
```
ansible-playbook -i inventory.ini playbook.yaml --limit base
```

W przypadku deployu roli flask_app, gdzie znajdują się zaszyfrowane secrety wywołaj deploy z dodaniem opcji `--ask-vault-pass`.
```
ansible-playbook -i inventory.ini playbook.yaml -t app_deploy --limit <ADRES_IP_MASZYNY> --ask-vault-pass
```

