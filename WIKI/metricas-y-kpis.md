---
tema: Métricas y KPIs
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/metricas-importantes.md, RAW/formacion/lecciones/clase-mas-importante-como-testear-y-escalar.md, RAW/formacion/lecciones/cuando-considerar-una-oferta-validada.md, RAW/contexto-chatgpt.md]
---

# Métricas y KPIs

La tesis de fondo: **todo el negocio se reduce a comparar dos números.**

> Costo por visita vs. revenue por visita. La diferencia es tu ganancia por visita.
> (`RAW/formacion/lecciones/metricas-importantes.md`)

**Las fórmulas, para no confundirlas:**

```
Costo por visita   = importe gastado ÷ visitantes
Revenue por visita = facturación     ÷ visitantes
```

Ejemplo: gastás 100 USD y traes 200 visitantes → **0,50 de costo por visita**. Si esas 200 visitas facturan 200 USD → **1,00 de revenue por visita** → **ROAS 2**.

Y el revenue por visita solo se construye de dos maneras: **mejor conversión** o **mejor AOV**.

Hay una forma aún más compacta de decirlo, que Santiago usa como marco unificador:

> **Meta cobra por impresión. Gana el que menos impresiones necesita para lograr una conversión.**

Cuanto más afilado el embudo —mejores anuncios, mejor landing— menos impresiones hacen falta por venta, y más margen queda para escalar. Todos los KPIs de abajo son formas de medir ese mismo cociente.

Y aplica igual sea cual sea el funnel: venta directa, VSL o quiz. Cambia qué es la conversión, no la aritmética.

De ahí salen las dos familias de métricas, y cada una se arregla por un camino distinto:

| Familia | Qué mide | Se mejora con |
|---|---|---|
| **Métricas de anuncio** | El costo por visita | Mejores creativos |
| **Métricas de conversión** | El revenue por visita | Mejor funnel y oferta |

### Ninguna métrica se juzga sola

> Con un **CPM regalado** te podés permitir un **CTR de 0,5%**, porque el CPC igual sale económico. Todo depende de cuánto es el CPC.

Los KPIs de abajo son referencias, no umbrales absolutos. La única pregunta que importa siempre es si entra más dinero del que sale.

### Testear no es gastar

> «Cuando lanzás una oferta nueva **no estás gastando dinero: estás comprando datos**.»

Reencuadre que explica por qué el volumen de ofertas y de creativos no es derroche — es la única forma de conseguir la información que decide todo lo demás.

Son correlacionadas, no independientes. Un CPC de 0,10 USD te deja tolerar una conversión mala; un CPC de 1 USD exige un 7% de conversión para ser rentable, que Santiago describe como «inhumano». Por eso el diagnóstico nunca es sobre una métrica aislada: se mira el conjunto para encontrar **dónde está el cuello de botella del embudo**.

## KPIs de anuncio

| Métrica | KPI de referencia | Notas |
|---|---|---|
| **CPC** | LatAm 0,10–0,50 USD · USA hasta 1 USD | La métrica por excelencia. Indica si el funnel va a estar en positivo antes de tener ventas |
| **CTR** | ≥ 1,5–2%, idealmente 2,5%+ | Duplicar el CTR es reducir el CPC a la mitad |
| **CPM** | Sin KPI fijo | Meta premia con CPM bajo a quien no aburre a sus usuarios |
| **Hook rate** = reproducciones de 3s ÷ impresiones | Estándar 30% — **Santiago exige >50%** | Se crea como métrica personalizada |
| **Retention rate** = **thruplays ÷ impresiones** | Estándar 5% — **Santiago exige >10%** | Idem |
| **Frecuencia** | No debe dispararse al escalar en frío | Frecuencia 2 sin llegar a audiencias nuevas = problema de creativo |

Hook rate y retention rate son los que **mueven la aguja del CTR**: si retienes más gente en los primeros 3 segundos, más gente llega al CTA, sube el CTR y baja el CPC en cadena.

Una idea que atraviesa todo el material: **el targeting hoy está en el creativo, no en los intereses del conjunto de anuncios.** Es la razón de fondo por la que la estrategia de escalado es diversidad creativa y no segmentación fina (ver [[escalado-en-meta-ads]]).

## KPIs de conversión

| Métrica | KPI |
|---|---|
| **Comprate** = compras ÷ landing page views | ≥ 2%, y ≥ 2,5% antes de escalar |
| **Visita → inicio de checkout** | ≥ 10% |
| **Inicio de checkout → compra** | 25–30% |
| **AOV / front-end ratio** | ≥ 1,5 · hasta 2–2,5 en productos digitales |

El ratio visita → inicio de checkout es el que mide **cuán persuasiva es la página de ventas**. Si no llega al 10%, el problema está en la landing, no en los anuncios (ver [[pagina-de-ventas]]).

El AOV/front-end ratio mide si el backend está haciendo su trabajo: con un front de 10 USD, el AOV debería estar en 15 como mínimo. Ver [[aumento-de-aov]].

## CPA break-even

