# TeamUp-Random

Portfolio Django web aplikacija za nasumično generiranje sportskih timova.

## O projektu

TeamUp-Random pomaže pri organizaciji rekreativnih utakmica — uneseš imena igrača, odabereš sport i formaciju, a aplikacija nasumično podijeli igrače u dva balansirana tima.

Podržani sportovi:
- Nogomet (5+1, 4+1, 10+1)
- Košarka (6v6, 3v3)
- Tenis (2v2)
- Odbojka (6v6, 4v4, 2v2)
- Rukomet (6+1, 4+1)

### Kako funkcionira

1. Odaberi sport i formaciju
2. Unesi imena igrača (i golmane gdje je potrebno)
3. Klikni **Generiraj timove** — aplikacija nasumično podijeli igrače u 2 tima
4. Ako nisi zadovoljan, možeš **ponovno generirati** timove s istim igračima

**Račun nije obavezan** za generiranje timova. Ako želiš spremiti rezultate:
- prijavi se ili registriraj
- klikni **Spremi rezultate**
- spremljeni timovi dostupni su u **Moj račun**, grupirani po sportu

## Tehnologije

- Python 3
- Django 6
- SQLite
- HTML / CSS / JavaScript
- Bootstrap 5 (početna stranica)

## Instalacija i pokretanje

```bash
# Kloniraj repozitorij
git clone https://github.com/tvoj-username/TeamUp-Random.git
cd TeamUp-Random

# Kreiraj virtualno okruženje (preporučeno)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Instaliraj ovisnosti
pip install -r requirements.txt

# Postavi bazu
python manage.py migrate

# (Opcionalno) Kreiraj admin korisnika
python manage.py createsuperuser

# Pokreni aplikaciju
python manage.py runserver
```

Aplikacija je dostupna na: `http://127.0.0.1:8000/`

Admin panel: `http://127.0.0.1:8000/admin/`

## Struktura projekta

```
TeamUp-Random/
├── account/          # Prijava, registracija, povijest spremljenih timova
├── pages/            # Sportovi, formacije, generiranje timova
├── project_settings/ # Django postavke
├── static/           # CSS, JS, slike
└── templates/        # HTML predlošci
```

## Credits

Početna stranica temelji se na **Agency** temi od [Start Bootstrap](https://startbootstrap.com/), licencirana pod MIT licencom. Tema je prilagođena i proširena za potrebe ovog projekta.
