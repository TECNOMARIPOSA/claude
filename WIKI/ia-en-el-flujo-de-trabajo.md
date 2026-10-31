---
tema: IA en el flujo de trabajo
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/masterclass-ia.md, RAW/formacion/lecciones/intro-a-las-apps-de-ia.md, RAW/formacion/lecciones/como-comunicarle-tu-idea-a-google-antigravity-y-setear-la-app.md, RAW/prompts/_indice.md, RAW/youtube/_indice.md]
---

# IA en el flujo de trabajo

La IA no es un accesorio en este negocio: es lo que hace viable la economía del modelo. **Sacar 10 creativos al día y producir un ebook en 10 minutos solo tiene sentido con IA en cada paso.**

Hay lecciones dedicadas al tema — `MasterClass IA` (1h 30min, la más larga de toda la formación), `Intro a las Apps de IA` (25 min) y `Como comunicarle tu idea a Google Antigravity` (28 min) — **todavía sin destilar en detalle**.

## Dónde entra la IA, paso a paso

| Fase | Herramienta | Qué produce |
|---|---|---|
| Modelado de oferta | Prompt Cowboy → ChatGPT | Nombre, contenido, bonus |
| Investigación | Google AI Studio + ChatGPT deep research | Deep research, avatar, offer brief, creencias |
| Hooks | Claude / Hengspark AI en modo investigación | Arsenal de hooks desde contenido viral |
| Guiones | Claude / ChatGPT + prompts de 7 pasos | Guiones y variaciones |
| Producto | Gamma App / Claude | Ebooks completos |
| Portadas y mockups | Sora / Higgsfield / Midjourney | Assets de venta |
| Video | VEO 3, Flow, Seedance, Sora 2, HeyGen | Creativos UGC y VSL |
| Voz | ElevenLabs | Locución |
| Landing | DeepSeek, Magic Patterns, Google AI Studio | HTML de la página de ventas |

Ver [[stack-de-herramientas]] para el inventario completo.

## El patrón: documentos como memoria

El movimiento más característico del sistema, y el que más multiplica el resultado:

> Generar **documentos de investigación una vez** y después **adjuntarlos a cada nueva tarea** de IA.

El deep research, el Avatar Sheet, el Offer Brief y el documento de creencias se guardan en Google Drive por producto y se suben al chat cada vez que hay que producir algo. Eso convierte cada generación en una tarea con contexto real del negocio en lugar de una respuesta genérica. Ver [[investigacion-de-mercado]].

Varios prompts lo exigen explícitamente: el de testimonios en Sora 2 no escribe nada hasta recibir los cuatro documentos.

## Un proyecto de ChatGPT por producto

Patrón operativo concreto: crear un **proyecto** en ChatGPT por cada producto, con sus archivos adjuntos (sales page, avatar, offer brief, investigación) y con **instrucciones fijas**.

### El truco de las instrucciones: endurecer la IA

En el campo de **instrucciones del proyecto** se pega el prompt de `prompt-educar-chatgpt`:

> «De ahora en adelante necesito verdad, no consuelo. Quiero que me desafíes, que cuestiones mis excusas, que me demuestres mis puntos ciegos…»

El motivo:

> «Las inteligencias artificiales **son complacientes, quieren endulzarte el oído**. Le das un rol para que se vuelva crítica.»

El prompt se usa de una forma concreta: **no como mensaje suelto, sino como instrucción permanente del proyecto**, de modo que afecta a todo lo que se genere dentro — guiones incluidos.

## Prompts como activo

Los 23 prompts de `RAW/prompts/` son procesos congelados, no ideas sueltas. Comparten estructura —rol, contexto, reglas duras, formato de salida obligatorio— y varios terminan con una **instrucción de confirmación** antes de generar («confirmá que entendiste y pedime los documentos»), que evita output prematuro.

Existe un meta-prompt (`prompt-generador-de-prompts-maestros`) para producir prompts nuevos con ese mismo marco. Ver [[biblioteca-de-prompts]].