El número que Santiago manda «tatuarse en la cabeza». Es **lo que entra neto en la cuenta bancaria por cada venta**, ya descontadas comisiones y conversión de divisa.

Ejemplo del material: vendes a ARS 19.000, te entran ARS 17.000, dólar a 1.200 → CPA break-even = **14,16 USD**. Todo costo por resultado por encima de eso se corta.

El matiz importante: si hay upsells, el break-even **no es el precio del front**. Hay que añadir en Meta la columna *valor de conversión de compras promedio*, porque de lo contrario se matan conjuntos rentables por juzgarlos contra un ticket que no es el real.

## Cómo se lee una oferta recién lanzada

Antes de tener conversiones ya se puede estimar el potencial, solo con el costo por visita:

1. Se asume un comprate del 2% como parámetro de partida.
2. Con ticket de 15 USD: 100 sesiones → 2 compras → 30 USD ingresados.
3. Si el costo por visita es de 0,30 USD, esas 100 sesiones cuestan 30 USD → break-even exacto.
4. Si el costo por visita es de 1 USD, harían falta 7 compras por cada 100 visitas (7% de conversión) para ser rentable. Descartar.

La confirmación real llega con las ventas, pero este cálculo dice **si vale la pena seguir invirtiendo energía** en las primeras horas.

> «Entra más dinero a tu cuenta del que sale.» Es la señal de una oferta ganadora, normalmente ya al primer o segundo día.

## Cómo diagnosticar un día malo

Orden concreto de revisión al cerrar el día, para no tocar lo que no hay que tocar:

1. **Inicio de checkout ÷ landing page views**
2. **AOV ÷ front-end**
3. **Compras ÷ inicios de checkout**

Y el diagnóstico que da casi siempre:

> «Muy probablemente te haya bajado el ratio **compras ÷ inicio de checkout**. Pero eso **no es que tu funnel no funcione: son tus ads**, nada más. No toques nada.»

Un día malo con el funnel intacto es un problema de creativos, no de embudo. La respuesta es **más anuncios**, no rehacer la landing. Ver [[diagnostico-de-checkout]] y [[renovacion-de-creativos]].

## Días sin ventas: son normales

Uno de los errores de lectura más caros, y el que más decisiones malas provoca:

> «Hasta invirtiendo **200 dólares al día** hubo un día que no vendí nada. Analizá la data: dos días antes venías haciendo 150 de profit al día. Pero generalmente no ves eso, **ves el día malo**.»

**Meta es inconstante.** Tirar anuncios no garantiza vender todos los días.

**Analizar siempre en «máximo»** (todo el histórico del conjunto), nunca el día suelto. Un día bueno arrastra los costos promedio hacia abajo y el siguiente parece un desastre sin serlo.

Y un matiz sobre el tamaño: **cuanta más inversión diaria, más constancia**. Con presupuestos chicos hay más varianza día a día, simplemente porque llega menos tráfico.

> Si los costos están dentro de lo que podés tolerar, seguí. La decisión se toma sobre el CPA acumulado, no sobre la foto de hoy.

## Dónde apalancarse

Santiago es explícito sobre su propio sesgo, y lo plantea como una pregunta que cada uno debe responderse:

> Es más fácil bajar el costo del tráfico que subir el porcentaje de conversión de la landing.

Su recomendación operativa para mejorar anuncios a partir de datos: filtrar por CTR > 3%, **descargar esos creativos, pasarlos al teléfono y mirarlos como si fueran TikTok**, analizando qué pasa en el segundo 2 y en el segundo 5 que hace que la gente se quede.

Si los KPIs están en rango y aun así el funnel no despega, el diagnóstico continúa en [[optimizacion-de-roas]].

## Complementos prácticos

- **CPC bajo suele venir con CTR bajo**, porque ese tráfico sale de audiencias muy masivas. La excepción es un creativo excepcional.
- **El CPC depende también de la densidad poblacional y la competencia del público**, no solo del creativo.
- **Cuánto cuesta la fuga de carga:** con CPC de 0,20, 1.000 visitas cuestan ~200 USD si carga el 100%. Con un **80% de carga** cuestan **~250 USD**. Esa diferencia se pierde antes de medir conversión.
- **El lazy load importa sobre todo con videos de testimonios**: si la landing los carga todos de entrada, el first paint se vuelve pesadísimo.
- **Mercados en inglés:** se tolera CPC y CPM más alto porque la landing puede convertir **~7%**. Ahí se mira CPA y AOV, no CPC ni CPM sueltos.
- **CPA break-even en moneda local:** recalcularlo con **el tipo de cambio del día**.
- **Si hay mucho inicio de checkout y poca compra**, casi siempre es percepción de valor en el checkout, no el tráfico.
- **Método de análisis de ganadores:** además de verlos como si fueran TikTok, analizarlos **frame por frame** (hook, B-roll, edición) para aislar qué elemento generó la retención.

Relacionado: [[testeo-de-creativos]] · [[escalado-en-meta-ads]] · [[validacion-de-oferta]] · [[optimizacion-de-roas]]
