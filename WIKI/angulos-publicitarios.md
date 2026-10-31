---
tema: Ángulos publicitarios
actualizado: 2026-08-10
fuentes: [RAW/prompts/prompt-angulos.md, RAW/prompts/prompt-angulos-manuales-launch-expert.md, RAW/prompts/prompt-guiones-por-nivel-de-conciencia.md, RAW/formacion/lecciones/apalancate-de-lo-que-ya-funciona.md, RAW/formacion/lecciones/variaciones-de-lo-que-ya-funciona-brools-hooks-guiones.md, RAW/contexto-chatgpt.md]
---

# Ángulos publicitarios

El ángulo es **la puerta de entrada al mismo producto**. Es la variable que más rendimiento da cuando se testea bien, y la que más se desperdicia cuando se «varía» cambiando dos palabras.

## La regla que separa variación real de variación falsa

Una variación cuenta si cambia alguna de estas dimensiones:

- **Hook**
- **Mecanismo**
- **Ángulo**
- **Objeción** que ataca
- **Emoción** que activa
- **Nivel de conciencia** del público
- **Forma de presentar** el producto

No cuenta si solo cambian palabras. Pedir 30 variaciones y recibir 30 versiones casi idénticas es un fracaso.

Ver [[guiones-de-video-ads]].

## Ángulos que Santiago usa como categorías

Aparecen nombrados en el prompt de storytelling largo: **anti-culpa, económico, autoridad, transformación**. Con estructura de guion:

- Producto / oferta
- Nicho y buyer persona
- **Dolor central emocional** — la herida profunda: culpa, vergüenza, soledad, miedo, frustración
- Ángulo de venta principal
- Transformación concreta y observable, con detalle sensorial

## Los cinco niveles de conciencia

La dimensión más elaborada del sistema. Cada nivel exige una entrada distinta:

| Nivel | Qué sabe el público | Objetivo del anuncio |
|---|---|---|
| **Inconsciente del problema** | Nada. No busca nada | **Despertar conciencia**: sorpresa, curiosidad, revelación |
| Consciente del problema | Sabe que le pasa algo | Nombrar el problema con precisión |
| Consciente de la solución | Sabe que hay soluciones | Presentar el mecanismo |
| Consciente del producto | Conoce el producto | Diferenciar |
| Más consciente | Listo para comprar | Oferta y urgencia |

Cada uno tiene su prompt en `prompt-guiones-por-nivel-de-conciencia`, todos con la misma estructura de 7 pasos. Ver [[biblioteca-de-prompts]].

## Cómo se encuentran ángulos nuevos

**1. Investigación de mercado.** El deep research y el documento de creencias son la mina principal: deseos, objeciones, lenguaje real, diferenciación. Ver [[investigacion-de-mercado]].

**2. Competencia.** Estudiar creativos, duración, hooks, estructuras y ofertas — para entender **qué funciona y por qué**, no para copiar.

**3. Contenido orgánico viral.** Los creadores de TikTok con alto ratio views/seguidores ya validaron qué capta atención en ese nicho. Ver [[hooks]].

**4. Prompt dedicado.** `prompt-angulos` hace investigación online del nicho; `prompt-angulos-manuales-launch-expert` genera ángulos de alto CTR combinando psicología visual y copy, formateados para Launch Expert AI Creative Suite.

## Diversidad de formato, no solo de hook

Error que Santiago señala como muy extendido:

> «Recaen siempre en **el mismo formato creativo** y lo único que hacen es **iterar el hook**. Cambian los primeros 5–10 segundos y nada más.»

**Meta castiga eso con CPM más alto.** El motivo es el mismo de siempre: la plataforma no quiere mandarle contenido repetido a la misma persona, porque se cansa y se va.

> «Meta premia la **diversidad** del creativo y la **calidad** del creativo.»

Formatos que hay que rotar:

- **Voz en off + visuales** (el más usado)
- **UGC review** · **UGC testimonio** · **UGC con avatar de IA**
- **Testimonial**
- **Captura de pantalla**
- **Carrusel**
- **Educacional**
- **Imagen estática / scroll stopper**
- **Anuncios largos** y **cortos**

**Y también hay que variar el tamaño:** 16:9 · 9:16 · 3:4 · 1:1. Es otra dimensión de diversidad que Andrómeda premia y que casi nadie toca.

Y el argumento de fondo: **distintas personas compran con distintos formatos**. Alguien que no compraría con un video en voz en off compra con un carrusel.

Ver [[ugc-y-video-generativo]] y [[renovacion-de-creativos]].

## Olvidate de los intereses

> «Segmentar por intereses **quedó en 2020**. Meta hoy funciona completamente diferente.»

El targeting está en el creativo: **cantidad, calidad y diversidad**. Es la razón de fondo por la que la estrategia de escalado es volumen creativo y no segmentación fina ([[escalado-en-meta-ads]]).

## Un producto, dos mercados

El ángulo no solo cambia la entrada: puede cambiar **a quién le vendes el mismo producto**. Caso real de una mentoría, con un ebook sobre caída de cabello:

| Ángulo | Público | Promesa |
|---|---|---|
| Profesional | **Estilistas** | Manejá bien este problema y **aumentá tu clientela** |
| Consumidor final | Mujeres a las que se les cae el pelo | Cuidá tu pelo **en casa** |

Mismo PDF, dos ofertas, dos mercados, dos landings. Es la forma más barata de multiplicar una oferta ya validada — y encaja con que las ofertas caducan a los 3–4 meses ([[modelo-low-ticket]]).

Ambos ángulos, además, caen en big niches distintos: el primero en **dinero** («gana dinero con tu oficio»), el segundo en **salud**. Ver [[segmentos-de-mercado]].

## La regla de oro del testeo de ángulos

> **Testear varios ángulos. No quedarse con uno solo.**

Y cuando uno funciona: sacar variaciones **de ese ángulo**, jugar con él, exprimirlo. Es lo que produce la mejora progresiva de CPA que describe [[testeo-de-creativos]].

## Apalancarse en lo que ya funciona

Dos lecciones dedicadas al principio: `apalancate-de-lo-que-ya-funciona` y `variaciones-de-lo-que-ya-funciona [B-ROLLS - HOOKS - GUIONES]`. Los tres elementos que se varían sobre una base ganadora son exactamente esos: **B-rolls, hooks y guiones**.

## Complementos prácticos

### Minar reseñas y comunidades, no solo la Ads Library
- **Dónde buscar:** G2, Capterra, Trustpilot, AppSumo, Gumroad, Hotmart, comentarios de TikTok, Reddit, X, Product Hunt y comunidades de nicho (Slack, Discord).
- **Qué buscar:**
  - Momentos «ah-ha» que los usuarios reportan solos.
  - Funciones secundarias que valoran más que la principal («compraron por X y se quedaron por Y»).
  - Con qué alternativa cara o complicada se lo compara favorablemente.
  - **Usos y perfiles inesperados.**
- **Salida:** al menos **3 ángulos alternativos**, cada uno con citas reales que lo respalden.

### Proporciones
- **90% variaciones del ganador** (avatar, hook, edición, clickbait) **+ 10% ángulos nuevos**, modelando competencia directa e indirecta.
- **Ángulos completamente nuevos 2–3 veces por semana**, para no saturar uno solo. El resto de los días, sub-ángulos y variaciones de lo validado.

Relacionado: [[hooks]] · [[guiones-de-video-ads]] · [[testeo-de-creativos]] · [[investigacion-de-mercado]]
