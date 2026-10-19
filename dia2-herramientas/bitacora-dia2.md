# Bitácora · Día 2 · Herramientas de desarrollo

- **Coder: Laura Vargas Lenis**
- **Fecha: 15/10/2026**
- **TL: Johan**

---

## 1. Mi entorno de desarrollo (Etapa 1)

- Versión de Ubuntu: Ubuntu 26.04.1 LTS
- Versión de Python: Python 3.14.4
- ¿Dónde está instalado Python? (resultado de `which python3`): /usr/bin/python3
- Con mis palabras, la diferencia entre un compilador y un intérprete es: El compilador traduce todo y entrega. El Intérprete solo lo traduce línea por línea
- ¿Qué pasó con la línea 4 de `hola.py` y por qué?: No se ejecutó. Porque hubo un error en la línea 3, se le pidió que imprimiera la variable mensaje_oculto pero nunca fue creada dicha variable

| Herramienta | ¿Qué es? (sistema operativo, editor, intérprete, compilador o navegador) |
|---|---|
| Ubuntu | SO|
| VS Code |Editor |
| Python |Intérprete |
| Chrome |Navegador |
| gcc |Compilador |

## 2. Reinstalación de VS Code (Etapa 2)

- ¿Cómo estaba instalado VS Code? (snap, .deb o no estaba): Estaba instalado como snap
- Comando que usé para desinstalarlo: sudo snap remove code
- Comando que usé para instalarlo: sudo apt install ./code_*.deb
- ¿Por qué es importante instalar desde la fuente oficial?: Porque desde otros portales puede contener software malicioso
- ¿Qué pasó con mi configuración al desinstalar? ¿Dónde vive?: Vive en /usr/bin/code y se instaló como un paquete .dep

## 3. Perfiles y extensiones (Etapa 3)

- Con mis palabras, un perfil de VS Code es: Es una forma de guardar diferentes configuraciones de acuerdo con el gusto y/o necesidad del coder
- ¿Qué cambia en el Explorador entre un perfil y otro?: De acuerdo con las extensiones y/o configuraciones que se tenga, cambian los 
- ¿Por qué VS Code pregunta si confío en el publicador de una extensión?: Porque las extensiones tienen los mismos permisos que el VS Code

## 4. Duelo de perfiles (Etapa 4)

| Prueba | Perfil2-Basico | Perfil1-Pro |
|---|---|---|
| 1. Auto guardado |No | Sí|
| 2. Auto Rename Tag |No |Cuando se cambia <h1> a <h2> inmediatamente cambia el final |
| 3. Error Lens |Solo línea roja |Da guías de lo que se espera que vaya, no solo muestra el subrayado rojo |
| 4. Íconos |Más complejo la rápoida detección de los archivos | |
| 5. Guías de indentación |Solo veo una al inicio | |
| 6. Extensiones corriendo |Las básicas, con pocos ms de activación |Tiene muchas más extensiones con tiempos de activación hasta 215 ms |

**Reflexión**

1. ¿Noté diferencias en la experiencia de trabajo entre los dos perfiles? ¿Cuáles?
   -El pro fácilita más el entendimiento del código y ayuda a reducir errores
2. ¿Qué ventajas tiene usar múltiples perfiles en VS Code?
   -Se pueden adecuar perfiles de acuerdo con las necesidades de los diferentes proyectos
3. ¿Cómo influyen las extensiones en la productividad y en el rendimiento del editor?
   -Pueden ahorrar tiempo al escribir las terminaciones del código automáticamente, así mismo reducen los errores de syntax, se ve más agradable visualmente. En cuanto al Auto Rename, considero que si VS Code tiene esta opción no haría falta instalar la extensión y esto ayudaría a reducir la carga
4. ¿Cuándo sería útil usar perfiles distintos en un entorno profesional? (dos ejemplos)
   -Cuando se tengan proyectos grandes, puesto que se facilitaría la compresión del código y permiten detectar errores rápidamente
   -Al tener perfiles por lo necesario se reduce la carga de extensiones innecesarias, mejorando así el rendimiento

## 5. Inspección y modificación (Etapa 5)

- Página que usé: https://es.wikipedia.org/wiki/Medell%C3%ADn 
- Cinco etiquetas que encontré y para qué sirven:
  1.<html> Se selecciona toda la página, por lo que esta etiqueta contiene todo el documento HTML
  2.<header> Es donde se encuentran los encabezados
  3.<div> agrupa textos o imagenes, o el conjunto de ambas
  4.<figure> contiene imágenes
  5.<span> identifica fragmentos del texto y establece estilos
- ¿Qué pasó con mis cambios al recargar y por qué?: Los cambios fueron eliminados, porque el código modificado no se encuentra cargado al dominio de la página
- Con mis palabras, el DOM es: un archivo de la página en donde se pueden hacer pruebas sin dañar el contenido cargado al público

## 6. La consola (Etapa 6)

| Operación | Mi predicción | Resultado real |
|---|---|---|
| `2 + 3` | 5| 5|
| `10 - 4 * 2` |2 | 2|
| `(10 - 4) * 2` |12 |12 |
| `10 / 4` |2.5 |2.5 |
| `10 % 3` | |1 |
| `2 ** 8` |256 |256 |
| `120000 * 0.19` |22800 |22800 |
| `365 * 24` |8760 |8760 |

