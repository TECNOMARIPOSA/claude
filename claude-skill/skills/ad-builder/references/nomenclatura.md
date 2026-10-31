# Nomenclatura — el ID que cruza archivo ↔ anuncio ↔ historial

El ID es lo único que convierte los números de UTMify en aprendizaje. Sin él, un anuncio ganador es
un número de serie.

---

## 1. El ID

```
<ANG>-N<n>_<FMT>_H<nn>_v<N>
```

| Parte | Qué es | Ejemplo |
|---|---|---|
| `ANG` | Ángulo — 3 letras, tabla §2 | `ECO` |
| `N<n>` | Nivel de conciencia, 1 a 5 — tabla §3 | `N2` |
| `FMT` | Formato — tabla §4 | `UGC` |
| `H<nn>` | Hook, correlativo **dentro del producto** | `H03` |
| `v<N>` | Versión. Nunca se sobrescribe: sube el número | `v1` |

Ejemplo completo: **`ECO-N2_UGC_H03_v1`**

### Variantes de un ganador

Heredan el ID y agregan letra: `ECO-N2_UGC_H03a`, `…H03b`. Así el ID dice de qué desciende sin abrir
el archivo. Si lo que cambia es el hook sobre un cuerpo validado, sube el número de hook y se mantiene
el resto: `ECO-N2_UGC_H07_v1` con nota en el historial de que reusa el cuerpo de `H03`.

---

## 2. Códigos de ángulo

Salen de `WIKI/angulos-publicitarios.md` y de los nichos que corre la operación.

| Código | Ángulo | Ejemplo de entrada |
|---|---|---|
| `ECO` | Económico / ganar dinero con el oficio | "Convertí lo que ya sabés hacer en ingresos" |
| `VEL` | Velocidad / atajo / tiempo | "En 14 días", "sin años de práctica" |
| `SIM` | Simplicidad / sin experiencia previa | "Aunque nunca hayas agarrado una aguja" |
| `AUT` | Autoridad / profesional | "El método que usan los que cobran caro" |
| `TRA` | Transformación | Antes → después observable |
| `CUL` | Anti-culpa | Saca la culpa de encima del comprador |
| `IDE` | Identidad / pertenencia | "Si sos de las que…" |
| `PSO` | Prueba social | Cantidad de compradores, resultados reales |
| `CUR` | Curiosidad / secreto / revelación | "Lo que nadie te cuenta sobre…" |
| `MIE` | Miedo / riesgo de no actuar | Costo de seguir igual |
| `URG` | Urgencia / escasez | Últimos cupos, cierre |
| `PSL` | Problema–solución directo | Nombra el problema y da el mecanismo |
| `VIL` | Villano oculto | ⚠️ Revisar compliance: el villano no puede ser el comprador |
| `DIR` | Venta directa / oferta | Precio, garantía, bonus. El 3er concepto típico de la CBO |

Un ángulo nuevo que no entre en la tabla **se agrega acá con su código** antes de producir, no
después.

---

## 3. Nivel de conciencia

| Código | Nivel | Qué hace el anuncio |
|---|---|---|
| `N1` | Inconsciente del problema | Despertar conciencia: sorpresa, curiosidad |
| `N2` | Consciente del problema | Nombrar el problema con precisión |
| `N3` | Consciente de la solución | Presentar el mecanismo |
| `N4` | Consciente del producto | Diferenciar |
| `N5` | Más consciente | Oferta y urgencia |

Es la dimensión que menos se testea y la que más cambia el CPA. Dos creativos del mismo ángulo en
niveles distintos **no son la misma variación**.

---

## 4. Códigos de formato

| Código | Formato |
|---|---|
| `IMG` | Estático / scroll stopper |
| `CAR` | Carrusel |
| `MOS` | Mosaico de producto / grilla de páginas reales |
| `SCR` | Captura de pantalla (chat, comentarios, resultados) |
| `EDU` | Educacional / infografía argumentada |
| `VOZ` | Voz en off + visuales |
| `UGC` | Talking-head a cámara |
| `REV` | UGC review / reacción |
| `TES` | Testimonial |
| `GRN` | Green screen |
| `TUT` | Tutorial / paso a paso |

Meta premia la diversidad de formato y castiga iterar solo el hook sobre el mismo formato. El
formato está en el ID justamente para poder auditar eso: si todas las filas del historial de un mes
dicen `IMG`, ahí está el problema.

---

## 5. Ratio

Sufijo del nombre de archivo, no del ID: `45` (4:5) · `11` (1:1) · `916` (9:16) · `169` (16:9).

Variar el ratio también cuenta como diversidad para Andrómeda.

---

## 6. Los tres lugares donde va el ID

### Archivo en disco

```
CREATIVOS/entregas/<YYYY-MM-DD>/<dashboard>-<producto-slug>/
  <YYMMDD>_<producto-slug>_<ID>_<ratio>.png
```

Ejemplo:
`CREATIVOS/entregas/2026-08-11/DASH1-mi-producto/260811_mi-producto_ECO-N2_MOS_H03_v1_45.png`

La fecha se repite en carpeta y archivo **a propósito**: un archivo suelto en Descargas sigue siendo
identificable.

### Nombre del anuncio en Meta

```
<DDMM> <ID>
```

Ejemplo: `1108 ECO-N2_MOS_H03_v1`

Es lo que devuelve UTMify en el campo `name`. **Sin esto el historial no se puede llenar.** Meta
acepta el nombre en la creación del anuncio y también editándolo después — si una tanda ya se subió
con `AD - 7`, se puede renombrar y a partir de ahí queda atribuida.

### Fila del historial

Columna `ID`, con el mismo string exacto.

---

## 7. Parseo desde UTMify

El nombre del anuncio se parte así:

```
1108 ECO-N2_MOS_H03_v1
└──┘ └─┘ └┘ └─┘ └─┘ └┘
fecha ANG NC FMT HOOK ver
```

Regex de referencia:

```
^(\d{4})\s+([A-Z]{3})-N([1-5])_([A-Z]{3})_H(\d{2})([a-z]?)_v(\d+)$
```

Un `name` que no matchee va a la sección **"sin atribuir"** del historial. No se adivina el ángulo
por el ID de Meta ni por el orden de creación.

---

## 8. Nombres de campaña y conjunto

No forman parte del ID, pero conviene sostener el criterio que ya se usa:

- Campaña de testeo: `Testeo <DD/MM/YYYY> — <producto>`
- CBO post-Andrómeda: `CBO <DD/MM> — <concepto>` donde concepto = el ángulo de los 3
- Copias: mismo nombre + ` [C1]`, ` [C2]`

Así, cuando se consulta UTMify a nivel campaña o conjunto, la agrupación por concepto ya viene hecha.
