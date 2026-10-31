---
tema: Investigación de mercado
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/investigacion-profunda-del-mercado-para-tu-product.md, RAW/contexto-chatgpt.md, RAW/prompts/prompt-angulos.md]
---

# Investigación de mercado

Es la pieza que Santiago llama «oro» y manda hacer «a rajatabla». No es investigación por curiosidad: produce **cuatro documentos que después alimentan todo lo demás** —guiones, imágenes, VSL, correcciones de landing— y que evitan volver a empezar de cero cada vez.

> «Esto te va a dar muchísima claridad y muchísima velocidad en la toma de decisiones.»
> (`RAW/formacion/lecciones/investigacion-profunda-del-mercado-para-tu-product.md`)

## El procedimiento

**1. Capturar la landing del competidor.**
Con la extensión **Fireshot** se hace un screenshot de la página de ventas completa y se guarda como imagen/PDF.

**2. Google AI Studio rellena la plantilla de prompt.**
En vez de completar a mano el campo «qué vendés, qué transformación prometés y a quién», se le pasa la captura a Google AI Studio y lo rellena a partir de la landing.

**3. Cadena de prompts en ChatGPT.**
Se ejecutan en secuencia sobre el mismo chat, adjuntando el PDF de la página de ventas:

- Prompt 1 → contexto del producto
- Prompt 2 → se suben dos documentos de metodología («Investigación parte 1 y 2»)
- Prompt 3 → **genera el prompt de deep research**

**4. Deep research en chat nuevo.**
El prompt generado se pega en un chat limpio, en modo investigación profunda. Hace 2–3 preguntas de aclaración (p. ej. en qué países se va a vender), tarda ~10 minutos y devuelve **un documento de ~22 páginas**.

**5. Los tres documentos derivados.**
Sobre el deep research se aplican plantillas sucesivas:

| Documento | Qué contiene |
|---|---|
| **Avatar Sheet** | Apariencia, entorno, lenguaje, nivel socioeconómico del avatar |
| **Offer Brief** | El resultado exacto que se celebra, mecanismo, claims permitidos |
| **Documento de creencias** | Se genera adjuntando los tres anteriores juntos |

## Dónde vive todo

Un **Google Drive con una carpeta por producto**. Es lo que convierte la investigación en un activo reutilizable en lugar de un chat perdido.

## Para qué sirve después

Estos documentos son la **fuente de verdad** que consumen los prompts de producción. Varios los exigen explícitamente antes de escribir nada — el de testimonios en Sora 2, por ejemplo, pide analizar Avatar Sheet, página de ventas, Offer Brief e investigación de mercado antes de generar. Ver [[biblioteca-de-prompts]].

Usos concretos que menciona el material:

- Generación de imágenes y guiones ilimitados
- VSL
- Corregir la página de ventas cuando baja la conversión
- Encontrar ángulos nuevos ([[angulos-publicitarios]])
- Alimentar cualquier IA con contexto real del producto y del avatar

## Investigación de ángulos

Complementaria y con prompt propio (`RAW/prompts/prompt-angulos.md`): investigación online sobre el producto para encontrar mercado, avatar, competidores, demanda, ángulos, hooks, objeciones y posicionamiento.

El principio que ordena el análisis de competencia: no copiar literalmente, sino identificar **qué está funcionando y por qué** para después **adaptar → mejorar → testear**.

Relacionado: [[seleccion-y-modelado-de-oferta]] · [[angulos-publicitarios]] · [[biblioteca-de-prompts]] · [[pagina-de-ventas]]
