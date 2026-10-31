---
tema: Internacionalización
actualizado: 2026-08-10
fuentes: [RAW/contexto-chatgpt.md, RAW/formacion/lecciones/multiidioma.md, RAW/formacion/lecciones/escalar-en-otras-cuentas-publicitarias-testear-varias-cuentas-publicitarias-para-relojear-el-cpm.md, RAW/youtube/_indice.md]
---

# Internacionalización

Vector de escala una vez que una oferta está validada y el mercado inicial se satura. Es el último eslabón del bucle del negocio ([[filosofia-de-marketing]]).

## Mercados

**Base histórica:** Argentina.

**Mercados habituales:** México · Estados Unidos · España · Uruguay · Chile · Colombia · resto de LatAm · Europa · Norteamérica · Reino Unido · Canadá · Australia · Nueva Zelanda.


## Replicar la oferta: el método de las «múltiples ofertas en profit»

La estrategia que más apalanca todo el sistema, y que suena a más trabajo del que es:

> «**No necesitás más de una sola oferta.** Tengo múltiples ofertas en profit porque tengo **esa misma oferta en diferentes mercados**.»

### Lo que hace falta

1. **Un funnel validado** — TSL, VSL o quiz, da igual cuál
2. **5–6 anuncios validados**
3. **Una pasarela que cobre en ese mercado**

Y nada más. En particular, **no hace falta LLC**: con Hotmart se puede validar la oferta en otro mercado sin empresa en EE.UU., sin Stripe y sin Shopify Payments. Ver [[shopify-y-checkout]].

### El problema que resuelve

En un mercado chico y barato como Argentina el CPC es bajísimo, pero **te topás con un techo**: al querer escalar, el CPC sube y la oferta no da más de sí. Estás en 300–500 USD/día y capeado.

La oferta no está agotada — **el mercado sí**.

### Los números cambian por completo

Dato concreto de una oferta suya fuera:

> **ROAS 2 con un CPC de 1,82 USD** y un **AOV de ~60 USD**.

Un CPC de 1,82 sería descarte inmediato en LatAm ([[metricas-y-kpis]]). Ahí funciona porque el ticket y el AOV son de otra escala. **Nunca se compara una métrica aislada entre mercados: se compara el conjunto.**

### Cómo traducir la tienda — el procedimiento

**Todo en la misma tienda.** No hace falta crear una nueva.

**1. Publicar el idioma en Shopify**
Configuración → **Idiomas** → agregar idioma → asignar a dominio → **Publicar**.

**2. Traducir con Translate & Adapt**
App de Shopify. «Traducir automáticamente» → tarda **~10 minutos**.

**3. El truco del URL**
Se añaden las **siglas del idioma después del dominio**: `tudominio.com/**en**/...`

Con eso la misma página se sirve en el otro idioma. Y funciona igual para el **carrito** y el **checkout**: mismo `/en/` en el URL del carrito y todo el flujo de pago aparece traducido.

**4. Lo que la IA no traduce**
- **Las imágenes hay que traducirlas a mano** (Canva, Higgsfield, Sora). Si la landing es de imágenes apiladas, es trabajo manual
- Si la landing es **con código**, se le pide a la IA que la traduzca — trivial. Otra ventaja del código sobre las imágenes ([[pagina-de-ventas]])

**5. Los anuncios**
Traducir el guion con ChatGPT → generar la voz en **ElevenLabs** o Google Studio. Ver [[ugc-y-video-generativo]].

**6. Opcional, y él no lo hace**
Dominio en inglés y fanpage en inglés. Si querés lanzar rápido, no hace falta.

> **Requisito duro:** Shopify Payments, o Stripe + PayPal. **Con Mercado Pago no se puede vender multiidioma**, sea de Argentina, Chile o Colombia. Ver [[shopify-y-checkout]].

### Lo que cambia en el ticket

El motivo real de hacerlo. Cifras de su tienda en habla inglesa, mostradas en pantalla:

| | Valor |
|---|---|
| Front | **29 USD** |
| Ticket promedio diario | 34 · 36 · 37,87 · **48 USD** |
| Semana completa | ~37 USD de ticket promedio, ~10.000 USD en ventas |

Frente a los 15–20 USD de ticket habituales en LatAm.

> «Podés duplicarle o triplicarle el ticket del front, exactamente el mismo producto, y **no vas a tener ningún tipo de fricción** al momento del pago.»

