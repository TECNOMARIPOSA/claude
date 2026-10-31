---
tema: Escalado en Meta Ads
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/tipos-de-escala.md, RAW/formacion/lecciones/clase-mas-importante-como-testear-y-escalar.md, RAW/formacion/lecciones/set-up-campana-desde-0.md, RAW/contexto-chatgpt.md]
---

# Escalado en Meta Ads

Dos vectores, y el orden importa:

1. **Diversificación creativa** — la escala estable. Más creativos nuevos cada día.
2. **Escala vertical** — subir presupuesto sobre lo que ya gana.

> «Yo he escalado a 1.000, 2.000 dólares al día solamente con nuevos creativos. Ni siquiera con campañas raras.»
> (`RAW/formacion/lecciones/set-up-campana-desde-0.md`)

Es un punto que conviene no perder de vista: las estructuras de campaña de más abajo son un multiplicador, no el motor. El motor es el volumen creativo de [[testeo-de-creativos]].

## De 6 ofertas validadas, escala 1

Expectativa que conviene tener antes de frustrarse:

> «De **seis ofertas validadas** —es decir, que ya están en profit— **solo una va a escalar agresivo**, la que vas a poder llevar a números tipo 11.000 de revenue en un día.»

**Validar ≠ escalar.** Una oferta puede ser rentable y aun así tener techo. Es otra razón para mantener el flujo constante de ofertas nuevas ([[modelo-low-ticket]]).

## Escala vertical

Condición de entrada: **7–10 compras en unos 3 días a buen CPA**.

Hay dos ritmos según cuánto riesgo quieras:

| Ritmo | Incremento diario | Condición |
|---|---|---|
| **Conservador** | **+25–30%** sobre el adset (ABO) o la campaña (CBO) | Mientras el **ROAS supere 1,5** |
| Prudente | **+15%** | El que aparece en la clase base |

Progresión conservadora desde 10 USD: **10 → 12,5 → 16 → 20 → 26**…

**Solo una subida al día**, no más. Si un día sube y al siguiente no vende, no se vuelve a subir — se deja quieto. Si se recupera, se sigue subiendo.

Alternativa: duplicar el conjunto ganador dentro de la misma ABO, o aislarlo en una **CBO 1-1-1** (una campaña, un conjunto, el anuncio ganador) a 10 USD y aplicarle la misma lógica de corte.

## El ritmo semanal: subir el estándar

El patrón operativo que ordena la semana (`RAW/formacion/mentorias/mentoria-2025-09-24.md`):

| Días | Qué se hace |
|---|---|
| Lunes a miércoles | **Testear** — mínimo 10 creativos al día |
| **Jueves a domingo** | **Duplicar** los ganadores acumulados |

La lógica: durante la semana se construye una base de creativos validados; el fin de semana se meten dúplicas y **se sube el «estándar» de facturación diaria**.

> Venís con un estándar de 500.000/día → metés dúplicas el finde → pasás a 600.000 → la semana siguiente apuntás a 700.000–800.000.

Es escalado por escalones, no lineal: cada fin de semana fija un nuevo piso.

### La mayoría de las dúplicas no vende

Expectativa realista, para no interpretarlo como fracaso:

> «Yo dupliqué por 10 y al menos **5 o 6 no me han vendido**.»

**Regla de corte:** si una dúplica gasta **~4 USD sin vender**, se corta. A ese ritmo lleva unos dos días y medio corriendo, suficiente para que Meta encuentre comprador en ese pool de audiencia. Si no lo encontró, no lo va a encontrar.

### Ajuste fino contra el CPA break-even

Con un break-even de 12 USD, los umbrales que usa:

| Costo por resultado | Acción |
|---|---|
| Llega a **10** | **Bajar el presupuesto un 30%** |
| Llega a **11** | **Cortar** |

Y una regla que evita un error común:

> Cuando un anuncio se cae a 11, **no dupliques ese**. Duplicá **el original**, que sigue corriendo bien.

### Qué pasa con la conversión al duplicar

**Se rompe, y es normal.** Al meter mucho tráfico de golpe la conversión de la landing baja el primer día.

