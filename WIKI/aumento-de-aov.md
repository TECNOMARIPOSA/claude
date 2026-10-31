---
tema: Aumento de AOV (backend)
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/luego-de-validar-la-oferta-crearas-un-backend-que-aumente-el-roas.md, RAW/formacion/lecciones/upselling-previo-a-la-compra-selleasy.md, RAW/formacion/lecciones/upselling-post-compra-one-clic-upsell.md, RAW/formacion/lecciones/rokt-after-sell.md, RAW/formacion/lecciones/tu-deber-es-aumentar-el-ticket-promedio.md, RAW/contexto-chatgpt.md]
---

# Aumento de AOV (backend)

Santiago presenta este módulo como el que «nadie te va a enseñar» y el que cambia el rumbo del negocio. La razón es estructural, no motivacional: **el backend es lo que te deja pagar el tráfico más caro que tu competencia.**

Con un front de 15 USD y un CPA de 13, estás casi muerto. Con seis productos detrás que llevan el AOV a 25, ese mismo CPA de 13 es un negocio excelente. Ver [[metricas-y-kpis]] para el AOV/front-end ratio.

## Qué es exactamente el backend

> Los **productos adicionales que le vendés al mismo cliente dentro del mismo proceso de compra**.

No es email marketing ni remarketing: es lo que pasa entre que pulsa «comprar» y llega a la página de gracias.

## El backend es tu foso defensivo

Además de subir el AOV, cumple una función que casi nadie ve:

> **Todos te modelan el front** — la página de ventas y los anuncios. Pero **muy pocos saben que tenés ofertas por detrás.**

El backend es lo único que la competencia **no puede ver ni copiar** desde la biblioteca de anuncios. Y se traduce en poder de puja:

| | Competidor sin backend | Vos con backend |
|---|---|---|
| Front | 27 USD | 27 USD |
| AOV | 27 USD | **45 USD** (ratio 1,7) |
| CPA máximo tolerable | **27 USD** | **44 USD** |

Con 50% más de margen para pujar, **le ganás la subasta sistemáticamente**. Ver [[seleccion-y-modelado-de-oferta]] para el reverso: por qué clonar a alguien con backend es perder.

## La aritmética de apilar

Sin backend, tu AOV **es** tu precio. Con backend, deja de estarlo:

| Sin backend | Con backend |
|---|---|
| Producto de 197 → **AOV 197** | Producto de 197 + 3 order bumps de 20 + suscripción de 9/mes + upsells de 50 y 60 + downsells → **AOV 250–300** |

Y el caso extremo que Santiago cita como real:

> **Front de 7 USD con un AOV de 50 USD.** Solo con upsells, order bumps y downsells. Nada más.

Un ratio de 7×. El KPI de 1,5 es el suelo, no el techo.

> «He participado en lanzamientos donde **solo con los productos complementarios recuperé toda la inversión** publicitaria.»

## El dato base

> Entre un **30 y un 40% de las compras** entran con productos adicionales.

Condicionado a tres cosas: que los productos **complementen** de verdad, que sean irresistibles y que estén **bien presentados**. Un producto con solo imagen y título casi no se agrega.

## Qué construir, y cuándo

**Después de validar, nunca antes.** El orden es: validar una oferta → crear **5 o 6 productos adicionales** → recién entonces escalar fuerte.

De dónde salen esos productos:

1. **Los order bumps del competidor** al que modelaste
2. **Comprar su oferta** para ver qué ofrece post-pago

Caso real del material (`luego-de-validar...`), producto de herrería con 229 ventas del principal:

| Producto adicional | Ventas |
|---|---|
| 50 canapés creativos | 36 |
| (adicional 1) | 23 |
| Postres | 17 |
| Recetas de panes | 12 |
| Finger food para niños | 7 |
| Guía completa (post-pago) | 1 |

## Las dos ventanas de upsell

### Pre-compra — SellEasy

**Siempre genera fricción y siempre baja la conversión.** Eso se asume. El objetivo es que la subida de AOV compense de sobra la caída de pedidos.

Santiago probó **One Click Upsell, Essential Upsell y SellEasy**, y se quedó con **SellEasy**: es la que menos conversión sacrifica por AOV ganado. One Click Upsell permite descripciones en los productos, pero tarda 2–3 segundos en abrir el pop-up y esa demora cuesta conversión.

Se configuran **dos campañas distintas**:

| Tipo | Dónde aparece |
|---|---|
| **Venta adicional en el carrito** | Carrusel dentro del carrito |
| **Complementos de carrito** | Ventana emergente al pulsar «pagar pedido», ocupa 60–70% de pantalla |

Configuración que usa:

