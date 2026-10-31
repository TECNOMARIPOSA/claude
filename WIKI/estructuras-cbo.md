---
tema: Estructuras CBO
actualizado: 2026-09-24
fuentes: [operación real en Meta Ads, septiembre 2026; material de escalado de la formación]
---

# Estructuras CBO

**En una CBO el presupuesto va a nivel de campaña y Meta lo reparte solo entre los conjuntos.** Por eso una CBO se lee siempre **a nivel campaña**, nunca conjunto por conjunto. En una ABO, el presupuesto va en cada conjunto y cada uno se juzga por separado.

## La notación

Se lee **Campañas-Conjuntos-Anuncios**:

- **1-1-1**: 1 campaña, 1 conjunto, 1 anuncio.
- **1-1-5**: 1 campaña, 1 conjunto, 5 anuncios distintos. Es la base del [[metodo-v3]].
- **1-3-1**: 1 campaña, 3 conjuntos, 1 anuncio en cada uno.
- **1-50-1**: 1 campaña, 50 conjuntos, 1 anuncio en cada uno (ABO de micropresupuesto).

## Mapa de estructuras CBO

| Estructura | Forma | Qué hay adentro | Presupuesto | Para qué |
|---|---|---|---|---|
| **V3** | 1-1-5 / 1-1-10, suma un conjunto por tanda | Anuncios **distintos** de la misma tanda | 90–500 USD/día | La campaña principal de cada oferta ([[metodo-v3]]) |
| **Winners** | 1-1-N | Los 6 a 10 mejores anuncios, clonados por post ID | ~250 USD/día | Llevar los ganadores a otra cuenta |
| **CBO de testeo** | 1-3-N | 3 conjuntos = **3 conceptos** distintos, variaciones en contenido flexible | 35 USD (y una copia a 30) | Testear después de Andrómeda ([[testeo-de-creativos]]) |
| **Aislada** | 1-3-1 | **El mismo** anuncio ganador en los 3 conjuntos | 3× el CPA medio | Escalar un ganador solo |
| **Pocket** | 1-8-1 | **El mismo** anuncio ganador en 8 conjuntos | 75% del precio del front | Un ganador, más audiencias |
| **Mixta** | 1-4-N | 4 o 5 ganadores distintos, duplicados en 4 conjuntos | según el ticket | Poner a competir varios ganadores |
| **Power** | 1-8-N | 7 u 8 ganadores distintos, duplicados en 8 conjuntos | según el ticket | Cuentas con muchos ganadores |
| **Launch Pocket** | 1-10-N | 3 a 6 ganadores, duplicados | 3 a 5× el precio del front | Lanzar varios ganadores juntos |
| **CBO de ganadores** | 5 CBO idénticas | 3 a 5 conjuntos con un ganador distinto cada uno | 30 / 40 / 50 / 60 / 70 USD | Ver qué presupuesto "agarra viaje" |

Detalle de cada una, y de CostCap, BidCap, intrapuja y micropresupuesto, en [[escalado-en-meta-ads]].

## CBO frente a ABO, con datos

Una semana en una cuenta con 60 campañas de escala, contando solo los anuncios con **60 USD o más de gasto** (el núcleo):

| Estructura | ROAS del núcleo | CPA del núcleo | ROAS de la cola (<60 USD) |
|---|---|---|---|
| CBO 1-1-1 | **1,93** | 36 USD | 0,10 |
| CBO 1-3-1 | **1,64** | 40 USD | 0,00 |
| ABO 1-1-1 | **1,35** | 50 USD | 0,28 |

**Lo que dice la tabla:** la estructura importa mucho menos que el creativo y que no dispersar el presupuesto. Mirando todo junto, la ABO parece la peor (ROAS 0,92), pero es porque ahí vivía la mayor parte de la cola de duplicados. Esa es la razón del [[metodo-v3]].

## Reglas para operar una CBO

1. **Se lee a nivel campaña.** Que un conjunto no gaste no es un problema: Meta eligió.
2. **No se toca la estructura mientras aprende.** Los conjuntos que no vendieron se apagan recién a los **~15 días**, o cada **48 horas** en una Pocket (los caros o sin gasto).
3. **Antes de apagar, mirá los últimos 4 a 7 días**, no un día suelto. Un mismo creativo sube y baja de un día a otro.
4. **Nunca mezcles imagen y video** en la misma CBO de testeo, ni en el mismo anuncio de contenido flexible.
5. **Para escalar, se sube el presupuesto de la campaña entera.** No hace falta aislar conjuntos.
6. **Un mismo ganador puede estar en varias estructuras a la vez**: V3, aislada, CostCap y BidCap. No se pisan.
7. **Con un filtro duro de género, apagá Advantage+ Audience.** Si no, Meta lo toma como sugerencia.

Relacionado: [[metodo-v3]] · [[escalado-en-meta-ads]] · [[testeo-de-creativos]] · [[nomenclatura-del-metodo]] · [[setup-de-campanas]]
