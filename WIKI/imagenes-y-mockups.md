---
tema: Imágenes y mockups
actualizado: 2026-08-10
fuentes: [RAW/contexto-chatgpt.md, RAW/prompts/prompt-crear-mockups.md, RAW/prompts/prompt-one-shot-mockups.md, RAW/prompts/prompt-imagenes-ads.md, RAW/formacion/lecciones/como-crear-crear-recursos-visuales-con-ia-para-sus-landings-testimonios-mockups-fondos-imagenes-carruseles.md, RAW/formacion/lecciones/como-crear-un-arsenal-de-imagenes-con-ia.md]
---

# Imágenes y mockups

## El problema que resuelve un mockup

Un producto digital es intangible. El mockup es lo que le da **valor percibido** en la página de ventas. El principio, textual:

> El producto debe parecer algo que una persona estaría dispuesta a pagar.

No debe parecer un PDF barato, una plantilla genérica, una portada de Canva ni una imagen plana.

## La regla más dura: NO FLAT COVERS

Hay una preferencia declarada y fuerte contra los diseños planos. La estética buscada es **premium, editorial, realista, profesional, con profundidad**.

Santiago trabaja con lo que llama las **«Rules of $100K design»**:

- Cover art de nivel editorial
- Tipografía con apariencia **embossed**
- **Holographic overlays**
- Mockups premium
- Presentación de producto de alto valor percibido

## Los prompts

| Prompt | Enfoque |
|---|---|
| `prompt-crear-mockups` | Rol de Director de Arte Senior. Especialidad: *high-end product packaging* + psicología del color aplicada a ventas. Ojo obsesivo por iluminación de estudio y texturas reales (papel mate…) |
| `prompt-one-shot-mockups` | Director de Arte 3D + packaging de lujo. «Transformar productos digitales intangibles en objetos de deseo fotorrealistas con valor percibido de 100.000 USD» |
| `prompt-imagenes-ads` | Genera prompts de texto-a-imagen para anuncios estáticos a partir de los insumos creativos |

Ambos prompts de mockup se solapan bastante — conviene fusionarlos o decidir cuál queda ([[biblioteca-de-prompts]]).

## El one-shot prompt de mockups

Datos que hay que darle:

- **Nombre del entregable**
- **Qué imagen es**: producto principal, bonus o upsell
- **Tipo de mockup**: bundle completo · solo libro · solo caja · iPad · iPhone · MacBook · tapa blanda
- **Formato**: 1:1 · 16:9 · 3:4 · 9:16
- **El texto o PDF de la sales page**

Flujo: generar el one-shot prompt en **Claude**, ejecutarlo en **ChatGPT** para la imagen. (O todo en ChatGPT, aunque Claude da mejor output para el prompt.)

Para qué sirve el mockup, en una línea: **subir la percepción de valor de la oferta**.

## El prompt de imágenes no crea desde cero

Detalle que cambia cómo se usa:

> El prompt **se apalanca de imágenes ganadoras que vos le pases**. No inventa de la nada.

De dónde salen esas imágenes de referencia:

- **Las tuyas que ya funcionaron**, si la oferta lleva tiempo corriendo — es lo mejor
- Si la oferta es nueva: **herramientas espía** (AdsPro y similares) para extraer las que están escalando en el nicho

### El flujo

1. **Google AI Studio (Gemini 3.5 Pro)** procesa la **página de ventas** con el prompt base
2. Contexto mínimo que hay que darle: **nombre de marca, nicho, qué vendés y a quién**
3. Santiago además adjunta los documentos de [[investigacion-de-mercado]]: **avatar, creencias previas a la compra, offer brief e investigación de mercado**
4. El output son los **textos** de los creativos; las imágenes se generan después en otra IA

## Recursos visuales para landings

Hay lección dedicada que cubre la producción completa de assets: **testimonios, mockups, fondos, imágenes y carruseles**. Los testimonios de las landings ganadoras Santiago los crea **con su propio WhatsApp** ([[pagina-de-ventas]]).

