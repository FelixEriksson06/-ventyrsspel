import random as rand
import keyboard
import sys


class Monster:
    def __init__(self, namn):
        self.namn = namn
        self.styrka = rand.randint(1, 10)
        self.hp = rand.randint(1, 10)

    @classmethod
    def rand_monster(cls):
        lista_alla_monster = ["goblin", "Drake", "Orc", "varulv", "dvärg"]
        name = rand.choice(lista_alla_monster)
        return cls(name)


class Weapon:
    def __init__(self, namn, styrka, värde):
        self.namn = namn
        self.styrka = styrka
        self.värde = värde

    @classmethod
    def rand_vapen(cls):
        alla_olika_vapen = [
            cls("träsvärd", 2, 1),
            cls("järnsvärd", 4, 2),
            cls("guldsvärd", 6, 3),
            cls("diamantsvärd", 8, 4),
            cls("kristallsvärd", 10, 5)
        ]
        return rand.choice(alla_olika_vapen)


def strid(hjälte_hp, hjälte_styrka, monster_styrka, antal_död, antal_dödade, monster_namn, guld, saker_ryggsäck):
    print(f"""du öppnade dörren och hamnade i en strid!
        
    vad vill du göra?! Din styrka är {hjälte_styrka}, {monster_namn}  har styrkan {monster_styrka}!
        
    1. fly och förlora 2 hp
    2. attackera monstret för en chans att vinna""")
    val_strid = input("")

    if val_strid == "1":
        hjälte_hp = hjälte_hp - 2
        print(f"du flydde från striden och tappade 2 hp, din hp är nu {hjälte_hp}")
    elif val_strid == "2":
        print("Det här är dina vapen i din ryggsäck! Välj ett fort för att strida monstret")
        for index, weapon in enumerate(saker_ryggsäck, 1):
            print(f"{index}. {weapon.namn} - Styrka: {weapon.styrka}")
        print("välj vapnet genom att skriva in den position vapnet har i listan")
        nummer_för_val_vapen = int(input(""))

        while True:
            try:
                if 1 <= nummer_för_val_vapen <= len(saker_ryggsäck):
                    val_vapen = saker_ryggsäck[nummer_för_val_vapen - 1]
                    print(f"Du valde vapnet {val_vapen.namn}, vilket betyder att din styrka nu är {hjälte_styrka + val_vapen.styrka}")

                    val_vapen = saker_ryggsäck[nummer_för_val_vapen - 1]
                    hjälte_styrka_med_vapen = hjälte_styrka + val_vapen.styrka
                
                    if hjälte_styrka_med_vapen >= monster_styrka or rand.randint(hjälte_styrka, monster_styrka + hjälte_hp / 2) >= monster_styrka:
                            hjälte_hp = hjälte_hp + 4
                            guld = guld + 5
                            print(f"eftersom din egna styrka med hjälp av vapnets styrka blir {hjälte_styrka_med_vapen} krossar du monster som bara har styrkan {monster_styrka}")
                            print(f"Du vann Striden! du har nu tjänat 4 hp och har nu {hjälte_hp} hp och 5 mer guld, din totala guld är nu {guld}  ")
                            antal_dödade += 1    
                    elif val_strid == "2" and hjälte_styrka < monster_styrka:
                            hjälte_hp = hjälte_hp - 2
                            print(f"Du förlorade striden! Du tappade 2 hp och har nu {hjälte_hp} hp")
                            antal_död += 1
                    break
                else:
                    print("Det numret matchar inget vapen i ryggsäcken. Välj igen.")
            except ValueError:
                print("Det där är inte ett giltigt nummer. Välj ett nummer!!")

    print("Tryck space för att gå vidare")
    keyboard.wait('space')
    return hjälte_hp, hjälte_styrka, saker_ryggsäck, antal_död, antal_dödade, guld

