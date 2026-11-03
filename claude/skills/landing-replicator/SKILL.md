---
name: landing-replicator
description: >
  Skill completa para analizar, investigar y replicar/mejorar landing pages de productos low ticket (infoproductos, cursos, ebooks, packs digitales — mercado LATAM/Brasil).

  ACTIVAR SIEMPRE cuando el usuario:
  - Pegue una URL, HTML o captura de pantalla de una landing page
  - Diga frases como "analizá esta landing", "replicá esta página", "mejorá esta oferta", "cloná esta landing", "hacé deep research de esta oferta"
  - Pida analizar mockups, extraer prompts de imágenes, o generar los visuales en Higgsfield
  - Pida analizar competencia o estudiar cómo está construida una oferta

  Workflow de 5 fases: extracción completa (incluyendo análisis visual de mockups) → deep research del avatar y competencia → brief estratégico → HTML mejorado production-ready → prompts Higgsfield listos para generar cada imagen/mockup de la landing.

  La Fase 5 (prompts Higgsfield) se activa siempre que haya imágenes en la landing o el usuario mencione querer generar/replicar los visuales.
---

# Landing Replicator & Offer Enhancer

Workflow de 4 fases para analizar landing pages, investigar la oferta en profundidad y entregar un brief estratégico + HTML mejorado production-ready.

---

## INPUTS SOPORTADOS

| Tipo | Cómo procesarlo |
|------|----------------|
| URL | `web_fetch` para extraer HTML completo + texto |
| HTML pegado | Leer directamente del mensaje del usuario |
| Captura de pantalla / imagen | Analizar visualmente con vision; extraer todos los elementos visibles |

---

## FASE 1 — EXTRACCIÓN COMPLETA DE LA LANDING

Extraer y documentar **todo** lo que contiene la landing. No omitir nada.

### 1.1 Mapa estructural completo (OBLIGATORIO — base del HTML)

Lo primero que se hace al leer la landing es construir este mapa. Es la plantilla que el HTML debe seguir sin desviarse.

```
MAPA ESTRUCTURAL — [NOMBRE DEL PRODUCTO]
═══════════════════════════════════════════
[BANNER/TOP BAR] "texto exacto"  →  CTA: ninguno / "texto"
       ↓
[SEC 1 — NOMBRE DE LA SECCIÓN]
  Elementos: headline, imagen, bullets, lead, etc.
  CTA: ❌ sin botón  /  ✅ "TEXTO EXACTO DEL BOTÓN"
       ↓
[SEC 2 — ...]
  ...
═══════════════════════════════════════════
RESUMEN:
  Total secciones: X
  Total CTAs: X  →  en secciones: N, N, N
  Timer: sí/no — duración original: X minutos
  Elementos de urgencia: [listar: cupos, viewers, frases]
  Precio: $X.XX / tachado $X.XX / ahorro X%
  Garantía: X días
```

### 1.2 Copy por sección
Para cada sección del mapa:
- **Headline / título** — transcribir literal
- **Subheadline / subtítulo** — transcribir literal
- **Lead / primer párrafo** — tono, promesa, gancho emocional
- **Bullets de beneficios** — listar todos, identificar patrón
- **Historia o narrativa** — ¿hay storytelling? ¿arco emocional?
- **Prueba social** — testimonios, cantidad de alumnos/clientes
- **Oferta y precio** — precio normal, precio con descuento, qué incluye, bonos
- **Garantía** — tipo, duración, lenguaje usado
- **CTAs** — texto exacto de cada botón, en qué sección aparece
- **Elementos de escasez/urgencia** — timers (cuántos minutos), cupos, frases exactas
- **FAQ** — preguntas y respuestas presentes
- **Cierre** — último mensaje antes del botón final

### 1.2 Tono comunicacional
Identificar y documentar:
- Registro: formal / coloquial / íntimo / motivacional / técnico / empático
- Persona gramatical predominante (tú/vos/usted/ustedes)
- Recursos retóricos frecuentes (preguntas directas, frases cortas de impacto, repetición, listas, metáforas)
- Emociones predominantes que activa (miedo, deseo, esperanza, vergüenza, aspiración, urgencia)
- Palabras o frases características del copy que definen el estilo

