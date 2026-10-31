---
tema: Página de ventas
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/estructura-de-una-pagina-de-ventas-que-convierte.md, RAW/formacion/lecciones/2-opciones-para-creacion-de-landing-en-shopify.md, RAW/formacion/lecciones/crea-tu-landing-page-con-diseno-irresistible-en-deepseek.md, RAW/prompts/prompt-escribir-sales-page.md, RAW/prompts/prompt-html-google-ai-studio.md]
---

# Página de ventas

Objetivo no negociable: **comprate ≥ 2,5–3%**. Por debajo de eso no se escala tráfico, se arregla la landing. Ver [[metricas-y-kpis]].

La landing debe ser «el hogar del buyer persona»: hablarle directamente al avatar, no ser una página bonita.

## La estructura que convierte

Santiago muestra tres landings distintas —recetas, esoterismo, alimentación saludable— para demostrar que **la estructura es siempre la misma**:

1. **Promesa de transformación**, preferiblemente **con un número**
   *«Transforma tu mesa en un banquete gourmet con más de 80 recetas»* · *«Despierta tu brujo interior… en solo 7 días»*
2. **Dolores** — entre 3 y 6. Formato «Este ebook es para vos si…»
3. **Beneficios / transformaciones** — entre 3 y 6
4. **Presentación del producto** con mockups
5. **Botón** + resumen de oferta
6. **Garantía** — 30 días
7. **Bonus** — presentados uno a uno
8. **Testimonios**
9. **Preguntas frecuentes**
10. **CTA final** con resumen de oferta

## La regla del ahorro en dinero, no en porcentaje

De las cosas más accionables del material:

> **Nunca pongas «50% off».** Si le pones 60% de descuento, la persona sale de la landing a calcular cuánto es. Hay que hablarle como a un nene: **«Te ahorrás 30.000 pesos si comprás ahora»**.

Un porcentaje obliga a hacer una cuenta. Una cifra absoluta no.

## Transformación, nunca características

> «Vos no entraste a esta mentoría porque tenía más de 100 clases. Entraste por la transformación.»

A nadie le importa si el ebook tiene 200 o 300 páginas. Le importa qué va a saber hacer después. Si vendes un bolígrafo, vendes la necesidad del bolígrafo, no que sea azul y de tinta.

## Elementos de urgencia y escasez

Los que aparecen en las landings que corren:

- «Últimos 3 cupos en oferta»
- «Solo hoy, jueves 3 de julio» (fecha dinámica)
- «El precio está por subir»
- «31 personas están viendo esto»
- «Tu lugar está reservado por 15 minutos»
- Contador regresivo
- Precio anterior tachado + ahorro en dinero

## Dos formas de construirla

| Vía | Cómo | Opinión de Santiago |
|---|---|---|
| **Código HTML** | Generada con IA, alojada en Shopify | **La recomendada.** «Nadie en el mercado está haciendo esto» |
| **Imágenes apiladas** | Imágenes de Canva puestas como secciones en Shopify | Funciona, pero es lo que hacen los novatos |

El argumento competitivo: los que corren con imágenes pagan apps de Shopify (~8 USD/mes) para conseguir los bloques de urgencia y reseñas. Con código sale gratis y queda mejor.

### Magic Patterns, en concreto

**«Es un ChatGPT que crea landing pages.»** Se le pasa un prompt + **el copy completo del sales letter** y tarda 2–3 minutos.

Dos cosas a tener en cuenta:

- La landing queda alojada en **el hosting de Magic Patterns**, no en Shopify
- Hay que **conectarle un dominio o subdominio**: *Publish → Customized domains → Add a new domain*

Empieza gratis y luego tiene planes de pago.

Otras herramientas para generar la landing con código: **DeepSeek**, **Google AI Studio**. Hay prompts dedicados a los tres en [[biblioteca-de-prompts]] — el de Google AI Studio adapta una landing HTML existente a un producto nuevo manteniendo la estructura, y el de Magic Patterns detecta nicho y avatar leyendo el copy.

Santiago comparte los códigos de sus landings ganadoras para que los alumnos los modelen, con una condición explícita: **modelar la estructura, no correr su oferta**.

## Cómo evaluar un cambio en la landing

> **Mínimo 3 días de tráfico.** No se puede tocar la landing y mirar la conversión al momento.

Es el error de medición más común: un cambio se juzga con el dato del día, que está dominado por ruido.

### Menos puede ser más

