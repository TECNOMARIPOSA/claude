---
tema: Email y automatizaciones
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/recupero-de-carritos.md, RAW/formacion/lecciones/mail-corporativo.md, RAW/contexto-chatgpt.md]
---

# Email y automatizaciones

Es la tercera vía de remonetización, después de los upsells pre y post compra ([[aumento-de-aov]]). Santiago la señala como una de las ventajas grandes de Shopify: permite construir relación a largo plazo con el cliente sin coste de adquisición.

## Recupero de carritos abandonados

App: **Sendvio** (empieza gratis). Se instala, se activa en el tema y se configura el remitente.

### La secuencia que configura

Seis emails con descuento escalonado:

| # | Cuándo | Descuento |
|---|---|---|
| 1 | 5 minutos | — |
| 2 | 1 hora | 10% |
| 3 | 3 horas | 10% |
| 4 | 6 horas | 10% |
| 5 | 2 días | **30%** |
| 6 | +3–4 días | 30% |

La lógica: el aviso inmediato no quema descuento, y el 30% se reserva para cuando el carrito ya está frío.

### Detalle sobre el dominio

Si el dominio no se puede autenticar (por estar asociado a otra cuenta, o sin DKIM/DMARC), **los emails se envían igual**. El único riesgo es caer en spam. No es bloqueante para arrancar.

Hay casos de **Gmail rechazando emails** por la configuración del dominio: la autenticación merece atención cuando el volumen crece.

## Otras automatizaciones

Desde el mismo panel se configuran flujos adicionales:

- **Agradecimiento por primera compra** — bienvenida a los 5 minutos, y a los 7 días un email mostrando otros productos con descuento
- **Petición de reseñas**
- **Recompensa a clientes leales**

Todas siguen el mismo patrón: plantilla base + edición de asunto y contenido.

## Stack de email

| Herramienta | Uso |
|---|---|
| **Sendvio** | Automatizaciones dentro de Shopify (carritos, post-compra) |
| **Flodesk** | Email marketing, listas, campañas |
| **Mail corporativo** | Hay lección dedicada al setup |

Con Flodesk se ha trabajado limpieza de listas y double opt-in.

## WhatsApp

Canal paralelo, usado tanto para tráfico como para retención:

- Ads → WhatsApp como funnel de entrada
- Comunidades **VIP**
- Seguimiento de consultoría
- **ManyChat** conectado a Instagram

Ojo: si Instagram está conectado a ManyChat a través de un perfil de Facebook que después se bloquea, reconectarlo a otro ManyChat da problemas. Conectalo con un perfil estable.

## Complementos prácticos

- **Remitente:** usar el nombre real de la marca, no uno genérico del nicho. Si el dominio principal ya está asociado a otra cuenta de email, **autenticar un subdominio**.
- **El descuento del carrito abandonado por email es del 30%.** Recupera bastantes más ventas que un 10%, y a veces el cliente termina comprando el upsell en vez del producto original.
- Referencia de e-commerce físico: un flujo bien armado (3 emails con demoras escalonadas y descuento creciente) puede llegar a ser **~20% de la facturación**.
- **WhatsApp vs. email según el mercado:** en LatAm hispanohablante, la entrega y el remarketing por WhatsApp convierten mejor que el email, porque el mail cae en Promociones y no se abre. **En habla inglesa, el email y el SMS rindieron más** que WhatsApp.
- **Calentar el número** de WhatsApp Business o API antes de mandar notificaciones de entrega en volumen, para que no lo bloqueen.
- **El teléfono no es obligatorio en el checkout.** Cada campo de más es fricción.

Relacionado: [[aumento-de-aov]] · [[shopify-y-checkout]] · [[stack-de-herramientas]] · [[modelo-low-ticket]]