- ¿Por qué `0.1 + 0.2` no da exactamente `0.3`?: Porque los computadores guardan números decimales en binario y algunos números no se pueden representar de forma exacta
- Errores o advertencias que encontré en la página (o "ninguno"):
Advertencia Source map error: No sources are declared in this source map.
Resource URL: https://es.wikipedia.org/w/load.php?lang=es&modules=mmv.codex&skin=vector-2022&version=156kh
Source Map URL: https://es.wikipedia.org/w/load.php?lang=es&modules=mmv.codex&skin=vector-2022&sourcemap=1&version=156kh 
- Diferencia entre un error y una advertencia: Una advertencia sugiere que hay algo a revisar, sin embargo, la página sigue funcionando. Un error es que algo no anduvo bien, ya sea una instrucción mal escrita o similar, esto si impide el correcto funcionamiento de el apartado de la página que presenta error

## 7. La red / Network (Etapa 7)

| Imagen | Formato | Tamaño | Tiempo | Código de estado |
|---|---|---|---|---|
|Panorámica Medellín |jpeg |19.29 kB |88 ms | 200|
|Edificio Bancolombia |png |82.89 kB |91 ms |200 |
|Antigua alcaldía |jpeg |20.41 kB |92 ms |200 |

| Experimento | Solicitudes | Transferido | Load |
|---|---|---|---|
| A. Sin caché |61 |794.47 kB |535 ms |
| B. Con caché |15 |220.01 kB |292 ms |
| C. Red lenta |17 |261.47 kB|1.31 s |

- Archivo más pesado de la página y su tipo: tipo html y pesa 1.34 MB
- ¿Por qué la página cargó más rápido con caché?: Porque ya guarda los archivos descargados al iniciar la página por lo que no tiene que volver a hacerlo
- ¿Por qué un desarrollador querría probar con una red lenta?: Para ver cómo correría la página con una red más limitada
- ¿Qué haría para que una imagen pesada cargue más rápido?: guardar el caché

## 8. Dispositivos móviles (Etapa 8)

| Ancho (px) | Dispositivo | ¿Cambia el menú? | ¿Imágenes bien? | ¿Scroll horizontal? | Observación |
|---|---|---|---|---|---|
| 320 |Responsive |No |Imágenes bien |No scroll horizontal texto e imágenes se adecuan al ancho de página | |
| 375 |Responsive |No |Imágenes bien |No scroll horizontal texto e imágenes se adecuan al ancho de página | |
| 768 |Responsive |No |Imágenes bien |No scroll horizontal texto e imágenes se adecuan al ancho de página | |
| 1024 |Responsive |No |Imágenes bien |Sí scroll horizontal texto e imágenes se adecuan al ancho de página | |
| 1440 |Responsive |No |Imágenes bien |Sí scroll horizontal texto e imágenes se adecuan al ancho de página | |

- ¿Por qué es importante probar varias resoluciones antes de entregar un proyecto?: Para asegurar que desde los diferentes dispositivos y sus rotaciones se pueda tener acceso a todos los paneles de información

## 9. Laboratorio de errores (Etapa 9)

| # | Tipo | ¿Dónde lo detecté? | Mensaje o síntoma | Causa | Solución aplicada |
|---|---|---|---|---|---|
| 1 |Failed to load resource |styles.css |the server responded with a status of 404|File not found |la ruta estaba errónea iba a la carpeta css, pero la carpeta se llama CSS|
| 2 |Uncaught |app.js |Cannot read properties of null (reading 'addEventListener') | |En la línea 13 del app.js se identificaba el botón como btn-saludar, pero en el html estaba boton-saludar |
| 3 |Uncaught ReferenceError | app.js:17:37|nombreCodr is not defined
    at HTMLButtonElement |Variable no definida |En la línea 17 estaba escrito nombreCodr en lugar de nombreCoder |
| 4 |Failed to load resource |styles.css |the server responded with a status of 404|File not found |la ruta estaba errónea iba a la carpeta css, pero la carpeta se llama CSS|

- Uno de los errores, descrito con detalle, y cómo lo resolví:
Error: Uncaught Cannot read properties of null (reading 'addEventListener')
El error estaba en la línea 13 del archivo app.js, en esta línea la variable del botón era 'btn-saludar'. Sin embargo, en el archivo intex.html cuando se llamaba al botón lo hacía con 'boton-saludar' por lo que no encontraba nada llamado así
- ¿Qué vi al pausar con el breakpoint?:
El paso a paso de lo que pasa en cada orden del código
- ¿Qué pasó al cambiar `visitas` por 99 y al borrarlo?:
Al colocar 99 sale 100 y al borrarlo sale 1
- ¿Para qué usan el localStorage las páginas reales? ¿Qué NO debería guardar ahí?: No se deben guardar contraseñas ni datos sensibles, puesto que cualquier usuario 
- Ancho exacto en el que se apilan las tarjetas y regla de CSS responsable:
- ¿Por qué no basta con mirar solo la consola para encontrar errores?:

## 10. Comparación con Firefox (Etapa 10)

| Herramienta | Chrome: nombre y atajo | Firefox: nombre y atajo | Diferencia que noté |
|---|---|---|---|
| Inspeccionar HTML y CSS | | | |
| Consola | | | |
| Red | | | |
| Simulación de dispositivos | | | |
| Almacenamiento local | | | |
| Mensaje del error que reintroduje | | | |

- Una característica de Firefox interesante o diferente a Chrome (qué es, para qué sirve y cómo la probé):

## 11. Reflexión final (Etapa 11)

- La herramienta que más voy a usar y por qué:
- Lo más difícil del día y cómo lo resolví:
- Las DevTools explicadas para alguien que no programa (3 líneas):