> «No te asustes. Lo importante es que siempre mires el **CPA**.»

Y el dato que lo hace tolerable:

> «Yo salgo en profit con una conversión del **1,5%**. Poco profit, pero salgo. ¿Por qué? Porque los anuncios son muy clickables.»

El 2,5% sigue siendo el objetivo ([[metricas-y-kpis]]), pero un CPC muy bajo compra margen para tolerar menos conversión. Otra vez la misma ecuación: costo por visita vs. revenue por visita.

## Bid automático vs. bid manual

Marco que ordena todas las estructuras de abajo.

**Bid automático — «volumen o valor más alto»**
Le das libertad total a Meta. Es la estrategia normal, la que se usa **tanto para testear como para escalar**.

> **«Valor más alto» es para cuando tenés un buen backend.** Con backend le pedís que maximice valor de compra, no cantidad de conversiones. Ver [[aumento-de-aov]].

**Bid manual — tres variantes**

| Estrategia | Qué le dices a Meta |
|---|---|
| **Objetivo de costo por resultado** (CostCap) | No gastes si no conseguís ventas a este CPA |
| **Objetivo de ROAS** | No gastes si no alcanzás este ROAS |
| **Límite de puja** (BidCap) | No pujes por encima de esto |

En las tres, **si Meta no puede cumplir el parámetro, no entra a subasta**.

### La regla de reparto de la cuenta

> Para invertir más presupuesto necesitás **una parte de la cuenta en manual bid y otra en bid automático**.
>
> **No podés tener todo en manual bid.** Todo en automático sí se puede.

Es una restricción estructural: las campañas manuales solas no absorben presupuesto porque se autolimitan.

## Las tres estructuras de escala

Todas requieren **anuncios ya ganadores** (≥5 compras a buen CPA). No se usan para descubrir, se usan para exprimir.

### 1. CostCap — escala agresiva por picos

Campaña ABO usando el **objetivo de costo por resultado**. Le dices a Meta cuánto estás dispuesto a pagar y Meta solo gasta si consigue ese costo.

- **7 conjuntos**, todos con **el mismo anuncio ganador**
- Presupuesto **15–25 USD por conjunto**
- Bids escalonados: 4, 5, 6, 7, 8, 9, 10 USD (el del medio ≈ mitad del ticket)

Operativa diaria:

- Revisar **4 veces al día**. Es la estructura que más seguimiento pide
- A las 9–10 h: los que no arrancaron, cortar. Los que vendieron a buen costo, **duplicar presupuesto**
- Si sigue vendiendo, duplicar otra vez (50 → 100 → 200 USD)
- Si un conjunto se dispara de costo, cortar
- **Por la noche, resetear toda la campaña a cero**: todos los conjuntos vuelven al presupuesto base y se reactivan

Es normal que casi ningún conjunto arranque: en el ejemplo del material, de 49 conjuntos arrancó uno, con una compra a 3 USD. El freno lo pone Meta.

**No sirve para consistencia.** Es para reventar días concretos que ya vienen bien. Si nunca arranca en dos días, subir los bids.

Truco: si un conjunto validó (3 compras a 3 USD), duplicar presupuesto **y subir el bid** a la vez — le dice a Meta que hay margen y el presupuesto «se patina en minutos».

### 2. CBO de ganadores

Campaña CBO con **3–5 conjuntos, cada uno con un anuncio ganador distinto** (aquí sí, anuncios diferentes). Pone a competir a todos los ganadores entre sí.

La táctica: lanzar **5 CBOs idénticas con presupuestos distintos** (30 / 40 / 50 / 60 / 70 USD) y ver cuál «agarra viaje». Las que llegan al CPA sin vender se cortan; la que engancha se deja correr.

### 3. Micro presupuesto

Campaña ABO con **10–20 conjuntos, todos con el mismo anuncio ganador**, a **2,77 USD cada uno**.

La lógica es exigirle a Facebook una conversión con un gasto diario mínimo. No se optimiza nunca —un conjunto necesita 50 conversiones en 7 días para eso— pero saca conversiones baratas por fuerza bruta.

