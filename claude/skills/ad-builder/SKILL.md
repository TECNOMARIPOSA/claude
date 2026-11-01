---
name: ad-builder
description: Sistema de producción y testeo de creativos para Meta Ads — estáticos y UGC con Higgsfield, nomenclatura trazable, historial de resultados alimentado desde UTMify y reglas de compliance por nicho. Usar cuando el usuario pida creativos, ads, ángulos, hooks, variaciones para testear, reels UGC, análisis de competencia, o cuando pregunte qué creativo funcionó o qué producir hoy.
---

# Ad Builder — producción y trazabilidad de creativos

> Sistema de producción **con memoria**. La metodología de testeo vive en
> `WIKI/testeo-de-creativos.md` — este documento **no la reemplaza, la ejecuta**.
> Lo que agrega es lo único que hoy falta: saber **qué ángulo ganó**, no solo qué anuncio ganó.

---

## 0. El problema que resuelve

Los anuncios en Meta hoy se llaman `AD - 1`, `AD - 7`, `10/8 - 10`. UTMify devuelve por anuncio
spend, CPA, ROAS, profit, hook rate y retención — data de primera contra un nombre que **no dice
nada**. Cuando algo gana, se sabe que ganó "el AD - 7". No se sabe con qué ángulo, qué nivel de
conciencia ni qué formato ganó, y a los 4 días ese anuncio está apagado y el aprendizaje se perdió.

Con varios dashboards, varios idiomas y ~10 creativos por día, eso es la diferencia entre acumular criterio
y repetir el mismo test cada semana.

Tres piezas, en orden de importancia:

| Pieza | Qué hace |
|---|---|
| `references/historial-resultados.md` | **El corazón.** Una fila por creativo: ángulo, nivel de conciencia, formato, hook, números reales de UTMify, veredicto. Se lee ANTES de producir y se escribe DESPUÉS de cada lectura de resultados. |
| `references/nomenclatura.md` | El ID que cruza el archivo con el anuncio en Meta y con la fila del historial. **Sin esto el historial no se puede llenar solo.** |
| Producción | Estáticos y UGC con Higgsfield (`references/motor-higgsfield.md`) |

**Si se copia una sola cosa de acá, que sea el historial.**

---

## 1. Antes de producir — obligatorio

1. **Leer el historial del producto** en `references/historial-resultados.md`. Si el producto no
   está, crear su bloque.
2. **Leer los temas de la WIKI que apliquen.** Como mínimo `testeo-de-creativos`,
   `angulos-publicitarios` y `renovacion-de-creativos`. La metodología está ahí y puede haber
   cambiado desde la última sesión.
3. **Abrir el producto real** — el PDF, la landing, el checkout. No escribir copy desde el histórico
   de creativos.
4. **Chequear la economía** (§5). Si la ecuación no cierra, decirlo antes de producir, no después.

Si falta alguna de las cuatro, decirlo y pedirla. No producir "mientras tanto".

---

## 2. Dónde va todo

```
SegundoCerebro/
├── .claude/skills/ad-builder/
│   ├── SKILL.md                        ← este archivo
│   └── references/
│       ├── historial-resultados.md     ← el registro vivo
│       ├── nomenclatura.md             ← IDs, ángulos, formatos
│       ├── utmify-mapa.md              ← tus dashboards + cómo leer los números
│       └── motor-higgsfield.md         ← modelos, costos, workflows
└── CREATIVOS/
    ├── entregas/<YYYY-MM-DD>/<dashboard>-<producto-slug>/
    └── swipe/                          ← ads de competencia
```

`RAW/` y `WIKI/` **no se tocan desde acá**. Las reglas del bibliotecario (`CLAUDE.md`) siguen
vigentes: `RAW/` es de solo lectura y `WIKI/` se escribe solo al procesar RAW.

Una carpeta por tanda y por dashboard. Nunca todo junto: con 10 creativos diarios en varios dashboards,
una carpeta plana se vuelve inmirable en una semana.

---

## 3. Nomenclatura — la pieza que hace que el historial se llene solo

