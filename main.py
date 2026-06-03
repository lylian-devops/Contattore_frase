
def controlla_frasi(testo):
    risultati = []
    frasi = re.split(r'(?<=[.!?])\s+', testo.strip())

    for i, frase in enumerate(frasi, 1):
        problemi = []

        if frase and not frase[0].isupper():
            problemi.append("inizia con lettera minuscola")
        if frase and frase[-1] not in ".!?":
            problemi.append("manca punteggiatura finale (. ! ?)")
        if "  " in frase:
            problemi.append("contiene spazi doppi")
        parole = frase.split()
        if len(parole) < 2:
            problemi.append("troppo corta (meno di 2 parole)")
        if len(parole) > 40:
            problemi.append(f"troppo lunga ({len(parole)} parole, max consigliato: 40)")
        if re.search(r'[a-zàèéìòù]\s+[A-Z]', frase):
            problemi.append("possibile frase non terminata correttamente")

        stato = "OK" if not problemi else "PROBLEMI TROVATI"
        print(f"\nFrase {i}: \"{frase}\"")
        print(f"  Stato: {stato}")
        if problemi:
            for p in problemi:
                print(f"  - {p}")

        risultati.append({"frase": frase, "problemi": problemi})

    totale = len(frasi)
    corrette = sum(1 for r in risultati if not r["problemi"])
    print(f"\n{'='*50}")
    print(f"Riepilogo: {corrette}/{totale} frasi corrette")
    return risultati


if __name__ == "__main__":
    testo_esempio = """Oggi è una bella giornata.
ho dimenticato l'ombrello a casa.
Il sole splende alto nel cielo!
Andiamo al mare  insieme?
ciao."""

    print("ANALISI DEL TESTO\n" + "="*50)
    controlla_frasi(testo_esempio)
