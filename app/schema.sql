DROP TABLE IF EXISTS produit;

CREATE TABLE produit (
    id INTEGER NOT NULL PRIMARY KEY ,
    nom TEXT NOT NULL ,
    prix REAL NOT NULL DEFAULT 0.0,
    categorie TEXT NOT NULL ,
    description TEXT NOT NULL,
    statut TEXT NOT NULL ,
    photo TEXT NOT NULL
);