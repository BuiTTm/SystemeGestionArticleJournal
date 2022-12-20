# Guide d'utilisateur

Ceci est le guide d'utilisateur pour le projet de session du cours MGL7361.

## Créer un article

Tous les types d'utilisateur peuvent créer un article. Vous devez être authentifié avec un des utilisateurs fournis, ou votre propre utilisateur.

Vous devez tout d'abord cliquer sur "Voir mes articles" sur la page d'accueil, ou sur "Mes articles" dans la barre de menu.

Une fois sur cette page, vous pouvez cliquer sur "Soumettre un article".

Pour soumettre votre article, vous devez ajouter un titre, une description, les auteurs secondaires et choisir une catégorie. Une fois l'article créé, vous pourrez soumettre un document PDF qui constitue la première version de votre article.

## Soumettre une version d'article

Une fois sur la page d'un article, vous pouvez soumettre une version d'article. Une version est un document PDF contenant votre article.

Vous pouvez soumettre autant de versions que vous le souhaiter. Les évaluateurs vont pouvoir commenter la version la plus récente pour vous aider à publier votre article. Les commentaires sont toujours à propos de votre version la plus récente.

## Assigner un comité d'évaluateurs

Seuls les administrateurs peuvent assigner un comité d'évaluateurs à un article. Nous avons déjà créé un administrateur pour vous sous le courriel `admin@mgl7361.com`. Le mot de passe est `motdepasse123` tel que stipulé dans les procédures d'installation.

Une fois authentifié en tant qu'administrateur, vous pouvez accéder au panel de l'administrateur en cliquant sur "Espace administrateur" sur la page d'accueil. Il est aussi accessible directement à http://localhost:8000/admin.

Une fois dans l'espace administrateur, vous devez choisir l'entité `Comites`. Vous pourrez alors cliquer sur `Add Comite` pour ajouter un nouveau comité.

Pour créer le comité, vous devez choisir les évaluateurs dans ce comité, l'article lié au comité ainsi que la date à laquelle la décision du comité doit être rendue.

Une fois le comité créé, l'article passera automatiquement au statut `Relecture`.

## Voir les articles à évaluer

Seuls les évaluateurs peuvent voir les comités d'évaluation dans lesquels ils sont. Nous avons déjà créé deux évaluateurs pour vous, dont un sous le courriel `evaluateur1@mgl7361.com`. Le mot de passe est `motdepasse123` tel que stipulé dans les procédures d'installation.

Vous pouvez voir les articles à évaluer en cliquant sur "Mes comités d'évaluation" dans la barre de navigation

## Ajouter un commentaire sur un article

Seuls les évaluateurs peuvent voir les comités d'évaluation dans lesquels ils sont. Nous avons déjà créé deux évaluateurs pour vous, dont un sous le courriel `evaluateur1@mgl7361.com`. Le mot de passe est `motdepasse123` tel que stipulé dans les procédures d'installation.

Une fois dans la section "Mes comités d'évaluation", vous devez choisir l'article que vous souhaitez évaluer.

Pour cet article, vous verrez les informations et vous pourrez télécharger la version la plus récente. Vous verrez aussi les commentaires précédents laissés par vous ou vos collègues.

Pour ajouter un commentaire sur la version la plus récente de l'article, il suffit d'écrire le commentaire et de cliquer sur "Publier" dans le bas de la page.

## Autres fonctionnalités

Nous avons manqué de temps pour implémenter toutes les fonctionnalités identifiées. Les fonctionnalités ci-hautes représentent bien ce que vous pouvez faire avec notre plateforme. Évidemment, les permissions d'administrateur et l'espace administrateur vous permettent de faire beaucoup de manipulations à la base de données si ça vous tente d'essayer.
