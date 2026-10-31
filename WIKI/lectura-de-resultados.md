---
tema: Lectura de resultados
actualizado: 2026-09-24
fuentes: [análisis semanales de ofertas reales en UTMify y Meta Ads, septiembre 2026]
---

# Lectura de resultados

**Cuando una oferta no da ganancia, lo primero que se culpa es el anuncio. En las ofertas medidas, casi nunca era el anuncio: era la landing.** Estas son las lecturas que salieron de analizar semanas reales, con el orden en que conviene revisar.

## 1. Antes de leer: que los números sean reales

- **Cargá comisiones, impuestos y costo de producto en UTMify.** Si están en 0, la ganancia que muestra es bruta. En un caso, una semana que figuraba con +800 USD daba pérdida con el 8–10% de comisión de la plataforma.
- **Mirá las ventas pendientes.** En una oferta había 109 pendientes contra 232 aprobadas. Cortar sin mirarlas es decidir con la mitad de los datos.
- **El país del comprador en UTMify no es confiable** ([[tracking-y-atribucion]]).

## 2. ¿Es el anuncio o la landing?

Cuando el CTR del link está en **4–7%** y el hook rate en **40–60%**, el anuncio está por encima del promedio. El problema está más abajo en el embudo.

**La métrica que separa a los ganadores de los perdedores es cuánta gente pasa de ver la landing a iniciar el pago.** No el hook, no la retención:

| Anuncios | ROAS | Inician el pago (de cada 100 que ven la landing) |
|---|---|---|
| Ganadores | ≥ 1,14 | **~15** |
| Neutros | ~1,0 | ~12,5 |
| Perdedores | ≤ 0,69 | ~10 |

- El anuncio con **mejor retención** de una semana **vendió cero**. El de mejor hook dio un ROAS normal.
- **Los relevos de un ganador cansado** tenían un hook rate más bajo (0,45–0,52 contra 0,60), pero **casi el doble de gente que pasaba al pago**. Atraían menos gente, pero gente mejor.
- **Cuánto vale arreglarlo:** en una oferta, llevar ese paso de 8,8% a 12% con la misma inversión daba **+83 ventas por semana** y el ROAS pasaba de 1,04 a 1,42.

Qué tocar en la landing: [[pagina-de-ventas]].

## 3. Las tarjetas rechazadas

- En una oferta, **1 de cada 4 pagos se rechazaba** (23%), y cada semana peor.
- Subir la aprobación del 75% al 88% valía casi lo mismo que arreglar la landing. **Las dos cosas juntas llevaban el ROAS de 1,05 a 1,53.**
- Causas y soluciones: [[diagnostico-de-checkout]] y [[procesadores-de-pago]].

## 4. El backend

- **Ratio AOV / precio del front: objetivo 1,5.** Las ofertas sanas medidas dieron **1,94 y 2,02**.
- Mirá cuántos compran cada OTO. En una oferta, **el OTO más caro casi no vendía** (2,6%) mientras el primero llegaba al 30%. Ese OTO es el que hay que revisar.
- Ver [[aumento-de-aov]].

## 5. La cuenta

- **Las cuentas no rinden igual.** Con los mismos anuncios, una cuenta perdía plata porque su **CPM era 45% más caro** que el de otra, no por el creativo. Compará el CPM entre cuentas antes de culpar al anuncio.
- **Un solo creativo sosteniendo casi todo el gasto es una alarma.** En una oferta, un anuncio era el 79% de la inversión semanal y estaba cayendo. Hay que tener los relevos listos antes ([[renovacion-de-creativos]]).

## 6. El horario y el presupuesto

- **Mirá el ROAS por franja horaria.** En una oferta, de 12 a 20 h se perdía toda la plata (ROAS 0,78 con el 34% del presupuesto), y de 20 a 00 h se ganaba (1,36) con solo el 9%. El nicho compraba de noche. Ver [[escalado-en-meta-ads]].
- **El ROAS baja cuando sube el gasto diario.** En una misma oferta: 178 USD/día → 1,30 · 306 → 1,17 · 652 → 0,98 · 1.232 → 0,93. Escalar tiene un costo: medí dónde está tu techo.

## 7. Las reglas automáticas de corte

**Una regla que corta muy temprano mata tests buenos por azar.** Con un CPA real de ~20 USD, una regla que cortaba a los 8 USD sin venta tenía **67% de probabilidad de matar un conjunto sano**. Mataba dos de cada tres tests buenos y se llevó casi el 9% del gasto de la semana.

- **Corte sano: ~2 veces el ticket**, o 2–3 veces el CPA objetivo ([[metodo-v3]]).
- La cuenta: la probabilidad de cero ventas en un conjunto sano es más o menos e^(−gasto ÷ CPA). A 8 USD con CPA de 20 USD da 0,67. A 40 USD da 0,14.

## El orden para revisar

1. ¿Los números están completos (comisiones y pendientes)?
2. ¿El anuncio trae clics baratos? Si sí, pasá al siguiente punto.
3. ¿Cuántos pasan de la landing al pago? Si son menos de ~12 de cada 100, el trabajo está en la landing.
4. ¿Cuántos pagos se aprueban? Si son menos del ~85%, el trabajo está en el checkout.
5. ¿El AOV llega a 1,5 veces el front?
6. ¿Alguna cuenta o franja horaria está perdiendo?

Relacionado: [[metricas-y-kpis]] · [[diagnostico-de-checkout]] · [[pagina-de-ventas]] · [[tracking-y-atribucion]] · [[metodo-v3]]
