
print("Välkommen till frågesporten!")
print("----------------------------")

poang = 0

fragor = [
    {
        "fraga": "Vad heter Sveriges huvudstad?",
        "svar": "stockholm"
    },
    {
        "fraga": "Hur många ben har en spindel?",
        "svar": "8"
    },
    {
        "fraga": "Vad är 5 + 7?",
        "svar": "12"
    },
    {
        "fraga": "Vilken planet kallas den röda planeten?",
        "svar": "mars"
    },
    {
        "fraga": "Hur många dagar har en vecka?",
        "svar": "7"
    }
]

for i, fraga in enumerate(fragor, start=1):
    print(f"\nFråga {i}: {fraga['fraga']}")
    svar = input("Ditt svar: ").strip().lower()

    if svar == fraga["svar"]:
        print("Rätt svar! 🎉")
        poang += 1
    else:
        print(f"Fel svar! Rätt svar är {fraga['svar']}.")

print("\n----------------------------")
print("Frågesporten är slut!")
print(f"Du fick {poang} av {len(fragor)} poäng.")

procent = poang / len(fragor) * 100
print(f"Du fick {procent:.0f}% rätt.")

if poang == len(fragor):
    print("Fantastiskt! Alla rätt!")
elif poang >= 3:
    print("Bra jobbat!")
else:
    print("Försök igen så går det ännu bättre!")