- Descuento del **60%** con las funciones de descuento de SellEasy
- Marcar «no mostrar productos que ya están en el carrito»
- Sin selección de cantidad, sin aleatorizar
- Copy del encabezado que le funciona muy bien: **«Quienes compraron este ebook también sumaron estos extras»**
- El **timer funciona en complementos de carrito pero no en la venta adicional del carrito**

Cifra que menciona como objetivo alcanzable: **ticket promedio de 34,65 USD con un front de 16,99**.

### Order bumps en el checkout

Solo posibles con **Hotmart** (ver [[shopify-y-checkout]]): Shopify únicamente permite modificar el checkout en su plan de ~2.000 USD/mes, y el plan Grow cuesta 66 USD.

**La descripción es lo que convierte.** Es el punto que Santiago subraya con más fuerza:

> «Por eso hay tantas aplicaciones de pre-sell upsell de Shopify que no funcionan un carajo. Porque tienen una imagen y el título del producto. **Lo que funciona es la descripción.**»

Anatomía de un order bump que convierte:

- **Precio tachado + % off** (14,99 → 7,99, «47% off»)
- **Descripción persuasiva**, no un título
- Fórmula de prueba social que usa: *«El 90% de los clientes nos recomendaron agregar este producto en este punto»*
- Y una descripción breve de qué se lleva
- **Complementario de verdad**: «si vendés zapatillas, ofrecé tres medias por el precio de una»

**KPI: un order bump debe convertir por encima del 20%.** Si no llega, se rota. En la práctica, uno bien montado **convierte entre el 30 y el 40%**.

> Circula por ahí la regla de «una venta de order bump cada 5 del producto principal» (20%). Santiago la corrige: eso es el **suelo**, no lo normal.

> Error común que señala al mirar la biblioteca de anuncios: gente escalando un producto con **los mismos tres order bumps un mes entero**. Hay que testear continuamente — sacarlo, cambiarlo, subirlo o bajarlo de posición, mover el precio.

**Pero equipo ganador no se cambia.** Si un order bump convierte al 40% y está primero, no se toca. Solo se rota cuando **baja el rendimiento**.

### Cómo se valida el backend

**Ciclo de una semana**, no de un día. Al cabo de la semana se sienta a mirar los números producto por producto.

La métrica que usa no es la conversión del bump, sino **cuánto revenue por visitante aporta cada producto adicional**:

> «Capaz que me generó 30 centavos. Pero yo sé que 30 centavos de dólar adicionales **por visitante al sitio web** me generó este producto.»

Es la forma correcta de compararlo con el costo por visita ([[metricas-y-kpis]]): cada céntimo que suma el backend al revenue por visita es margen que puedes gastar en tráfico más caro.

### Post-compra — Aftersell (antes One Click Upsell)

> «El upsell post pago es la mejor forma de upsellar.»

El argumento es psicológico: tienes al cliente en su **punto de máxima emocionalidad** —tarjeta ya pasada, pago aprobado, esperando el producto— y en una situación donde **un clic le debita más dinero**, sin volver a introducir datos.

> **Actualización:** esta restricción es de **Shopify**, no del método. Con **Impultienda** se puede hacer post-pago **desde Argentina** y en multidivisa. Ver [[shopify-y-checkout]].

**Restricción técnica en Shopify:** solo funciona con checkout en dólares. Requiere Shopify Payments, Stripe o PayPal, y **eliminar Shopify Markets**. Si vendes en pesos argentinos, no hay upsell post-pago. Con Markets activo solo lo ven quienes están en países con moneda dólar (EE.UU., Ecuador, El Salvador).

Se puede mantener el conversor de moneda en la landing y el carrito; lo que tiene que estar en dólares es el checkout.

La app actual es **Aftersell**; antes usaba One Click Upsell.

**Estructura del funnel post-pago:**

```
OTO 1  ──acepta──►  OTO 2
   │
 rechaza
   ▼
DOWNSELL (mismo producto, 25% menos)
```

El OTO 1 del ejemplo es un **bundle 5 en 1** que empaqueta los cinco upsells pre-compra como «sistema de facturación acelerada»: *«Te ahorra 75 dólares — a solo 25»*, con etiqueta Best Seller.

El copy del downsell es un buen ejemplo del registro que usa — empatía explícita y sacrificio visible:

> «No quiero que el dinero sea una razón por la que tu taller siga estancado… voy a hacer algo que mi contador me prohibiría. Prefiero perder yo esos 7 dólares de ganancia antes de que tú pierdas la oportunidad.»

**KPI: el take rate debe estar por encima del 15%.**

**Cómo subirlo:** el OTO tiene que **resolver el mismo problema del producto principal, pero mejor, más fácil y más rápido**. El cliente ya demostró que ese problema le importa. Ver [[embudo-vsl-post-pago]].

