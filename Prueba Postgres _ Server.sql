drop table Alumnos;
create table Alumnos(
IDAlumno	int not null,
Nombre_apellido varchar(100),
Edad int not null,
País varchar(50) not null,
Carrera varchar(5) not null,
Cohorte	int not null,
Dispositivo_usado varchar(100),
Cam_Mic varchar(50),
Actividad_preferida varchar(100),
primary key (IDAlumno)
);

insert into Alumnos values(0,'Emmanuel Corral',35,'Argentina','DS',05,'Notebook','Ambos','Juegos');
insert into Alumnos values(1,'Melina Griffo',30,'Argentina','DS',05,'Notebook','Mic','Charlar');
insert into Alumnos values(2,'Federico Olivieri',29,'Argentina','DS',03,'Notebook','Ambos','Dar órdenes');
insert into Alumnos values(3,'Emmanuel Jimmy',28,'Uruguay','DS',05,'Celular','Cam','Juegos');
insert into Alumnos values(4,'Lucho Asuncio',30,'Chile','DS',05,'Celular','Mic','Juegos');
insert into Alumnos values(5,'Benja Pastor',27,'Chile','DS',03,'Notebook','Ambos','Charlar');

select * from alumnos order by IDAlumno;