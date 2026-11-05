# Historial de resultados

Registro vivo de qué se produjo, qué corrió y qué pasó. **Se lee antes de producir. Se escribe apenas
hay números, en el mismo turno, sin esperar a que lo pidan.**

Sin esto, cada sesión repite los tests de la anterior.

---

## Cómo se usa

**Un bloque por producto**, agrupado por dashboard. El bloque se crea la primera vez que se produce
para ese producto — no hace falta crearlos todos por adelantado.

Plantilla del bloque:

````markdown
## <DASHBOARD> · <Nombre del producto>

- **Dashboard:** `<id>` · TZ `<-3|-4>`
- **Ticket front:** — · **AOV real (UTMify):** — · **CPA medio:** — · **CPA break-even:** —
- **Idioma / mercado:** —
- **Compliance:** riesgos específicos del nicho

| Fecha | ID | Ángulo | NC | Formato | Hook (resumen) | Spend | Ventas | CPA | ROAS | CTR | Hook rate | Veredicto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

**Aprendido:**
- H05 v2: el usuario pidió acercar la hoja y usar una ilustración más realista. Regla: en este producto, hoja grande que se sale del cuadro y lámina realista (paisaje con animales) funcionan mejor que la lámina plana.
- H05: formato de «contenido del producto» (hoja inclinada mitad numerada/mitad pintada + franja de beneficios + categorías), calcado en estructura de la referencia argentina. Usa la lámina más vistosa del ebook. Sin oferta dentro de la imagen.
- Feedback del usuario sobre H03/H04 v1: la imagen debe parecerse más a los anuncios de referencia, con la ilustración como protagonista, y **sin 50% OFF ni bonos dentro de la imagen** (la oferta va en el texto). Regla para próximas piezas de este producto. v2 aplica esto: hoja grande mitad numerada/mitad pintada con lámina real del ebook.
- H04 abre un ángulo nuevo (`REG`, agregado a la nomenclatura) con la estructura de los anuncios argentinos 2 y 4; escena de hogar con lámina real del ebook enmarcada. Se quitó «Día de la Madre» por ser fecha local.
- H03 toma el gancho del anuncio argentino 5 (celular «solo un minuto»), con diseño propio de marca (verde oliva + durazno, Fraunces) y una página real del ebook sobre la hoja. Si H03 y H02 comparten ángulo (PSL-N2), el ángulo es el mismo y cambia el hook: no cuentan como ángulos distintos.
- (prosa — vale más que la tabla)

**Sin atribuir:** anuncios que corrieron sin nomenclatura y no se pueden asignar a ningún ángulo.
````

Reglas:

- Los montos van en **USD ya convertidos** (UTMify los devuelve en centavos).
- `Hook rate` y retención solo aplican a video; en estáticos va `—`.
- Ninguna celda se completa "a ojo". Si el dato no está, va `—`.
- El veredicto sale de la tabla de `utmify-mapa.md` §4.
- **❌ mata el anuncio, nunca el ángulo.** Un ángulo se marca perdedor solo con ≥3 creativos
  distintos y gasto acumulado ≥ CPA break-even sin ventas — y eso se anota en **Aprendido**, no en la
  columna de veredicto.

Veredictos: ✅ Validado · 🟢 Vende · ⏳ En testeo · ❌ Descartar · 🔁 Fatigado · ⚠️ Inconcluso.

---

## Índice de bloques

*(vacío — se agrega un renglón por cada producto al crear su bloque)*


## LATAM · Calma en colores

- **Dashboard:** — · **Idioma / mercado:** español neutro, Latinoamérica
- **Ticket front:** 15 USD (precio normal 30 USD) · AOV real: — · CPA medio: — · CPA break-even: —
- **Compliance:** bienestar/estrés: sin promesa médica ni «cura»; prueba social solo con citas reales

| Fecha | ID | Ángulo | NC | Formato | Hook (resumen) | Spend | Ventas | CPA | ROAS | CTR | Hook rate | Veredicto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-11-05 | PSL-N2_IMG_H01_v1 | Problema–solución | N2 | Estático 4:5 | «¿Terminas el día con la cabeza a mil?» | — | — | — | — | — | — | ⏳ Sin correr (reemplazada por H02) |
| 2026-11-05 | PSL-N2_IMG_H02_v1 | Problema–solución («tiempo para ti») | N2 | Estático 4:5 | «Un té. Unos colores. Una ilustración.» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | PSL-N2_IMG_H03_v2 | Problema–solución («celular: un minuto → una hora») | N2 | Estático 4:5 | «Solo un minuto en el celular… y pasó una hora.» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | REG-N3_IMG_H04_v2 | Regalo («no termina en un cajón, termina en tu pared») | N3 | Estático 4:5 | «Un regalo que no termina en un cajón: termina en tu pared.» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | DIR-N4_IMG_H05_v2 | Venta directa («qué incluye») | N4 | Estático 4:5 | «Más de 100 ilustraciones para pintar por números» | — | — | — | — | — | — | ⏳ Sin correr |

**Aprendido:**
- H02 calibrada con el copy y las imágenes reales de los 5 anuncios argentinos (pasados por el usuario). Foto de portada real del usuario.
- Primera pieza (H01) hecha sin poder leer los 5 anuncios de referencia de Argentina (la Biblioteca de Meta devolvió 403). Pendiente calibrar con su copy real.