**Dato de referencia:** una tienda suya con front de **27 USD** y **AOV de 39,44** → ratio 1,44. Por debajo del KPI de 1,50, pero él lo considera aceptable.

Hay prompts dedicados a generar estas piezas: `prompt-crear-upsells` (ecosistema de productos encadenados) y `prompt-vsl-oto-post-purchase` (guion de video para el OTO, estructura de 8 puntos). Ver [[biblioteca-de-prompts]].

## Front y backend son variables independientes

Idea que abre una palanca que mucha gente no ve:

> «Podés tocar dos variables. Son variables diferentes.»

**Si el front está en profit, no lo toques.** Montá post-pago para subir AOV y ROAS, y listo.

**Si querés más volumen**, existe esta jugada:

```
Bajar el front  →  menos fricción  →  más conversión  →  CPA más bajo
       +
  Post-pago     →  compensa el AOV
```

El resultado buscado: **más flujo de clientes con el mismo AOV**. Se sacrifica margen unitario en el front y se recupera detrás.

**Cómo testearlo sin romper lo que funciona:** crear un producto nuevo con el precio más bajo **dentro de la misma landing** y dirigir tráfico ahí, dejando el original intacto.

### Ticket alto = menos volumen, y es matemático

Al vender tickets altos hay **más adspend y menos cantidad de ventas**. Es aritmética, no un problema.

> Una oferta en habla inglesa con **3–5 ventas el primer día** puede ser excelente: con CPA de 7 USD y ticket de 29, los números cierran.

Lo que importa es que se mantenga el ROAS, no el número de pedidos. Ver [[metricas-y-kpis]].

## Otras vías de remonetización

- **Secuencias de email** desde Shopify para relación a largo plazo (Flodesk)
- **Recupero de carritos** — hay lección dedicada
- **Low-ticket → consultoría high-ticket**, el salto de línea de negocio

## Complementos prácticos

- **AOV = facturación ÷ clientes**, no ÷ ventas.
- Ejemplo mínimo: front de 17 USD sin nada → AOV 17. El mismo front, con 5 order bumps de 10 USD vendidos en 10 ventas → **AOV 22**. Esos 5 USD son los que dejan aguantar la puja cuando la competencia sube.

### Mapa completo de dónde se ofrece algo más
1. Pre-compra en el carrito
2. Order bumps en el checkout
3. **Add-ons dentro de la propia sales page.** Los botones llevan a una sección de oferta con el «stack», un bloque de **add-ons recomendados (opcional)** y un botón que manda al checkout con todo cargado. Mete menos fricción que un carrito, pero también menos compromiso de compra. **Hay que testear cuál convierte mejor en cada producto.** Se genera con Claude igual que el carrito HTML.
4. Post-compra
5. **Email de largo plazo:** la venta puede llegar recién en el email nº 20, no en el primero.
6. **Comunidad de WhatsApp post-compra:** aportar valor y, de a poco, ofertar recompra.
7. **Lanzamientos afiliados de terceros:** invitar a la base de compradores a un lanzamiento ajeno del mismo nicho en Hotmart y cobrar comisión de afiliado (~60%) sobre el high-ticket. Monetiza la base sin crear producto.

### Los 5 order bumps que no se pisan
Cada bump ataca una objeción o necesidad distinta; ninguno promete lo mismo:
1. **Acelerador** (velocidad)
2. **Seguro / anti-error** (checklist de riesgos)
3. **Done-For-You** (plantillas para copiar y pegar)
4. **Swipe file / inspiración** (banco de ejemplos y casos)
5. **Toolkit / recursos externos** (proveedores, calculadoras, contratos)

Si los entregables son solo texto o PDF, **no se prometen videocursos** en el bump.

### Escalera de precios de referencia (variante)
- Order bumps **7–27 USD** → OTO1 **47–97** (el de mayor valor percibido) → downsell **27–37** si rechaza el OTO1 → OTO2 **37–67**. AOV objetivo ≈ **1,5× el front**.
- El bump pre-checkout es **opcional para el MVP**. No hace falta tenerlo para salir a validar.

### Aftersell: configuración
- Activarlo en **post-purchase upsell + thank you page + order status page**.
- Crear un «funnel» nuevo disparado por el producto principal. En cada oferta: headline y subheadline, **timer con el nombre del cliente** y minutos de reserva, imagen o carrusel, botones aceptar/rechazar y texto de garantía.
- Para no perder conversión con el checkout en USD, sumar una app de conversión visual (ej. **Currency Converter Plus**). El visitante sigue viendo su moneda en landing y carrito aunque el checkout cobre en dólares.

Relacionado: [[modelo-low-ticket]] · [[metricas-y-kpis]] · [[shopify-y-checkout]] · [[validacion-de-oferta]]