- Si un conjunto gasta 4–6 USD sin vender, apagar
- Los que dan costos regalados, duplicarlos varias veces
- Alternativa: llevar los buenos directamente a 10 USD

### 4. BidCap acelerada

CBO con **límite de puja** en vez de auto-bidding, y **tipo de entrega: acelerada**.

- Presupuesto: mínimo 100 USD, Santiago la arranca en **500 USD**
- Un conjunto por cada anuncio ganador (los que tengas: 2, 10, 100)
- **Bid inicial = el precio del front.** Si vendes a 19,99, el bid va en 9,99 según el ejemplo del material
- Si no gasta: **subir 50 centavos cada hora** hasta que arranque

Al ser manual bidding y estar capeada, **aguanta escalas mucho más agresivas**: se puede cambiar presupuesto y bid sin que se desmadre.

El diagnóstico que da si no funciona es directo:

> «Si no te vende es porque tus anuncios son una mierda, o tu oferta no pega, o tenés mal redactado el landing page.»

### 5. Intrapuja

Qué hacer **después** de que una CostCap o BidCap encuentre su puja ganadora. Es un test de puja en dos niveles.

Partiendo de una CostCap para ticket de 20 USD (presupuesto 50 USD/conjunto, bid central = ticket ÷ 2 = 10, y de ahí 3 hacia arriba y 3 hacia abajo):

1. El conjunto con **bid 10** empieza a vender → surfear presupuesto
2. **Duplicar ese conjunto × 9** → quedan bids 10.1, 10.2 … 10.9
3. Si gana el **10.6**, repetir: **10.6 × 9** → 10.61, 10.62 … 10.69

Eso es la **intrapuja de la intrapuja**. Misma lógica para BidCap, que arranca con el bid en el precio del front y baja de uno en uno (20, 19, 18, 17, 16, 15, 14).

La diferencia con la CostCap básica: aquí **se pueden meter varios anuncios ganadores**, no solo uno.

### Una vez que el bid está validado, no se vuelve a testear

El atajo que ahorra el trabajo entero a partir de la segunda vez:

> Si validaste que el bid ganador es **10,70**, todos los winners nuevos que saques los tirás **directamente en 10,70**.

El test de puja se hace una vez por oferta, no por creativo. Después es solo cargar ganadores en la estructura que ya sabés que funciona.

### Operativa diaria de estas campañas

- **Activar a medianoche**
- **Primer vistazo a las 9 de la mañana**: los que vendieron, duplicar presupuesto (+50% o +100% según ROAS)
- Los bids que **gastaron y no vendieron**, apagar. Los que no gastaron, no pasa nada
- **Reiniciar todo al día siguiente**

### 6. Aislada — ABO y CBO

La estructura más simple y la que más usa día a día. **Existe en dos versiones**, y lanza las dos:

| | ABO aislada | CBO aislada |
|---|---|---|
| Estructura | 3 conjuntos, **el mismo creativo winner** en cada uno | Idéntica |
| Presupuesto | **3× CPA medio por conjunto** | **3× CPA medio a nivel campaña** |
| Optimización | Volumen más alto | Volumen más alto |

**CPA medio = ticket ÷ 2** ([[testeo-de-creativos]]).

Al ser CBO, la campaña reparte sola y **encuentra qué público funciona mejor** para ese creativo.

### El día 2

Con testeo acelerado (3× CPA medio) suelen aparecer creativos con 3–5 ventas ya el primer o segundo día. Esos ganadores van directos a:

1. **ABO aislada**
2. **CBO aislada**
3. **CostCap** con 7 conjuntos — para testear el bid

La lógica: la CBO reparte sola y **encuentra qué público funciona mejor para ese creativo**.

> «Es como una mini launch pocket.»

### 7. Las «Pocket» — dos variantes

Se parecen y conviene no confundirlas:

| | **CBO Pocket** | **Launch Pocket** |
|---|---|---|
| Conjuntos | **8** | **10** |
| Contenido | **El mismo** anuncio ganador en los 8 | **3–6 winners** distintos, duplicados |
| Presupuesto (CBO) | **75% del front** | **3–5× el precio del front** |
| Cuándo | Tenés **un** creativo ganador | Tenés varios |

