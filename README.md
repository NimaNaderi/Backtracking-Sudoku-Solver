# 🧩 Backtracking-Sudoku-Solver

> **Hinweis:** Dieses Projekt wurde ursprünglich im **[Februar 2025]** entwickelt und nun für Portfolio-Zwecke auf GitHub veröffentlicht.

**AI Sudoku Solver Pro** ist eine hochperformante Desktop-Anwendung, die Sudoku-Rätsel nicht nur generiert, sondern den Lösungsprozess mithilfe von **Künstlicher Intelligenz (AI)** und dem **Backtracking-Algorithmus** in Echtzeit visualisiert.

Dieses Projekt demonstriert die praktische Anwendung komplexer Algorithmen, logischer Problemlösung und moderner GUI-Entwicklung mit Python.

![AI_Sudoku_Solver_Pro](https://github.com/user-attachments/assets/20519186-b5e3-4d8d-b63f-b92daf1a32f1)

## 🚀 Hauptfunktionen (Key Features)

* **🧠 AI-gestützter Lösungsalgorithmus:** Verwendet rekursives Backtracking, um selbst schwierigste Rätsel in Millisekunden zu lösen.
* **⚡ Echtzeit-Visualisierung:** Der Denkprozess des Algorithmus wird live dargestellt – man sieht, wie die KI Entscheidungen trifft und korrigiert.
* **🎨 Modernes UI/UX:** Benutzerfreundliche Oberfläche mit **Dark Mode** und **Light Mode** für optimale Lesbarkeit.
* **🌍 Mehrsprachigkeit:** Vollständig lokalisiert in **Deutsch**, **Englisch** und **Persisch**.
* **🎲 Intelligente Generierung:** Erstellt bei jedem Start ein einzigartiges, valides Sudoku-Rätsel.
* **🚀 High-Performance:** Optimierter Code für minimale Latenz und maximale Geschwindigkeit bei der Berechnung.

## 🛠️ Technologie-Stack

* **Sprache:** Python 3.x
* **GUI-Framework:** Tkinter (Standardbibliothek)
* **Algorithmus:** Rekursives Backtracking (Tiefensuche / DFS)
* **Design-Pattern:** OOP (Objektorientierte Programmierung)

## 🧩 Der Algorithmus (Logik)

Das Herzstück dieser Anwendung ist der **Backtracking-Algorithmus**. Er arbeitet nach dem Prinzip von "Versuch und Irrtum" (Trial and Error), jedoch auf eine hochstrukturierte und logische Weise:

1.  Suche das nächste leere Feld.
2.  Versuche eine Zahl von 1 bis 9.
3.  Prüfe, ob die Zahl gemäß den Sudoku-Regeln gültig ist (Zeile, Spalte, 3x3-Box).
4.  Wenn gültig -> Gehe zum nächsten Feld (Rekursion).
5.  Wenn keine Zahl passt -> Gehe einen Schritt zurück (**Backtrack**) und versuche eine andere Zahl.

Dieser Ansatz garantiert, dass eine Lösung gefunden wird, sofern eine existiert.
