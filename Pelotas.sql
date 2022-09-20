CREATE DATABASE if NOT EXISTS Pelotas;
USE Pelotas;
CREATE TABLE Planta( ID_Planta INT UNSIGNED PRIMARY KEY AUTOINCREMENT, Color VARCHAR(15) NOT NULL);
CREATE TABLE Maquina(ID_Maquina INT UNSIGNED PRIMARY KEY AUTOINCREMENT, ID_Planta INT(5), Marca VARCHAR(20)
Modelo VARCHAR(20), Estado BOOLEAN);
CREATE TABLE Tecnico(ID_Tecnico INT UNSIGNED PRIMARY KEY AUTOINCREMENT, Nombre VARCHAR(25), F_Ingreso DATE
F_Baja DATE, F_Nacimiento DATE, Telefono VARCHAR(10));
CREATE TABLE Taller(ID_Reparacion INT UNSIGNED PRIMARY KEY AUTOINCREMENT, ID_Tecnico INT FOREIGN KEY, 
ID_Maquina FOREIGN KEY INT(6)
F_Ingreso DATE, F_Egreso DATE, Tipo_Reparacion VARCHAR(200));



