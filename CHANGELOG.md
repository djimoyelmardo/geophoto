# Journal des versions

## v2.3 – 2026-10-05
- GPS activé automatiquement à l'ouverture de l'application.
- Bouton « Terminer l'opération » : efface les photos et le nom de l'agent pour repartir d'un formulaire vide (avec confirmation).
- Le champ « Auteur » devient « Agent OFB » (l'attribut exporté reste `auteur`).

## v2.2 – 2026-10-05
- Correction du partage sur Android : Chrome refusait le fichier `.geojson` (« Permission denied »).
  Le fichier de points est désormais joint en CSV sur Android, en GeoJSON sur iPhone.
- Repli automatique vers la variante suivante si un type de fichier est refusé.
- Alerte au-delà de 10 fichiers par partage sur Android.

## v2.1 – 2026-10-04
- Application installable sur l'écran d'accueil (manifest, icônes, plein écran).
- Aide à l'installation affichée selon le téléphone (Android : bouton ; iPhone : consigne Safari).
- Numéro de version affiché en bas de l'application.

## v2.0 – 2026-10-04
- Annotation : trait libre, flèche, rectangle, ellipse, texte, cote avec mesure, repères numérotés.
- Photo originale conservée en plus de la photo annotée.
- Stockage local des photos (IndexedDB) : elles survivent à la fermeture de la page.
- Fonctionnement hors-ligne (service worker), bibliothèques intégrées à index.html.
- Sélection des photos à partager, statut « à envoyer » / « partagée », alerte au-delà de 20 Mo.
- GeoJSON : ajout des champs `id`, `fichier_original`, `annotee`.

## v1.0 – 2026-10-04
- Prototype : photo, position GPS moyennée, conversion Lambert-93, EXIF GPS, GeoJSON, partage.