def marknad(guld, hjälte_hp, hjälte_styrka):
    while True:
        print(f"""Välkommen till marknaden. Här kan du använda guld för att köpa liv och styrka!
        Du har {guld} guld, {hjälte_hp} hp och {hjälte_styrka} styrka just nu.
        Vad vill du köpa?

        1. Köp 2 styrka för 20 guld
        2. Köp 2 liv för 30 guld
        3. Du vill inte ha någonting från marknaden""")
        
        try:
            marknad_svar = int(input("Ditt val: "))
            if marknad_svar not in [1, 2, 3]:
                print("Välj ett nummer mellan 1, 2 eller 3.")
            else:
                break
        except ValueError:
            print("Skriv in ett nummer 1, 2 eller 3. Försök igen.")

    if marknad_svar == 1:
        if guld >= 20:
            print(f"Du köpte 2 styrka och har nu styrkan {hjälte_styrka + 2} men förlorade 20 guld vilket betyder att du bara har {guld - 20} guld kvar.")
            hjälte_styrka += 2
            guld -= 20
        else:
            print("Du har inte tillräckligt med guld")
    elif marknad_svar == 2:
        if guld >= 30:
            print(f"Du köpte 2 liv och har nu livet {hjälte_hp + 2} men förlorade 30 guld vilket betyder att du bara har {guld - 30} guld kvar.")
            hjälte_hp += 2
            guld -= 30
        else:
            print("Du har inte tillräckligt med guld")
    
    print("Klicka på space för att gå vidare: ")
    keyboard.wait('space')
    return guld, hjälte_hp, hjälte_styrka


def kista(saker_ryggsäck):
    print("""Du öppnade dörren och hittade en kista
            Klicka på space för att se vad du fick: """)
    keyboard.wait('space')

    random_weapon = Weapon.rand_vapen()
    print(f"Du hittade en {random_weapon.namn} med {random_weapon.styrka} styrka. Vapnet kommer hamna i din ryggsäck")

    saker_ryggsäck.append(random_weapon)
    
    print("Klicka på space för att gå vidare: ")
    keyboard.wait('space')
    return saker_ryggsäck


def fälla(hjälte_hp):
    while True:
        try:
            ditt_nummer = int(input("Du hamnade i en fälla! Gissa på ett nummer 1-3 för att klara dig: "))

            random_nummer = rand.randint(1, 3)
            rätt_nummer = random_nummer

            if ditt_nummer == rätt_nummer:
                print("Du klarade det och förlorade inte någon hälsa! ")
            else:
                print(f"Du klarade det inte och tappade 1 hp. Din hälsa är nu {hjälte_hp - 1}")
                hjälte_hp = hjälte_hp - 1
            break
        except ValueError:
            print("Skriv in ett nummer som är en siffra 1, 2 eller 3. Försök igen.")
        except ditt_nummer not in [1, 2, 3]:
                print("Välj ett nummer mellan 1 och 3!!!")


    print("Klicka på space för att gå vidare: ")
    keyboard.wait('space')
    return hjälte_hp


def ryggsäck(saker_ryggsäck):
    print(f"Det här har du i din ryggsäck: {', '.join([item.namn for item in saker_ryggsäck])}")
    print("Klicka på space för att gå vidare: ")
    keyboard.wait('space')


def stats(hjälte_styrka, hjälte_hp, guld, antal_dödade, antal_död):
    print(f"""
    Stats:

    Styrka: {hjälte_styrka}
    HP: {hjälte_hp}
    Antal dödade monster: {antal_dödade}
    Antal gånger du har dött: {antal_död}
    """)

    print("Klicka på space för att gå vidare: ")
    keyboard.wait('space')


def dörr(hjälte_hp, hjälte_styrka, saker_ryggsäck, monster_styrka, antal_dödade, antal_död, guld, monster_namn):
    print("""Välj dörr:
                  
                  1. 
                  2.
                  3.
                  
                  """)
    
    dörr_tal = input("")
    if dörr_tal in ["1", "2", "3"]:
        slumptal_dörr = rand.randint(1, 3)

        if slumptal_dörr == 1:
            hjälte_hp, hjälte_styrka, saker_ryggsäck, antal_död, antal_dödade, guld = strid(
                hjälte_hp, hjälte_styrka, monster_styrka, antal_död, antal_dödade, monster_namn, guld, saker_ryggsäck
            )
        elif slumptal_dörr == 2:
            saker_ryggsäck = kista(saker_ryggsäck)
        elif slumptal_dörr == 3:
            hjälte_hp = fälla(hjälte_hp)
        else:
            print("Välj 1, 2 eller 3!")

    return hjälte_hp, hjälte_styrka, saker_ryggsäck, antal_död, antal_dödade