También existe un prompt para generar **secciones de comentarios de Instagram ultra realistas** como prueba social (`prompt-comentarios-positivos-ig`).

## Imágenes en el testeo

Las imágenes no son un formato secundario. En el pre-testeo la proporción es **20 imágenes por cada 10 videos** ([[testeo-de-creativos]]), y en el material aparece más de un caso donde el creativo que vendió fue una imagen mientras los videos tenían el CPC duplicado.

## Optimización técnica

Las imágenes de la landing se optimizan en dos pasos, en este orden:

1. **Squoosh.app** → reduce paleta y convierte a **WebP**
2. **TinyPNG** → comprime el WebP (~6% adicional)

Se usa el archivo que sale de TinyPNG. Importa por velocidad de carga, que impacta directamente en la brecha entre CPC y costo por visita ([[metricas-y-kpis]]).


## Mockups con fondo transparente para el checkout

Arriba del checkout va un **conjunto de mockups 16:9 con fondo transparente**. El proceso que funciona:

1. Generarlos en Higgsfield (Nano Banana Pro), 16:9, sobre **fondo magenta plano #FF00FF**. Nunca sobre blanco.
2. **El pedido del fondo va arriba de todo en el prompt**, como "CRITICAL REQUIREMENT: solid magenta #FF00FF background. Not white. Not cream." Si va al final, lo ignora y saca fondo blanco.
3. **Recortarlo con un script propio por color (chroma key)**, no con el quitafondos automático, que se come el papel blanco y los tonos crema del producto. Pedile a Claude el script: toma el color de las 4 esquinas, hace un borde suave, erosiona 1 píxel y limpia el reflejo magenta. Verificación: cero píxeles magenta dentro del producto.
4. Exportar en **WebP (~120 KB)** para subir, y guardar el PNG maestro de 1920×1080.

- **El texto sale exacto** si se lo cita entre comillas y se pide "spelled exactly, correctly kerned", acentos incluidos. Aprovechalo para poner un dato real de la oferta en pantalla, no texto de relleno.
- **El mockup del checkout lleva la identidad de la página de ventas que la persona acaba de ver**, no la del backend. Si no coincide, parece otro producto.

## Herramientas

| Para qué | Herramienta preferida |
|---|---|
| **Mockups** | **Sora** — «no me gusta nano banana para mockups» |
| **Anuncios en imagen** | **Nano banana** |
| Prompt del mockup | **Claude**, y se ejecuta en ChatGPT/Sora |

Otras: Midjourney v6 · DALL-E 3 · Higgsfield · Grok (B-roll) · Canva (landings de imágenes apiladas) · Fireshot (capturas de competencia).

**Truco de encadenado:** una vez generado el mockup del producto principal, se le pide a la IA *«seguí esta línea y creame una similar para el bonus X»* — así toda la oferta queda con **estética coherente**. Un bundle completo sale en unos 5 minutos.

## Complementos prácticos

- **Mismo prompt en varios modelos a la vez** (Higgsfield y Sora; Nano Banana Pro, Seedream 4.5, Flux). Cada uno da un resultado distinto y salen variantes reales del mismo concepto.
- **Filtros para buscar anuncios de imagen ganadores en la herramienta espía:** formato imagen, **más de 3 días corriendo**, marca con **+30 anuncios activos**, nicho relacionado. Se usan como referencia de composición («adaptá este formato ganador a mi producto»), nunca copiados literales.
- **Segundo y tercer anuncio del mismo concepto** variando lo visual sin repetir composición. Así se arma el contenido flexible.
- **Meta tiene generación de imágenes nativa** en el editor de anuncios, con variantes automáticas a partir de una imagen subida.
- **Testimonios y capturas para la landing:** el prompt de imagen no se escribe a mano. Se le pide a ChatGPT o Claude («comentario de Facebook», «captura de chat de WhatsApp», «fondo de landing de alto valor percibido»).

Relacionado: [[pagina-de-ventas]] · [[creacion-de-productos-digitales]] · [[ugc-y-video-generativo]] · [[biblioteca-de-prompts]]
