---
tema: Guiones de video ads
actualizado: 2026-08-10
fuentes: [RAW/prompts/prompt-guiones-7-pasos.md, RAW/prompts/prompt-guiones-por-nivel-de-conciencia.md, RAW/prompts/prompt-guiones-30-segundos.md, RAW/prompts/prompt-ads-storytelling-largos-publico-frio.md, RAW/formacion/lecciones/como-crear-un-arsenal-de-guiones-con-ia.md, RAW/formacion/lecciones/prompt-cowboy-y-claude-para-los-guiones.md]
---

# Guiones de video ads

## La fórmula de 7 pasos

Es la estructura base de toda la producción creativa del método:

| # | Paso | Función |
|---|---|---|
| 1 | **Hook** | Frase disruptiva que detiene el scroll en 3s. Ver [[hooks]] |
| 2 | **Re-hook** | Empatía. «Yo también estaba…», «Sé cómo se siente…». Valida el problema |
| 3 | **Presentación del producto** | «Hasta que conocí [Nombre]…» |
| 4 | **Beneficios / características** | «Tiene X que te permite Y» |
| 5 | **Tutorial / mecánica** | Demostración breve de uso |
| 6 | **Testimonial / prueba social** | «Miles de [avatar] ya están eligiendo…» |
| 7 | **CTA** | Instrucción directa |

## La regla de variación modular

Esto es lo que convierte la fórmula en un sistema de testeo, y es la razón de que Santiago pueda sacar 10 creativos al día:

> **Los pasos 3–7 son el «cuerpo del anuncio» y se mantienen IGUALES dentro de un mismo concepto creativo. Solo se varían los pasos 1 y 2** (hook y re-hook) para probar distintos ángulos de entrada: miedo, deseo, curiosidad.

Cada nuevo creativo es un hook nuevo pegado a un cuerpo probado. Es barato de producir y aísla la variable que más pesa. Ver [[testeo-de-creativos]].

Entrega estándar del prompt: 1 concepto completo (pasos 1–7) + 2 variaciones solo de inicio.

## Los cinco niveles de conciencia

La versión más elaborada del sistema: **un prompt distinto por nivel de conciencia de Schwartz** (`prompt-guiones-por-nivel-de-conciencia`, 5 prompts en un documento). Misma estructura de 7 pasos, distinta psicología de entrada.

Ejemplo del nivel más difícil, **Inconsciente del problema**: la persona no sabe que tiene un problema, no busca solución, no percibe que haya nada que cambiar. El objetivo del anuncio deja de ser vender y pasa a ser **despertar conciencia** — provocar sorpresa, curiosidad, revelación. El espectador debe pensar *«nunca había pensado en esto… tal vez me está pasando a mí»*.

El nivel de conciencia es una de las dimensiones que hay que **variar deliberadamente** al testear.

## Formatos por duración

| Formato | Prompt | Lógica |
|---|---|---|
| **30 segundos** | `prompt-guiones-30-segundos` | «Narrativa de compresión»: historia emocional completa + venta en 30s exactos |
| **Storytelling largo (1:30+)** | `prompt-ads-storytelling-largos-publico-frio` | Anuncio-historia que no parece publicidad. **El producto aparece pasado el primer minuto**; el 70% es narración emocional. Para público frío |
| **UGC 8–15s** | — | Segmentos cortos para Seedance |
| **Testimonial 14s** | `prompt-testimonios-sora-2` | Máx. 35–40 palabras. Hook (0–3s) / Beneficio (4–10s) / Cierre + CTA (11–14s) |

## Reglas de producción

**La longitud importa.** Si hay un competidor de referencia, se mantiene aproximadamente su misma duración. Un guion no debe ser más largo solo porque «tiene más información».

**Tono nativo de redes**, dinámico y conversacional. Explícitamente: que no suene a «anuncio de televisión aburrido» ni a IA.

