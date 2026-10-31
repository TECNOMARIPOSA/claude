---
tema: Shopify y checkout
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/configuracion-tienda-de-shopify.md, RAW/formacion/lecciones/configurar-pantalla-de-pagos.md, RAW/formacion/lecciones/upselling-post-compra-one-clic-upsell.md, RAW/formacion/lecciones/rokt-after-sell.md, RAW/formacion/lecciones/carrito-html.md, RAW/contexto-chatgpt.md]
---

# Shopify y checkout

> ⚠️ **El método ya no usa Shopify. Todo se vende por Impultienda.** Lo que esta página dice de Shopify queda solo como referencia, para quien venga de ahí. La sección de Impultienda es la vigente.

Shopify fue la plataforma principal hasta que el método pasó a Impultienda. Tema base: **Dawn**.

## Setup inicial

Secuencia cubierta en el material, en orden: crear cuenta Gmail y Shopify → configuración de tienda → crear productos → conectar dominio → editar tema → configurar pantalla de pagos → instalar pixel → app de entrega automática.

Hay lecciones dedicadas a cada paso, incluida la **plantilla en blanco del theme Dawn**.

### Los detalles que rompen la tienda si se olvidan

**Plan:** empezar con el de **1 USD/mes durante 3 meses** para testear. Después el **Grow (~65 USD/mes)**, que cobra menos comisión — llega más dinero a tu Mercado Pago.

**⚠️ Configuración crítica:** activar **«preparar automáticamente las líneas de artículo del pedido»**.

> Shopify es una plataforma de e-commerce físico. Sin esa opción **espera que hagas el fulfillment** y el producto digital nunca se entrega.

**Métodos de pago** (Argentina): Mercado Pago tarjetas + **Checkout Pro** + **cuotas sin tarjeta**.

> Las cuotas sin tarjeta importan más de lo que parece: **la persona puede no tener plata en la cuenta y comprarte igual**, porque Mercado Pago se lo financia.

**Dominio:** un registro tipo **A** con nombre `@` y un registro **CNAME**, apuntando desde tu proveedor (Hostinger u otro). El mismo trámite que la verificación de dominio en Meta.

**Entrega automática:** app **Digital Downloads** del Shopify App Store. Se instala, se sube el PDF al producto y entrega solo.

**Al crear el producto:** destildar todas las opciones de producto físico (envío, inventario).

### Precio mínimo

> **De 15.000 pesos para arriba. Por debajo no vas a estar rentable.**

Con precio de comparación tachado alrededor de 29.999. Ver [[pagina-de-ventas]].

## La decisión de moneda

Es la decisión con más consecuencias del setup, y tiene un trade-off real:

| Con Shopify Markets | Sin Markets (todo en USD) |
|---|---|
| Checkout en moneda local | Checkout en dólares para todos |
| Mejor conversión de checkout (previsible) | **Habilita el upsell post-pago para todo el mundo** |
| Upsell post-pago solo visible en países con moneda USD | — |

Santiago dice no haber notado diferencias medibles de conversión entre Shopify Payments, Stripe y PayPal, y estaba planeando **eliminar los mercados y correr solo en dólares** para ver si sube el AOV sin sacrificar conversión.

Truco intermedio: mantener el **conversor de moneda en la landing y el carrito**, y dejar solo el checkout en dólares.

**Si vendes en pesos argentinos, no hay upsell post-pago.** Es una limitación dura de Shopify.

## Apps del funnel

| App | Función |
|---|---|
| **SellEasy** | Upsell pre-compra. La elegida tras comparar |
| **Aftersell** | Upsell post-compra (actual) |
| **One Click Upsell** | Upsell post-compra (anterior); también sirve pre-compra |
| **Sendvio** | Recupero de carritos y automatizaciones ([[email-y-automatizaciones]]) |
| **UTMify / Trackify** | Atribución ([[tracking-y-atribucion]]) |
| App de entrega automática | Entrega del producto digital |

Detalle de la configuración de upsells en [[aumento-de-aov]].

## Carrito y entrega

- **Carrito HTML** y **redirección al carrito** cuando la landing se hace con código — hay lecciones específicas, porque una landing en HTML puro necesita conectarse al carrito de Shopify a mano
- **Entrega de producto con código HTML** y app de entrega automática
- Elementos trabajados: cart, checkout, botones, Shop Pay, «Continue Shopping»

