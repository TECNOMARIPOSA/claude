---
tema: Tracking y atribución
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/tracking-avanzado-creando-y-configurando-utmifi.md, RAW/formacion/lecciones/solucion-tracking.md, RAW/formacion/lecciones/instalar-el-pixel-de-utmify-y-correr-diferentes-productos-en-1-sola-cuenta-de-shopify.md, RAW/formacion/lecciones/instala-el-pixel-con-app.md, RAW/contexto-chatgpt.md]
---

# Tracking y atribución

## El problema que resuelve

El pixel de Meta con la integración nativa de Shopify **tarda entre 30 minutos y una hora** en reflejar las conversiones. Con escala normal es tolerable; con escala agresiva es caro:

> Apagás campañas que realmente están rentables. Al final del día filtrás por ayer y te das cuenta de que apagaste algo que te estaba imprimiendo dinero.

Es un problema específico de las estructuras que exigen revisar 4 veces al día —CostCap, bid cap, ROAS cap— donde se toman decisiones cada pocas horas. Ver [[escalado-en-meta-ads]].

## La solución: UTMify

Plataforma brasileña (`utmify.com.br`) que trackea **en tiempo real por UTMs** en lugar de por pixel. Los UTMs son códigos únicos que el cliente arrastra desde el anuncio hasta la venta aprobada, así que la atribución no depende del lag de Meta.

### Configuración, en cuatro piezas

**1. Webhooks de Shopify → UTMify.** Hay que crear **cuatro**, todos apuntando al mismo URL, formato JSON, versión más reciente:

- Creación del pedido
- Actualización del pedido
- Pago del pedido
- Cancelación del pedido

**2. Script de UTMs en el tema.** Se pega en `theme.liquid`, **antes del `</body>`**.

**3. Parámetros de URL en TODOS los anuncios.** El código va en *Seguimiento → Parámetros de URL* al crear cada anuncio. Sin excepción — si falta en un anuncio, ese anuncio no se atribuye.

> Consejo del material: guardar ese código en un bloc de notas para no entrar a UTMify cada vez.

**4. Pixel de UTMify.** Configuración concreta:

| Ajuste | Valor |
|---|---|
| Regla de add to cart | **Deshabilitado** |
| Regla de inicio de checkout | **Habilitado**, «contiene URL» = URL de la tienda |
| Ventas | Solo ventas aprobadas |

El código que devuelve se pega también en `theme.liquid`.

## Stack con quiz + checkout externo

Configuración concreta para el montaje más complejo que aparece en el material: **InLead** (quiz) + **Shopify** (pago y pop-up) + **Impultienda** (checkout).

| Dónde | Qué va |
|---|---|
| **Impultienda** | **ID del pixel** + **token** del pixel |
| **UTMify** | Se conecta con **credencial de API** — *no* pegando el código |
| **Shopify** | Instalar la app de **Facebook e Instagram** (envía la data limpia a Meta) |
| **InLead — `<head>`** | **Código capturador de UTMs** + cloaker |
| **InLead — `<body>`** | Capturador |

**El error más común:** falta el **capturador de UTMs en el head de InLead**. Sin él, las UTMs **no se sostienen a lo largo del quiz** y las ventas llegan sin atribución.

Caso real: un alumno con 50–60 ventas diarias sin trackear estaba **apagando anuncios a ojo** y llegó a matar creativos con **ROAS 3**. Bien configurado, la pérdida es de 1 o 2 ventas por cada 100.

> Nota: **Impultienda** es el nombre real de la plataforma. En una transcripción anterior aparecía distorsionado y quedó marcado como dudoso — queda confirmado aquí. Ver [[embudo-vsl-post-pago]].

## Un dashboard de UTMify por oferta

UTMify permite crear **dashboards** (subcuentas) dentro de la misma cuenta. Lo normal es **uno por oferta**.

Se crean en *Avanzado → Nuevo dashboard*. Dos ajustes que deciden si los números sirven:

- **Zona horaria**: la misma que tengas en el checkout **y** en la cuenta publicitaria. Si no coinciden, los días no cuadran
- **Costos de la pasarela de pagos** — porcentuales y fijos. Sin esto, el profit que muestra el panel es bruto y engaña

Ver también la regla de un pixel por tienda, más abajo.

> Santiago conecta los perfiles de Facebook a UTMify vía **Multilogin**, el navegador antidetección que usa para mantener fingerprint e IP separados por perfil. Ver [[contingencia-de-cuentas]].

## La regla de arquitectura

> **Un dashboard, un pixel, una tienda, un producto.**

Se pueden correr varios productos en la misma tienda **solo si comparten el mismo pixel**. Si no comparten pixel, la atribución se rompe.

Recomendación de Santiago: **aislar un producto por tienda**. Quien quiera tienda multiproducto de verdad, que use **Trackify** en lugar de UTMify.

