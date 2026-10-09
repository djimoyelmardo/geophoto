# Journal des versions

## v3.1 – 2026-10-09
- « Viser l'objet sur la carte » : placer sur une grande carte l'objet photographié quand il est à distance.
  Le point s'applique à la photo suivante seulement.
- La photo prend la position de l'objet ; la position de l'agent, la distance et l'azimut sont conservés
  (attributs `mode_position`, `agent_x_l93`, `agent_y_l93`, `agent_lon`, `agent_lat`, `distance_agent_m`, `azimut_deg`).

## v3.0 – 2026-10-06
- Nouvelle interface : bandeau de position en tête (X, Y, précision), couleurs marines, boutons plus grands.
- Carte de contrôle (fonds IGN, plan ou vue aérienne) : position en direct, cercle de précision, photos de l'opération.
- Correction manuelle du point d'une photo sur la carte ; attributs `position_corrigee` et `ecart_gps_m`.
- Aide intégrée à l'application.
- Fichier de points daté (`geophoto_AAAAMMJJ_HHMM.geojson` ou `.csv`) pour ne plus écraser les envois précédents.
- Galerie : une photo non annotée est enregistrée avec son bandeau de coordonnées quand l'incrustation est cochée.

## v2.4 – 2026-10-05
- « Terminer l'opération » n'efface plus rien : les photos sont enregistrées dans la galerie du téléphone
  (annotée si elle l'est, sinon l'originale), rangées dans « Opérations précédentes », et le formulaire est vidé.
- Nouvelle rubrique « Opérations précédentes » : cocher, décocher, enregistrer en galerie,
  remettre dans le formulaire, supprimer la sélection.
- Le nom de l'agent est conservé d'une opération à l'autre.

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