Presupuesto de la Launch Pocket en concreto: front de 10 USD → **30–50 USD/día**; front de 20 → **60–100 USD/día**.

**Lógica de la CBO Pocket:** el mismo creativo en 8 audiencias distintas, y **Meta redirige el presupuesto hacia los conjuntos que rinden**.

**Presupuesto: 75% del precio del front** (o el precio del front entero para arrancar).

#### Cómo se opera una Pocket

> **⚠️ Las CBO se analizan SIEMPRE a nivel campaña**, nunca conjunto por conjunto. Es la pregunta que más le hacen y la respuesta no cambia.

- Dejar correr **48–72 horas** al presupuesto inicial
- **Cada 48 h: apagar los conjuntos caros o sin gasto** — así el presupuesto se redirige a los que funcionan
- Si a las **24 h no genera ninguna venta**, apagar y pasar a otro creativo. Con el 75% del front en juego, se pierde dinero rápido
- **Escala conservadora: cada 24 h, si el ROAS supera 1,8, subir presupuesto**

## El flujo actual: saltarse el testeo

Cómo encadena hoy las estructuras, que **no coincide** con el flujo clásico de [[testeo-de-creativos]]:

```
PRE-TESTEO ──vendió──────────► Aislada (doble) + CostCap
     └──────CPC bajo─────────► Launch Pocket
```

Se **salta la fase de testeo intermedia**. Lo que vendió en pre-testeo va directo a estructuras de escala.

La Launch Pocket cumple una función concreta:

> Aprovechar los anuncios con **CPC bajo** que aún no vendieron. Si no, matás muchos que tenían potencial **solo porque gastaron poco presupuesto**.

## Programación y corte

**Programar siempre a las 00:00.** El motivo es de optimización, no de comodidad:

> Le das a Meta el 100% del presupuesto y las 24 horas para que lo gaste en el mejor momento del día. Si programás a las 19:00, le das **6 horas para gastar 100 dólares** — te lo puede quemar.

**Matar la campaña en cuanto llega al CPA objetivo sin vender**, aunque sean las 9 de la mañana. Es para **cuidar el ROAS**.

> «Cuando estás en una oferta que anda muy bien, te suele vender **apenas empieza a gastar**.»

Si el pico de ventas está claramente por la noche, se puede probar a dejarlas correr — pero con más riesgo de gasto.

## La franja horaria de la oferta

Detalle poco obvio y muy rentable:

> Una oferta que **no está en momentum** responde al surfeo **solo hasta cierta hora del día**. Pasada esa franja, el ROAS empieza a caer.

Hay que **encontrar la franja horaria de tu oferta** y dejar de surfear ahí. No mantener presupuestos altos mientras estás perdiendo ROAS.

## Reglas automáticas de corte

Conviene tener **reglas configuradas en Meta** que apagan solas cuando el costo por resultado llega al límite.

El motivo, de un caso real: a un alumno una campaña **se le disparó 150 USD en dos horas** mientras no miraba.

> «Si no, **se te va el ROAS**.»

Con estructuras que se revisan 4 veces al día, la regla automática cubre los huecos entre revisiones.

## Diversificar las CostCap

Configuración que Santiago aprueba: **4 CostCap corriendo a la vez**, cada una con **5 anuncios distintos entre sí**, en **formatos y ángulos distintos**.

No son cuatro copias de lo mismo: es diversidad creativa dentro de la estructura de escala. Ver [[angulos-publicitarios]].

## Una cuenta publicitaria por oferta

Se usa una **CP distinta por oferta**. Una cuenta se reutiliza solo si la oferta anterior ya dejó de correr — la condición es que **no haya nada corriendo** ahí.

Ver [[contingencia-de-cuentas]] para la arquitectura de cuentas.

## Más anuncios, no más ofertas

Distinción que ordena las prioridades según el objetivo:

> Para escalar **una oferta** a cinco o seis cifras al día, **no tenés que sacar más ofertas: tenés que sacar más anuncios para esa oferta**.