## KPI del checkout

**Inicio de checkout → compra: 25–30%.** Si el ratio cae ahí, el problema es del checkout, no de la landing. Ver [[metricas-y-kpis]].

Es una zona con problemas frecuentes: eventos que no se registran y apps que interfieren y hay que eliminar. Ante números raros, revisar el checkout antes que los creativos.

## Hotmart como checkout alternativo

No solo para lanzamientos: sirve como **pasarela de venta directa**, y en algunos escenarios es mejor que Shopify.

**Cómo se monta, si ya corres landing con código:** duplicar la página y **cambiar el link de los botones** para que apunten al checkout de Hotmart en vez del de Shopify. Eso es todo.

| | Shopify | Hotmart |
|---|---|---|
| **Conversión de checkout** | **~50%** | **~10%** |
| Por qué | La gente compra producto físico ahí y **confía en el checkout**. Y Mercado Pago Checkout Pro ya lo conocen | Menor, aunque ha mejorado (autodetecta email y métodos de pago previos) |
| **Order bumps en checkout** | Solo con el plan de ~2.000 USD/mes | **Sí, nativos** ([[aumento-de-aov]]) |
| **Conversión de moneda** | Vía Markets | **Automática**, al país del comprador |
| **Retiro de fondos** | Según pasarela | **Cada 2 días** (antes 14) |
| Plan recomendado | Grow, 66 USD/mes | — |

**Contrapartida de Hotmart:** las conversiones **tardan 3–4 días en aparecer** en su panel, lo que estrangula la toma de decisiones diaria. Shopify con Mercado Pago **liquida de inmediato**. Si estás escalando y necesitas decidir cada pocas horas, ese lag pesa — es el mismo problema que resuelve UTMify frente al pixel ([[tracking-y-atribucion]]).

El **retiro cada 2 días** es más importante de lo que parece. La versión cruda del problema, de cuando Hotmart liquidaba a 15 días:

> «Si quiero gastar mil dólares, tengo que tener **quince mil guardados**.»

Frente a Shopify + Mercado Pago: *«ayer hice mil dólares, hoy ya lo saqué y lo puse en Payoneer»*.

> Ojo con las fechas: en junio de 2025 Hotmart liquidaba a **15 días**; en noviembre de 2025 ya ofrecía **cada 2**. El dato mejoró, pero sigue por detrás de la liquidación inmediata.

**Cuándo usar Hotmart:** si no tienes acceso a Shopify Payments, si quieres order bumps sin pagar el plan caro, o para validar producto antes de montar tienda.

## Moneda local y precio psicológico

Hallazgo concreto del mercado argentino:

> Si tirás una campaña en Argentina y ponés el ebook a **9 dólares**, no vendés nada. **El precio en dólares le da temor a la gente.**
>
> A **19.000 pesos** —que liquidados son ~15 dólares, o sea *más caro*— la gente te compra.

No es el importe, es la **moneda**. Cobrar en la divisa local elimina una fricción psicológica que el precio bajo no compensa.

**Escalera de precio que recomienda:** salir a probar a **15.000**, y cuando la oferta funciona, subir a **19.000**. Coherente con el test de ticket de [[optimizacion-de-roas]]: subir el precio rara vez cuesta la conversión que uno teme.

## Impultienda — la tercera vía

> ⚠️ **Hoy la recomendación es Impultienda, no Shopify**, por la conversión del checkout.

**«Es como un Shopify para venta de productos digitales.»** Está en **beta**.

**Qué pide en el checkout:** solo **correo electrónico** + método de pago. A veces nombre y apellido; **el teléfono no es obligatorio**.

> El cuello de botella que más ve en alumnos y en quien le escribe **es la conversión del checkout**. Y en Shopify no se puede tocar: el checkout es fijo y pide dirección de residencia, nombre, apellido, correo… Cada campo es fricción.

> Contexto que conviene tener: la creó **un alumno de su consultoría** y se validó entre sus miembros —**100.000 USD facturados en 12 días** durante el testeo—. Santiago reparte un **código de referido** (`Bilbao`). La recomendación está respaldada por uso real, pero no es una evaluación neutral entre plataformas.

### Lo que resuelve

