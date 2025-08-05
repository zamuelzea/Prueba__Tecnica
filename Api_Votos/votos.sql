CREATE DATABASE Votos_bd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE Votos_bd;

CREATE TABLE Votantes (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Votante VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) NOT NULL UNIQUE,
    Ha_Votado BOOLEAN DEFAULT FALSE
);

CREATE TABLE Candidatos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Candidato VARCHAR(100) NOT NULL,
    Partido VARCHAR(100),
    Votos INT DEFAULT 0
);

CREATE TABLE Votos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Id_Votante INT NOT NULL,
    id_Candidato INT NOT NULL,
    FOREIGN KEY (Id_Votante) REFERENCES Votantes(Id),
    FOREIGN KEY (id_Candidato) REFERENCES Candidatos(Id),
    UNIQUE (Id_Votante)
);