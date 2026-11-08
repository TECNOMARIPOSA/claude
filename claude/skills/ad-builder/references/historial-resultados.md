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
- H15–H17: tres hooks nuevos sobre la estructura de H09 (autocuidado, sin saber dibujar, cambia el scroll por color). Siguen siendo DIR-N5: si alguno gana, es hook, no ángulo.
- H09 («Despeja la mente pintando», 4:5) **generó una venta** (dato del usuario; sin números de UTMify todavía). H11–H14 son 4 variaciones en 1:1 (formato que sirve en todas las ubicaciones de Meta) con el mismo ángulo, estructura y botón, cambiando 2.ª línea del titular, escena, lámina y gancho. Una venta no valida el ángulo: falta spend y CPA.
- H08–H10: tres hooks de venta directa (deja el celular / despeja la mente / relájate), tres escenas y tres láminas distintas, con la regla de textos grandes para celular. Las tres comparten ángulo DIR-N5: si una gana, cuenta como hook, no como ángulo nuevo.
- H07 v2: el usuario pidió textos más grandes, legibles en celular. Regla de producción para este producto: el texto más pequeño de una imagen 1080×1350 debe medir ≥ 26–27 px (≈ 9 px a 360 px de ancho), titular ≥ 80 px, y menos elementos de texto por pieza. Aplicar también a H03–H06 si se van a usar.
- H07: estilo de la referencia con tablet + hoja; la tablet muestra la portada real del ebook. Ángulo `SIM` (ya existía en la tabla).
- H06: estilo de una imagen de referencia del usuario (hoja a medio pintar con pincel, vela, titular con palabra manuscrita). Ángulo nuevo `CAL` añadido a la nomenclatura; copy sin promesa médica.
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
| 2026-11-05 | CAL-N2_IMG_H06_v1 | Calma («dale un respiro a tu mente») | N2 | Estático 4:5 | «Dale un respiro a tu mente pintando» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | SIM-N3_IMG_H07_v2 | Simplicidad («sin experiencia ni materiales especiales») | N3 | Estático 4:5 | «¡Pinta tu propia obra de arte!» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | DIR-N5_IMG_H08_v1 | Venta directa («deja el celular») | N5 | Estático 4:5 | «Deja el celular y pinta un rato» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | DIR-N5_IMG_H09_v1 | Venta directa («despeja la mente») | N5 | Estático 4:5 | «Despeja la mente pintando» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-05 | DIR-N5_IMG_H10_v1 | Venta directa («relájate») | N5 | Estático 4:5 | «Relájate con un ritual de colores» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H11_v1 | Venta directa (variación de H09: «pintando») | N5 | Estático 1:1 | «Despeja la mente pintando» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H12_v1 | Venta directa (variación de H09: «sin pantallas») | N5 | Estático 1:1 | «Despeja la mente sin pantallas» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H13_v1 | Venta directa (variación de H09: «en 30 minutos») | N5 | Estático 1:1 | «Despeja la mente en 30 minutos» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H14_v1 | Venta directa (variación de H09: «con una pausa») | N5 | Estático 1:1 | «Despeja la mente con una pausa» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H15_v1 | Venta directa (hook nuevo: autocuidado) | N5 | Estático 1:1 | «Regálate 30 minutos solo para ti» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H16_v1 | Venta directa (hook nuevo: sin saber dibujar) | N5 | Estático 1:1 | «Pinta sin saber dibujar» | — | — | — | — | — | — | ⏳ Sin correr |
| 2026-11-08 | DIR-N5_IMG_H17_v1 | Venta directa (hook nuevo: cambia el scroll) | N5 | Estático 1:1 | «Cambia el scroll por color» | — | — | — | — | — | — | ⏳ Sin correr |

**Aprendido:**
- H02 calibrada con el copy y las imágenes reales de los 5 anuncios argentinos (pasados por el usuario). Foto de portada real del usuario.
- Primera pieza (H01) hecha sin poder leer los 5 anuncios de referencia de Argentina (la Biblioteca de Meta devolvió 403). Pendiente calibrar con su copy real.
