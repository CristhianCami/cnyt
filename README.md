# CNYT Lab 01

En el laboratorio 01 se realizó la libreria "calculadora", donde se implementaron algunas operaciones básicas de los números complejos,
entre las cuales tenemos:
  
  * _Suma_
  
  * _Resta_
  
  * _Multiplicación_
  
  * _División_
  
  * _Módulo_
  
  * _Conjugado_
  
  * _Conversión entre representación polar y cartesiano_
  
  * _Fase de un número complejo_

## Suma :gem:

```
k = (r[0] + t[0], r[1] + t[1])
```

## Resta :gem:

```
k = (r[0] - t[0], r[1] - t[1])
```

## Multiplicación :gem:

```
k = (r[0]*t[0] - r[1]*t[1],r[0]*t[1] + r[1]*t[0])
```

## División :gem:

```
k = ((r[0]*t[0] + r[1]*t[1])/(t[0]**2+t[1]**2),(r[1]*t[0] - r[0]*t[1])/(t[0]**2+t[1]**2))
```

*Para seguir revisando __cada__ una de las funciones de la calculadora, ingrese al* código fuente [Código fuente](https://github.com/CristhianCami/cnyt/blob/master/numerosComplejos.py).:+1::+1:

## ¿Cómo utilizar la calculadora?

  * Descargar el contenido en este repositorio.
  * Abrir el archivo calculadoraComplejos.py
  * Ahora se puede realizar cualquiera de las operaciones descritas anteriormente, como ejemplo:
    ```
    suma((2,3),(5,-1))
    ```

### __Este programa puede ser usado por cualquier usuario__
