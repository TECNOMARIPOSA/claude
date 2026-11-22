# PicassoIA · video igual al de Argentina, con el cuadro de Calma en Colores

## Cómo es el video de referencia (34 s, 9:16)
Es una secuencia de tomas cortas, todas con una mano pintando con pincel sobre un cuadro de pintura por números, con subtítulos grandes y palabras resaltadas:
1. **0–5 s:** el cuadro terminado, primero muy de cerca y luego se aleja hasta mostrarlo apoyado en un caballete sobre una mesa de madera, con frascos de pintura y pinceles.
2. **5–11 s:** primerísimo plano de la lámina numerada: un pincel pinta de rosa una zona pequeña (labios) y otro pincel mancha de verde.
3. **11–18 s:** planos cerrados de una mano rellenando zonas con pintura sobre la lámina (ojos, negro del contorno).
4. **18–25 s:** más planos de la mano; toma de una mano con un frasquito rojo y un pincel; pinceladas grandes naranjas que cubren una zona.
5. **25–31 s:** pincel pintando un círculo naranja; la obra casi terminada.
6. **31–34 s:** el cuadro terminado, otra vez de cerca, y se aleja hasta el cuadro en el caballete con las pinturas.
Sonido: voz en off con música suave. Los subtítulos (que se ven en ese video) se añaden después.

## Imágenes para subir a PicassoIA (el cuadro de Calma en Colores)
| Archivo | Para qué |
|---|---|
| `PICASSO3_imagen-escena-pintando_916.png` | **Imagen inicial**: mano con el pincel sobre la lámina de las Cataratas del Iguazú, mitad pintada. |
| `PICASSO3_imagen-escena-cuadro-terminado_916.png` | **Imagen final** (último cuadro): la misma mesa con el cuadro terminado. |
| `PICASSO3_imagen-cuadro-terminado-color_4x5.png` | El cuadro a color, solo la ilustración (1600×2000). Úsala como **referencia** o para planos de «cuadro terminado». |
| `PICASSO3_imagen-cuadro-numerado_4x5.png` | La lámina numerada, solo la ilustración (1600×2000). Referencia para los primeros planos con números. |

## Cómo generarlo (importante)
Un video de 34 s con 12 tomas distintas **no se genera de una vez**: los modelos hacen clips de 5–15 s. Se hace por clips y se une en CapCut. Con Seedance 2.5 Lite (imagen a video, 9:16, 720p):

| Clip | Duración | Imagen inicial | Qué pedir |
|---|---|---|---|
| A (apertura y cierre) | 10 s | Escena con el cuadro terminado | Plano muy cercano del cuadro que se aleja despacio hasta verlo sobre la mesa con pinturas |
| B (mano pintando cerca) | 10 s | Escena pintando | Mano que pinta con toques cortos; cámara se acerca un poco |
| C (primer plano numerado) | 5 s | Cuadro numerado | Pincel que pinta una zona pequeña de azul sobre un número |
| D (la lámina se llena) | 10 s | Escena pintando (inicio) + cuadro terminado (final) | La lámina se va llenando de color |

## Prompts (inglés, suelen funcionar mejor)
**Clip A:** Vertical social-media ad video. Extreme close-up of a finished paint-by-numbers painting of a tropical waterfall, vivid colours with black outlines and small numbers. The camera slowly pulls back to reveal the painting lying on a warm wooden table with eucalyptus leaves, a lit candle and small paint pots. Soft window light, calm cozy mood. Smooth steady movement. No text, no logos.

**Clip B:** Vertical video, top-down close shot of a woman's hand painting a paint-by-numbers sheet with a thin brush on a wooden table. Short precise dabs filling the numbered zones with vivid colour; the hand drifts slowly leftwards, lifts to pick up paint and returns. Colour appears where the brush passes. The camera pushes in slowly about 15%. Natural five-finger hand, sharp focus on the brush tip. No text, no logos.

**Clip C:** Vertical macro close-up of a thin brush painting a small blue zone on a numbered line-art paint-by-numbers sheet. The paint fills the shape neatly up to the black outline, a few numbers visible. Gentle slow camera push-in, soft light, shallow depth of field. No text, no logos.

**Clip D:** Vertical video of the same scene: a hand painting the sheet; the whole sheet gradually fills with colour from the waterfall to the jungle until it is completely painted. Slow gentle zoom-out at the end. No text.

## Después (en CapCut o similar)
- Une los clips en el orden del video de referencia: A (cuadro terminado) → C → B → D → A (cierre).
- Añade los subtítulos y la voz en off del guion H30 (tengo el guion adaptado a LATAM en `CREATIVOS/entregas/2026-11-20/.../261120_calma-en-colores_PSL-N3_VOZ_H30_v1_TEXTO.md`).
- Música suave.

## Aclaraciones
- El video de Argentina usa pintura acrílica sobre lienzo en caballete. Calma en Colores vende láminas **para imprimir**, así que el prompt muestra una lámina de papel sobre la mesa, no un lienzo: así lo que ve la persona coincide con lo que compra.
- La cuenta de PicassoIA que me mostraste no permite generar (plan «Free trial» sin MCP). Estos archivos son para que tú lo pidas en su web, o para cuando actives un plan.
- Tampoco he verificado cómo se ve el video generado.