Detalle completo en `references/nomenclatura.md`. El resumen:

```
ID = <ANG>-N<n>_<FMT>_H<nn>_v<N>
```

Ejemplo: `ECO-N2_UGC_H03_v1` — ángulo económico, nivel de conciencia 2, formato UGC talking-head,
hook 03, versión 1.

**El mismo ID va en tres lugares y tiene que coincidir:**

| Dónde | Formato |
|---|---|
| Nombre del archivo | `<YYMMDD>_<producto-slug>_<ID>_<ratio>.png` / `.mp4` |
| **Nombre del anuncio en Meta** | `<DDMM> <ID>` — ej: `1108 ECO-N2_UGC_H03_v1` |
| Fila del historial | columna `ID` |

⚠️ **El nombre del anuncio en Meta es el eslabón crítico.** Es el campo `name` que devuelve UTMify.
Si el anuncio se sube como `AD - 7`, esa tanda queda fuera del historial para siempre: los números
existen pero no se pueden atribuir a nada. Al entregar una tanda, **entregar también la lista de
nombres de anuncio para copiar y pegar**, en el orden de los archivos.

Los parámetros de URL de UTMify van igual en todos los anuncios, sin excepción
(`WIKI/tracking-y-atribucion.md`).

---

## 4. Testeo — la metodología es la de la WIKI

No se inventa criterio acá. Lo que sigue son solo las reglas que tocan **producción**:

### 4.1 Qué produce cada capa

| Capa | Volumen | Qué se produce |
|---|---|---|
| **Pre-testeo** (oferta ya estable) | 30/día: 20 imágenes + 10 videos, 1,50–2 USD c/u | Volumen alto, ángulos y formatos variados. Es un **filtro**, no un experimento |
| **Testeo** (producto nuevo) | 5–10 anuncios ABO, presupuesto según ticket | Cada creativo un ángulo distinto |
| **CBO post-Andrómeda** | 3 conjuntos = **3 conceptos** distintos, el tercero suele ser venta directa | 6 conceptos/día, 4 campañas (2 originales + 2 copias) |

**Nunca mezclar imágenes y video en la misma CBO.** O todo imágenes, o todo video.

### 4.2 Una variable por comparación (no por tanda)

La regla del sistema original —"una sola variable por tanda"— **no se aplica tal cual** acá, porque
el pre-testeo es volumen y diversidad por diseño. Se aplica al **nivel de la comparación**:

> **Look/formato nuevo → sobre un ángulo YA validado.**
> **Ángulo nuevo → con el look/formato YA validado.**

Si se estrenan los dos a la vez y el CPM se dispara, no hay forma de saber cuál falló. Un formato
nuevo se prueba con 1–2 piezas contra el ganador, nunca con una tanda entera.

Cuando el usuario pide volumen **y** un look nuevo a la vez, se reconcilia así: **todas las piezas en
el look nuevo, todas con ángulos ya validados.** Una variable cambia y hay volumen.

### 4.3 Variación real vs variación cosmética

Una variación cuenta si cambia hook, mecanismo, ángulo, objeción, emoción, nivel de conciencia o
forma de presentar el producto. **Cambiar dos palabras no es una variación** — y Meta lo castiga con
CPM más alto. Rotar también el **formato** y el **ratio** (4:5 · 1:1 · 9:16 · 16:9): es una dimensión
que Andrómeda premia y que casi nadie toca.

### 4.4 Muestra antes del lote

Para una línea creativa nueva: **1 pieza de muestra → mostrarla → esperar OK → recién ahí el lote.**
A 2 créditos la imagen el costo no es el problema; el problema es entregar 20 piezas con un defecto
sistemático que se veía en la primera.

### 4.5 Una sola versión viva por ID

Al cerrar la tanda, cada ID tiene **exactamente un archivo**. Los descartes se borran **después de
abrirlos y confirmar cuál es cuál**. Si conviven `v1` y `v2` del mismo ID, se sube el equivocado.
Las carpetas de fechas anteriores no se tocan: son historial.

