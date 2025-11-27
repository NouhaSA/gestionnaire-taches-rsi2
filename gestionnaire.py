# gestionnaire.py
import json
from tache import Tache

class GestionnaireTaches:
    def __init__(self):
        # dict: id -> Tache
        self.taches = {}

    def ajouter_tache(self, titre, description, auteur="anonymous"):
        t = Tache(titre, description, auteur)
        self.taches[t.id] = t
        return t

    def supprimer_tache(self, id_):
        return self.taches.pop(id_, None)

    def lister_taches(self):
        # retourne لائحة من dicts
        return [t.to_dict() for t in self.taches.values()]

    def changer_statut(self, id_, statut):
        t = self.taches.get(id_)
        if t:
            t.statut = statut
            return t
        return None

    # Optional: sauvegarde / chargement simple
    def sauvegarder(self, chemin_fichier):
        try:
            with open(chemin_fichier, "w", encoding="utf-8") as f:
                json.dump(self.lister_taches(), f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    def charger(self, chemin_fichier):
        try:
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.taches = {}
            for d in data:
                t = Tache.from_dict(d)
                self.taches[t.id] = t
            return True
        except FileNotFoundError:
            return False
        except Exception:
            return False
