---
tema: Disputas, contracargos y reembolsos
actualizado: 2026-09-24
fuentes: [clases de la formación y experiencias de la comunidad, agosto–septiembre 2026]
---

# Disputas, contracargos y reembolsos

**Un contracargo te cuesta mucho más que un reembolso.** Por eso hay dos posturas, y las dos necesitan la misma base: una página pública de términos con una garantía clara.

## El límite que no hay que pasar

**~0,9–1% de contracargos.** Por encima de eso, Hotmart, PayPal y los procesadores empiezan a restringir productos o cuentas.

## La base: términos y condiciones

- Publicá **Términos y Condiciones** con una ventana de garantía clara (por ejemplo, **7 días**), y hacé que se acepten en el checkout.
- Ponele **causas concretas** a la garantía. Por ejemplo: "solo hay devolución si se consumió menos del 5% del contenido" o "si hubo un error técnico documentado que impidió usarlo y soporte no respondió".
- Esa página sirve para dos cosas: filtrar a quién reembolsar y tener un argumento para defender cada disputa. Sin ella, no hay con qué defenderse.
- También ayuda a pasar la revisión de Stripe ([[procesadores-de-pago]]).

## Postura 1: reembolsar sin pelear

- Ante cualquier reclamo, se devuelve la plata antes de que se convierta en contracargo.
- Pelear disputas de Stripe **rara vez se gana**, incluso con pruebas sólidas (hay mucho "fraude amistoso"), y cada disputa cobra un fee.
- Si no las vas a pelear, **desactivá la respuesta automática de Stripe**.

## Postura 2: pelearlas con Claude Code

1. Abrí **Claude Code desde la carpeta del segundo cerebro**, para que tenga todo el contexto del negocio.
2. Conectá Stripe y MercadoPago. Lo mejor es por **MCP, CLI o API**. Si la plataforma no tiene ninguno, usá **Claude en Chrome** con una pestaña real. Alcanza con pasarle los links de la documentación y decirle "quiero conectar mi Stripe y mi MercadoPago": te guía paso a paso.
3. Pasale el link de tu página de términos.
4. Pedile que revise las disputas abiertas y responda cada una con las pruebas y los términos.
5. **Automatizalo:** pedile una rutina que cada **12 horas** busque disputas nuevas y responda las que tengas a favor.

## Evitar la disputa antes de que pase

- **Entrega automática redundante:** dos métodos de entrega a la vez, así nadie dice que no le llegó ([[shopify-y-checkout]]).
- **Seguimiento de pagos fallidos** automatizado con Claude conectado a Stripe o MercadoPago. Guardá la prueba de entrega de cada venta.

## Pasar la revisión de Stripe

- Cuando Stripe bloquea una cuenta, **casi nunca es por fraude**: falta una landing pública clara sobre el negocio.
- Lo que ayuda a que la aprueben: descripción del negocio, precios claros, contacto de soporte y una **política de reembolso y cancelación visible y coherente con lo declarado en Stripe**.
- **Términos y Condiciones** que funcionaron: Titular · Aceptación · Producto y entrega · Precio y pago · Garantía y reembolsos (ventana de **7 días**) · Propiedad intelectual · Resultados · Privacidad · Contacto y soporte. Van en el pie de página y enlazados desde la landing que se declara en Stripe.
- Hotmart reembolsa casi sin cuestionar. Hay que contarlo en el cálculo de margen.

Relacionado: [[procesadores-de-pago]] · [[llc-banca-y-fiscal]] · [[email-y-automatizaciones]]