---

## 5. Economía — chequear antes de producir

Los números de referencia son los de `WIKI/testeo-de-creativos.md` y `WIKI/metricas-y-kpis.md`:

- **CPA medio = ticket ÷ 2.** Gobierna presupuesto y corte.
- **CPA break-even = después de comisiones.** Un producto de 15 USD deja ~13.
- **Requisito previo: comprate > 2,5%.** Si la landing no llega, el trabajo no es creativo.

⚠️ **El AOV se lee de UTMify, no del precio de lista.** El AOV real incluye order bumps, upsells y
backend — por ejemplo, un ticket de 16,99 puede dar un AOV de 22,20. Usar el precio del front como AOV
subestima el margen y hace matar creativos rentables. UTMify da el número real: `revenue ÷
approvedOrdersCount` del dashboard, o el campo `arpu` a nivel anuncio.

Si el usuario reporta **caída brusca de tráfico o de ventas**, la hipótesis por defecto es **fatiga
creativa o problema de entrega/tracking**, no un problema de ángulo. Lo que necesita es munición
nueva y barata de rotar — y verificar el pixel antes de concluir que el creativo falló
(`WIKI/tracking-y-atribucion.md` tiene el checklist).

---

## 6. Historial de resultados — cómo se llena

Archivo: `references/historial-resultados.md`. Mapa de dashboards y consultas:
`references/utmify-mapa.md`.

**Se lee antes de producir. Se escribe apenas hay números, en el mismo turno, sin esperar a que lo
pidan.**

### 6.1 El ciclo

1. Consultar UTMify a **nivel anuncio** (`get_meta_ad_objects`, `level: "ad"`) del dashboard y el
   rango de fechas de la tanda.
2. Parsear el ID desde el campo `name` del anuncio.
3. Escribir/actualizar la fila con los números reales: spend, ventas aprobadas, CPA, ROAS, profit,
   CTR, y en video `hook` (hook rate) y `retention`.
4. Aplicar el veredicto (§6.2).
5. Abajo de la tabla, **en prosa, qué se aprendió**. Eso vale más que la tabla.

Anuncios cuyo `name` no tenga ID: se listan aparte como **"sin atribuir"**. No se inventa a qué
ángulo pertenecían.

### 6.2 Veredictos

| | Cuándo | Qué se hace después |
|---|---|---|
| ✅ **Validado** | ≥5 conversiones a buen CPA (10+ para Pocket/CostCap) | Pasa a estructuras de escala. Sacar variaciones **de ese ángulo** |
| 🟢 **Vende** | Vendió con CPA < break-even, todavía sin 5 conversiones | Dejar correr, evaluar a diario |
| ⏳ **En testeo** | No llegó al CPA medio todavía | No tocar |
| ❌ **Descartar** | Llegó al CPA medio / break-even sin una sola venta | Se mata el **anuncio** |
| 🔁 **Fatigado** | Fue ganador y cayó: CPC ↑, CPM ↑, CTR ↓ | **Renovar el hook, no matar el ángulo.** El cuerpo está validado (`WIKI/renovacion-de-creativos.md`) |
| ⚠️ **Inconcluso** | Se apagó antes de llegar al CPA medio, o corrió en pre-testeo a 1,50–2 USD sin venta | **No es ❌.** El ángulo queda disponible |

### 6.3 La regla que más plata cuesta olvidar

> ❌ mata el **anuncio**. Nunca mata el **ángulo**.

En pre-testeo cada creativo recibe 1,50–2 USD. Con eso Meta entrega ~150 impresiones calificadas:
alcanza para filtrar, **no alcanza para concluir sobre un ángulo**. Marcar ese ángulo como perdedor
lo bloquea para siempre por una muestra de 2 dólares.

**Un ángulo solo se marca ❌ cuando acumuló gasto ≥ CPA break-even repartido en ≥3 creativos
distintos de ese mismo ángulo, sin una sola venta.** Hasta ahí es ⚠️ Inconcluso.

