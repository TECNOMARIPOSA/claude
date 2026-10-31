---
tema: Método V3 — estructura de campañas
actualizado: 2026-09-24
fuentes: [operación real en Meta Ads, septiembre 2026; estructura V3 de Grupo Firgon]
---

# Método V3 — estructura de campañas

**Una campaña CBO por oferta y por cuenta. Adentro, un conjunto por tanda de creativos. En cada conjunto, de 5 a 10 anuncios distintos.** Las renovaciones no abren campañas nuevas: entran como un conjunto nuevo dentro de la campaña que ya está corriendo.

Es la estructura con la que se montan hoy todas las ofertas. Las demás estructuras de [[escalado-en-meta-ads]] siguen existiendo, pero se usan sobre esta base, no en lugar de ella.

## Por qué existe: la cola de duplicados

El patrón anterior era duplicar campañas y conjuntos con el mismo creativo y matarlos a los ~20 USD de gasto. Medido en cuatro ofertas reales durante una semana:

| | Cola (anuncios duplicados con poco gasto) | Núcleo (anuncios con gasto real) |
|---|---|---|
| Parte del gasto | **25% a 75%** según la oferta | el resto |
| ROAS | **0,23 a 0,99** | **1,10 a 1,69** |

En total, la cola se comió más de la mitad de lo que ganaba el núcleo. En una de las ofertas, **42 de 46 campañas duplicadas no hicieron ni una venta** y quemaron el 16% del presupuesto semanal. Un mismo creativo llegó a aparecer **7 veces** en conjuntos distintos.

Después de pasar a V3, la cola bajó al **5–10% del gasto** en las mismas ofertas. V3 corta el problema de raíz: una campaña, un conjunto por tanda, anuncios distintos adentro. No hay duplicados que repartan el presupuesto.

## La estructura

```
Campaña   V3 · <Producto> · <Cuenta>       CBO · Ventas · Compra · Volumen más alto
 ├─ Conjunto  18-9     → 5 a 10 anuncios (18/9 - 1 … 18/9 - 10)
 ├─ Conjunto  20-9     → la tanda siguiente
 └─ Conjunto  22-9     → y así, una por tanda
```

La notación es **Campañas-Conjuntos-Anuncios**: V3 es una **CBO 1-1-5** o **1-1-10** que va sumando conjuntos. Ver [[estructuras-cbo]] y [[nomenclatura-del-metodo]].

### Campaña

- Objetivo **Ventas**, conversión en el **sitio web**, evento **Compra**.
- **CBO**: el presupuesto va a nivel de campaña.
- Estrategia de puja: **Volumen más alto**, sin tope de costo.
- Presupuesto de referencia en las ofertas actuales: de **90 a 500 USD por día**, según la cuenta y el mercado.

### Conjunto

- País o países del mercado (Tier 1, LatAm o un país solo; ver [[internacionalizacion]]).
- Edad **18–65**.
- **Advantage+ Audience activado**, salvo cuando el producto exige un filtro duro de género. Con Advantage+ activado, el género es solo una sugerencia y Meta lo entrega igual al otro. Si el producto es solo para mujeres o solo para hombres, **hay que apagarlo**.
- Ubicaciones automáticas. Si aparecen errores de "entrega inestable" o problemas de tracking, probá sacar **Threads**.
- Atribución de **7 días clic + 1 día visualización**.
- **DSA obligatorio** si algún país del conjunto es de la Unión Europea (España, Irlanda, Francia…). Se completa con el nombre de la Página que anuncia.
- Hora de inicio: **00:00 del mercado objetivo**.

### Anuncio

- Video o imagen **único**. En video, **9:16**.
- Título con prueba social, por ejemplo `⭐️⭐️⭐️⭐️⭐️ 4.9/5`.
- Botón de llamada a la acción: **Más información**.
- Link con los UTMs dentro de la URL (ver [[nomenclatura-del-metodo]]).
- Si la tanda se sube por catálogo, ver [[subir-ads-con-metodo-catalogo]].

## Renovaciones: siempre en la misma campaña

**Cada tanda nueva de creativos es un conjunto nuevo dentro de la campaña que ya corre**, con el nombre de la tanda. Nunca va en una campaña paralela.