Es el mismo PDF. Lo que cambia es el poder adquisitivo del mercado.

### No todas las ofertas agarran en todos los mercados

Contrapeso necesario, de un caso real en mentoría: una oferta que vendía bien en LatAm se pasó a inglés y **dos días sin una sola venta**, pese a tener buenos números de tráfico —muchos inicios de checkout y carritos abandonados—. Bajar el precio no lo arregló.

El diagnóstico de Santiago:

> «Hay ofertas que en un mercado no agarran. Podés probar esa oferta en Italia, Francia o Rusia. **Pero si no agarra, no le insistas. No le gastes mucho dinero.**»

Misma disciplina que en [[validacion-de-oferta]]: la replicación es barata, pero no es gratis, y no convierte una oferta en universal. Si el cuello está en el checkout, se puede intentar mejorar la oferta antes de abandonar ([[diagnostico-de-checkout]]).

### Mercados menos obvios

Además de los habituales, menciona **Rusia, mercado árabe y Rumania**. La lógica: si una comunicación funciona, puede funcionar en culturas donde nadie está corriendo esa oferta.

Existe una clase en el canal sobre **traducir una tienda de Shopify por completo**.

### Cómo encaja con la caducidad de las ofertas

Las ofertas mueren a los 3–4 meses ([[modelo-low-ticket]]). Replicarlas en mercados nuevos es la forma más barata de **extender la vida de una oferta ya validada** antes de tener que buscar otra: el trabajo duro —comunicación, funnel, creativos— ya está hecho y pagado.

## Densidad poblacional: el criterio que decide el techo

Por qué unos mercados escalan y otros no:

> La sostenibilidad y el potencial de escala salen de la **densidad poblacional**. Más audiencia = los creativos se saturan más lento = la oferta aguanta más presupuesto.

| Mercado | Tamaño | Nota |
|---|---|---|
| **Tier 1 habla inglesa** | ~400 millones | **El de mayor potencial**: mayor ticket promedio, más escalabilidad y sostenibilidad |
| **LatAm habla hispana** | Muy grande | Buen equilibrio tamaño/dificultad |
| País individual | Chico | Techo rápido |

> ⚠️ **El mercado inglés es más difícil de entrar.** **No se recomienda para empezar.**

El orden natural: validar en tu país → LatAm → habla inglesa.

## A qué países targetear

El targeting que se usa por mercado.

### Si estás empezando: tu propio país

Vender en tu país con **tu pasarela local** (Mercado Pago argentino, mexicano, uruguayo…) integrada a Shopify. Es lo que hizo él antes de poder costear una LLC.

Alternativas si te bloquearon la pasarela local:

| Vía | Coste | Alcance |
|---|---|---|
| **Hotmart** | — | Todo el mundo |
| **LLC** | 400–500 USD de apertura | Todo el mundo, a los pocos días |
| **Shopify Payments** | — | Solo si resides en EE.UU./Europa o tienes ciudadanía europea |

### Mercado LatAm

Targeting habitual: **Estados Unidos** (por el volumen de hispanohablantes), **Chile, Colombia, Perú, Uruguay, México y Europa** (a veces solo España).

**Argentina se excluye** de ese conjunto — porque corre la misma oferta en una tienda Shopify aparte con Mercado Pago, lo que **sube la conversión del checkout**.

### Mercados en inglés

**Tier 1**: Estados Unidos, Canadá, Reino Unido, Australia, Nueva Zelanda. Los de mayor capacidad de compra.

Ampliación posible con **ticket más barato**: Sudáfrica, o directamente **Worldwide** (hay angloparlantes en India, Indonesia y toda Europa).

### Otros mercados

| Mercado | Táctica |
|---|---|
| Italia, Francia | Targetear el país directamente |
| Francés | O bien **Europa + idioma francés** (hay francófonos en varios países) |
| Rusia | **Worldwide + idioma ruso** — Meta no permite targetear Rusia directamente |

### El método para depurar

1. Correr unos días **por continente** (América del Norte, del Sur, Central, Europa, Caribe)
2. Calcular por país el **revenue por visita** y compararlo con el **costo por clic**
3. Dejar solo los países rentables — **después de 100–300 conversiones**, no antes

Es la misma ecuación de siempre ([[metricas-y-kpis]]), aplicada como filtro geográfico.

