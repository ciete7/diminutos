drop database if exists sistema_salas;

create database sistema_salas

character set utf8mb4
collate utf8mb4_general_ci;

use sistema_salas;

create table Usuario(
    id_usuario int primary key auto_increment,
    username varchar(50) not null unique,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    telefono varchar(20),
    email varchar(100) unique,
    password_hash varchar(255) not null,
    tipo_usuario VARCHAR(20) NOT NULL DEFAULT 'empleado'
);

create table Sala(
    id_sala int primary key auto_increment,
    nombre varchar(100) not null,
    ubicacion varchar(100) not null,
    capacidad int not null,
    estado ENUM('Disponible', 'En mantenimiento') not null,

    constraint chk_sala_capacidad
    check(capacidad>0)
);

create table Reserva(
    id_reserva int primary key auto_increment,
    id_usuario int not null,
    id_sala int not null,
    fecha DATE not null,
    hora TIME not null,

    constraint fk_reserva_usuario
    foreign key (id_usuario)
    references Usuario(id_usuario)
    on update cascade
    on delete restrict,

    constraint fk_reserva_sala
    foreign key (id_sala)
    references Sala(id_sala)
    on update cascade
    on delete restrict
);