def trolldryck(hjälte_hp, hjälte_styrka):
    print(f"""Du har {hjälte_hp} liv och {hjälte_styrka} styrka just nu!

                Vill du köpa en trolldryck som kommer öka din styrka med 3 men minska ditt liv med 5?

                1. Gör utbytet
                2. Skit i det""")
    
    val_trolldryck = input("")
    
    if val_trolldryck == "1":
        print(f"Din styrka ökade från {hjälte_styrka} till {hjälte_styrka + 3}, men Kevin tog 5 liv från dig vilket betyder att du bara har {hjälte_hp - 5} liv kvar")
        hjälte_styrka = hjälte_styrka + 3
        hjälte_hp = hjälte_hp - 5
    elif val_trolldryck == "2":
        print("Jahopp")
    else:
        print("Välj 1 eller 2!")

    print("Klicka på space för att gå vidare: ")
    keyboard.wait('space')
    return hjälte_hp, hjälte_styrka


def kevin(guld, hjälte_hp, hjälte_styrka, saker_ryggsäck):
    print("""Tjo jag heter Kevin, vad vill du ha?

                1. Gå till marknaden
                2. Köpa en trolldryck
                3. Äh, det var inget""")
    
    val_kevin = input("")

    if val_kevin == "1":
        guld, hjälte_hp, hjälte_styrka = marknad(guld, hjälte_hp, hjälte_styrka)
    elif val_kevin == "2":
        hjälte_hp, hjälte_styrka = trolldryck(hjälte_hp, hjälte_styrka)
    elif val_kevin == "3":
        return hjälte_hp, saker_ryggsäck, guld
    else:
        print("Välj 1, 2 eller 3!")

    return hjälte_hp, saker_ryggsäck, guld

def död(hjälte_hp, hjälte_styrka, saker_ryggsäck):
    hjälte_hp = 10
    hjälte_styrka = 4
    saker_ryggsäck.clear()
    saker_ryggsäck.append[Weapon("träsvärd", 2, 1)]
    return hjälte_hp,hjälte_styrka,saker_ryggsäck

def main():
    hjälte_namn = input("Vad heter du?")
    hjälte_hp = 10
    hjälte_styrka = 4
    saker_ryggsäck = [Weapon("träsvärd", 2, 1)]
    antal_död = 0
    antal_dödade = 0
    guld = 10

    while hjälte_hp > 0:                
        print(
            f"""
            Hej {hjälte_namn}!

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck   
            3. Kolla stats
            4. Prata med Kevin
            5. Stäng av spelet
            """
        )
        
        val_main = input("")

        if val_main == "1":
            hjälte_hp, hjälte_styrka, saker_ryggsäck, antal_död, antal_dödade = dörr(
                hjälte_hp, hjälte_styrka, saker_ryggsäck, Monster.rand_monster().styrka, antal_dödade, antal_död, guld, Monster.rand_monster().namn
            )
        elif val_main == "2":
            ryggsäck(saker_ryggsäck)
        elif val_main == "3":
            stats(hjälte_styrka, hjälte_hp, guld, antal_dödade, antal_död)
        elif val_main == "4":
            hjälte_hp, saker_ryggsäck, guld = kevin(guld, hjälte_hp, hjälte_styrka, saker_ryggsäck)
        elif val_main == "5":
            sys.exit()
        else:
            print("Välj 1, 2 eller 3!")
    else:
        print(""" Du förlorade alla dina liv och DOG!!
                1. Spawna igen och börja från början!
                2. Ge upp och stäng av""")
        
        svar_död = input("")

        if svar_död == "1":
            hjälte_hp, hjälte_styrka, saker_ryggsäck = död(hjälte_hp, hjälte_styrka, saker_ryggsäck)
        elif svar_död == "2":
            print("Spelet stängs av")
            sys.exit()
        else:
            print("Välj 1 eller 2!")
            
main()