Y el corolario: con una tanda ⚠️ Inconclusa la conclusión correcta es **"no sé"**, no una
recomendación estratégica. Una muestra que no alcanza para juzgar un creativo tampoco alcanza para
juzgar la oferta ni el modelo de negocio.

---

## 7. Investigación de competencia

Las plataformas espía que usa (AdsPro, Minea, GetCook, vía Scalebus) están en
`WIKI/stack-de-herramientas.md`. La Biblioteca de Anuncios de Meta es gratis y no pide login:

```
https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=<query>&search_type=keyword_unordered&media_type=all
```

Para navegarla desde acá, usar la skill **claude-in-chrome** (abre el Chrome real del usuario, con
sus sesiones). No hace falta pegar JavaScript a mano.

Cómo hacerlo bien:

1. **NO filtrar por `media_type=image`.** La mayor parte del mercado corre video y carrusel.
2. **Los ángulos viven en el COPY, no en la imagen.** Extraer el texto de cada ad.
3. **Señales de que algo escala:** muchos ads activos del mismo anunciante · antigüedad (8+ meses
   corriendo = está funcionando) · "This ad has multiple versions".
4. Buscar por **frases de dolor que usa el cliente**, no por nombre de categoría.
5. Cubrir competencia **directa** e **indirecta** (mismo trabajo, otro formato).
6. En sus nichos, cruzar **mercados**: lo que escala en EN suele no estar corriendo todavía en ES/IT
   /DE. Es la vía más barata de ángulos nuevos (`WIKI/internacionalizacion.md`).

Lo que se encuentra va a `CREATIVOS/swipe/`.

⚠️ **Nunca usar material rippeado de ads ajenos como b-roll** — copyright y rechazo de Meta. Mirarlos
para aprender, no para reusar.

---

## 8. Producción de estáticos

Motor, modelos y costos: `references/motor-higgsfield.md`. Reglas que son de método, no de motor:

### 8.1 Densidad — por qué un creativo "correcto" se ve vacío

Copiar la *estructura* de un ganador no alcanza. Lo que falta casi siempre es **riqueza**:

| Hacer | En vez de |
|---|---|
| Objetos ilustrados a todo color, con sombreado y textura, **con contenido real legible adentro** (una página del producto con su texto de verdad) | glifos planos de un color — se ven como icon-set genérico |
| **Dos líneas completas** de descripción por ítem | una línea corta que deja aire muerto |
| Composición **borde a borde**, sujeto grande saliéndose del cuadro | márgenes generosos y todo flotando |
| Patrón de fondo tenue llenando huecos | zonas de blanco liso |

El recurso más potente: **que los objetos muestren contenido real del producto**. Una página con su
texto verdadero vende sin una línea de copy — el prospecto ve exactamente lo que va a recibir. Es
además el formato más barato de refrescar: se cambia qué páginas se muestran y listo.

Y la regla de la WIKI que manda sobre todo lo demás: **NO FLAT COVERS**. Estética premium,
editorial, realista, con profundidad (`WIKI/imagenes-y-mockups.md`).

### 8.2 Reglas de prompt para texto en imagen

| Regla | Fórmula |
|---|---|
| Toda lista va literal y cerrada | `exactly these seven items in this order and no others: "…"` |
| Los apóstrofos hay que pedirlos | escribir el texto con apóstrofo **y** agregar `The apostrophe in X must be clearly visible.` |
| Decir el ENFOQUE además del texto | `Every description must be about CROCHET, never about knitting.` |
| Bloquear texto inventado | `No extra invented text or paragraphs anywhere.` |
| Estructuras contadas se colapsan | `Count them carefully: there must be seven, numbered 1 to 7, with NO number skipped` |
| Deletrear la palabra que falla | `The word on item 4 is "FIND", spelled F-I-N-D.` |
| Si colapsa en ruido | agregar `Clean rendering, sharp readable type.` |

En mercados no ingleses el modelo falla más con tildes, ñ y caracteres cirílicos/árabes: deletrear
la palabra crítica y revisarla explícitamente al mirar la imagen.