### 1.3 Diseño y UX (si aplica)
- Paleta de colores principal
- Tipografía visible
- Secciones identificadas y su orden
- Elementos visuales destacados (imágenes, iconos, mockups, videos)
- Layout: full-width / columnas / con sidebar

### 1.4 Análisis Visual de Mockups e Imágenes
**Activar siempre que la landing tenga imágenes de producto, mockups, bonos, íconos o ilustraciones.**

Para cada imagen identificada en la landing:

**Si la imagen está disponible como URL (CDN, Shopify, etc.):**
- Listar todas las URLs de imágenes extraídas del HTML, agrupadas por categoría:
  - Hero / mockup principal del producto
  - Imágenes de categorías / síntomas / secciones
  - Imágenes de bonos
  - Íconos de garantía / badges
  - Otros elementos visuales

**Si la imagen es accesible visualmente (captura, imagen adjunta):**
Analizar cada mockup/imagen con visión y documentar:

```
MOCKUP: [nombre o posición en la landing]
─────────────────────────────────────────
Tipo: [portada de ebook / pack 3D / ícono / flat lay / ilustración / foto]
Estilo visual: [minimalista / realista / ilustración digital / fotográfico / etc.]
Paleta: [colores predominantes con hex aproximado si se puede]
Tipografía visible: [fuentes usadas, si hay texto en la imagen]
Elementos: [qué aparece en la imagen — objetos, personas, fondos, texturas]
Mood/sensación: [qué transmite — natural, premium, urgente, cálido, etc.]
Texto visible: [título, subtítulo u otros textos dentro de la imagen]
Dimensiones aproximadas: [landscape / portrait / square / banner]
```

**Luego, para cada mockup, generar el PROMPT HIGGSFIELD listo para usar:**

Ver formato exacto en la sección FASE 5 — PROMPTS HIGGSFIELD.

---

## FASE 2 — DEEP RESEARCH DE LA OFERTA Y EL AVATAR

Usar `web_search` para investigar en profundidad. Ejecutar **al menos 6-8 búsquedas** cubriendo todos los ángulos.

### 2.1 Investigación del Avatar
**Búsquedas sugeridas:**
- `"[nicho/producto]" foro preguntas problemas reddit OR quora`
- `"[nicho]" "no puedo" OR "me cuesta" OR "no entiendo" OR "frustrante"`
- `"[nicho]" amazon reviews OR reseñas libros similares`
- `"[nicho]" grupos facebook OR comunidades comentarios`

**Documentar:**
- **Creencias limitantes** — qué cree el avatar que le impide avanzar
- **Deseos profundos** — resultado final que realmente quiere (no el producto, sino la vida que quiere)
- **Miedos específicos** — a fracasar, al juicio ajeno, a perder dinero, a no poder
- **Lenguaje nativo** — exactamente cómo describe su problema en sus propias palabras
- **Objeciones frecuentes** — por qué no compraría / qué lo frena
- **Transformación deseada** — quién quiere ser / cómo quiere que cambien las cosas

### 2.2 Investigación de Competencia y Ángulos de Copy
**Búsquedas sugeridas:**
- `"[producto similar]" landing page comprar LATAM`
- `site:hotmart.com [nicho]` o `site:gumroad.com [nicho]`
- `"[nicho]" curso ebook plantilla barato español`
- `[nicho] ads facebook copy anuncio 2024 2025`

**Documentar:**
- Ángulos de copy más usados en el mercado (qué promesas se repiten)
- Ángulos que NADIE está usando (oportunidades de diferenciación)
- Precios de referencia en el nicho
- Bonos/extras que la competencia incluye
- Ganchos de titulares que están funcionando

### 2.3 Investigación del Producto
**Búsquedas sugeridas:**
- `[tema del producto] guía completa resultados`
- `[tema del producto] cuánto tiempo resultados`
- `[tema del producto] errores comunes principiantes`

**Documentar:**
- Beneficios reales y demostrables del resultado que ofrece
- Objeciones específicas del producto (¿funciona realmente? ¿es difícil? ¿cuánto tarda?)
- Claims que se pueden fortalecer con datos/evidencia
- Ángulos de credibilidad disponibles

---

## FASE 3 — BRIEF ESTRATÉGICO

Entregar un brief estructurado con todos los hallazgos y decisiones de mejora. Formato:

