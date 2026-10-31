---
tema: Setup de campañas
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/set-up-campana-desde-0.md, RAW/formacion/lecciones/clase-mas-importante-como-testear-y-escalar.md, RAW/formacion/lecciones/segmentos-de-publico.md]
---

# Setup de campañas

Configuración concreta de una campaña de testeo en Meta, paso a paso. Se hace **una sola vez**: después todo es duplicar.

## Campaña

| Ajuste | Valor |
|---|---|
| Objetivo | **Ventas** |
| Presupuesto a nivel campaña | **Desactivado** (esto es lo que la hace ABO en vez de CBO) |
| Nomenclatura | `Testeo ads [fecha] [producto]` — ej. `Testeo ads 23/1 Keto` |

## Conjunto de anuncios

| Ajuste | Valor |
|---|---|
| Nomenclatura | `[fecha] - [nº de creativo]` — ej. `23/1 - 1` |
| Conversión | **Sitio web** |
| Optimización | **Maximizar el número de conversiones** |
| Pixel | El conjunto de datos conectado a la tienda |
| Evento de conversión | **Comprar** |
| Presupuesto | **5 USD** para arrancar |
| Programación | **Día siguiente a las 00:00** |
| Fecha de finalización | **Ninguna. Siempre lifetime** |
| Público | Solo el país. Generalmente **abierto** |
| Ubicaciones | Todas, por defecto |

Sobre el evento «Comprar»: **es normal que no aparezca como activo en la primera campaña.** Se selecciona igual.

Sobre la fecha de finalización, la razón de no ponerla: los conjuntos se apagan a mano cuando cae el rendimiento, no por calendario.

## Anuncio

- Página de Facebook + cuenta de Instagram
- **Subida manual**, una sola imagen o video
- **Destildar «anuncio multi-anunciante»**
- URL de destino: la página de ventas del producto
- **Destildar todas las mejoras con IA** de Meta
- CTA: «Ver más» o «Comprar» según el anuncio
- Descripción: vacía

**El título** lleva un truco concreto: el nombre del producto seguido de **«4.9 de 5»**, con formato de reseñas.

**El texto principal** se genera con ChatGPT ([[biblioteca-de-prompts]], `prompt-meta-ads-primary-text`).

## Ajustes que se pasan por alto

Errores de montaje que Santiago dice ver constantemente:

**⚠️ No activar «compartir hasta un 20% del presupuesto con otros conjuntos».** Eso convierte la ABO en una CBO de facto.

**Público:** «obtener conversiones de todos los públicos».

**Optimización: maximizar el número de conversiones — «porque no tenés backend».** El matiz importa: una vez montado el backend, esa elección se puede reconsiderar. Ver [[aumento-de-aov]].

**CTA: «Más información».** (En material anterior aparecía «Ver más» o «Comprar» — este es el más reciente.)

**Limpieza del anuncio:**
- Quitar **anuncios multi-anunciante**
- Desactivar **todas las mejoras esenciales** (debe quedar en 0 de 2)
- **Quitar los comentarios** del anuncio
- Descripción vacía; headline específico del producto


## Cuentas nuevas: calentar antes de lanzar

Corré **2 o 3 días una campaña de tráfico a 1–3 USD por día** con un video liviano, que no sea la oferta real. Recién después lanzá la oferta. Ver [[problemas-de-cuentas-meta]].

## Por qué a las 00:00 del mercado

Si publicás muy tarde en el día del país al que apuntás, Meta mete todo el presupuesto del día en pocas horas. Programá siempre a las **00:00 hora del mercado objetivo**, no la tuya.

## Duplicar

Configurado el primer conjunto, se duplica tantas veces como creativos haya (4 duplicados para un test de 5), **con la configuración original y en la misma campaña**. El duplicado **arrastra toda la configuración**: pixel, evento, presupuesto, público.

Secuencia exacta: duplicar ×4 → renombrar los conjuntos (2, 3, 4, 5) → **guardar como borrador** → ir a anuncios, renombrar y **cambiar el video** de cada uno → volver a campañas y **publicar**.

Lo único que se cambia en cada copia: **el número en el nombre y el creativo**. Opcionalmente el texto principal.

> «Cinco formas distintas de comunicar una misma cosa.»

## Segmentación

El material es deliberadamente laxo aquí, y es coherente con la tesis de que **el targeting vive en el creativo**:

- Generalmente **todo abierto**, para que compren hombres y mujeres
- Si el producto es muy específico de género (belleza, fitness femenino), segmentar por sexo
- Si se quieren intereses: 3–5 del nicho
- «Acá no hay ninguna regla. Todo funciona.»

Hay lección dedicada a `Segmentos de Publico`.

## La columna que hay que añadir

**Valor de conversión de compras promedio.** Sin ella se matan conjuntos rentables: si el front son 17 USD pero los upsells llevan el valor real a 25, juzgar contra 17 apaga campañas que están ganando dinero.

Ver [[metricas-y-kpis]] y [[aumento-de-aov]].

## Lectura de resultados

Las dos métricas que se miran primero: **cantidad de resultados** y **costo por resultado**. La comparación siempre es contra el CPA break-even.

Ejemplos del material: 26,55 USD de valor promedio con 15 USD de costo por compra = casi duplicando. Frente a conjuntos que gastaron 15–21 USD sin vender, apagados sin dudar.

> «Yo en 15 ya tengo que apagarlo porque mi front está en 17. Estos son los que te sacan el profit.»

Relacionado: [[testeo-de-creativos]] · [[escalado-en-meta-ads]] · [[metricas-y-kpis]] · [[tracking-y-atribucion]]