### 8.3 Revisión visual — obligatoria

**Que el job vuelva `completed` no significa que la imagen sirva. Hay que ABRIR y MIRAR cada una.**

El flujo es: descargar el resultado a `CREATIVOS/entregas/…` y leer el archivo con la herramienta de
lectura de imágenes. Dos fallas que solo se ven mirando:

1. **Colapso** — a mayor densidad pedida, más chance de ruido: manchas y letras rotas. La API lo
   reporta como éxito.
2. **Deriva de contenido** — el layout sale perfecto pero el texto dice otra cosa, o dice algo que el
   producto no hace.

Verificar además, uno por uno: números, cantidades ("+800 planos", "15.000 planos"), listas y
cualquier dato que venga del producto. **Nunca imprimir una cifra que no esté confirmada en el
producto real.**

---

## 9. Producción de UGC y video

Motor y workflows: `references/motor-higgsfield.md`.

### 9.1 Reglas fijas (de `WIKI/ugc-y-video-generativo.md`, no negociables)

- **9:16 vertical** · cámara handheld, natural, documental
- **Sin subtítulos** — se agregan después en CapCut
- **Sin texto sobreimpreso**, sin música salvo que la pida
- Voz natural, español latino o argentino según mercado; inglés en mercados EN
- Si pidió que el personaje **sostenga** el producto, lo sostiene **mientras habla**
- Avatares recurrentes: Diego · Cami (29, runner) · Mateo (28) · Delfi (30) · Susana (56, maestra
  jubilada). **No son personas del equipo.**

Cuando un workflow de Higgsfield quiera quemar captions o "Step N" en el frame: **desactivarlo**.

### 9.2 Guion

- **HOOK = la solución o la promesa en los primeros 3 segundos.** Nunca un buildup de dolor: pierde
  al espectador. El dolor entra después, corto, como validación.
- Testimonio UGC: **14 segundos máximo, 35–40 palabras.** Hook (0–3s) / beneficio (4–10s) / cierre
  (11–14s).
- Venta directa larga: 2:00–3:00 min. Contar palabras antes de mandar a voz (~2,9 palabras/segundo).
- Marcar los b-rolls en el guion: `[BROLL: <clip> @ ~Xs]`, uno cada 10–15 s.

> ⚠️ **ABRIR EL PRODUCTO ANTES DE ESCRIBIR EL GUION.** Un guion escrito desde el histórico de
> creativos termina afirmando cosas que el producto no hace. Un estático flojo se regenera por 2
> créditos; un video con un claim falso cuesta créditos, render y un empalme para arreglarlo — y si
> llegó a correr, es riesgo de cuenta.

### 9.3 La regla modular — la que ahorra la plata

> **Un cuerpo validado + N hooks cortos.** El cuerpo se genera una vez; las variantes son solo el
> arranque.

Cuando un video vende, hacer **20, 30, 40 variaciones de hook sobre el MISMO cuerpo** antes de gastar
en guiones nuevos. No 2 o 3 — ese es el error típico. Las cuatro formas de renovar (hooks del mismo
ángulo, cambio de formato de hook, hooks de virales del nicho, hook delante del hook) están en
`WIKI/renovacion-de-creativos.md`.

### 9.4 B-rolls

En orden de rendimiento: **detalle de página real del producto** · **reuso de los propios estáticos**
· capturas de la landing · stock. Mostrar **el elemento del que habla la voz**, no la página entera:
a 3 segundos en un celular ninguna página completa se lee. Recortar a 9:16 **alineado a la
izquierda**, no centrado — centrado corta las frases justo por donde empiezan.

⚠️ Recortar cualquier barra de precio si el usuario pidió no mostrarlo.

### 9.5 Zonas seguras de Meta

Arriba ~12%, abajo ~22%, derecha ~12%. Nada importante ahí. Si se pone un titular sobre el video, va
**sobre el torso (~57% de altura)**: arriba está la zona insegura y a la altura de la cara le tapa la
boca al avatar, que en un talking-head es peor que taparle los ojos.