Un hallazgo contraintuitivo: **quitar dolores y beneficios puede subir la conversión**.

> «Hay algunos que están de más. También pueden probar eso.»

La estructura pide 3–6 de cada uno. Pasarse de ahí dilata la página sin añadir persuasión.

También menciona **emojis** para hacer la lectura más amena.

### El texto del botón importa

Caso real de un alumno, y buen ejemplo de cuello de botella invisible:

> El primer botón decía **«Descargar recetas»**. La gente entendía que era **gratis**, hacía clic, y se topaba con un checkout. Resultado: muchísimos carritos iniciados y pocas compras.

Si el ratio carritos → compras está roto, revisar qué promete literalmente el texto del botón. Ver [[diagnostico-de-checkout]].

## TSL vs. VSL

- **TSL** (*textual sales letter*) — la landing escrita. Es lo estándar en low-ticket
- **VSL** (*visual sales letter*) — la oferta se presenta dentro del video; toda la psicología está ahí y no se puede pausar

> **Los VSL se usan para productos de 49 USD para arriba.** Para low-ticket de 10–20, la TSL es lo que corresponde.

El VSL **en vertical** funciona bien, no solo en horizontal.

Forma de decidir sin adivinar: **duplicar la página en versión TSL y mandar los anuncios ganadores ahí** para comparar conversión contra la versión con VSL. El producto ya está validado, así que se aísla la variable landing.

## Optimización técnica

La velocidad de carga importa por una razón medible: **la diferencia entre CPC y costo por visita es la pérdida de leads por lentitud**. Si esos dos números se separan, hay que optimizar. Ver [[metricas-y-kpis]].

**Fórmula, como métrica personalizada en el administrador de anuncios:**

> **Carga = visitas a la página de destino ÷ clics en el enlace**

**KPI concreto de carga: entre 60% y 85–90%.**

### Cómo subirla: Lazy Load

> Que la landing **cargue por secciones a medida que se scrollea**, no entera de golpe.

Si carga todo de una, el *first paint* es pesadísimo y pierdes gente antes de que vea nada. Con lazy load solo se carga el primer bloque y el resto va apareciendo.

> Por debajo del 60% **estás perdiendo mucho tráfico**: gente que hizo clic, que ya pagaste, y que nunca llegó a ver tu página.

Santiago lo señala como algo a lo que «nadie le da bola», pese a ser una fuga que se paga en cada clic.

Existe prompt dedicado (`prompt-optimizar-carga-web-html`) para Core Web Vitals sin tocar el diseño, y lecciones sobre conversión de imágenes a WebP (Squoosh.app → TinyPNG, en ese orden).

## Tres vías para subir el comprate

No todas pasan por la landing:

1. **Meter mano en la landing** — estructura, oferta, promesa
2. **Ajustar el targeting**
3. **Trabajar los creativos**

Y el comprate se descompone en dos ratios; **mejorar cualquiera de los dos sube el general**:

```
Comprate = (inicio de checkout ÷ landing page views) × (compras ÷ inicio de checkout)
```

Si el primero está bien (>10%) y el segundo mal, el problema **no es la landing**: es el checkout o la oferta. Ver [[diagnostico-de-checkout]].

## Diagnóstico por métrica

| Síntoma | Dónde mirar |
|---|---|
| Comprate < 2,5% | Estructura, oferta, promesa |
| Visita → checkout < 10% | La landing no persuade |
| Checkout → compra < 25% | El checkout, no la landing. Ver [[shopify-y-checkout]] |
| CPC ≠ costo por visita | Velocidad de carga |

## Un producto o bundles: el trade-off

Dos formas de montar la oferta en la landing, y ninguna es gratis:

| | Un solo producto | Bundles (varias opciones) |
|---|---|---|
| Fricción | **Mínima** — la decisión es sí o no | Mayor: hay que elegir |
| Conversión | Más alta | **Más baja** |
| AOV en el front | El precio | **Más alto** |

> «Ofrecer bundles, order bumps o upsells previos **genera fricción** y vas a perder cantidad de pedidos. Pero vas a ganar AOV. Si sabés upsellear bien, compensa.»

Lo mismo aplica a los order bumps del carrito ([[aumento-de-aov]]): **todo lo que añadas antes del pago cuesta conversión y paga en AOV**. Por eso el post-pago es superior — suma AOV **sin** tocar la conversión del front.

## Alternativa: quiz antes de la oferta

