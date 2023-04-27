# Funktion der Anwendung
Diese Django-App ist zur Testung der Performance von RPA- Software auf einer lokalen Installation gedacht gedacht.
In das Suchformular können automatisiert Strings eingeegebn werden, die Strings werden zurückgegeben und neue Strings können eingegeben werden.

# Zur Verwendung einer Django-App: 
1. Klonen der Ordnerstruktur und Dateien
2. falls nicht vorhanden: Installation von Django und Python
 * Windows: ...\> py -m pip install -e django\
 * Linux/Mac: $ python -m pip install -e django/
3. Navigation mittels Comandozeile in das Verzeichnis rpa_test (es existieren zwei Verzeichnisse mit diesem Namen, das höhere, in dem die Datei manage.py liegt, ist auszuwählen)
4.  * Windows: ...\> py manage.py runserver
    * Lnux/Mac: $ python manage.py runserver
5. Aufrufen der Anwendung im Browser unter:
http://localhost:8000/testapp/
bzw.
http://127.0.0.1:8000/testapp/