> Dato de contexto del mismo video: 10 tiendas activas, margen aproximado del **40%**. La cifra de facturación se transcribe de forma ambigua («más de $10,000» frente a los 119K del título), así que **no es fiable en el estado actual del material**.

## Cuándo salir del mercado local

**Umbral:** cuando ya tienes facturación sostenible, **100–300 USD de ganancia al día** (`RAW/formacion/mentorias/mentoria-2025-11-13.md`).

El argumento es de tamaño de audiencia: Argentina son ~44 millones de personas. Sumar Uruguay, Chile, Colombia, Ecuador y México es del orden de **10× la audiencia**.

Y tiene una consecuencia operativa concreta que Santiago mide:

> «Tiro una dúplica en una CBO a 50 dólares y **me dura una semana**. En Argentina muy pocas veces me duró.»

Más audiencia = **los creativos se saturan más lento** = escalado más estable y sostenible. Conecta con [[renovacion-de-creativos]]: parte del desgaste de creativos en mercados chicos es simple agotamiento del público.

Con experiencia, los productos nuevos se lanzan **directamente afuera**.

**No hace falta Shopify Payments para empezar:** se puede validar en Hotmart, que cobra en todo el mundo. Ver [[shopify-y-checkout]].

## Localizar, no traducir

El principio está declarado sin ambigüedad: no se traducen anuncios. Se adapta **lenguaje, acento, avatar, referencias, precio, mercado, oferta y copy**.

| Mercado | Registro |
|---|---|
| Argentina | Español argentino / rioplatense (a veces marplatense) |
| LatAm | Español latino neutro |
| EE.UU., Reino Unido, Canadá, Australia, NZ | Inglés |

El avatar también cambia por mercado, no solo el idioma. Ver [[ugc-y-video-generativo]].

## Implicaciones técnicas

**La decisión de moneda tiene consecuencias reales**, y es probablemente el punto de fricción más importante de la expansión:

- Con **Shopify Markets**: checkout en moneda local, mejor conversión, pero **el upsell post-pago solo se ve en países con moneda dólar**
- Sin Markets, **todo en USD**: se pierde algo de conversión de checkout, pero se habilita el upsell post-pago para todos

Para subir el AOV, la segunda opción es la que habilita el upsell post-pago. Ver [[shopify-y-checkout]] y [[aumento-de-aov]].

Hay lección dedicada a **multiidioma** en la tienda.

## CPM por mercado

El CPC tolerable cambia radicalmente:

- **LatAm**: 0,10–0,50 USD
- **Estados Unidos**: hasta 1 USD

Pero los números del funnel también cambian (ticket, AOV, conversión), así que la comparación siempre es del conjunto, no de una métrica. Ver [[metricas-y-kpis]].

Táctica relacionada: **testear varias cuentas publicitarias para «relojear» el CPM** — hay lección específica. Correr el mismo producto en varias cuentas permite comparar y escalar más agresivo. Ver [[escalado-en-meta-ads]].

## Infraestructura financiera

Evaluada para cobrar internacionalmente: **AstroPay, Payoneer, Trust Wallet** (con su tarjeta de débito), SWIFT/BIC, transferencias entre Payoneer y AstroPay. Ver [[stack-de-herramientas]].

## Fuente de ofertas

La internacionalización funciona también en sentido inverso: **Brasil y Estados Unidos son la fuente de ofertas a modelar**, precisamente porque van por delante y lo que allí funciona aún no se está corriendo en el mercado local. Ver [[seleccion-y-modelado-de-oferta]].

## Complementos prácticos

- **VSL en otro idioma:** grabar el avatar en HeyGen **sin subtítulos** y usar la traducción de un clic para generar las otras versiones desde la misma grabación.
- **Doblaje barato:** aislar el audio sobre un **video negro** y traducirlo con HeyGen. Sale mucho más barato que el doblaje dedicado de ElevenLabs.
- **Escala por región:** targetear región completa (Norteamérica, Sudamérica, Centroamérica y Caribe, Europa) con el resto abierto. Después cruzar el **revenue por sesión por país** (lifetime, desde la tienda) con el **costo por visita desglosado por país** en Ads Manager, y quedarse solo con los países donde el revenue por sesión supera al costo por visita.

Relacionado: [[modelo-low-ticket]] · [[shopify-y-checkout]] · [[metricas-y-kpis]]
