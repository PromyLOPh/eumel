		     EUMEL-Installationsanleitung			  GMD
_____________________________________________________________________________
_____________________________________________________________________________
 
Betriebssystem  :  EUMEL (Version 1.8) 
Hardware        :  IBM-PC/AT und Kompatible 
SHard-Version   :  4.9, 5.0 und 5.1 
 
Erforderliche Disketten
 
  - EUMEL-Installationsanweisung :  "Installationsanweisung" (MS-DOS-Diskette)
  - EUMEL-Generierungsdiskette   :  "SETUP-EUMEL AT"
  - EUMEL-Systemdiskette         :  "EUMEL-Hintergrund"
  - EUMEL-Zusatzdisketten        :  "std.zusatz"
                                 :  "std.graphik"
				 :  "std.printer" (9-Nadel-Drucker)
				 :  "std.printer" (24-Nadel-Drucker
				 :  "std.printer" (Laser-Drucker)
  - EUMEL-Handbuecher 		 :  "handbuecher.1" (Textverarbeitung"
  				 :  "handbuecher.2" (System- und Programmier-
				     handbuch)
  - EUMEL-DOS-Schnittstelle	 :  "austausch" (DOS-DAT und NETZ)

Die Diskette "SETUP-EUMEL" ist ein kleines EUMEL-System zur Installation
des Betriebssystems EUMEL auf einem AT-kompatiblen Rechner. Auf diesem
System laufen Programme ab, die im Dialog mit dem Benutzer das Einrichten 
einer oder mehrerer EUMEL-Partitionen ermoeglichen. Diese Diskette darf
nicht schreibgeschuetzt sein! Beim Einrichten einer EUMEL-Partition wird
nach Pruefung der Festplatte durch "SETUP-EUMEL" der hardwarenahe Teil des
EUMEL-Systems, 'SHard' (Software/Hardware-Interface), auf die Festplatte
geschrieben.  Die Hintergrunddisketten beinhalten das eigentliche Betriebs-
system EUMEL (den Systemkern (EUMEL-0-Maschine)) und die darauf aufbauenden
Systemteile (Hintergrund)).                              
 
Leistungen des SETUP EUMEL. 
===========================
 
Wenn Sie bereits ein Betriebssystem auf Ihrer Festplatte installiert haben,
muessen Sie darauf achten, dass noch ausreichend Platz fuer ein EUMEL-System
uebrig ist. Die Mindestgroesse einer Partition fuer ein EUMEL-System betraegt
ca.  1MB, die maximale Groesse ist vom benutzten Systemkern abhaengig: Der in
der Version 1.8.6 M+ verwendete Systemkern u186+1523 erlaubt eine maximale
Groesse von 128 MB. Andere, aeltere EUMEL Versionen erlauben nur eine Parti-
tionsgroesse von 16 MB. Aus Kompatibilitaetsgruenden stellt das Installati-
onsprogramm eine Kontrollfrage bei öberschreiten der 16 MB Grenze. 

Soll neben EUMEL auch eine MS-DOS Partition auf der Festplatte sein, muss,
da MS-DOS standardmaessig die gesamte Festplatte belegt, dieses System ge-
sichert, mit dem MS-DOS-Kommando 'fdisk' (o.ae.) die Partition geloescht und
entsprechend kleiner neu eingerichtet werden. Sie koennen auch bei der
EUMEL-Installation alle bereits bestehenden Systeme loeschen; dazu bietet
Ihnen der SETUP-EUMEL die Option 'Loeschen der gesamten Partitionstabelle'
an. Dabei gehen jedoch alle Daten auf der Festplatte verloren. Achten Sie 
also darauf, dass sie alle Daten vorher gesichert haben!  Um nun die Partiti-
onierung fuer Ihr EUMEL-System vorzunehmen, legen Sie die Diskette 
"SETUP-EUMEL" ohne Schreibschutzmarke in das Start-Laufwerk. Sollten Sie ein
Geraet mit zwei Laufwerken besitzen, dann ist es das Laufwerk A:.
(Bei Unklarheiten im Benutzerhandbuch des Herstellers nachsehen.)  Schalten
Sie nun den Rechner ein bzw. betaetigen Sie den Tastatur-RESET, wenn Ihr
Geraet bereits eingeschaltet ist (meistens mit dem gleichzeitigen Druck der
Tasten CTRL, ALT und DEL). Der SETUP-EUMEL gibt zunaechst folgende SHard-
Meldung aus:                                        

Setup-SHard fuer EUMEL auf IBM PC/AT V 5.1g
Copyright (C) 1985,86,87,88,89,90 Martin Schoenbeck Beratungen GmbH, Sprenge 


Warten Sie beim Hochfahren des SETUP-EUMELs, bis Ihnen nach einem Zwischen-
bildschirm ("SETUP-EUMEL fuer Modul- SHard") eine Partitionstabelle angezeigt
wird. Dieser koennen Sie entnehmen, ob bereits Partitionen auf der Festplatte
eingerichtet und wie diese spezifiziert sind.  Angezeigt werden neben Groesse,
Start- und Endspur der einzelnen Partitionen auch eine Typ-Nummer. Fuer
EUMEL-Partitionen werden in aufsteigender Reihenfolge die Typ-Nummern 69 bis
72, fuer MS-DOS je nach Groesse der eingerichteten Partition die Nummern 1
oder 4 vergeben. Ausserdem wird die gerade aktive Partition durch einen ent-
sprechenden Eintrag in der Tabelle kenntlich gemacht. "Aktiv" ist die Parti-
tion, die nach dem naechsten Einschalten des Rechners bzw. nach dem naechsten
Tastatur-RESET gestartet wuerde. Sie sehen zusaetzlich ein Menue mit folgen-
den zur Auswahl stehenden Funktionen:                               

             
____________________________________________________ 
 
   -  EUMEL-Partition einrichten                  1 
   -               erneuern (Neuer SHard)         2 
   -               aktivieren                     3 
   -               loeschen                       4 
   -  Partitionstabelle loeschen                  5 
   -  SHard-Konfiguration anzeigen                6 
   -  SHard konfigurieren                         7 
   -  SHardmodule laden oder loeschen             8 
   -  SETUP-EUMEL beenden                         0 
____________________________________________________ 
 
 
EUMEL - Partition einrichten -
==============================
 
Eine neue EUMEL-Partition wird gemaess den im weiteren erfragten Angaben
eingerichtet. In die Partition wird ein SHard geschrieben, dessen Konfigu-
ration die gelieferte Grundkonfiguration oder die von Ihnen eingestellte
ist (s. Partitionieren der Festplatte, Seite 3). 
 
EUMEL - Partition erneuern (Neuer SHARD) - 
==========================================

In eine bereits vorhandene Partition wird ein SHard in der eingestellten
Konfiguration geschrieben. Der bis dahin vorhandene SHard wird ueberschrieben.
Die Moeglichkeit besteht jedoch nur, wenn die Partition mit einem SETUP-EUMEL
eingerichtet worden ist. Erneuern bedeutet, nur den SHard auszutauschen auf
einer Partition, die schon einen fertigen EUMEL enthaelt, ohne dass man dabei
den EUMEL loescht. Das ist dann sinnvoll, wenn man eine neue Version des 
SHard benutzen moechte oder den SHard aus irgendwelchen Gruenden (z.B. Strea-
mer gekauft) um einen oder mehrere Module erweitern will. Diese Aktion kann
nur durchgefuehrt werden, wenn bereits ein SHard mit der Versionsnummer 4.x
in dieser Partion vorhanden ist. éltere (Version 2.7, 2.8 etc.) koennen nicht
ersetzt werden. 
 
 

EUMEL - Partition aktivieren -
==============================

Eine Partition wird ausgewaehlt und aktiv gesetzt, d.h. beim naechsten Start
des Rechners wird das System, das auf dieser Partition steht, hochgefahren. 
 							       
EUMEL - Partition loeschen - 
=============================

Hierbei wird ein Eintrag aus der Partitionstabelle entfernt. Die EUMEL-
Partition wird nicht wirklich geloescht, d.h. wenn man nach dem Loeschen den
Plattenbereich noch nicht anderweitig verwendet hat, kann das EUMEL-System
auf dieser Partition durch ein "EUMEL-Partition einrichten" auf genau dem-
selben Plattenbereich (Start-/Endzylinder) wieder hergestellt werden. 
 							       
Partitionstabelle loeschen. 
===========================
 
Dies ist eine sehr gefaehrliche Option! Es werden hiermit alle Partitionen
auf der Platte geloescht (nicht nur die von EUMEL). Auch hier gilt zwar, das
die Partitionen selbst an sich unangetastet bleiben und wiederhergestellt 
werden koennten aber dies ist bei anderen Betriebssystemen oft nicht moeglich.
Also VORSICHT! 

SHard-Konfiguration anzeigen.  
=============================
 
Die Module des SHard, der bereitgestellt ist, um auf die Platte geschrieben
zu werden, werden angezeigt. Es werden alle definierten Kanaele angezeigt und 
zu jeder Kanalnummer der assoziierte Modulname. Aufgelistet ist die zuletzt
mit dem SETUP-EUMEL zusammengestellte Konfiguration. 
 
SHard konfigurieren. 
====================
 
Zusammenstellen von einer SHardbasis und SHardmodulen zu einem neuen SHard,
um eine neue Partition einzurichten oder den SHard einer bestehenden Parti-
tion zu ersetzen.
 ACHTUNG:   Bitte diesen Menuepunkt nicht experimentell benutzen! 
 Eine Anleitung zum Thema Module etc. wird separat erscheinen.
 
SHardmodule laden oder loeschen. 
================================
 
Hiermit koennen neue Module oder neue Versionen von Modulen in den SETUP-
EUMEL geladen werden oder nicht mehr benoetigte Module geloescht werden.
Die neuen Module werden von einer EUMEL-Archivdiskette gelesen, deren Name
zuvor eingegeben werden muss. 
 ACHTUNG:   Bitte diesen Menuepunkt nicht experimentell benutzen! 
 Eine Anleitung zum Thema Module etc. wird separat erscheinen. 
 
 
SETUP-EUMEL beenden. 
====================
 
SETUP-Programm ordnungsgemaess beenden. 
ENDE-Meldung abwarten! 
 
Partitionieren der Festplatte.
==============================
 
Die eigentliche Partitionierung beginnt nun, indem Sie Menue-Punkt 1
"EUMEL-Partition einrichten" anwaehlen. (Punkt 1 wird Ihnen nur dann nicht
angeboten, wenn die Festplatte bereits vollstaendig belegt ist. Sichern Sie
dann das alte System und loeschen eine oder alle Partitionen.) Die Kontroll-
abfrage "Neue EUMEL-Partition einrichten? (j/n)" beantworten Sie entsprechend
mit "j".  Beim Generieren einer EUMEL-Partition werden Angaben zu Groesse und
Startzylinder abgefragt. Dafuer werden Vorgaben gemacht, die Sie bestaetigen,
indem Sie die <RETURN>-Taste betaetigen, oder die Sie ueberschreiben koennen. 
Die abschliessende Abfrage "Sind die Partitionsangaben korrekt?" fordert Sie
zur öberpruefung Ihrer Eingaben auf.
 
Nach der Eingabe und der öberpruefung der Sektoren erscheint eine Meldung
wie z.B.: 
 
Ich habe keine schlechten Sektoren gefunden   oder 
Ich habe 2 schlechte Sektoren gefunden 
SHard wird auf die Partition geschrieben 
Bitte betaetigen Sie eine Taste! 
 
Danach gelangen Sie wieder in das Generierungsmenue. Waehlen Sie "0" fuer
"SETUP-EUMEL beenden". öber eine Sicherheitsfrage verlassen Sie nun den
ersten Teil der Installation. Warten Sie unbedingt, bis auf dem Bildschirm
die Meldung "ENDE" erscheint, bevor Sie die Diskette "SETUP EUMEL" aus dem
Laufwerk nehmen.  
                          
 
 
Installieren eines EUMEL-Hintergrundes. 
=======================================
 
Im naechsten Schritt wird auf ihrer Festplatte das vollstaendige EUMEL-System
installiert.  Bitte betaetigen Sie den Tastatur-Reset an Ihrem Rechner
(oder die Tasten CTRL, ALT und DEL oder den AUS-/EIN-Schalter).  Auf dem
Bildschirm erscheint die folgende Meldung: 
                            
_____________________________________________________________________________ 
                                  
SHard fuer EUMEL auf IBM PC,AT V 5.1g 
Copyright (c) 1985, 86, 87, 88, 89 Martin Schoenbeck Beratungen GmbH, Spenge 
Ladevorgang kann durch Tastendruck unterbrochen werden 
Habe leider keine EUMEL-0-Maschine gefunden 
Ladevorgang unterbrochen, druecken Sie eine Taste um fortzufahren. 
_____________________________________________________________________________ 
 
Legen Sie nun die erste Hintergrunddiskette (EUMEL-Hintergrund) in das
Laufwerk ein und betaetigen Sie eine Taste. Der Systemkern wird geladen und
es erscheinen Angaben zu HG-, RAM-, und Pufferkapazitaet sowie zu den ange-
schlossenen Kanaelen, diesmal jedoch bezogen auf die Festplatten-Partition.
Warten Sie nun, bis die Meldung "HG ungueltig" kommt. Druecken Sie anschlies-
send eine beliebige Taste.
Falls Sie in ein bereits bestehendes EUMEL-System einen neuen Urlader ein-
spielen wollen, lesen Sie bitte den Abschnitt: 
 "Installation eines neuen Urladers".  
 
Ein Menue bietet Ihnen dann folgende Auswahl: 
______________________________________ 				                                       

 (1)  Systemstart 
 (2)  Hintergrund vom Archiv laden 
 (3)  Hardwaretest 
 (4)  neuen Urlader vom Archiv laden 
______________________________________ 

Waehlen Sie Menue-Punkt (2) "Hintergrund vom Archiv laden" und bestaetigen
Sie die Abfrage "Alten HG ueberschreiben?" mit "j".  Das Laden des Hinter-
grundes kann einige Minuten in Anspruch nehmen. Es koennen bei beschaedigten
Disketten Lesefehler auftreten; dann gibt das System eine der Meldungen

'Harter Lesefehler' bzw.  'Softerror' aus.

Bei letzterem koennte der entsprechende Sektor nach mehrmaligem Versuch noch 
gelesen werden. Bei einem harten Lesefehler koennen Sie die Diskette nicht
verwenden. Bitte benachrichtigen Sie in diesem Fall die GMD und Sie bekommen
die defekten Disketten ersetzt. Wenn der Hintergrund eingelesen ist, erscheint
die Aufforderung

'fertig, bitte RESET'.

Vergessen Sie nicht, vor der Betaetigung des Tastatur-RESET die Hintergrund-
diskette aus dem Diskettenlaufwerk zu entfernen.  Wenn Sie waehrend des Hoch-
fahrens keine Taste druecken, dann startet der Lader durch und das EUMEL-
System meldet sich mit einer Tabelle von Geraeteanpassungen: 
___________________________________________________________________________ 
 
psi                transparent        pc.1.25             pc.2.25 
pc.3.25            pc.1.24            pc.2.24             pc.3.24 
psi25              tandberg.2244s     DEC.VT100.ascii     DEC.VT100.german 
DEC.VT220.ascii    DEC.VT220.german   FT10/20.german      FT10/20.ascii 
ampex210.ascii     ampex210.german    ampex220.german     ampex232 
Wyse.WY50.ascii    Wyse.WY50.german   Wyse.WY60.german    Wyse.WY99.german 
Wyse.WY120.german 
 
Kanal 1 (j/n) 
___________________________________________________________________________ 

Da unterschiedliche Tastaturen auch unterschiedliche Tastenbelegungen haben,
ist es notwendig, mit Hilfe der Konfigurationstabelle Ihre Tastatur und Ihren
Bildschirm an das EUMEL-System anzupassen. Dafuer bietet Ihnen das System 
"Kanaele" an. Kanal 1 entspricht dem Haupt-Terminal des Rechners, muss also
auf jeden Fall konfiguriert werden. Beantworten Sie die Frage "Kanal 1 (j/n)"
mit "j". Das EUMEL-System funktioniert auch, wenn Sie zunaechst nur Kanal 1 
mit der Anpassung konfigurieren, die Ihrem Geraetetyp entspricht. Wenn Ihr
Rechner eine AT-Tastatur hat, ist die korrekte Konfiguration "pc.1"; 
die Konfigurationen "pc.2" und "pc.3" decken die meisten der Rechner ab,
deren Tastenbelegung von der Standard-AT Tastatur geringfuegig abweicht. Die
Erweiterung ".24" bzw. ".25" gibt die Anzahl der Bildschirmzeilen wieder. 
Standardmaessig sind im SHard 24 Zeilen eingestellt.  Weitere Kanaele zum An-
schluss von Druckern oder weiteren Terminals koennen jederzeit bei Bedarf
vorgenommen werden (EUMEL Systemhandbuch Teil 1). Die Anfrage nach der Konfi-
guration weiterer Kanaele kann deshalb verneint werden. Die Abfrage 'koennen
unbenutzte Geraetetypen geloescht werden (j/n)' beantworten Sie einstweilen
mit 'n'.
                           
Zusatzprogramme.                  
================
         
Nachdem das System vollstaendig installiert ist, kann noch typspezifische
Software eingespielt werden. Diese befindet sich auf der Diskette
"std.zusatz". 

Der folgende Ablauf skizziert schon das Prinzip jeder Arbeit in einem 
EUMEL-System. 

Task ankoppeln mit den Befehl:
  'continue("taskname")' bzw. 'begin("taskname")',

Eingabe von Kommandos wie 'edit', 'run' oder 'generate shutup dialog
manager', abschliessend Task abkoppeln durch <ESC> <q>. Eine ausfuehrliche
Beschreibung finden Sie in den EUMEL-Handbuechern. Nach Einstellen des
Kanals 1 befinden Sie Sich auf Supervisor-Ebene. Um die auf der Diskette 
befindlichen Programme an der richtigen Stelle zu uebersetzen, sind folgende
Schritte notwendig: 
Druecken Sie die <SV>-Taste (F1). Damit landen Sie im Supervisor-Menue, dem
Systemverteiler. Mit <ESC> <c> und Eingabe des Tasknamens 'SYSUR' (auf Gross-
schreibung achten!) holen Sie die Task 'SYSUR' an das Terminal.
Diese Task meldet sich mit 'maintenance:'. Da Sie mit einem Mehrbenutzer-
system arbeiten, muessen Sie das Diskettenlaufwerk zunaechst fuer sich reser-
vieren:
 'archive("std.zusatz")'.
  
Erst dann koennen Sie Dateien von der Diskette holen:
 'fetch("AT install",archive)' und das Installationsprogramm ausfuehren:
 'run'.

Der weitere Ablauf erfordert keine Eingriffe.  Nach Ablauf der
Programme sollten Sie schliesslich eine besondere Task zum Abschalten
einrichten. Dazu muessen Sie nocheinmal die Task 'SYSUR' an den Bildschirm
holen und dort das durch die Zusatzsoftware (u.a.) neu hinzugewonnene 
Kommando 
 'generate shutup dialog manager' geben.

Nach Absetzen des Kommandos koennen Sie 'SYSUR' durch <ESC> <q> wieder ver-
lassen. Um menuegesteuert das Betriebssystem abzuschalten oder einen Partiti-
onswechsel vorzunehmen, steht Ihnen die Task 'shutup dialog' zur Verfuegung.
Bei Ausfuehrung des Supervisor-Kommandos 'continue("shutup dialog")' wird
Ihnen die aktuelle Partitionstabelle angezeigt, so wie Sie diese bereits bei
der Generierung kennengelernt haben, d.h. mit Angabe von Groesse, Start- und
Endzylinder der eingerichteten Partitionen. Sie koennen dann eine beliebige
Partition menugesteuert auswaehlen und starten oder das Betriebssystem
kontrolliert abschalten (sog. 'shutup'). Dabei wird der aktuelle Systemzu-
stand automatisch gesichert. 
 
Archivformate bei ATs und Kompatiblen mit zwei Diskettenlaufwerken:  
 
Standardmaessig ist der Archivkanal 31 an das Laufwerk 'A:' gebunden, das
eine Kapazitaet von 1,2 Megabyte besitzt. Ist jedoch bei Ihrem Geraet ein
zweites Diskettenlaufwerk, z.B. mit einer Kapazitaet von 360 Kilobyte ein-
gebaut, dann koennen Sie auf dieses Laufwerk ueber den Kanal 30 zugreifen.
Dazu richten Sie unter 'SYSUR' eine Task ein, die Sie z.B. 'ARCHIVE 360'
benennen. Geben Sie in dieser Task das Kommando  'archive manager (30)'; 
dann koennen Sie von jeder Benutzertask das Archiv mit dem Kommando
 'archive ("Archivname",/ "ARCHIVE 360")'
anmelden. Der Zugriff auf eine Diskette in diesem Laufwerk geschieht z.B.
ueber  'list(/"ARCHIVE 360")' oder 'save ("Dateiname",/"ARCHIVE 360")'.


Installation eines neuen Urladers                    
=================================
 
Wenn Sie den alten Urlader mit einem neuen (z.B. protected mode) ueber-
schreiben wollen, starten Sie das EUMEL-System zunaechst neu. Sobald
die Meldung 
 
   Ladevorgang kann durch Tastendruck unterbrochen werden 
 
erscheint, druecken Sie eine beliebige Taste (z.B. ENTER).
Auf dem Bildschirm erscheint nun zusaetzlich die Meldung 
 
   Ladevorgang unterbrochen, druecken Sie eine Taste um fortzufahren
 
Legen Sie nun die Diskette mit dem neuen Urlader in das Bootlaufwerk und
druecken Sie wieder eine beliebige Taste. Danach werden folgende Meldungen
auf dem Bildschirm ausgegeben:  
_________________________________________ 
 
   EUMEL wird von Diskette geladen 
 
 
   E U M E L - Vortest 
 
   Terminals: 1 .... 
   RAM-Groesse (gesamt):        .... kB 
   Pufferbereich:               .... kB 
   Hintergrund-Speicher         .... kB 
 
   Speichertest:  ********** 
__________________________________________ 
 
In der Zeit, in der die Sternchen des Speichertests erscheinen, druecken Sie
bitte wieder die ENTER-Taste. Nach dem Speichertest erscheint dann
folgendes Menue: 
 
__________________________________________ 
 
   (1)   Systemstart 
   (2)   neuen Hintergrund vom Archiv laden 
   (3)   Hardwaretest 
   (4)   neuen Urlader vom Archiv laden 
__________________________________________ 
 
Waehlen Sie Menuepunkt 4 und auf dem Bildschirm erscheinen die
folgenden Zeilen: 
 
_________________________________________ 
   #     xxx
    fertig, bitte RESET 
_________________________________________ 
 
wobei hinter dem #-Zeichen die uebertragenen Bloecke des neuen Urladers
gezaehlt werden. 
 
Anschliessend entfernen Sie bitte die Urladerdiskette aus dem Laufwerk und
druecken den RESET-Schalter Ihres Rechners. Das EUMEL-Betriebssystem wird
nun mit dem neuen Urlader gestartet. 
 
 
                         
Tastenbelegung.                             
===============
 
EUMEL-Zeichen:  Taste auf dem IBM-PC/AT 
 
  MARK       :  bild (oder Pfeil nach oben) 
 
 
  RUBIN      :  Einfueg 
 
  RUBOUT     :  Loesch 
 
  TAB        :  <==> 
 
  HOP        :  Pos 1 
 
  ESC        :  Eing Loesch 
 
  SV         :  CTRL g    oder    F1 
 
Bemerkung: Die CTRL-Taste kann auch mit STRG bezeichnet sein. 
 
Sollte die Tastaturbelegung noch nicht die EUMEL-spezifischen Tasten 
(HOP, MARK, SV, RUBIN, RUBOUT) an den entsprechenden Orten anbieten, koennen
Sie durch Ankoppeln der Task "configurator" und Absetzen des Befehl 
'configurate' die Tastaturen (auch fuer zusaetzlich angeschlossene Terminals)
kanalweise umkonfigurieren.
Naeheres entnehmen Sie bitte dem Systemhandbuch, S.6ff.  
 
 
                            
 
Die einzelnen Schritte der Installation im öberblick:                     
===================================================== 
 
  1. Die Diskette 'SETUP-EUMEL' in das Laufwerk stecken. 
 
  2. Rechner einschalten oder Tastatur-RESET 
 
  3. EUMEL-Partition einrichten. 
 
  4. Generierung beenden und auf 'ENDE'-Meldung warten. 
 
  5. Diskette 'SETUP-EUMEL AT ' entnehmen. 
 
  6. Tastatur-RESET. 
 
  7. Die Meldung 'Leider keine EUMEL-0-Maschine gefunden' abwarten. 
 
  8. Hintergrunddiskette ('EUMEL-Hintergrund') einlegen und Taste druecken. 
 
  9. Nach der Meldung 'HG-ungueltig' eine Taste betaetigen, um in den Start-
     dialog zu gelangen. 
 
 10. Menupunkt 2 anwaehlen: Neuen Hintergrund vom Archiv laden.
     Hintergrunddiskette einlegen und 'Alten HG ueberschreiben?' mit "j"
     quittieren.
 
 11. Hintergrunddiskette entnehmen und anschliessend Tastatur-RESET aus-
     fuehren. 
 
 12. Kanal 1 konfigurieren. 
 
 13. Zusatzprogramme installieren.
 
 14. shutup dialog installieren. 
 

 Sollten Sie bei der Installation des EUMEL-Systems auf Fehler stossen oder
 sollten sonstige Probleme auftauchen, wÅrden uns folgende Angaben bei der 
 Fehlersuche unterstuetzen:
    
    - Rechnertyp und Rechnerkonfiguration.
    - SHard-Konfoguration (Ausdruck mit Funktion 6 des SETUP-EUMEL)
    - Genaue Beschreibung des fehlerhaften Befehls mit allen Parametern,
      moeglichst Bildschirmausdruck.
    - Telefonnummer (Privat/Dienstlich)	fÅr evtl. Rueckrufe
 
 
 
    ---==>    Ausdrucken der mitgelieferten HandbÅcher      <==-- 
 
Um die mitgelieferten HandbÅcher ausdrucken zu kînnen, mÅssen Sie eine Task
mit dem Namen `PRINTER' als Sohn der Task `SYSUR' einrichten. 
DafÅr geben Sie im SUPERVISOR-MenÅ 
 
            begin ("PRINTER", "SYSUR") 
 
ein. Sie befinden sich jetzt in der Task PRINTER. 
Nachdem Sie die Diskette mit den passenden Druckertreibern (9/24-Nadel-,
bzw. Laserdrucker) eingelegt haben, geben Sie das Kommando 
 
            archive ("std.printer") 
 
Nachdem Sie die Diskette angemeldet haben, kînnen Sie mit 
 
            fetch ("readme", archive) 
 
eine Installationsanleitung laden, welche Sie sich durch 
 
            edit ("readme") 
 
ansehen kînnen. Richten Sie sich fÅr alle weiteren Schritte nach dieser 
Anleitung. Au·erdem mu· der Kanal, an dem der Drucker betrieben werden soll,
korrekt konfiguriert sein. Falls es sich um eine parallele Schnittstelle
handelt (KanÑle 14, 15 oder 16) so ist die passende Konfiguration 
`transparent, gro·er Puffer'. Wenn Sie den Drucker an einer seriellen
Schnittstelle betreiben, so ist die Einstellung von den Vorgaben des
Druckerherstellers abhÑngig. Sehen Sie in den Unterlagen zum Drucker nach,
um die gewÅnschten Informationen zu erhalten. 
 
Zur Konfigurierung s. oben. 
 
 
Wenn Sie die Task PRINTER installiert haben, mÅssen Sie sich eine beliebige
andere Task einrichten: 
 
            begin ("handbÅcher") 
 
In der Task reservieren Sie wieder das Laufwerk 
 
            archive ("handbÅcher.1") 
 
Laden Sie nun alle Dateien von Diskette 
 
            fetchall (archive) 
 
Um die Dateien auszudrucken sagen Sie dem Computer 
 
            print (ALL myself) 
 
Nachdem Sie die Dateien ausgedruckt haben sollten Sie sie lîschen 
 
            forget (ALL myself) 
 
Verfahren Sie nun mit der zweiten Diskette ebenso wie mit der ersten. 
Nachdem Sie beide Disketten ausgedruckt haben, sollten Sie das Laufwerk
wieder fÅr andere Tasks freigeben 
 
            release (archive) 
 
Falls Sie nur einzelne Dateien drucken wollen (zum Beispiel, um zu testen,
ob der Drucker funktioniert), verwenden Sie das Kommando 
 
            print ("dateiname") 
 
Um die Mîglichkeiten Ihres Druckers in Bezug auf Zeilenbreite und
SeitenlÑnge optimal ausnutzen zu kînnen, kînnen Sie sich vor dem Drucken die
entsprechenden Kapitel im Benutzerhandbuch ansehen. Es sind dies die Kapitel
5.2 und 5.3 (lineform & pageform). 


