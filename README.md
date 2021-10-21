
## Correr proyecto:

- Deberas clonarte este repositorio
- Parado en la raiz del proyecto, ejecutar `docker-compose.yml`
- Listo, el proyecto ya esta corriendo en http://localhost:8000/

## Endpoints:
- Crear una tarea
  - http://localhost:8000/api/task/ 
  - METHOD = POST
  -     data = {
              "title":"Titulo",
              "description":"Descripcion"
              "status":0
              }

- Eliminar una tarea
  - METHOD = DELETE
  - http://localhost:8000/api/task/<id> 
- Marcar tareas como completadas
  - METHOD = PUT
  - http://localhost:8000/api/task/<id> 
 -     data = {
              "status":0
              }

- Poder ver una lista de todas las tareas existentes
  -  METHOD = GET
  -  http://localhost:8000/api/task/
  -  
- Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma
  -  METHOD = GET
  -  http://localhost:8000/api/task?title=titulo&date=2021-10-11
