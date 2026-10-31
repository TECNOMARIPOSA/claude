---
tema: Nomenclatura del método
actualizado: 2026-09-24
fuentes: [operación real en Meta Ads, septiembre 2026]
---

# Nomenclatura del método

**Todo se nombra con la fecha de la tanda que trae el archivo del editor, no con la fecha en que arranca a correr.** El nombre del archivo es la identidad del creativo y no cambia. La fecha de arranque es una decisión de pauta y sí cambia. Si los dos no coinciden, no hay forma de cruzar un reporte con la carpeta del editor.

## Campañas

| Tipo | Nombre | Ejemplo |
|---|---|---|
| Campaña V3 | `V3 · <Producto> · <Cuenta>` | `V3 · Mi Producto · CP1` |
| Winners | `V3 · <Producto> · <Cuenta> — Winners` | `V3 · Mi Producto · CP2 — Winners` |
| Por catálogo | `V3 · <Producto> · <Cuenta> · Catálogo` | `V3 · Mi Producto · CP3 · Catálogo` |
| Puja manual | `V3 · <Producto> · <Cuenta> — BidCap $<n> Acelerada` | `… — BidCap $32 Acelerada` |
| Estructura explícita | `<Producto> l CBO 1-1-5 l <fecha>` | `Mi Producto l CBO 1-1-5 l 15/9` |

`<Cuenta>` es el nombre corto de la cuenta publicitaria (CP1, CP2…). Con muchas cuentas, es lo único que te dice dónde está cada campaña cuando mirás los reportes de UTMify.

## Conjuntos

| Caso | Nombre |
|---|---|
| Una tanda del editor | La fecha, con guion: `18-9` |
| Segunda tanda del mismo día | `17-9 #2` |
| Conjunto de winners | `Winners · Broad 18-65` |
| Winners con filtro de género | `Winners · Broad H 18-65` (hombres) / `Broad M 18-65` (mujeres) |
| Primer conjunto, sin fecha | `Broad` |

**Una tanda es un conjunto.** Si 10 anuncios tienen que arrancar el mismo día pero vienen de dos tandas, van en **dos conjuntos de 5**.

## Anuncios

| Qué | Formato | Ejemplo |
|---|---|---|
| Anuncio | Fecha con **barra**, espacio, guion, número | `18/9 - 1` … `18/9 - 10` |
| Segunda tanda del día | Sufijo `#2` | `17/9 - 3 #2` |
| Con prefijo de editor o concepto | 2 letras antes de la fecha | `MI 12-9-6`, `CE 15-9-1` |
| Archivo del editor | Prefijo, fecha y número con **guiones** | `ei-18-9-1.mp4` |

El anuncio `18/9 - 1` corresponde al archivo `…-18-9-1.mp4`. Así, cualquiera puede ir del reporte al archivo en segundos.

### Si usás la skill `ad-builder`

La skill agrega un ID de ángulo (`ECO-N2_UGC_H03_v1`: ángulo, nivel de conciencia, formato, hook y versión). Se pone **después** del nombre por fecha, así no se pierde el cruce con el editor:

```
18/9 - 1 | ECO-N2_UGC_H03_v1
```

Con eso, UTMify puede filtrar por fecha (`18/9`) o por ángulo (`ECO-`). Ver la skill en `.claude/skills/ad-builder/references/nomenclatura.md`.

## Pujas manuales: escaleras e intrapujas

Las campañas de puja manual se nombran por el **objetivo** de cada conjunto:

| Estructura | Nombres de los conjuntos | Paso |
|---|---|---|
| Escalera CostCap | `OBJ 4`, `OBJ 5` … `OBJ 10` | 1 USD |
| Escalera BidCap | `OBJ 17`, `OBJ 18` … `OBJ 23` | 1 USD |
| Intrapuja | `Intrapuja 10` → 10,0 · 10,1 · 10,2 … | 0,10 USD alrededor del bid ganador |

Arranque de referencia: **50 USD por conjunto**. En una oferta medida, los mejores escalones fueron CostCap 4, 6 y 8 USD, y BidCap 21 y 22 USD. Cada oferta tiene los suyos: hay que testearlos. Ver [[escalado-en-meta-ads]].

## UTMs: la misma plantilla en todas las campañas

Los UTMs van **dentro del link del anuncio**:

```
https://tu-dominio.com/?utm_source=FB&utm_campaign={{campaign.name}}|{{campaign.id}}&utm_medium={{adset.name}}|{{adset.id}}&utm_content={{ad.name}}|{{ad.id}}&utm_term={{placement}}&utm_id={{campaign.id}}
```

- **Usá la misma plantilla en todas las campañas.** Si en unas `utm_term` lleva la ubicación y en otras el ID del conjunto, el análisis por creativo en UTMify no cierra.
- Si la plataforma de checkout necesita un parámetro propio (por ejemplo `&ref=…`), va al final, siempre igual.
- El `&h=…` que aparece en la vista previa lo agrega Meta. No lo copies.
- Ver [[tracking-y-atribucion]].

Relacionado: [[metodo-v3]] · [[estructuras-cbo]] · [[setup-de-campanas]] · [[tracking-y-atribucion]]