- **Más ofertas** → crecimiento horizontal, cubre la caducidad ([[modelo-low-ticket]])
- **Más anuncios sobre la que ya vuela** → escala vertical real

## Delegar para poder escalar

Umbral que menciona: cuando ya llevás **10.000–50.000 USD de profit**, empieza a delegar.

**Lo primero que se delega: la edición operativa de anuncios en CapCut.**

> «Los anuncios son lo más importante, pero **lo operativo de la edición no lo es**. Si no, vas a estar esclavo todo el día editando videos.»

Lo que **no** se delega es el nivel de arriba: **los guiones** y la dirección creativa. Ver [[guiones-de-video-ads]].

Su propia cadencia declarada llegó a **2 ofertas al día** — sostenible solo con un equipo de 10+ personas.

## Contingencia y expansión

- **Otras cuentas publicitarias**: correr el mismo producto en varias cuentas permite comparar CPM y escalar más agresivo. Hay lección dedicada (`escalar-en-otras-cuentas-publicitarias...`)
- **Contingencia de perfiles y BMs**: arquitectura de backup para no quedarse sin poder anunciar. Ver [[contingencia-de-cuentas]]
- **Expansión geográfica** como vector de escala una vez saturado el mercado inicial. Ver [[internacionalizacion]]

## ⚠️ Ninguna estructura salva un funnel malo

Contrapeso necesario a todo lo anterior, en sus palabras:

> «Una estructura de campaña **no te va a salvar el negocio**. No va a volcar un funnel negativo en uno positivo.»
>
> «Cuando tenés un funnel cuya matemática da, **solo es gastar más dinero en anuncios**. No importa la estructura de campaña — importa muy poco.»

Las estructuras son un multiplicador de algo que ya funciona. Si los números no dan, el problema está en [[optimizacion-de-roas]], no en la campaña.

## Regla transversal

> No tolerar campañas con costo por resultado por encima del CPA break-even. Es muy fácil conseguir anuncios nuevos por debajo.

## Complementos prácticos

### Estructuras que faltan
- **Micro-presupuesto para descartar rápido:** ABO de **5–7 conjuntos** (1 anuncio c/u) a **1,5× el ticket por conjunto**. Con 5 × 30 USD, la pérdida máxima es 150. Antes de tirar la oferta, se puede probar otro mercado.
- **ROAS-cap:** bid inicial = ROAS mínimo aceptable (ej. 2). Si no arranca, **bajar de a 0,1** (1,9 → 1,8…).
- **CostCap, variante:** bid = **CPA promedio de la cuenta** o un poco más para que arranque. Cualquiera de los tres bid manuales se arma igual: 1 conjunto con N ganadores, o N conjuntos con 1 ganador cada uno.

### Surfeo cada ~2 horas

Se aplica a las campañas de puja manual (CostCap, BidCap, ROAS cap) y también a la **campaña V3** ([[metodo-v3]]), **siempre que sostenga un ROAS mayor a 2–2,5**. Por debajo de eso, la escala sigue la regla de una subida por día.

- **Si sostiene buen CPA:** duplicar el presupuesto (o subirlo 50%) y esperar 2 h para la próxima decisión.
- **Si el CPA sube: bajar el bid**, no tocar el presupuesto.
- **Si deja de gastar:** subir el bid (ej. +1) y **esperar una hora** antes de volver a subirlo.
- **Nunca surfear con 1 venta.** Esperar **3–5 ventas con ROAS 2,5+**.
- **Duplicar presupuesto hasta que suba el CPM**, que es la señal de saturación. Ahí se frena.
- **Reseteo nocturno, excepción:** si el día cerró muy bien, dejar la campaña **un escalón más arriba** que el punto de partida.
- **En los días de mejor ROAS de la tienda**, animarse a un **10×** en las CBO que vienen funcionando. El peor caso es resetear.

CBO mixta, power y gigante: ver [[estructuras-cbo]]. Varias cuentas por CPM y cambio de ecosistema: ver [[organizacion-y-registro]] y [[problemas-de-cuentas-meta]].

Relacionado: [[testeo-de-creativos]] · [[metricas-y-kpis]] · [[setup-de-campanas]] · [[aumento-de-aov]]
