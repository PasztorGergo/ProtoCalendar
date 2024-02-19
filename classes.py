from random import randint
from datetime import date

class Task:
    id = None
    title = ""
    path = ""
    is_completed = None
    description = ""
    date = None

    def __init__(self, title, description, date, id) -> None:
        self.title = title
        self.description = description
        self.is_completed = False
        self.date = date

class Calendar:

    def add(self,tasks):
        print("Új Protogén rajz hozzáadása")
        title = input("Adja meg a rajz címét: ")
        description = input("Adjon hozzá leírást(opcionális): ")
        cal_date = input("Adja meg az időpontot(EEEE/HH/NN): ")

        try:
            id = self.id = hex(randint(0,10**3))
            sep_date = cal_date.split("/")
            print(sep_date, id)
            tasks.append(Task(title, 
                                   description, 
                                   date(int(sep_date[0]),int(sep_date[1]), int(sep_date[2])),
                                    id
                                ))
            print("Új ötlet hozzáadva", id, "azonosítóval", cal_date, "időpontra.")
        except:
            print("Sikertelen művelet. Kérlek próbáld újra!")

    def rewrite(self,tasks):
        id = input("Létező ötlet módosítása\nAdd meg az ötlet azonosítóját: ")
        copy = None

        if len(copy := [keresett for keresett in tasks if keresett.id == id]) > 0:
            for prop in copy[0]:
                if prop != "id" or "is_completed":
                    match prop:
                        case "path":
                            if (new_path := input(f"Adja meg az új útvonalt\n({copy[0].path})\n vagy lépjen tovább enterrel: ")) != "":
                                copy[0].path = new_path
                        case "title":
                            if (new_title := input(f"Adja meg az új címet\n({copy[0].title})\n vagy lépjen tovább enterrel: ")) != "":
                                copy[0].title = new_title
                        case "description":
                            if (new_desc := input(f"Adja meg az új leírást\n({copy[0].description})\n vagy lépjen tovább enterrel: ")) != "":
                                copy[0].descritption = new_desc
                        case "date":
                            if (new_desc := input(f"Adja meg az új dátumot\n({copy[0].date})\n vagy lépjen tovább enterrel: ")) != "":
                                copy[0].descritption = new_desc
            print("Az adatok sikeresen módosításra kerültek.\nAz új adatokkal együtt:")
            for prop in copy[0]:
                match prop:
                        case "path":
                            print("Útvonal:",copy[0].path)
                        case "title":
                            print("Cím:",copy[0].title)
                        case "description":
                            print("Leírás:",copy[0].description)
                        case "date":
                            print(f"Dátum:",copy[0].date)
        else:
            print("A(z)", id, "azonosítóval ellátott ötlet nem létezik. Kérlek próbáld újra!")

    def complete(self,tasks):
        id = input("Létező ötlet teljesítése\nAdd meg az ötlet azonosítóját: ")
        if len(copy := [keresett for keresett in tasks if keresett.id == id]) > 0:
            new_path = input("Add meg a képhez tartozó (abszolút) útvonalat: ")
            copy[0].path = new_path
            copy[0].is_completed = True
            print(f"A(z) {copy[0].title} című rajz sikeresen teljesítve.\nElérhetőség:{copy[0].path}")
        else:
            print("A(z)", id, "azonosítóval ellátott ötlet nem létezik. Kérlek próbáld újra!")

    def display(self):
        pass