---

## 10. Compliance — el método, no la lista

Cada nicho tiene sus reglas. El método para encontrarlas se repite:

1. **Identificar quién compra.** Si una parte grande de los compradores pertenece a un grupo, **ese
   grupo no puede ser el villano del ad**. En los productos para docentes, ni las escuelas ni el
   sistema educativo pueden ser el problema.
2. **Encuadrar el hueco como una etapa, no como la falla de alguien.** Vende igual y mide mejor: la
   pieza reescrita por compliance suele ser la que gana.
3. ⚠️ **Una estructura de dos columnas crea un perdedor aunque el copy no lo diga.** Antes de usarla,
   preguntarse quién queda en la columna perdedora. Si es el comprador, reencuadrar: **dos
   instrumentos distintos, ambos útiles**, sin rojo ni cruces de un lado.
4. **Nichos de riesgo de cuenta en esta operación** — marcar el creativo como riesgo y correrlo
   aislado, nunca en la cuenta que sostiene la facturación:
   - **Salud y cuerpo**: protocolos de inflamación, dietas, "Ozempic natural", estética. Sin promesa
     médica, sin antes/después de cuerpo, sin cifras de pérdida de peso.
   - **Dinero**: "ganá X al mes", ingresos con crochet/manualidades. Los claims de ingresos son la
     causa más común de rechazo y de restricción de cuenta.
   - **Religión / espiritualidad**: hay precedente registrado de **recategorización de pixel** que
     tumbó las ventas. Si se corre, con dominio y pixel dedicados
     (`WIKI/tracking-y-atribucion.md`, `WIKI/contingencia-de-cuentas.md`).
5. Que un competidor tenga algo corriendo prueba **tolerancia hasta hoy, no que esté dentro de
   política**. La enforcement es asimétrica por mercado e idioma — y más si corrés varios idiomas.
6. **Prueba social: solo citas reales.** Nunca redactar un testimonio como si fuera de un cliente.
7. Sin precio ni claims cuantificados si el usuario pidió no mostrarlos: ni en copy, ni en overlay, ni
   en capturas de landing con la barra de precio.

---

## 11. Checklist antes de cerrar una tanda

- [ ] Leí el historial del producto antes de producir
- [ ] Leí los temas de la WIKI que aplican
- [ ] Abrí el producto real y verifiqué que nada del copy sea falso
- [ ] La comparación cambia **una** variable (look nuevo con ángulo validado, o al revés)
- [ ] **Abrí y miré cada imagen/video** — no confié en el `completed` del job
- [ ] Verifiqué números, listas y datos uno por uno
- [ ] Compliance: nadie de la audiencia queda como villano; nicho de riesgo marcado
- [ ] Archivos con la nomenclatura completa, en `CREATIVOS/entregas/<fecha>/<dashboard>-<producto>/`
- [ ] **Entregué la lista de nombres de anuncio para copiar y pegar en Meta**
- [ ] Una sola versión viva por ID; descartes borrados
- [ ] Historial actualizado, con lo pendiente y los defectos conocidos
- [ ] Le dije el costo real en créditos y en qué carpeta quedó todo

---

## 12. Los errores más caros, resumidos

1. **Subir el anuncio sin la nomenclatura** → los números existen en UTMify y no se pueden atribuir a
   ningún ángulo. Es el estado actual y el que este sistema viene a cortar.
2. **Marcar ❌ un ángulo por una muestra de pre-testeo** → 2 dólares bloqueando un ángulo para
   siempre. ❌ mata el anuncio, no el ángulo.
3. **Escribir el guion sin abrir el producto** → claims falsos ya generados, y riesgo de cuenta si
   llegan a correr.
4. **Confiar en que el job volvió OK** → imágenes con texto roto o cifras inventadas entregadas como
   buenas.
5. **Cambiar look y ángulo en la misma comparación** → el CPM se dispara y no hay forma de saber cuál
   de los dos falló.
6. **Mezclar imágenes y video en la misma CBO** → contra la regla explícita del método post-Andrómeda.
