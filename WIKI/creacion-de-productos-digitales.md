---
tema: Creación de productos digitales
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/como-crear-ebooks-completos-con-ia-contenido-portadas-y-mockups.md, RAW/formacion/lecciones/como-hacer-increibles-ebooks-con-claude-higgsfield.md, RAW/formacion/lecciones/crea-un-gpt-personalizado-para-sumar-a-tu-oferta.md, RAW/prompts/prompt-ebook-con-claude.md]
---

# Creación de productos digitales

La fase que en el modelo antiguo era el cuello de botella y hoy no lo es. La consigna: **producir lo más rápido posible para salir a validar** ([[validacion-de-oferta]]).

> «Ya saben cómo crear un ebook en 10 minutos, una portada con IA en 0 minutos y un mockup para su página de ventas.»

## El producto es lo menos importante — y aun así tiene que ser 10/10

Dos afirmaciones que parecen contradecirse y no lo hacen:

> «El producto digital es **lo menos importante**. Lo que genera dinero es **la comunicación**.» Los anuncios son el **90-95% del éxito**.

> «El producto que entregues tiene que ser **lo mejor que la persona puede recibir en su casilla de correo**. Tiene que sentirse feliz de haber puesto sus 15, 19 o 29 dólares.»

**El producto no adquiere clientes: los retiene.** No mueve la aguja del CPA, pero sí la de recompra, recomendación y backend ([[modelo-low-ticket]]).

**El error correspondiente:** tardar un mes creando el PDF antes de saber si la oferta vende. Ver el flujo MVP de [[validacion-de-oferta]].

## Las cuatro herramientas

**Prompt Cowboy → ChatGPT → Gamma App → Sora**

**Qué hace Prompt Cowboy:** transforma un *lazy prompt* —vago, de una línea— en un prompt potente y estructurado. Se le escribe algo como «quiero que actúes como experto en prompting para crear ebooks» y devuelve el prompt de verdad, que se lleva a ChatGPT.

Y el principio que lo justifica:

> **Mejor input, mejor output.** «Cuando entendés que la IA es tu empleado, y que cuanto mejor te comuniques mejores resultados vas a tener, cambia la cosa.»
>
> «Muchas veces estamos disconformes con lo que nos genera la IA, pero es porque **no la sabemos utilizar**.»

Merece la pena pedirle a ChatGPT que **detalle aún más** el prompt antes de llevarlo a Gamma. El coste es un minuto; la diferencia en el ebook resultante, grande.

## El flujo completo

Entrada: el documento de oferta con nombre, contenido, bonus y nombres de bonus ([[seleccion-y-modelado-de-oferta]]).

**1. ChatGPT genera el prompt para Gamma.**
Se le pide un prompt detallado para el ebook concreto. El material insiste en **exigir detalle**: la primera respuesta suele ser genérica y hay que pedir explícitamente qué debe contener cada página.

Instrucción útil del ejemplo: *«Ignora la portada, la introducción, los tips y el cierre. Solo las 15 recetas»* — la portada se hace aparte y con otra herramienta.

**2. Gamma App genera el ebook.**

- Crear nuevo → **Pegar texto** → formato **A4**
- «Generar a partir de notas o un esquema»
- Número de módulos (en el ejemplo, 20)
- Cantidad de texto: **detallado**
- Elegir tema
- **Mientras genera**: configuración de página → tamaño de fuente **L** → «adaptar el contenido para que se ajuste»

**3. Portada con Sora.**
Se le pide a ChatGPT el prompt para Sora, se genera en **formato 2:3** (proporción de portada de libro) y se descarga.

**4. Mockups de presentación.**
Prompt pedido a ChatGPT para Sora, con especificación explícita: **mockup en formato libro + mockup en formato iPhone, en un entorno coherente con la temática** del producto. Salen las imágenes para la página de ventas. Ver [[imagenes-y-mockups]].

**5. Montaje final en Gamma.**
Se sube la portada como imagen del primer módulo (diseño de fondo → reemplazar imagen → efecto de superposición) y se añade una imagen a cada sección.

## Duración según el rol del producto

- **Bonus**: cortos, 15–20 páginas. No necesitan más
- **Producto principal**: más extenso, pero la lógica es la misma

## Vía alternativa: ebook con Claude

El prompt `prompt-ebook-con-claude` toma otro camino: rol de autor experto + director editorial + maquetador de PDFs que domina **HTML/CSS para impresión (paged media)**. Produce el ebook completo maquetado, no un generador de slides. Hay también una lección de **Claude + Higgsfield**.

Ver [[biblioteca-de-prompts]].

## GPT personalizado como parte de la oferta

Hay lección dedicada a **crear un GPT personalizado para sumarlo a la oferta**. Es un bonus de coste marginal cero con valor percibido alto — encaja exactamente con la lógica de bonus de [[seleccion-y-modelado-de-oferta]].

## Nota de contexto

Santiago cuenta en esta lección que tuvo que **rehacer su propia oferta porque un alumno se la modeló**. Lo presenta como normal:

> «Cuando a vos te va bien, alguien te va a copiar.»

Es coherente con el resto del sistema: la ventaja no está en el producto, está en la velocidad de iteración y en el backend. Existe además una lección específica, `como-burlar-a-tu-competencia-para-que-no-te-copien`.

## Herramientas

**Gamma App** (ebooks) · **ChatGPT** (prompts y contenido) · **Claude** (ebooks maquetados) · **Sora** (portadas y mockups) · **Higgsfield**

## Complementos prácticos

- **Dos calidades según la etapa:** para el **MVP**, Gamma (rápido y suficiente para validar). Recién después de validar, **Claude + Higgsfield** o **Claude + KIE.ai**: un ebook ilustrado de 100–150 páginas sale **~3–7 USD** con modelos tipo GPT-image por API.
- **Auditoría antes de entregar:** hubo reclamos por PDFs hechos con IA con imágenes mal puestas y errores de layout. Conviene **una segunda pasada con otro modelo** que busque errores, sobre todo si el documento tiene muchas imágenes.
- **Gamma, detalles de oficio:**
  - Borrar del texto pegado las líneas de metadata o instrucciones.
  - **Una línea pegada al borde del módulo es señal de texto cortado.**
  - «Probar un nuevo diseño» para rehacer un módulo que quedó feo.
  - **Exportar a PDF** al final.
  - Mockups de presentación en **1:1** (libro + iPhone en un entorno acorde a la temática).
- **Ebook 100% texto en HTML editorial con Claude** (sin imagen por página):
  - **Mapeo promesa → capítulo:** antes de escribir, extraer de la landing cada promesa y bullet, y cubrirlos todos.
  - **Estándar:** «test del ¿y cómo?» (la pregunta de implementación se responde en el mismo párrafo). Cada capítulo sigue concepto → por qué importa → cómo se hace → ejemplo → errores comunes → mini-resumen. **Nunca estadísticas inventadas.**
  - **Salida:** un HTML autocontenido A4 con `break-before: page` en portada, índice y capítulos, `orphans`/`widows`, y cajas de tip, error común, checklist y ejercicio en CSS puro.
  - **Extensiones:** Guía Enfocada 20–30 págs · Ebook Completo 40–60 · Manual Definitivo 80+.
- **Referencias de temario según el nicho:** Etsy (plantillas, patrones) y Domestika (cursos). Sirven para entender qué estructura espera el comprador. Adaptar, no copiar el contenido de otro.

Relacionado: [[seleccion-y-modelado-de-oferta]] · [[imagenes-y-mockups]] · [[ia-en-el-flujo-de-trabajo]]