**El input obligatorio** es la investigación de mercado — avatar, dolores, deseos, propuesta de valor. Los prompts están construidos para no generar nada hasta recibirla. Ver [[investigacion-de-mercado]].

## El montaje de un video ad, paso a paso

Orden fijo que sigue Santiago:

**1. Guion** → **2. Audio/voz** → **3. Visuales** → **4. Montaje en CapCut**

| Paso | Herramienta | Detalle |
|---|---|---|
| Capturar la landing | **Fireshot** | Screenshot completo de la página de ventas |
| Guion | **Claude** | Se sube la captura + el prompt de guion. Se puede usar la landing **en vez de** la investigación de mercado si hay prisa |
| Voz | **Audio Labs** (vía Scalebus) o ElevenLabs | |
| Visuales | **TikTok** o **Pinterest** | B-roll ya viral ([[hooks]]) |
| Montaje | **CapCut** | Aquí se añaden los subtítulos |

## El flujo de producción

1. Investigación de mercado → documentos base
2. **Prompt Cowboy** para afinar el prompt (hay dos lecciones dedicadas a Prompt Cowboy + Claude)
3. Claude / ChatGPT genera el arsenal
4. Variación sobre ganadores con `prompt-variacion-de-guiones-winners` (guion winner + sales page → variantes masivas)
5. Producción visual: [[ugc-y-video-generativo]]

## Complementos prácticos

### Storytelling largo para público frío (1:30–2:30): los 7 beats
1. Hook confesional o polémico (3 s)
2. El juicio o la tensión (alguien juzga, o la protagonista se siente insuficiente)
3. El momento de verdad (una escena cotidiana que revela lo oculto)
4. El giro emocional
5. **El producto como herramienta concreta, recién al ~60% de la pieza**
6. La transformación, con detalle sensorial
7. Cierre que dignifica + CTA

- **Tres variantes narrativas del mismo dolor:** (a) la persona afectada en confesión, (b) alguien que la juzgaba y se redime, (c) una figura de autoridad que ayuda en vez de señalar.
- **Reglas:**
  - Primera persona oral y frases cortas.
  - El producto nunca aparece antes del 60%.
  - Sin curas milagrosas.
  - **Se valida el dolor, nunca se acusa al espectador.**

### Diagnosticar antes de variar un guion ganador
Primero se le pide a la IA que diagnostique **por qué funciona**: estructura, hook, problema que activa, promesa, mecanismo, prueba social, cierre y frases de más carga emocional. También se analiza la landing, para detectar testimonios o garantías que el guion no aprovecha. Recién después se piden variantes en **6 categorías**:
1. **Hook:** pregunta directa, dato impactante, confesión o error, resultado primero, contraste, identidad
2. **Ángulo emocional:** miedo a perder, deseo de ganar, vergüenza, orgullo, esperanza, enojo con el sistema
3. **Protagonista:** fundador, cliente transformado, alguien que casi no compra, narrador externo
4. **Estructura:** resultado primero, fracaso previo, lista o revelaciones, testimonio en primera persona, documental
5. **Duración:** 15 s (solo hook + CTA), 30 s, 60–90 s con más prueba social
6. **Objeción:** «ya lo intenté», «no tengo tiempo», «es caro», «no es para mí», «no confío»

### Más reglas
- Con un guion que vendió: **pedir 10 variaciones que toquen los mismos dolores** y probarlas con B-rolls distintos. El mismo guion con otro fondo puede conectar con otro segmento.
- **Prompt Cowboy por target:** con el copy de la landing se arma el meta-prompt una sola vez, y en Claude se piden guiones para distintos públicos del mismo nicho (ej. amas de casa, después emprendedoras) sin reescribir el contexto.

Relacionado: [[hooks]] · [[angulos-publicitarios]] · [[testeo-de-creativos]] · [[biblioteca-de-prompts]] · [[ugc-y-video-generativo]]
