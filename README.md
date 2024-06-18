<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Jeu de la Vie</h1>

<p>Le Jeu de la Vie est une simulation informatique inventée par le mathématicien John Horton Conway en 1970. C'est un automate cellulaire basé sur une grille de cellules qui peuvent être vivantes ou mortes, avec des règles simples déterminant l'évolution de la grille à chaque étape. 3 étudiants à Polytech Dijon ont pris le temps de recoder cette simulation aux dimensions infinies et offrir à l'utilisateur une expérience unique.</p>

<h2>Sommaire</h2>
<ul>
    <li><a href="#regles-du-jeu">Règles du Jeu</a></li>
    <li><a href="#fonctionnalites">Fonctionnalités</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#utilisation">Utilisation</a></li>
    <li><a href="#contributions">Contributions</a></li>
    <li><a href="#remerciements">Remerciements</a></li>
</ul>

<h2 id="regles-du-jeu">Règles du Jeu</h2>
<ul>
    <li><strong>Survie :</strong> Une cellule vivante avec 2 ou 3 voisins vivants reste vivante.</li>
    <li><strong>Mort par isolement :</strong> Une cellule vivante avec moins de 2 voisins vivants meurt.</li>
    <li><strong>Mort par surpopulation :</strong> Une cellule vivante avec plus de 3 voisins vivants meurt.</li>
    <li><strong>Naissance :</strong> Une cellule morte avec exactement 3 voisins vivants devient vivante.</li>
</ul>

<h2 id="fonctionnalites">Fonctionnalités</h2>
<ul>
    <li><strong>Edition :</strong> Permettre à l'utilisateur de dessiner ces propres configurations afin d'en observer le résultat.</li>
    <li><strong>Chargement de motifs :</strong> Permet de charger des configurations de cellules prédéfinies par les créateurs de ce jeu.</li>
    <li><strong>Simulation :</strong> Exécute les étapes de la simulation selon les règles du jeu.</li>
    <li><strong>Interface utilisateur :</strong> Interface graphique pour visualiser la grille et interagir avec la simulation.</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
    <li>Clonez le dépôt :
        <pre><code>git clone https://github.com/Kentosky/Jeu_De_La_Vie.git
cd Jeu_De_La_Vie</code></pre>
    </li>
    <li>Installez <a href="https://drive.google.com/file/d/1g3jx-kb9sxNnLexoBJgq8AtHwf2k3g2a/view?usp=sharing">la vidéo de fond d'écran</a>.
    </li>
    <li>Installez les dépendances :
        <pre><code>pip install pygame
pip install pygame-widgets
pip install moviepy</code></pre>
    </li>
</ol>

<h2 id="utilisation">Utilisation</h2>
<ol>
    <li>Lancez le script principal pour démarrer la simulation :
        <pre><code>python main.py</code></pre>
    </li>
    <li>Utilisez l'interface pour :
        <ul>
            <li>Découvrir les règles du Jeu de la vie</li>
            <li>Créer vos propres structures et en observer le résulat pendant la simulation</li>
            <li>Charger des motifs prédéfinis pour découvrir des types de structures</li>
        </ul>
    </li>
</ol>

<h2 id="contributions">Contributions</h2>
<p>Les contributions sont les bienvenues ! Pour proposer des modifications, veuillez :</p>
<ol>
    <li>Forker le dépôt</li>
    <li>Créer une branche pour votre fonctionnalité/amélioration</li>
    <code>git checkout -b feature/AmazingFeature</code>
    <li>Committer vos changements</li>
    <code>git commit -m 'Add some AmazingFeature'</code>
    <li>Pusher la branche</li>
    <code>git push origin feature/AmazingFeature</code>
    <li>Ouvrir une Pull Request</li>
</ol>

<h2 id="remerciments">Remerciements et Crédits</h2>
<ul>
    <li>Ce jeu de simulation a été entièrement développé par CUVELIER Line, BESSE Fabien et VILLERET Baptiste, 3 étudiants de Polytech Dijon. </li>
    <li>Nous remercions John Horton Conway pour avoir inventé le Jeu de la Vie.</li>
    <li>Nous remercions aussi la communauté open-source pour les bibliothèques et outils utilisés dans ce projet.</li>
</ul>

<p>Pour plus de détails, consultez le <a href="https://github.com/Kentosky/Jeu_De_La_Vie.git">dépôt GitHub</a>.</p>
</body>
</html>