```
═══════════════════════════════════════════
BRIEF ESTRATÉGICO — [NOMBRE DEL PRODUCTO]
═══════════════════════════════════════════

## 1. DIAGNÓSTICO DE LA LANDING ORIGINAL
- Qué está funcionando bien (conservar)
- Qué está débil o faltando (mejorar)
- Oportunidades perdidas identificadas

## 2. PERFIL DEL AVATAR
- Quién es (demografía + psicografía)
- Su problema principal en sus propias palabras
- Su deseo profundo
- Sus 3 principales objeciones
- Lenguaje que usa (frases textuales encontradas en la investigación)

## 3. MAPA DE ÁNGULOS DE COPY
- Ángulo actual de la landing
- Ángulo recomendado para la versión mejorada (y por qué)
- 3 titulares alternativos para testear
- Ganchos de apertura alternativos

## 4. DECISIONES DE MEJORA
- Cambios en estructura/orden de secciones
- Elementos nuevos a agregar (testimonios, bonos, urgencia, etc.)
- Elementos a eliminar o reducir
- Mejoras en la oferta (precio, bonos, garantía, nombre)
- Mejoras en el tono

## 5. OFERTA MEJORADA
- Nombre del producto (versión mejorada si aplica)
- Nueva propuesta de valor en 1 oración
- Stack de bonos sugerido
- Precio recomendado y justificación
- Garantía recomendada
═══════════════════════════════════════════
```

---

## FASE 4 — HTML MEJORADO PRODUCTION-READY

### PASO 0 — MAPEO OBLIGATORIO ANTES DE ESCRIBIR UNA SOLA LÍNEA DE HTML

⚠️ ESTO ES INNEGOCIABLE: antes de escribir cualquier código, construir y mostrar al usuario el mapa completo de la landing original. Solo después proceder con el HTML.

```
MAPA ESTRUCTURAL — [NOMBRE DEL PRODUCTO]
═══════════════════════════════════════════
[BANNER/TOP BAR] texto exacto | CTA: ninguno / "texto del botón"
       ↓
[SEC 1 — NOMBRE]
  Elementos: qué contiene (headline, imagen, bullets, etc.)
  CTA: ❌ ninguno  /  ✅ "TEXTO EXACTO DEL BOTÓN"
       ↓
[SEC 2 — NOMBRE]
  Elementos: ...
  CTA: ❌ ninguno  /  ✅ "TEXTO EXACTO DEL BOTÓN"
       ↓
[SEC N — ...]
  ...
═══════════════════════════════════════════
TOTAL CTAs: X  →  Posiciones: sec 3, sec 7, sec 9
TOTAL SECCIONES: X
TIMER: ¿existe? ¿cuántos minutos?
ELEMENTOS DE URGENCIA: cupos, viewers, frases
```

Este mapa ES la plantilla del HTML. No se agrega, no se elimina nada que no esté aquí.

---

### REGLA ABSOLUTA DE FIDELIDAD ESTRUCTURAL

El HTML replica la arquitectura EXACTA de la landing — mismo número de secciones, mismo orden, mismos CTAs en las mismas posiciones.

**Lo que SÍ se mejora dentro de cada sección:**
- Copy (más específico, más emocional, lenguaje del avatar)
- Diseño visual (tipografía, colores, layout, espaciado)
- Descripciones de beneficios, bonos, FAQ más elaboradas
- Tono comunicacional según Fase 1

**Lo que NO se toca bajo ningún concepto:**
- Número de CTAs — si el original tiene 4, el HTML tiene 4. Ni uno más.
- Posición de los CTAs — si el CTA 1 va después de la sección de categorías, va ahí. No antes, no después.
- Número de secciones — si el original tiene 11 secciones, el HTML tiene 11.
- Orden de las secciones — el flujo narrativo del original es intencional, no se reordena.
- Secciones sin CTA — si la sección de bonos no tiene CTA en el original, no se le agrega uno.

**La única excepción:** cuando el brief (Fase 3) documentó EXPLÍCITAMENTE una mejora estructural aprobada por el usuario. En ese caso, marcar con comentario:
```html
<!-- ⬆ SECCIÓN NUEVA — aprobada en brief -->
<!-- ⬆ CTA ADICIONAL — aprobado en brief -->
```

---

### REGLAS DE CTAs

