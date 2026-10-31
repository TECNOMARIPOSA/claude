---
tema: Embudo VSL post-pago
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/creando-embudo-vsl-post-pago-criminal.md, RAW/formacion/lecciones/vsl-con-heygen.md, RAW/prompts/prompt-vsl-oto-post-purchase.md, RAW/formacion/lecciones/crea-un-gpt-personalizado-para-sumar-a-tu-oferta.md]
---

# Embudo VSL post-pago

La versión más elaborada del backend: en vez de una imagen y un botón, **cada OTO es un video de venta con avatar**. Ver [[aumento-de-aov]] para la mecánica básica de upsells.

## La estructura de precios

Cuatro OTOs, **cada uno con su downsell al 50%**:

| | Habla inglesa (front 27 USD) | Habla hispana (front 19 USD) |
|---|---|---|
| OTO 1 | 37 USD | 29 USD |
| OTO 2 | **97 USD** — soporte 1-a-1 (GPT personalizado) | 19 USD |
| OTO 3 | 27 USD | 10 USD |
| OTO 4 | 20 USD | — |

El OTO de 97 USD es un **GPT personalizado como soporte 1-a-1**. Coste marginal cero, valor percibido alto — hay lección dedicada a crearlo. Es el mismo razonamiento que los bonus de [[seleccion-y-modelado-de-oferta]].

## El flujo completo, con los downsells

```
CHECKOUT (compra aprobada)
      │
      ▼
   OTO 1 ──acepta────────────────► OTO 2 ──acepta──► OTO 3 ──► THANK YOU
      │                              ▲                 ▲       (descargas)
   rechaza                           │                 │
      ▼                              │                 │
  DOWNSELL 1 ──acepte o rechace──────┘                 │
                                                       │
                     OTO 2 ──rechaza──► DOWNSELL 2 ─────┘
```

Reglas:

- **Cada OTO tiene su downsell**, que aparece solo al rechazar
- Del downsell **se sale siempre al OTO siguiente**, se acepte o se rechace
- Santiago monta **3 o 4 OTOs**
- **Todos los caminos terminan en la thank you page** con los links de descarga

## Un caso sin order bumps

Dato que aísla el efecto del post-pago: un embudo suyo con **ticket promedio de 43 USD** montado **sin order bumps ni upsells previos** — solo con OTOs post-pago en Impultienda.

Es la mejor evidencia de que el post-pago es la palanca de AOV más fuerte ([[aumento-de-aov]]).

## El principio de venta

Lo más transferible de la lección, y lo que decide si el post-pago funciona:

> **Tu objetivo es crearle nuevos problemas en el VSL post-pago y presentarle las soluciones ahí mismo.**

Concretamente: identificar los **problemas adicionales que la persona va a tener al implementar** el producto que acaba de comprar.

### La otra estrategia: el mismo problema, mejor resuelto

Alternativa —y probablemente la más fácil de acertar— al principio de «crear nuevos problemas»:

> **Resolver exactamente el mismo problema del producto principal, pero de forma más efectiva, más fácil y más rápida.**

Ejemplo concreto: vendiste un **recetario en PDF** → el OTO 1 es un **curso de cómo cocinar esas recetas**. Mismo problema, mejor solución.

Funciona porque el cliente **ya demostró** que ese problema le importa lo suficiente como para pagar. No hay que convencerlo de nada nuevo.

Las dos estrategias conviven: resolver mejor lo mismo (OTO 1) y abrir problemas siguientes (OTO 2 y 3).

Y el corolario sobre selección de nicho:

> El nicho más fácil para upsellear post-pago es el de **ingreso extra**: le vendiste la solución a «generar ingresos», pero ahora tiene el dolor de vender poco, y marketing, y ventas… siempre hay un problema siguiente.

## El proceso de producción

**1. Detectar los OTOs.**
Subir el **PDF de la página de ventas a Claude** y hablarle por micrófono explicando la estructura de precios que quieres. Claude propone los productos. Santiago alterna entre hacerlo con prompt y hacerlo a mano, según cuán claro tenga los problemas adicionales del nicho.

**2. Generar los entregables.** Se le piden a Claude en el mismo chat.

**3. Guion del VSL.**
Con `prompt-vsl-oto-post-purchase` ([[biblioteca-de-prompts]]), pidiendo **texto listo para pegar en ElevenLabs**. Sale un guion de ~8 minutos que después se acelera a **5–6 minutos**.

**4. Audio en ElevenLabs.**

**5. Avatar en HeyGen.**
- Prompt para crear el avatar, adaptado a la landing del front
- ChatGPT genera la imagen
- HeyGen: subir foto → crear avatar → **escena tras escena**, cargando los audios de ElevenLabs

**6. Edición en CapCut.**
Deliberadamente mínima. **Sin B-rolls.** «Lo más simple posible, no me enrosco con eso.»

**7. Alojar el video.**
**Bunny Stream** o **Panda Video**. Funcionan igual.

**8. Montar el embudo.**
Se crean los productos con nombre y precio, y se marca la casilla **post-compra**.

La plataforma es **Impultienda** (confirmado en `mentoria-2026-06-07`, donde aparece varias veces con transcripción limpia; en la transcripción de esta lección salía distorsionada). Se usa como **checkout**, a menudo combinada con Shopify e InLead. Ver [[tracking-y-atribucion]] para su configuración de pixel y UTMs.


## Detalles de producción que ya se probaron

