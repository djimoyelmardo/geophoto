# GéoPhoto

Application web mobile (PWA) pour prendre des photos géolocalisées, les annoter, les commenter
et les envoyer par mail. Aucun serveur : tout se passe sur le téléphone.

Application en ligne : https://djimoyelmardo.github.io/geophoto/

## Fonctions
- Position GPS en WGS84 et en Lambert-93 (EPSG:2154), avec précision affichée.
- Carte de contrôle sur fonds IGN (Géoplateforme) et correction manuelle du point.
- Annotation au doigt : trait, flèche, rectangle, ellipse, texte, cote, repères numérotés.
- Photos conservées sur le téléphone, utilisables hors-ligne.
- Partage vers l'application mail : photo annotée, photo originale, fichier `geophoto.geojson`.
- Coordonnées écrites dans l'EXIF des photos et dans le GeoJSON (lisibles dans QGIS).

## Organisation du dépôt
| Fichier | Rôle |
|---|---|
| `src/app.html` | Code source de l'application (à modifier) |
| `vendor/` | Bibliothèques : proj4 2.11.0, piexifjs 1.0.6, Leaflet 1.9.4 |
| `build.py` | Assemble `index.html` à partir des sources |
| `index.html` | Fichier généré, servi par GitHub Pages (ne pas modifier à la main) |
| `sw.js` | Cache hors-ligne ; incrémenter `CACHE` à chaque version |
| `manifest.webmanifest`, `icons/` | Installation sur l'écran d'accueil |
| `CHANGELOG.md` | Journal des versions |

## Publier une nouvelle version
1. Modifier `src/app.html`.
2. Lancer `python build.py`.
3. Incrémenter `CACHE` dans `sw.js` et compléter `CHANGELOG.md`.
4. Valider (commit), fusionner dans `main`, puis poser une étiquette : `git tag v2.1 && git push --tags`.

GitHub Pages publie automatiquement le contenu de la branche `main`.

## Utilisation dans QGIS
Glisser le fichier `geophoto_AAAAMMJJ_HHMM.geojson` dans QGIS. Pour afficher la photo au survol, enregistrer le projet
dans le dossier des photos et utiliser cette infobulle HTML :

```html
<b>[% "fichier" %]</b><br>[% "commentaire" %]<br>
<img src="file:///[% @project_folder %]/[% "fichier" %]" width="350">
```

### Depuis Android : fichier CSV
Android ne permet pas de partager un `.geojson` : le mail contient `geophoto.csv` à la place.
Dans QGIS : Couche → Ajouter une couche → Couche de texte délimité, délimiteur point-virgule,
champ X `lon`, champ Y `lat`, SCR EPSG:4326 (ou `x_l93` / `y_l93` en EPSG:2154).
Le bouton « Télécharger le GeoJSON » de l'application reste disponible pour l'obtenir à part.
