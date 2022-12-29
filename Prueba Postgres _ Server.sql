insert into "Alumno" values(0,'Emmanuel','Corral',35,01,True,True,'Argentina','Juegos');
insert into "Alumno" values(1,'Melina','Griffo',28,01,False,True,'Argentina','Charlar');
insert into "Alumno" values(2,'Ronal','Cabrera',27,01,True,False,'Argentina','Juegos');
insert into "Alumno" values(3,'Emmanuel','Fernandez',29,01,False,False,'Uruguay','Código');
insert into "Alumno" values(4,'Luciano','Asencio',31,01,True,False,'Chile','Juegos');
insert into "Alumno" values(5,'Matias','Martínez',26,01,True,True,'Chile','Charlar');
insert into "Alumno" values(6,'Valentín','Fogliatti',37,01,False,True,'Argentina','Juegos');
insert into "Alumno" values(7,'Leonel','Balleis',30,01,False,False,'Argentina','Charlar');
insert into "Alumno" values(8,'Maciela','Ortiz',31,01,True,False,'Argentina','Código');
insert into "Alumno" values(9,'Julio','Postigo',27,01,False,True,'Uruguay','Juegos');
insert into "Alumno" values(10,'Matías','Saez',25,01,False,True,'Chile','Dudas Henry');
insert into "Alumno" values(11,'Nicolás','Mulet',26,01,True,False,'Chile','Juegos');

delete from "Alumno";

insert into "Ta" values(01,'Fede','Olivieri','fede.olivieri@lagorra.com','8811225');

insert into "Sup" values(01,07,05,01,null,'Data');

select * from "Alumno";
select * from "Sup";
select * from "Ta";

select * from alumnos order by IDAlumno;

SELECT ROUND(AVG(edad),0) FROM "Alumno";

SELECT ROUND(AVG(edad),0) FROM Alumno;
