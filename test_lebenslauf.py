# Unit-Tests für LebenslaufTracker
import unittest
from lebenslauf import LebenslaufTracker

class TestLebenslaufTracker(unittest.TestCase):
    def setUp(self):
        self.t = LebenslaufTracker()
        self.t.projekt_hinzufuegen("Datenbankprojekt HTW", "Entwickler", "PostgreSQL, DBeaver")
        self.t.skill_hinzufuegen("SQL")

    def test_projekt_speichert_rolle_werkzeuge(self):
        p = self.t.projekte["Datenbankprojekt HTW"]
        self.assertEqual(p["rolle"], "Entwickler/in")
        self.assertEqual(p["werkzeuge"], "PostgreSQL, DBeaver")

    def test_projekt_doppelt_fehler(self):
        with self.assertRaises(ValueError):
            self.t.projekt_hinzufuegen("Datenbankprojekt HTW", "x", "y")

    def test_skill_doppelt_fehler(self):
        with self.assertRaises(ValueError):
            self.t.skill_hinzufuegen("SQL")

    def test_skill_nachweis_zu_projekt(self):
        self.t.skill_nachweis_hinzufuegen("Datenbankprojekt HTW", "SQL")
        self.assertTrue("SQL" in self.t.projekte["Datenbankprojekt HTW"]["skills"])

    def test_zertifikat_abgelaufen_wahr_falsch(self):
        self.t.zertifikat_hinzufuegen("AWS Cloud", "AWS", 2024)
        self.assertTrue(self.t.zertifikat_abgelaufen("AWS Cloud", 2026))

        self.t.zertifikat_hinzufuegen("Azure AZ-900", "Microsoft", 0)
        self.assertFalse(self.t.zertifikat_abgelaufen("Azure AZ-900", 2030))

if __name__ == "__main__":
    unittest.main()
