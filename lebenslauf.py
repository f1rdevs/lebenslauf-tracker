class LebenslaufTracker:
    def __init__(self):
        self.projekte = {}
        self.skills = []
        self.zertifikate = {}

    def projekt_hinzufuegen(self, titel, rolle, werkzeuge):
        if titel == "":
            raise ValueError("Titel leer")
        if titel in self.projekte:
            raise ValueError("Projekt existiert")
        self.projekte[titel] = {"rolle": rolle, "werkzeuge": werkzeuge, "skills": set()}

    def skill_hinzufuegen(self, name):
        if name == "":
            raise ValueError("Skill leer")
        if name in self.skills:
            raise ValueError("Skill existiert")
        self.skills.append(name)

    def skill_nachweis_hinzufuegen(self, projekt_titel, skill_name):
        if projekt_titel not in self.projekte:
            raise ValueError("Projekt unbekannt")
        if skill_name not in self.skills:
            raise ValueError("Skill unbekannt")
        self.projekte[projekt_titel]["skills"].add(skill_name)

    def zertifikat_hinzufuegen(self, name, ausgeber, ablauf_jahr):
        if name == "":
            raise ValueError("Zertifikat leer")
        if name in self.zertifikate:
            raise ValueError("Zertifikat existiert")
        self.zertifikate[name] = {"ausgeber": ausgeber, "ablauf_jahr": ablauf_jahr}

    def zertifikat_abgelaufen(self, zert_name, aktuelles_jahr):
        ablauf_jahr = self.zertifikate[zert_name]["ablauf_jahr"]
        if ablauf_jahr == 0:
            return False
        return ablauf_jahr < aktuelles_jahr



