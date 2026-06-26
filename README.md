# SmallRestAPI Project

Eine einfache REST-API mit FastAPI – als Lernprojekt, um den Umstieg von Codewars-Katas (isolierte Funktionen) zu einem "echten" Programm mit Struktur, Endpunkten und später Datenpersistenz zu üben.

## Was ist eine REST-API?

Eine REST-API ist eine Schnittstelle, über die andere Programme (z.B. ein Frontend, eine App oder einfach der Browser) per HTTP-Anfragen mit einem Server kommunizieren können. Statt eine Funktion direkt im Code aufzurufen, schickt man eine Anfrage über eine URL – z.B. `GET http://127.0.0.1:8000/todos`, um alle Todos abzurufen.

Die wichtigsten HTTP-Methoden dabei:

| Methode | Bedeutung |
|---|---|
| `GET` | Daten abrufen |
| `POST` | Neue Daten anlegen |
| `DELETE` | Daten löschen |
| `PUT` / `PATCH` | Daten ändern |

## Warum FastAPI?

FastAPI ist ein Python-Framework, um solche APIs zu bauen. Vorteile für den Einstieg:

- Sehr wenig Code nötig für einen funktionierenden Endpunkt
- Erstellt automatisch eine interaktive Dokumentation (`/docs`), in der man Endpunkte direkt im Browser testen kann
- Modern und in der Industrie verbreitet – gute Wahl, um etwas CV-taugliches zu bauen

## Setup – was wurde gemacht

**1. Virtuelle Umgebung (`.venv`)**

IntelliJ hat beim Projekt-Setup automatisch eine virtuelle Umgebung angelegt. Das ist ein isolierter Python-Bereich nur für dieses Projekt, damit installierte Pakete sich nicht mit anderen Projekten oder der System-Python-Installation vermischen.

**2. Pakete installiert**

```bash
pip install fastapi uvicorn
```

- **fastapi**: das eigentliche Framework, mit dem die Endpunkte definiert werden
- **uvicorn**: der Server, der die FastAPI-Anwendung tatsächlich laufen lässt (FastAPI definiert nur die Logik, uvicorn "schaltet den Server ein")

**3. Erster Endpunkt (`main.py`)**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

- `app = FastAPI()` erstellt die Anwendung
- `@app.get("/")` ist ein **Decorator**: er sagt FastAPI "wenn jemand eine GET-Anfrage an die URL `/` schickt, führe die folgende Funktion aus"
- Die Funktion `root()` gibt einfach ein JSON-Objekt zurück

**4. Server starten**

```bash
uvicorn main:app --reload
```

- `main` = Dateiname (`main.py`)
- `app` = Name der FastAPI-Instanz in dieser Datei
- `--reload` = Server startet automatisch neu, sobald der Code gespeichert wird (praktisch während der Entwicklung)

## Testen

Nach dem Start im Terminal sichtbar: `Uvicorn running on http://127.0.0.1:8000`

- Im Browser `http://127.0.0.1:8000` öffnen → zeigt `{"message": "Hello World"}`
- Im Browser `http://127.0.0.1:8000/docs` öffnen → automatische, interaktive API-Dokumentation, in der jeder Endpunkt direkt testbar ist

## Nächste Schritte

- [ ] `GET /todos` – alle Todos anzeigen
- [ ] `POST /todos` – neues Todo hinzufügen
- [ ] `GET /todos/{id}` – einzelnes Todo anzeigen
- [ ] `DELETE /todos/{id}` – Todo löschen
- [ ] Speicherung später von einer Python-Liste auf SQLite umstellen
- [ ] Containerisierung mit Docker