- **La VSL va en 9:16**, vertical. Las fotos del avatar se generan en 9:16, con la cara en el tercio de arriba y espacio libre abajo. El proyecto de HeyGen se configura en vertical **antes** de generar.
- **Movimiento del avatar: estable.** En vertical la cara ocupa más pantalla y el movimiento delata que es IA.
- **Subtítulos a la altura de las manos** (62–68% de la altura del cuadro). Tapan el movimiento que más delata al avatar.
- En CapCut: cortar silencios, acelerar a **1,2–1,4×**, confeti al inicio y un B-roll cada 3–5 segundos.
- El guion se le pide a Claude **"listo para pegar en ElevenLabs"**.
- **Tiempos en la página del OTO:** el botón y el texto aparecen a los **150 segundos** (cuando la VSL presenta la oferta). A los **600 segundos** se ocultan elementos. Temporizador rojo de **10 minutos**.
- Hosting: Panda Video o VTurb, con barra de progreso ficticia y "retomar reproducción".
- **Downsells:** van con ruleta, no con video (ver «Downsells con ruleta»).

## Downsells con ruleta

**Cada downsell es una página con una ruleta de descuento.** La persona gira, la ruleta frena en su descuento y recién ahí aparece el botón de pago. La ruleta reemplaza al delay del video.

- **Un descuento distinto en cada downsell**, por ejemplo **50% · 53% · 47% · 45%**. Con cuatro pantallas iguales al 50%, en la segunda la persona se da cuenta de que está arreglado.
- **Cada pantalla tiene su propia rueda.** Solo en el primer downsell el premio es el máximo de la rueda. En los demás hay valores más altos que no le tocan.
- **Nunca resaltes el número ganador** con tamaño o color: lo delata antes de girar.
- Los precios se redondean **hacia abajo** a dólar entero, así el descuento real siempre es igual o mayor al que se anuncia (37 → 18 USD es 51,4%, y se anuncia 50%).
- **Colores:** la ruleta usa la paleta de la marca, con buen contraste entre el texto y cada porción. Si la paleta es pastel, poné los números en un color oscuro en vez de blanco.
- Claude la arma en HTML a partir de la landing de la oferta, así hereda los colores y la tipografía.

## KPI

Take rate del post-pago **por encima del 15%** ([[aumento-de-aov]]).

## Requisito técnico

El upsell post-pago exige **checkout en dólares** — Shopify Payments, Stripe o PayPal, y eliminar Shopify Markets. En pesos argentinos no funciona. Ver [[shopify-y-checkout]].

## Complementos prácticos

- **La regla de orden: el ticket más alto va segundo, no primero.** Por ejemplo 37 → **97** → 27 → 18.
- Variante de precios en inglés: front 27 → OTO1 37 → OTO2 97 → **OTO3 al mismo precio del front** → **OTO4 ~10 USD menos que el front** (~17).
- **El post-pago vende más que el mismo producto ofrecido como order bump antes del pago.**
- **La VSL va en todos los OTO**, no solo en el primero. Los downsells, en cambio, van con **ruleta** (ver abajo).
- **Take rate de referencia para el OTO1: 20–35%**, algo menos en Argentina. El KPI de >15% es el piso.

### Estructura de 8 puntos del guion del OTO
1. Felicitar y tranquilizar sobre la compra que ya hizo
2. Validar el producto principal e introducir un **«pero»**: un caso concreto donde no alcanza
3. Presentar la nueva solución **con nombre propio** y una explicación que le dé credibilidad
4. Gatillo de escasez o exclusividad (era solo para alumnos, se libera únicamente por esta compra)
5. Entregables + bonos, con **un bono «secreto»** que solo se revela dentro del área de miembros
6. Anclaje de precio: precio normal vs. precio de cliente actual, pago único
7. **Garantía extendida (30+ días)**
8. CTA reforzando que la oferta es de una sola vez

### Configuración de cada pantalla de oferta (Impultienda)
- Ocultar header y footer del pedido: con un **timer a 600 s** no aparecen.
- Insertar el video con un bloque de código embed.
- **Un timer rojo que aparece recién en el segundo exacto en que el VSL presenta la oferta.** Hay que mirar el video y anotar ese segundo. El botón y el precio aparecen con el mismo delay.
- Cascada: OTO1 aceptado → OTO2; OTO1 rechazado → Downsell1 → OTO2; y así sucesivamente.

### Entrega vs. VSL
- **La entrega instantánea compite con el VSL post-pago.** Conviene un pequeño delay en el mail de entrega para no sacar al cliente de la pantalla del OTO.

### GPT personalizado como OTO de soporte 1-a-1
- ChatGPT Plus → Explorar → Mis GPTs → Crear. Para las instrucciones, Claude adapta un prompt-plantilla largo al producto pegándole el copy de la landing. El GPT puede **buscar en internet además de usar los PDFs**.
- Configuración: nombre y persona de experto, descripción corta, instrucciones, mensaje de ejemplo, **PDFs del producto como «Conocimiento»**, **generación de imágenes desactivada** e imagen de perfil hecha con IA.
- Entrega: el link va como **botón «Soporte 1 a 1» dentro del PDF**. Funciona aunque el comprador use ChatGPT gratis.

Relacionado: [[aumento-de-aov]] · [[guiones-de-video-ads]] · [[ugc-y-video-generativo]] · [[biblioteca-de-prompts]]
