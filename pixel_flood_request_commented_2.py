import socket

# Die ist der Methodenkopf. Er besteht aus dem Keyword def (definiere) dem Methodennamen
# und in den Klammern den Parametern. Der Doppelpunkt signalisert, dass ab hier der 
# Methodeninhalt folgt.
def draw_line_top(start, end, color):
    # min und max sind auch funktionen, die hier aufgerufen werden. Sie finden das Minimum
    # und das Maximum aus den Parametern. Das Ergebnis wird zurückgegeben. D.h. wir können 
    # es in unseren Variablen speichern.
    tmp = min(start, end)
    end = max(start, end)
    start = tmp
    # Hier wird wieder die Verbindung aufgebaut.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        # Hier beginnt eine Schleife (engl. loop)
        # Zuerst wird aber der Abstand von Anfang und Ende berechnet.
        # Die Methode range gibt mit jedem Durchlauf die nächsthöhere Zahl aus, beginnend mit 1.
        # Diese Zahl wird dann in die Variable vor dem Keyword "in" gefüllt. So ändert sich der Wert 
        # in x mit jedem Schleifendurchlauf um 1 und die Schleife endet, wenn das Maximum/die Länge
        # des Strichs erreicht wurde.
        for x in range(end - start):
            # Mit dem f vor dem String formatieren wir den Strings mit dem Inhalt aus unseren Variablen. 
            # Diese müssen dafür in geschweiften Klammern stehen um als solche erkannt zu werden.
            message = f"PX {x + start} 0 {color}\n"
            s.sendall(message.encode())
    print("draw line finished")
    
ip_address = "192.168.188.246"
port = 1337
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    message = "PX 223 5 12DF56\n"
    s.sendall(message.encode())
print("send the pixel")
draw_line_top(7, 11, "46FFF6")