- El conjunto nuevo **clona la configuración del que ya entrega**: segmentación, pixel, evento de optimización y atribución.
- Es una decisión de método. No se reevalúa en cada tanda, aunque la CBO tenga que repartir el presupuesto con el conjunto nuevo.
- Una tanda = un conjunto. Si llegan 10 anuncios de dos tandas distintas, van en **dos conjuntos de 5**. Un conjunto no puede llevar dos fechas.

## La campaña de winners

Cuando una oferta ya tiene ganadores claros, se abre en otra cuenta una campaña que **solo tiene los winners**:

- Campaña `V3 · <Producto> · <Cuenta> — Winners`, CBO, Volumen más alto, **250 USD por día** como referencia.
- **Un solo conjunto**, `Winners · Broad 18-65`, con la misma configuración estándar de la oferta.
- Adentro, los **6 a 10 mejores anuncios** por ROAS de 7 días, **clonados por post ID** desde la cuenta donde nacieron. Así conservan los likes y comentarios.
- **Cuidado con los ROAS altos de muestra chica.** Un anuncio con ROAS 5 y 24 USD de gasto no es un winner, es ruido.

## Escalar la V3: surfeo cada 2 horas

La campaña V3 se puede **surfear cada 2 horas, siempre que mantenga un ROAS mayor a 2–2,5**:

- Si sostiene ese ROAS, **duplicá el presupuesto** (o subilo 50%) y esperá 2 horas para la próxima decisión.
- Nunca con 1 venta: esperá **3 a 5 ventas** con ese ROAS antes de subir.
- Si el ROAS baja de 2, dejá de subir. Al final del día, volvé al presupuesto base o dejalo un escalón arriba si el día cerró muy bien.
- Detalle del surfeo en [[escalado-en-meta-ads]].

## Cuándo juzgar

- **Un anuncio suelto en testeo** se corta con la regla de [[testeo-de-creativos]] (al CPA medio o al break-even sin ventas).
- **Una campaña o un conjunto V3 entero no se juzga antes de gastar 2 o 3 veces el CPA objetivo.** Con un CPA de 42 USD, cualquier veredicto antes de 90–135 USD de gasto es ruido.
- **El creativo y la concentración del presupuesto pesan mucho más que el tipo de campaña.** Entre CBO 1-1-1, CBO 1-3-1 y ABO 1-1-1, los anuncios con gasto real rinden parecido. La diferencia la hace la cola.
- Las CBO se leen **a nivel campaña**, nunca conjunto por conjunto ([[escalado-en-meta-ads]]).
- Los ROAS del pixel de Meta vienen inflados frente a UTMify. Sirven para ordenar de mejor a peor, no como valor real ([[tracking-y-atribucion]]).

## Operativa multi-cuenta

- **Una cuenta master por producto.** Los videos se suben una sola vez y los anuncios se arman en esa cuenta. El resto de las cuentas los **clonan por post ID**, sin volver a subirlos. Solo hace falta que la cuenta destino y la Página estén en el **mismo Business**. La prueba social se concentra en un solo post.
- **No todos los winners tienen post ID.** Un anuncio armado directo sobre el video, sin publicación de Página detrás, no se puede clonar. Antes de perder acceso a una cuenta, separá los creativos que tienen post ID de los que no, y **bajá el MP4 de los que no**. Una cuenta deshabilitada todavía deja leer y descargar. Si salís del Business, ya no.
- Si la Página original se pierde, los videos siguen en la cuenta. Se pueden crear anuncios nuevos con la Página actual y clonar esos, pero la prueba social arranca de cero.
- Ver [[contingencia-de-cuentas]].

## Lanzamiento: un solo interruptor

Dejá los **conjuntos y los anuncios en ACTIVO** y **solo la campaña en PAUSA**. Así, lanzar es prender una sola cosa. Después de crear o editar algo, **verificá siempre el estado real** en el administrador. Meta a veces deja activo algo que figuraba en pausa.

Relacionado: [[estructuras-cbo]] · [[nomenclatura-del-metodo]] · [[testeo-de-creativos]] · [[escalado-en-meta-ads]] · [[renovacion-de-creativos]] · [[subir-ads-con-metodo-catalogo]]
