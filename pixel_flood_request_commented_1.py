# Das hier ist ein Kommentar und kein Teil vom Programm. 
# Kommentare beginnen mit einer # und werden von Codium grün dargestellt.
# Wir nutzen sie zum Beschreiben unseres Codes und werden nicht ausgeführt.
# Das Programm kannst du auf der Kommandozeile mit dem folgenden Befehl starten.
# python3 pixel_flood_request.py
# Diese beiden import-Befehle kannst du fürs Erste ignorieren. 
import socket
import time
 
# def definiert eine Methode, die wie ein Werkzeug für uns ist.
# Wir können sie immer wieder aufrufen. 
# Fürs Erste kannst du sie ignorieren. Unten wirst du sie wiedersehen.
# Alles was mit min. 4 Leerzeichen eingerückt wurde, gehört zur Methode.
def draw_line_top(start, end, color):
    tmp = min(start, end)
    end = max(start, end)
    start = tmp
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        for x in range(end - start):
            message = f"PX {x + start} 0 {color}\n"
            s.sendall(message.encode())
    print("draw line finished")
    
# Hier startet das Programm
# Dies ist die IP-Adresse. Sie wird mit dem Variablennamen ip_address gespeichert.
# Variablen helfen uns diese Dinge besser "anzufassen". Wir können uns die Variable
# wie einen Behälter vorstellen, wobei der Inhalt der Text hinter dem = ist.
# port ist genauso eine Variable. Wenn du Codium verwendest wirst du sehen, dass der
# Inhalt in einer anderen Farbe dargestellt wird. Das liegt daran, dass es sich hierbei 
# um eine Zahl und nicht um einen Text (String) handelt. Strings werden mit " vorne und 
# hinten markiert. 
ip_address = "192.168.188.246"
port = 1337

# Hier öffnen wir die Kommunikation zum Pixelflut-Server über einen Socket.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    # Unsere Nachricht enthält PX für Pixel, die Spalte, die Zeile, und die Farbe.
    # Die Farbe ist in RGB codiert. Wenn dich die Farbcodierung mit Hexadezimalzahlen 
    # interessiert, schaue auf diese Webseiten.
    # https://inf-schule.de/information/darstellunginformation/binaerdarstellungzahlen
    # https://inf-schule.de/information/darstellunginformation/binaerdarstellungbilder/einstieg_farbwerte
    # Ansonsten kannst du auch einfach zufällige Zeichen von 0-9 und A-F eintragen.
    # Am Ende des Strings siehst du noch ein \n. Das signalisiert dem Server, dass deine 
    # Nachricht zuende ist.
    message = "PX 223 5 12DF56\n"
    #Hier übergen wir mithilfe unserer Variablen die Nachricht zum versenden.
    s.sendall(message.encode())
# Die print Methode zeigt den Text aus dem Parameter auf der Konsole an. 
print("send the pixel")
# Hier begegnest du der Methode von oben wieder. 
# Wir sagen sie wird hier aufgerufen. Durch den Aufruf wird sie ausgeführt.
# Die Werte die in den Klammern stehen sind die Parameter.
# Sie beeinflussen, was die Methode oben macht.
# Du kannst diese Zeile kopieren, wieder einfügen 
# und die Parameter verändern für ein anderes Ergebnis.
# Wenn dich die "inner workings" der Mothode interessieren, lies dir gerne die Kommentare
# in der Datei pixel_flood_request_method.py durch.
draw_line_top(7, 11, "46FFF6")