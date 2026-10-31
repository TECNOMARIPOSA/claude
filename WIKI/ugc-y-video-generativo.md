---
tema: UGC y video generativo
actualizado: 2026-08-10
fuentes: [RAW/contexto-chatgpt.md, RAW/prompts/prompt-testimonios-sora-2.md, RAW/formacion/lecciones/vsl-con-heygen.md]
---

# UGC y video generativo

El UGC es una pata central de la estrategia creativa. La mayoría se produce con IA generativa, no con creadores reales.

## Reglas fijas de UGC

Aplican salvo instrucción contraria. Cuando no se respetan, son fuente recurrente de fricción:

- **9:16 vertical**
- Cámara **handheld**, natural, documental, realista
- Voz natural, sin sonar producido
- **Sin subtítulos** — Santiago los añade después en CapCut
- **Sin texto sobreimpreso** ni elementos gráficos innecesarios
- **Sin música** salvo que la pida
- Producto visible cuando corresponde
- Español latino o argentino según mercado ([[internacionalizacion]])
- Si pidió que el personaje **sostenga** el producto o el libro, lo sostiene **mientras habla** — no lo deja sobre una mesa

## Avatares

Personajes recurrentes de creativos. **No son personas del equipo.**

| Avatar | Perfil |
|---|---|
| Diego | Hombre |
| Cami | 29 años, runner, fitness |
| Mateo | 28 años |
| Delfi | 30 años |
| Susana | 56 años, maestra jubilada |

También se han pedido: mujeres de 35–40, madres, pastores, profesionales, personas en cocinas, personas mostrando productos.

**Contenido cristiano:** avatar pastor masculino de 50–60 años con apariencia real, contexto de iglesia. Detalle práctico registrado — ciertos nombres provocaban rechazo en los modelos y hubo que usar «Padre Fío» / «Padre Bio» como alternativa.

## El pack de producción

El prompt de testimonios en Sora 2 define el entregable estándar: **guion de voz (ElevenLabs) + prompt visual (Sora 2 / Runway)**, en tres estilos psicológicos distintos:

| Estilo | Psicología | Entorno |
|---|---|---|
| **El escéptico convertido** | «No creía, ahora estoy sorprendido» | Casa del avatar, selfie vertical |
| **El profesional satisfecho** | Serio, habla de ROI y resultados | Oficina o estudio bien iluminado |
| **El resultado tangible** | Alivio y felicidad | Usando el producto, lifestyle |

Regla de oro: **14 segundos máximo, 35–40 palabras**. Hook (0–3s) / Beneficio (4–10s) / Cierre + CTA (11–14s). Coherencia obligatoria entre avatar, entorno y guion.

## Prompts para video generativo

Regla crítica con **Flow / VEO 3** cuando se da una imagen de referencia:

> **«Guiate de esta imagen sin cambiar ni agregar nada.»**

Se preservan composición, personaje, entorno, vestimenta, posición, elementos, producto y escena. Solo cambia la acción o el diálogo pedido. Nada de elementos nuevos, nada de modificaciones arbitrarias.

Y cuando pide **«PROMPT NO UNA IMAGEN»**: se entrega solo el prompt, en bloque de código.

## Green screen

Para ciertos UGC se pide **fondo verde / chroma**, con el objetivo explícito de poder editar después en CapCut.

## Audio

- Voz natural, sin efectos innecesarios
- Persona hablando directamente a cámara
- Con ElevenLabs, **la duración del guion debe coincidir con la del creativo de referencia** del competidor

## Herramientas

**Video:** VEO 3 · Flow · Seedance 2.0 · Sora 2 · Runway · HeyGen (para VSL, hay lección dedicada)
**Voz:** ElevenLabs
**Edición y subtítulos:** CapCut

Ver [[stack-de-herramientas]].

## Complementos prácticos

### Avatar de VSL en HeyGen
- Imagen base: pedirle a ChatGPT **varias poses o variantes de la misma persona**, que mejoran la consistencia del personaje. **Prueba de autoridad en la imagen:** diplomas, fotos familiares de fondo, vestuario y joyas acordes al personaje, e instrucciones anti-IA explícitas.
- En HeyGen: personaje virtual con **3–5 fotos en 9:16**.
- **Voz:** clonada (ElevenLabs u otra) desde un audio grabado con el guion completo, dividido en tramos si hace falta, e importada como **«voz de terceros»**. No se deja que HeyGen genere el guion.
- **Un audio por escena**, en 9:16.
- **Edición de un VSL de front:** recortar los silencios entre frases, que mejora la retención, y **B-roll cada 3–5 segundos, sobre todo al inicio**. El VSL post-pago, en cambio, va sin B-roll.
- Alternativa más barata a HeyGen: **DreamFace**.
- El mismo avatar sirve como **«personaje de autoridad» reutilizable** para tandas de anuncios, no solo para el VSL.

### B-roll generado
- **Flow / Veo 3:** clips de 8 s **acelerados ~1,5×** para ganar ritmo.
- **Seedance** también está disponible por API (KIE, Apimart) o en planes «ilimitados» de terceros. Conviene desconfiar de lo «ilimitado»: hay reportes de límites reales y bugs.

Relacionado: [[guiones-de-video-ads]] · [[imagenes-y-mockups]] · [[biblioteca-de-prompts]]