| | Shopify | Impultienda |
|---|---|---|
| **Post-pago desde Argentina** | ❌ Imposible (Mercado Pago Checkout Pro) | ✅ **Sí** |
| Campos del checkout | Dirección, nombre, apellido, teléfono… | **Solo email + método de pago** |
| Order bumps | Plan de 2.000 USD/mes | ✅ Nativos |
| OTOs post-pago | Vía app externa | ✅ **Ilimitados**, nativos |
| Multidivisa | Vía Markets, y rompe el post-pago | ✅ Comprador ve su moneda, **tú cobras en USD** (Stripe) — **y los OTOs también** |
| Dominio propio | ✅ | ✅ Ya lo soporta |

**El checkout mínimo es la clave**: menos campos, menos fricción. Santiago pide únicamente correo y método de pago. Incluye Apple Pay y Google Pay.

Y se pueden combinar: multidivisa para el mundo **+ Mercado Pago targeteado a Argentina**.

### Otras funciones

- Al crear la tienda, **genera ebooks, bonus y upsells con IA** a partir de una descripción
- Landing con editor visual o **custom HTML** pegado (que es lo que él hace)
- Mail de entrega personalizable
- **Recupero de carrito por email masivo y por WhatsApp** (si la persona deja su teléfono)
- Métricas por tienda: ticket promedio, visitantes en vivo

## Por qué el post-pago no funciona en Argentina (con Shopify)

Explicación técnica de la limitación ya señalada en [[aumento-de-aov]]: la mayoría en Argentina paga con **Mercado Pago**, y su **Checkout Pro es una pantalla de pago externa**. Al confirmar el pago no devuelve al usuario a la página de gracias, así que **no hay dónde mostrar el upsell post-compra**.

No es un problema de configuración: es cómo funciona esa pasarela.

## Alternativas de plataforma

Mencionadas en el material: **Hotmart** (con checkout propio y comisiones), **Gumroad**, **Payhip**, **Whop**, **Stripe**. Infraestructura financiera evaluada para operar internacionalmente: AstroPay, Payoneer, Trust Wallet.

## Complementos prácticos

### Setup de tienda: detalles que faltan
- **Un Gmail nuevo por tienda.** Sirve para dar de alta Shopify y como Drive donde viven los ebooks que se entregan.
- **Plan Grow: cobra solo 1% de comisión** sobre los pagos. Es el motivo concreto para pasar del plan de 1 USD/mes al Grow.
- **Prefijo de pedido:** en Configuración → General, arrancar la numeración en un número al azar (ej. 30) para que el número de orden no delate que la tienda es nueva.
- **Checkout:** sacar el link de seguimiento de arriba; pedir solo apellido (sin empresa ni línea de dirección 2).
- **Impuestos y aranceles:** desmarcar el cobro global. Es un producto digital y no corresponde.
- **Sacar la contraseña de la tienda** (Tienda online) antes de lanzar. Si queda puesta, nadie puede entrar.
- **Producto:** desactivar «cobrar impuestos» y las variantes. Editar el **identificador** (el slug de la URL) a una palabra corta y prolija.
- **PayPal** para vender afuera: pide **cuenta empresarial**.

### Dominio: la vía barata
- No comprar el dominio dentro de Shopify, sale caro. **Namecheap** propaga DNS muy rápido, y los dominios **`.lat` cuestan ~2 USD/año**.
- Registros que pide Shopify: **1 TXT** (verificación de propiedad) + **2 registros A** (uno con `@` y otro con `www`). Propaga en ~1 minuto. Después, marcarlo como **dominio principal**.

### Tema, carrito y texto de impuestos
- En Dawn solo se editan **carrito y checkout**. La home y la página de producto nativas no se usan, porque el tráfico va de la landing propia directo al carrito.
- Carrito: sacar encabezado y barra de anuncios, dejar ítems y subtotal. **Mismo color de botón en carrito y checkout** (Configuración del tema → Colores).
- **Reemplazar el aviso de «impuestos» del checkout**, que genera objeción, por algo como *«Acceso instantáneo post compra vía correo electrónico»*. Se cambia en Editar código → contenido del tema predeterminado, buscando el texto y reemplazándolo.

### Alojar la landing HTML en Shopify (sin hosting externo)
1. Contenido → Páginas → nueva página → «Mostrar HTML» → pegar el código → Visible → Guardar.
2. Si se ve rota en mobile, es porque el Liquid del tema interfiere. Editar código → Templates → **Add a new template** → tipo `page`, formato `liquid` (ej. `plantilla-en-blanco-landings`) → pegar el snippet de plantilla en blanco → Guardar.
3. Asignarle esa plantilla a la página del paso 1.
- **Alojarla en Shopify sube la carga** (visitas a la página de destino ÷ clics) **de ~60% a ~80–90%**, frente a un proveedor externo.
- Imágenes: subirlas en **Contenido → Archivos**, siempre en WebP, y pegar el link generado en el `src` del código.

