from src import basis

# Die ist der Methodenkopf. Er besteht aus dem Keyword def (definiere) dem Methodennamen
# und in den Klammern den Parametern. Der Doppelpunkt signalisert, dass ab hier der 
# Methodeninhalt folgt.
def draw_line_top(start, end, color):
    # min und max sind auch funktionen, die hier aufgerufen werden. Sie finden das Minimum
    # und das Maximum aus den Parametern. Das Ergebnis wird zurückgegeben. D.h. wir können 
    # es in unseren Variablen speichern. tmp dient hier als Zwischenspeicher.
    tmp = min(start, end)
    end = max(start, end)
    start = tmp
    # Hier beginnt eine Schleife (engl. loop)
    # Zuerst wird aber der Abstand von Anfang und Ende berechnet.
    # Die Methode range gibt mit jedem Durchlauf die nächsthöhere Zahl aus, beginnend mit 1.
    # Diese Zahl wird dann in die Variable vor dem Keyword "in" gefüllt. So ändert sich der Wert 
    # in x mit jedem Schleifendurchlauf um 1 und die Schleife endet, wenn das Maximum/die Länge
    # des Strichs erreicht wurde.
    for x in range(end - start):
        basis.send_pixel(x, 0, "46FFF6")
    print("draw line finished")
    
# simpler Aufruf der send_pixel Funktion
basis.send_pixel(2, 5, "46FFF6")
# Aufruf einer Funktion die die send_pixel Funktion mehrfach aufruft
draw_line_top(7, 11, "46FFF6")
