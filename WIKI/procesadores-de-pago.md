---
tema: Procesadores de pago
actualizado: 2026-09-24
fuentes: [clases de la formación y experiencias de la comunidad, agosto–septiembre 2026]
---

# Procesadores de pago

**Cada procesador tiene un trade-off entre pagos rechazados, disputas y velocidad para cobrar.** Por eso se usan varios a la vez y nunca se concentra la plata en uno solo ([[llc-banca-y-fiscal]]).

| Procesador | Necesita LLC | A favor | En contra |
|---|---|---|---|
| **Stripe** | Sí | El estándar, menos pagos rechazados | Mira con lupa las cuentas nuevas y los picos de volumen. Las disputas casi nunca se ganan |
| **Whop** | No (verificación individual) | Multidivisa automática, más resistente a las disputas | Más pagos rechazados que Stripe en varios casos |
| **MercadoPago** | No | Mercado local | Rechazos sin motivo aparente |
| **PayPal** | No | Suma volumen | Mucha exposición a contracargos |

## Stripe

- Te liquida en **2 a 7 días hábiles**, según la antigüedad y la salud de la cuenta.
- Las cuentas nuevas están más vigiladas, sobre todo ante subas bruscas de volumen. Escalá de forma gradual.
- Si hay muchos pagos rechazados, activar **3D Secure** puede ayudar. No a todos les funcionó.
- Para pasar la revisión, publicá una página de empresa y de términos ([[disputas-y-reembolsos]]).

## Whop

- Tiene una **tarjeta propia** con la que podés usar al instante el saldo que todavía no se liquidó, pagando **~2% extra**. Si no, la liquidación normal tarda de 3 a 7 días.
- Retiros: casi siempre en **USDT** (TRC20 o Solana, menos comisión) hacia un exchange o P2P.
- **Reintento de pagos fallidos en los OTO: esperá 10–15 minutos.** Si reintentás muy rápido o muy tarde, aumentan los bloqueos.

## MercadoPago

Si empieza a rechazar pagos sin motivo, **renová las credenciales de producción** (Public Key y Access Token, o Client ID y Secret) desde MercadoPago Developers. Suele resolverse al instante.

## PayPal

Se recomienda **desactivarlo en Shopify** por el riesgo de contracargos. Hay quien lo deja por el volumen extra, asumiendo ese riesgo.

Relacionado: [[shopify-y-checkout]] · [[disputas-y-reembolsos]] · [[diagnostico-de-checkout]]
