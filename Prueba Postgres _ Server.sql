drop if exists Alumnos;
create table Alumnos(
IDAlumno	int not null,
Nombre_apellido varchar(100),
Carrera varchar(5) not null,
Cohorte	int not null,
Mail varchar(100),
primary key (IDAlumno)
);

insert into Alumnos values(0,'Emmanuel Corral','DS','05','emmanuel.ac@hotmail.com');
insert into Alumnos values(1,'Melina Griffo','DS','05','meli.griffo@hotmail.com');
insert into Alumnos values(2,'Federico Olivieri','DS','03','fede.olivieri@hotmail.com');

select * from alumnos order by IDAlumno;