# Journal des versions

## v2.0 – 2026-10-04
- Annotation : trait libre, flèche, rectangle, ellipse, texte, cote avec mesure, repères numérotés.
- Photo originale conservée en plus de la photo annotée.
- Stockage local des photos (IndexedDB) : elles survivent à la fermeture de la page.
- Fonctionnement hors-ligne (service worker), bibliothèques intégrées à index.html.
- Sélection des photos à partager, statut « à envoyer » / « partagée », alerte au-delà de 20 Mo.
- GeoJSON : ajout des champs `id`, `fichier_original`, `annotee`.

## v1.0 – 2026-10-04
- Prototype : photo, position GPS moyennée, conversion Lambert-93, EXIF GPS, GeoJSON, partage.