## Prompt Cowboy: el paso previo

Aparece como paso sistemático antes de ChatGPT. Transforma un prompt vago en uno bueno. Hay dos lecciones dedicadas (`Prompt Cowboy y Claude para los Guiones`, partes 1 y 2).


## La ventaja competitiva declarada

El argumento que repite: hacer landings con código generado por IA en vez de con imágenes de Canva o apps de pago, y producir volumen creativo que la competencia no puede igualar.

> «Nadie en el mercado está haciendo esto… ustedes están un paso adelante.»

## Complementos prácticos

### Claude Code como centro de la operación
- Usos: landings HTML, ebooks, **reglas de pausado automático al llegar al CPA objetivo que corren en la nube** (aun con la máquina apagada), **skills** reutilizables (buscar ofertas en la Ads Library, generar ebooks, editar video, armar landings) y consultas a UTMify por MCP.
- **Meta Ads CLI** (herramienta oficial de Meta): se reporta más estable que ir directo a la API, que en algunos casos se asoció a bloqueos de cuentas, y no se rompe con cada actualización de la Marketing API.
  - Setup: Claude Code + Python 3.12 → app en developers.facebook.com (ID + códigos) → **usuario del sistema** en el BM (Configuración del negocio → Usuarios del sistema, rol Admin) con activos asignados: **fanpage, cuentas publicitarias, la app y el pixel** → generar el token y pasárselo a Claude Code.
  - Conviene pedirle el paso a paso al propio Claude, incluso dictado por voz.
- **Qué se hace con él:**
  - Preguntar en lenguaje natural en qué países se vende y cuál es la estrategia por país. Detecta los países con ROAS negativo y, con tu OK, **los pausa en todas las campañas en segundos** (a mano son 20–30 min).
  - Crear campañas masivas con **un copy distinto por creativo**, en vez del mismo texto en 100 anuncios.
  - Investigar anuncios ganadores de la competencia directa e indirecta.
  - Chequear en caliente cambios en la tienda («cambié el precio de los upsells, ¿subió el AOV?»).
- **Navegador:** la extensión de Claude para Chrome o un MCP de navegador sirven para inspeccionar Ads Library y landings, y para configurar tiendas.

### Contexto persistente
- **Carpeta local como «segundo cerebro»:** conocimiento del negocio, transcripciones e historial, para que tenga contexto entre sesiones y cite de dónde sale cada recomendación.
- **Archivo de «aprendizajes»** para no repetir errores. Si una tarea se repite, convertirla en una skill.
- **Dos sesiones en paralelo** sobre la misma base de conocimiento para operaciones grandes. Cada una escribe un resumen antes de cerrar.

### Costo y consumo
- **La terminal (Claude Code) consume bastante menos que la app web o móvil** para la misma tarea.
- Si el plan se agota:
  - Automatizaciones nocturnas en la nube
  - Un proveedor secundario (Gemini, GPT/Codex)
  - **Bajar el nivel de effort** en tareas livianas
- Existe un modo auto/bypass para no aprobar cada permiso.

### Qué IA para qué
- **ChatGPT** para casi todo, imágenes incluidas.
- **Claude** para guiones y copy (más conversacional, mejor con contexto largo) y para el código de la landing.
- **DeepSeek** como alternativa gratis a Claude para código, más limitada en lo demás.
- **Al pedir imágenes, siempre dar el formato** (2:3 para portada de ebook, 1:1 para mockup o feed) y pedir explícitamente que **suba la percepción de valor** («que un producto de 20 se vea de 2.000»). Sin esa instrucción el resultado sale genérico.
- **Wispr Flow** (dictado por voz) para iterar prompts y copy más rápido.

Relacionado: [[biblioteca-de-prompts]] · [[stack-de-herramientas]] · [[creacion-de-productos-digitales]] · [[investigacion-de-mercado]]