## Cuando el pixel deja de marcar conversiones

Caso frecuente en las mentorías: hay ventas reales en Shopify pero **Meta no las atribuye a ningún anuncio**. Es paralizante, porque sin saber qué creativo vendió no se puede decidir nada.

**Checklist de diagnóstico:**

1. El **pixel está vinculado** a la app de Facebook e Instagram en Shopify
2. La **cuenta publicitaria está habilitada** dentro de ese pixel (*Canales de venta → Facebook e Instagram → cuentas publicitarias*)
3. El **dominio está verificado**: Administrador de eventos → Configuraciones → **Permiso de tráfico**
4. En la campaña está seleccionado **ese** pixel

**Si todo está bien y aun así no marca:** desinstalar la app de Facebook e Instagram en Shopify y **volver a instalarla**. No afecta a las campañas en curso.

### Qué hacer mientras tanto

**Calcular la conversión a mano:** ventas de Shopify ÷ visitas. Si tuviste 10 ventas y 500 visitas, tu comprate es 2% — no hace falta que Meta te lo diga.

**Rastrear el origen de las ventas desde Shopify** con el identificador de pedido, que indica de qué anuncio vino cada una.

> Sin esto, la única alternativa es volver a testear de cero, porque no sabés qué creativo funcionó.

## Cuando Meta recategoriza tu pixel

Caso real de una mentoría: a un alumno le **recategorizaron el pixel** como si vendiera productos religiosos, y **se cayeron todas las ventas** al recibir el aviso.

**Solución: cambiar el pixel *y* el dominio.** No basta con el pixel.

> El dominio queda **enganchado al pixel**. Si creás un pixel nuevo y lo enlazás al mismo dominio, te lo tumban también.

Es otra razón para tener [[contingencia-de-cuentas]] y varios dominios preparados ([[funnel-hacking]]).

## Historial de problemas de tracking

Fricciones frecuentes con el tracking de Shopify + Meta: eventos inactivos, problemas con Omega Pixel, checkout que no registraba eventos, aplicaciones que interferían y que hubo que eliminar.

Es un área frágil que conviene verificar cuando las métricas no cuadran, antes de concluir que el problema es creativo.



## Ventas contadas dos veces

El método ya no usa Shopify. Si venís de Shopify y todavía tenés la app de Facebook e Instagram instalada junto al pixel de UTMify, **desinstalala**: Meta cuenta cada venta dos veces. Ante la duda, la verdad son las ventas del checkout.

## El país de UTMify no es confiable

El desglose por país del comprador que muestra UTMify **puede agrupar toda LatAm en un solo país**. En un caso real reportó el 100% de las ventas en Argentina, mientras el pixel de Meta mostraba compras en México, España y Estados Unidos.

- **Nunca decidas el targeting por país con ese dato**: ni cortar, ni abrir, ni segmentar.
- Para leer por país, usá el desglose por país del Administrador de Anuncios, y aun así tomalo como una orientación.
- UTMify sí es la fuente de verdad para **facturación, ventas aprobadas y pendientes, CPA y ROAS real**.

## Herramientas

- **UTMify** — atribución en tiempo real por UTMs (la principal)
- **Trackify** — alternativa para tiendas multiproducto
- **Pixel de Meta** — base, con el lag conocido
- Instalación del pixel vía app: hay lección dedicada

## Complementos prácticos

- **UTMs que se pierden en la sales page:** pegar el script capturador de UTMs debajo del HTML de la landing. Sin él se pierden en el paso intermedio.
- El **pixel de UTMify y el script capturador van juntos**, uno debajo del otro, en `theme.liquid` antes de `</body>`. Al crear el pixel en UTMify se le pone nombre + **token de acceso**.
- **Una credencial de API por checkout.** No se comparte entre productos de la misma tienda. Si hay más de una tienda o checkout, los webhooks se repiten en cada una.
- **Hotmart:** configurar el webhook o GTM para capturar **todos los productos**, no solo el principal. Si no, los upsells no suman al ingreso y el CPA real queda subestimado.
- **Qué número manda cuando no coinciden:** en un caso, Meta reportó **64% más ventas** de las reales. El dato del checkout o de la plataforma de cobro es la verdad.
- **RPC (revenue per click) = valor de conversión total ÷ clics en el enlace.** Por país, se compara RPC vs. CPC y **se cortan los países donde el RPC es menor al CPC**.
- **Leer en ventanas móviles de 3 y 7 días**, no día por día.
- **Utmiflow** (de Impultienda) es una alternativa nativa en tiempo real. En varios casos fue más rápida que UTMify.
- UTMify tiene integración **MCP con Claude** para consultar métricas en lenguaje natural.

Relacionado: [[shopify-y-checkout]] · [[escalado-en-meta-ads]] · [[metricas-y-kpis]] · [[stack-de-herramientas]]