1. **Texto**: usar el texto mejorado del brief si lo hay; si no, respetar el texto original. NUNCA inventar CTAs.
2. **Posición**: el CTA va exactamente donde estaba en el original — ni una sección antes ni después.
3. **Cantidad**: contar los CTAs del original y replicar ese número exacto.
4. **Secciones sin CTA en el original = secciones sin CTA en el HTML.** Punto.

Si una sección del original no tenía CTA y querés agregar uno, eso va en el brief (Fase 3) para que el usuario lo apruebe — no se agrega silenciosamente en el HTML.

---

### ESTÁNDARES TÉCNICOS OBLIGATORIOS
- Un solo archivo HTML con CSS y JS inline
- Mobile-first, completamente responsive
- Sin dependencias externas (fuentes desde Google Fonts CDN)
- Meta Pixel ready: `<!-- META PIXEL -->` en el `<head>`
- Shopify-compatible (sin conflictos con Liquid)
- Timer: respetar el tiempo original (si era 10 min, poner 10 min — no cambiarlo a 15)

### ESTÁNDARES DE COPY
- Aplicar tono comunicacional de Fase 1
- Integrar lenguaje nativo del avatar de Fase 2
- Mejorar los textos de beneficios, bonos y FAQ con hallazgos del research
- Urgencia y escasez: solo los elementos que YA existían en el original

### PLACEHOLDERS
Si falta información real, marcar así:
```html
<!-- [PLACEHOLDER: descripción de qué va aquí] -->
```

---

## FASE 5 — PROMPTS HIGGSFIELD PARA MOCKUPS

Generar esta sección **siempre que haya imágenes de producto, bonos o mockups en la landing**, o cuando el usuario pida explícitamente recrear o generar los visuales.

### Flujo de decisión

```
¿La landing tiene imágenes accesibles visualmente?
        ├── SÍ → Analizar con visión → extraer descripción → generar prompt
        └── NO (solo URL sin acceso visual) → Inferir estilo desde contexto
              (nicho, paleta de la landing, tono, tipo de producto)
              → generar prompt aproximado marcado como [INFERIDO]
```

### Estructura del prompt Higgsfield

Para cada imagen/mockup, entregar un bloque con este formato exacto:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📸 PROMPT HIGGSFIELD — [NOMBRE DEL MOCKUP]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MODELO RECOMENDADO: [nano_banana_pro / soul_2 / ms_image]
RATIO: [1:1 / 4:5 / 9:16 / 16:9]

PROMPT:
[prompt completo en inglés, listo para pegar en Higgsfield]

NOTAS:
- [observaciones sobre el estilo, si necesita referencia]
- [si requiere mockup 3D o es imagen plana]
- [si hay texto que debe aparecer en la imagen]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Guía de modelos Higgsfield

| Tipo de imagen | Modelo recomendado |
|---|---|
| Mockup 3D de ebook/PDF premium, portada con detalle | `nano_banana_pro` |
| Pack múltiple de productos digitales con fondo | `nano_banana_pro` |
| Ilustración flat de ícono o categoría | `soul_2` |
| Imagen de producto para ads (DTC) | `ms_image` |
| Imagen de bono individual, cover simple | `soul_2` |
| Imagen con persona / UGC / avatar | `soul_2` |

### Estructura de un prompt de mockup efectivo para Higgsfield

Un buen prompt tiene 5 componentes en este orden:

```
[SUJETO PRINCIPAL] + [MATERIALES/TEXTURA] + [ESTILO VISUAL] + [PALETA/ILUMINACIÓN] + [FONDO/CONTEXTO]
```

**Ejemplos por tipo de mockup:**

**Portada de ebook/recetario (estilo ancestral/natural):**
```
Softcover book mockup titled "[TÍTULO]", rustic kraft paper texture cover with pressed botanical herbs and handwritten-style serif font, warm earthy tones, deep forest green and aged parchment, soft natural side lighting, styled on a wooden surface with dried lavender and mortar, ultra-detailed, 4K product photography
```

**Pack múltiple de bonos/libros:**
```
Flat lay of 10 digital book covers arranged in a neat grid, natural wellness theme, botanical illustration style, cohesive color palette of forest green, warm cream and terracotta, each cover has a distinct herb or plant motif, clean white background with soft shadows, top-down product photography, 4K
```

