# upperAPI

Esta API fué desarrollada con la simple finalidad de dar solución al ejercicio propuesto por "Reputación digital" para la seleccion de personal.
UpperAPI está desarrollada con el framework fastAPI y utiliza una base de datos sqlite.

## Demo
Si ud quiere probar la demo puede ingresar [aqui](http://kalinka.cultivoiot.com.ar:4040/docs#).

Para la autenticación debera utilizar los siguientes valores:

```
username:demo
password:demo
```
## Despliegue

* Descargar el repositorio


    [https://github.com/lucrohatsch/upperAPI.git](https://github.com/lucrohatsch/upperAPI.git)


* Crear en el directorio src el archivo .env con las siguientes variables
```
USR="usuario"
PSW="contraseña"
```

* Crear la imagen de docker

```
docker build . -t upper-api:1.0
```

* Ejecutar el contenedor
```
ducker container run --name upperAPI -p 4040:4040 upper-api:1.0 
```

* Ingresar al swagger desde el navegador


    [http://127.0.0.1:4040/docs](http://127.0.0.1:4040/docs)