### Botones → carrito, no checkout
- **Los botones de la landing van al carrito, no al checkout**, porque ahí se ofrecen los order bumps.
- Cómo armar el link: agregar **`.xml`** al final de la URL del producto, copiar el **primer número de variante** y usar **`https://tudominio.com/cart/{variante}:1`**.
- Excepción: si solo querés testear rápido y sin order bumps, usá el link directo del checkout. Se consigue simulando una compra y copiando la URL que aparece al tocar «Pagar pedido».
- En una landing hecha con imágenes dentro de Shopify: dejar solo **«Agregar al carrito»**, nunca «Comprar ahora», por la misma razón.

### Carrito HTML con order bumps, generado con Claude
- Se le pasa a Claude: un carrito de ejemplo ya armado, el código o PDF de la landing (para heredar tipografía y colores), la lista de productos a ofrecer y **`tudominio.com/products/producto.json`**, para que tome los IDs de variante reales.
- Instalación: pegar el bloque antes de `</body>` y cambiar el `href` de **todos** los botones por `onclick="openCart(); return false;"`. Si la landing es Liquid, va como plantilla personalizada.

### Pixel con la app oficial
- App **Facebook & Instagram** → conectar el BM → nivel de datos **«máximo»** → elegir el pixel, que se crea antes en Meta. Trackea sola Purchase, InitiateCheckout, AddToCart y PageView. **No la combines con el pixel de UTMify** si usás checkout externo: las ventas se cuentan dos veces. Elegí una sola fuente que le mande las compras a Meta ([[tracking-y-atribucion]]).

### Entrega: dos métodos a la vez, por redundancia
- **Digital Downloads:** un archivo por producto, incluidos bumps y upsells. Si hay varios bonus, conviene entregar un único **PDF «hub»** hecho en Canva, con links de Drive a cada ítem: bajan los reclamos de gente que no puede descargar todo.
- **Sacar el archivo de la página de gracias**, así esa pantalla queda para el upsell o VSL post-pago y la entrega va solo por mail.
- Plantilla de mail en español: botón «revertir a plantilla predeterminada», que la regenera en el idioma de la tienda.
- **Entrega por código, sin apps:** Configuración → Notificaciones → **Confirmación del pedido** → reemplazar el bloque de contenido por HTML propio con botones (Drive, grupo de WhatsApp, etc.).
- **Mantener las dos cosas a la vez** aunque el cliente reciba el aviso duplicado. Es preferible que le llegue dos veces a que no le llegue.

### Mail corporativo
- Cambiar el remitente `…@shopify-email.com` por uno del dominio propio. Se crea la casilla en el hosting (ej. Hostinger → Domains → Manage Email) y se verifican los DNS que pide Shopify.
- **Una sola casilla o webmail para todas las tiendas** permite centralizar y delegar la atención al cliente en una bandeja compartida.

### Plataformas
- **Multidivisa ≠ Markets.** Multidivisa convierte la moneda automáticamente; Markets fija a mano un precio por país.
- Si en la misma tienda vendés en ARS y en el resto de LatAm, **la multidivisa sola desajusta el precio en pesos**. Hay dos salidas: un Market manual por país (Argentina incluida) o **dos tiendas separadas** (una Argentina con Mercado Pago y otra multidivisa con Stripe o Whop).
- **Shopify:** en cuentas nuevas retiene los fondos más tiempo que Stripe.
- **Hotmart:** hay **alto riesgo de reembolsos** porque los otorga casi sin cuestionar.
- **Impultienda (estado reciente):** suma **dominios personalizados** (antes figuraba que no), apps móviles nativas (primero Android), tracking propio (**Utmiflow**), personalización del checkout con HTML, integración con **Whop** y Stripe, y entrega y remarketing por WhatsApp. **No** soportaba productos físicos ni suscripciones con Mercado Pago.

Relacionado: [[aumento-de-aov]] · [[tracking-y-atribucion]] · [[pagina-de-ventas]] · [[stack-de-herramientas]]
