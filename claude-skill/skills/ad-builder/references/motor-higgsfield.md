# Motor de producción — Higgsfield

Verificado el 2026-08-11: plan **ultra**, **2.782 créditos**. Consultar `balance` antes de un lote
grande; informar el costo antes de gastarlo.

No hace falta instalar nada: ni Node, ni ffmpeg, ni Homebrew, ni API keys. Todo pasa por el MCP ya
conectado.

---

## 1. Costos reales

| Qué | Modelo | Costo |
|---|---|---|
| Estático 1k, cualquier ratio | `nano_banana_pro` | **2 créditos** |
| Estático 1k, product ad | `marketing_studio_image` | **2 créditos** |

Una tanda de 20 estáticos = **40 créditos**. Con el saldo actual, ~1.390 imágenes.

**Siempre preflight antes de un lote**: `generate_image` con `get_cost: true` no lanza el job, solo
devuelve el costo. Obligatorio para video, donde el costo escala con la duración.

⚠️ **No sustituir un motor por otro sin comparar costo.** Si falta algo, pedirlo — no cambiar de
servicio por conveniencia.

`use_unlim`: **no usarlo por iniciativa propia**. Solo si el usuario lo pide explícitamente.

---

## 2. Estáticos

### Qué modelo

| Caso | Modelo | Por qué |
|---|---|---|
| Ad con **texto legible** (headline, lista, badge) | `nano_banana_pro` | Es el que renderiza tipografía sin romperla. Soporta 4:5 |
| Ad de producto / mockup comercial | `marketing_studio_image` | Pensado para ads de producto |
| Detalle o retoque sobre una imagen ya buena | mismo modelo + `medias` con el `job_id` anterior | Mantiene la línea visual |

Ratios disponibles en ambos: `1:1` · `4:5` · `3:4` · `9:16` · `16:9` · `4:3` · `5:4` · `3:2` · `2:3`
· `21:9`.

**4:5 es el que mejor rinde en Feed.** Resolución `1k` por defecto; `2k`/`4k` solo si el creativo lo
necesita de verdad — en un feed no se nota y el costo sube.

### Llamada

```
generate_image
  params:
    model: "nano_banana_pro"
    prompt: "<PROMPT>"
    aspect_ratio: "4:5"
    resolution: "1k"
    count: 1
```

`count` 2–4 sirve **solo para variantes del mismo prompt**. Para prompts distintos —que es el caso
normal de una tanda— usar `generate_image_batch` (2–12 pedidos independientes) y después
`jobs_wait` + un solo `show_generation_by_ids`.

### Después de generar — siempre

1. Descargar el resultado a `CREATIVOS/entregas/<fecha>/<dashboard>-<producto>/` con el nombre
   completo de la nomenclatura.
2. **Abrir el archivo y mirarlo.** Que el job vuelva `completed` no dice nada sobre si la imagen
   sirve.
3. Verificar texto, cifras y listas uno por uno contra el producto real.

### Encadenado de estética

Una vez aprobada la primera pieza, pasar su `job_id` como `medias` para las siguientes: mantiene la
línea creativa y evita que cada pieza de la tanda parezca de otro producto. Es lo que hace que un
`LC` (línea creativa) sea comparable consigo mismo.

### Mockups

`WIKI/imagenes-y-mockups.md` dice que para **mockups** la preferencia es Sora, no nano banana. Si
el usuario pide un mockup de producto para la landing, **entregar el prompt** salvo que pida
generarlo acá. Para ads dentro del feed, nano banana sí.

---

## 3. Video y UGC

Los workflows de Higgsfield son bundles con instrucciones propias. **Cargar el workflow antes de
generar**, nunca improvisar con `generate_video` suelto:

```
get_workflow_instructions                 → lista los workflows
get_workflow_instructions { workflow }    → carga el SKILL.md de ese workflow
```

| Necesidad | Workflow |
|---|---|
| UGC talking-head (creador hablando a cámara) — **el default** | `ugc-flow` |
| Producto solo, voz en off, nadie en cámara | `ugc-product-flow` |
| Unboxing / primera reacción | `ugc-unboxing-flow` |
| Try-on (productos usables) | `ugc-try-on-flow` |
| Tutorial paso a paso | `ugc-tutorial-flow` |
| UGC a partir de la URL de la landing, mostrando la página | `ugc-saas-flow` |
| Video narrado sin cara (explainer, historia) | `faceless-channel-video` |
| Thumbnail / portada | `youtube-thumbnail-generator` |

### Overrides obligatorios sobre cualquier workflow

Las reglas de `WIKI/ugc-y-video-generativo.md` mandan sobre lo que diga el workflow:

- **Sin subtítulos quemados.** Varios workflows los traen por defecto (`ugc-tutorial-flow` incluso
  quema "Step N"). Desactivarlos: los subs van después en CapCut.
- **Sin texto sobreimpreso ni gráficos**, salvo pedido explícito.
- **Sin música**, salvo pedido explícito.
- **9:16**, handheld, natural, documental.
- Voz en el idioma del mercado del dashboard, con el registro correcto (rioplatense para AR, latino
  para LatAm, inglés para EN).
- Si el personaje sostiene el producto, **lo sostiene mientras habla**.

### Costos de video

Escalan con la duración y el modelo. **Preflight obligatorio** con `get_cost: true`, y **generar una
pieza corta primero** para medir el consumo real antes de comprometer un lote. Con `ultra` hay
créditos suficientes para equivocarse una vez, no diez.

---

## 4. Otros tools útiles del stack

| Tool | Para qué |
|---|---|
| `generate_image_batch` + `jobs_wait` | Tandas de estáticos con prompts distintos |
| `reframe` | Pasar un creativo a otro ratio sin regenerarlo — la vía barata de la diversidad de tamaño |
| `upscale_image` / `upscale_video` | Subir resolución de un ganador antes de escalar |
| `remove_background` / `outpaint_image` | Recortes y extensiones de encuadre |
| `media_import_url` → `media_id` | Meter una referencia externa (swipe, página del producto) como input |
| `virality_predictor` | Chequeo de hook/retención antes de subir un video |
| `show_generations` | Recuperar generaciones anteriores de la sesión |

⚠️ `medias[].value` acepta **`media_id` o `job_id`**, nunca una URL directa. Para una imagen de
referencia que está en la web: primero `media_import_url`.

---

## 5. Lo que NO se usa

El sistema original de referencia corría **GPT Image 2 + HeyGen + Remotion + faster-whisper**. Acá no:

- No hay Node, npm, ffmpeg ni Homebrew instalados en esta máquina.
- Remotion existe para quemar subtítulos karaoke y jumpcuts — y la regla es **sin subtítulos**, se
  editan en CapCut.
- HeyGen cobra ~1 crédito por segundo de video y tiene tres bolsas de crédito distintas que no se
  comunican entre sí. Higgsfield ya está pago y conectado.

Si en algún momento hace falta edición local (empalmar hooks sobre un cuerpo validado), **eso se hace
en CapCut**, que es donde ya está el flujo de trabajo.
