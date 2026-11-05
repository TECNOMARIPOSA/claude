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
| 2026-11-05 | PSL-N2_IMG_H01_v1 | Problema–solución | N2 | Estático 4:5 | «¿Terminas el día con la cabeza a mil?» | — | — | — | — | — | — | ⏳ Sin correr |

**Aprendido:**
- Primera pieza hecha sin poder leer los 5 anuncios de referencia de Argentina (la Biblioteca de Meta devolvió 403). Pendiente calibrar con su copy real.