Cuando el CPC es alto y la landing directa no cierra los números, existe la vía de [[quiz-funnel]]: ~16 preguntas antes de mostrar la oferta, que convierte al 25–30% de quien llega al final y tolera CPC de hasta 1 USD.

## Complementos prácticos

### Construir con IA sin romper nada
- **Pedir siempre «pasame el HTML completo».** Si no, la IA corta a mitad de archivo. Si igual se corta: *«llegaste hasta la sección X, pasame el resto del HTML completo desde ahí»*.
- **Pegar el link del carrito o checkout ya en el prompt inicial**, para no reemplazarlo botón por botón después.
- **Partir de un template ya probado:** pegarlo en DeepSeek o Claude y pedirle que lo tome **como referencia visual**, con la misma jerarquía, cambiando solo el copy (que tiene que estar escrito antes) y la paleta.
- **Leer el código ahorra tiempo:** arriba está el CSS (estilos) y abajo el HTML (textos). Los cambios de texto o precio se hacen a mano, sin regenerar todo.
- **Pedir los cambios localizados:** *«en la sección que se titula X, agregá o cambiá Y»*. No se regenera la landing entera.
- **Pase de estética al final:** un prompt de «experto en diseño web HTML y efectos visuales, no toques el copy ni la estructura, solo mejorá el diseño» (armado con Prompt Cowboy). Objetivo: que se perciba como un producto de **2.500 USD y no de 20**.

### Magic Patterns: flujo real
- Primero se escribe el sales letter completo en un documento aparte, con los prompts de escribir y recortar el sales letter. Después se pega el prompt de generación + el sales letter.
- Ajustes de layout con **«visual editing»** (clic, borrar y mover bloques). Los cambios de contenido se piden por chat.
- Se le puede pegar **un screenshot de otra landing** para que replique un layout concreto, por ejemplo cómo se muestran los bonus.
- Hay dos prompts maestros para el final: **optimización total** de la landing y **eliminación de espacios**, que la compacta para mobile.
- **Multidivisa por IP:** una instrucción detecta el país del visitante y muestra el precio en su moneda. El precio por país se carga a mano y aproximado; un desfase de ~100 unidades no frena la compra.
- **Pixel:** se pega el script de UTMify, o se crea un pixel manual en Events Manager y se le pide a la IA que lo instale y **dispare `AddToCart` al hacer clic en los botones**.
- Subdominio: registro **CNAME apuntando a `magicpatterns.dev`**. Propaga en ~1 minuto.

### Landing con imágenes dentro de Shopify
- Personalizar → Página de productos → secciones **«Banner de imagen»** en el orden de la estructura, una imagen de Canva en cada una.
- En «Información del producto»: sacar el zoom de imagen y agregar Garantía y FAQ como **«contenido plegable»**.

### Google AI Studio (React + Tailwind): arquitectura fija
- **Sticky alert bar → Hero en 2 columnas → Sales letter (dolores en rojo, soluciones en verde) → Stack «qué incluye» → Bonus con caja de valor total tachado → Pricing dinámico con mockup + botón → Prueba social y footer.**
- La multidivisa se simula con `navigator.language` por JS.

### Style transfer desde una carta clásica
- Se toma una sales letter clásica de respuesta directa (el ejemplo es **Ted's Woodworking**) como plantilla de ADN. La IA hace ingeniería inversa de ritmo, cantidad de bullets de dolor, metáforas y agresividad contra la competencia, y la reescribe entera para el nicho nuevo.
- En un **segundo paso**, otro prompt convierte esa carta larga en la landing modular de bloques para compra impulsiva.

### Carga y VSL
- **Objetivo concreto del prompt de Core Web Vitals: menos de 1,5 s en 4G**, sin tocar nada visible.
- **Estructura de TSL con VSL:** Headline → VSL → Contador → Botón → texto de urgencia debajo.
- **Panda Video**, por qué conviene:
  - **Barra de progreso ficticia**, que avanza rápido al principio para que un video de 10 minutos «se sienta corto».
  - **Reanuda donde la persona lo dejó.**
  - Pesa poco y no afecta la carga de la landing.
- Se pega el embed en el HTML.

Relacionado: [[metricas-y-kpis]] · [[shopify-y-checkout]] · [[seleccion-y-modelado-de-oferta]] · [[quiz-funnel]] · [[optimizacion-de-roas]] · [[imagenes-y-mockups]]
