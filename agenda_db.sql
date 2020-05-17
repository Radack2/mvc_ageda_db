create database if not exists agenda_db;

use agenda_db;

create table if not exists contacto(
	id_contacto int not null auto_increment,
    c_nombre varchar(35) not null,
    c_apellidoP varchar(35) not null,
    c_apellidoM varchar(35),
    c_calle VARCHAR(35) NOT NULL,
    c_noext VARCHAR(7) NOT NULL,
    c_noint VARCHAR(7),
    c_col VARCHAR(35),
    c_zip VARCHAR(6),
    c_email VARCHAR(35),
    c_telefono VARCHAR(15),
    PRIMARY KEY (id_contacto)
    
) ENGINE=INNODB;

create table if not exists cita(
	id_cita int not null auto_increment,
    c_lugar varchar(35) not null,
    c_ciudad varchar(35) not null,
    c_estado varchar(35),
    c_fecha date not null,
    c_asunto varchar(250),
    primary key (id_cita)
    
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS detalles_cita (
	id_cita int not null,
    id_contacto int not null,
    nombre VARCHAR(35) NOT NULL,
    descripcion VARCHAR(250),
    PRIMARY KEY (id_cita , id_contacto),
    
    CONSTRAINT fkcita_detalles FOREIGN KEY(id_cita)
        REFERENCES cita(id_cita)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fkcontacto_detalles FOREIGN KEY(id_contacto)
        REFERENCES contacto(id_contacto)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)  ENGINE=INNODB;