**Ícono de categoría (síntoma/beneficio):**
```
Minimalist flat illustration of [TEMA — e.g. "digestive system with herbs"], soft botanical style, warm green and cream tones, circular badge format, clean white background, icon design for digital product landing page
```

**Imagen de garantía/badge:**
```
Circular trust badge illustration, green and gold color scheme, shield with laurel wreath, "14 day guarantee" text, premium seal style, clean white background, product UI asset
```

### Reglas para escribir los prompts

1. **Siempre en inglés** — Higgsfield procesa mejor en inglés
2. **Incluir el título del producto** si hay texto visible en la imagen original
3. **Especificar la paleta exacta** de la landing para mantener coherencia visual
4. **Indicar el uso final** al final del prompt: `for digital product landing page` / `for Meta Ads creative` / `for ebook cover`
5. **Para mockups 3D** incluir: tipo de objeto (softcover / hardcover / spiral / tablet screen) + materiales + iluminación
6. **Para imágenes de bonos**: mantener estilo consistente entre todos los bonos del mismo pack — indicar "part of a cohesive series of 10 book covers, same visual style as [descripción del estilo]"

### Entrega final de esta fase

Presentar resumen y preguntar al usuario qué quiere hacer:

```
RESUMEN DE IMÁGENES IDENTIFICADAS
──────────────────────────────────
Total imágenes: X
  - Mockup principal: 1
  - Imágenes de secciones: X
  - Bonos: X
  - Badges/íconos: X

¿Qué querés hacer con los mockups?
  A) Generarlos ahora con Higgsfield (directo en el chat)
  B) Recibir los prompts para generarlos vos mismo
  C) Usar las imágenes originales de la landing tal cual
```

**Si el usuario elige A — GENERACIÓN DIRECTA CON HIGGSFIELD:**

Usar `HIGGSFIELD:generate_image` para generar cada imagen.

Reglas:
- Modelo por defecto: `gpt_image_2`
- Hero/mockup principal: `quality: high`, `resolution: 2k`
- Bonos y secciones: `quality: low`, `resolution: 1k` (más económico)
- Máximo 4 jobs simultáneos — si devuelve rate limit, reintentar hasta que un slot se libere
- Verificar créditos con `HIGGSFIELD:balance` si hay muchas imágenes antes de arrancar

Orden recomendado:
1. Hero principal (1 job, quality high)
2. Bonos de a 3-4 en paralelo con quality low
3. Una vez generadas, actualizar las URLs en el HTML

**Si el usuario elige B — PROMPTS PARA GENERAR MANUALMENTE:**
Entregar todos los prompts en bloques listos para copiar y pegar en Higgsfield.

**Si el usuario elige C:** Mantener las imágenes originales en el HTML tal cual.

---

## NOTAS IMPORTANTES

- **Idioma**: Detectar automáticamente el idioma/variante de la landing original (español LATAM neutro, rioplatense, portugués brasileño) y replicar en el HTML mejorado.
- **Mercado LATAM**: Si el mercado es LATAM, incluir multi-currency comment en sección de precio (`<!-- MULTI-CURRENCY: implementar con Shopify Markets o JS -->`)
- **Fidelidad al tono**: La réplica debe sonar como la voz original del negocio, no como copy genérico. Priorizar la voz y el lenguaje nativo del avatar encontrado en la investigación.
- **Brief primero**: Siempre entregar el brief completo ANTES del HTML. Dar al usuario la oportunidad de ajustar decisiones antes de generar el código.

---

## FLUJO DE EJECUCIÓN

```
INPUT (URL / HTML / imagen)
        ↓
[FASE 1] Extracción completa
   └── [1.4] Análisis visual de mockups (SIEMPRE si hay imágenes)
        ↓
[FASE 2] Deep research (6-8 búsquedas web)
        ↓
[FASE 3] Brief estratégico → mostrar al usuario
        ↓
      ¿Ajustes?
      /       \
    Sí         No
     ↓           ↓
  Ajustar    [FASE 4] HTML mejorado completo
  brief           ↓
             [FASE 5] Prompts Higgsfield
                  → ¿Generar todos los mockups?
                  → Entregar prompts listos para copiar
```

Si el usuario quiere ir directo al HTML sin revisar el brief, ejecutar todo de corrido.
Si el usuario solo quiere los prompts de Higgsfield sin el HTML, ir directo a Fase 1.4 + Fase 5.
