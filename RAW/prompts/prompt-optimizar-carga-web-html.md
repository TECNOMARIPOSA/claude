---
nombre: Prompt Para Optimizar las Webs HTML
tipo: prompt
anadido: 2026-08-10
---

# Prompt Para Optimizar las Webs HTML

> Optimiza HTML de landing pages para Core Web Vitals y trafico pago sin alterar el diseno.

---

Prompt Para Optimizar las Webs HTML

Asume el rol de un Ingeniero de Performance Web Senior con especialización
en Core Web Vitals, optimización de landing pages para paid traffic
(Meta Ads, Google Ads, TikTok Ads) y despliegue en plataformas Shopify.

Tu único objetivo es tomar el código HTML que te entrego y devolverlo
optimizado al máximo nivel técnico posible, sin alterar absolutamente
nada de lo que el usuario ve: ni el diseño, ni el copy, ni los colores,
ni las secciones, ni el orden, ni las funcionalidades.

La página resultante debe cargar en menos de 1.5 segundos en conexión
móvil 4G y superar el 95% de tasa de carga exitosa en campañas de Meta Ads.

Te pego el código completo a continuación:

[PEGA AQUÍ TU CÓDIGO HTML COMPLETO]

═══════════════════════════════════════════════════
RESTRICCIÓN ABSOLUTA — LEE ESTO ANTES DE EMPEZAR
═══════════════════════════════════════════════════

NO puedes modificar, eliminar, reordenar ni agregar ninguno de estos
elementos: secciones de contenido, textos, títulos, copy de ventas,
precios, colores, tipografías visibles, imágenes mostradas,
funcionalidades interactivas (acordeones, carruseles, modales,
contadores, flip cards, formularios, animaciones de scroll).

El usuario final no debe notar ninguna diferencia visual ni funcional.
Solo cambia la implementación técnica interna.

═══════════════════════════════════════════════════
CONTEXTO TÉCNICO — SHOPIFY + CÓDIGO GENERADO CON IA
═══════════════════════════════════════════════════

- El código es un único archivo HTML (landing page completa).
- Las imágenes están alojadas en el CDN de Shopify
  (dominio: cdn.shopify.com).
- Las fuentes tipográficas se cargan desde Google Fonts.
- El código fue generado con IA y puede contener ineficiencias típicas:
  CSS no minificado, JS no diferido, imágenes sin atributos de carga,
  fuentes bloqueantes, recursos externos sin hints de precarga,
  animaciones que consumen GPU innecesariamente.
- No existe acceso al servidor, a archivos separados ni a configuración
  de hosting. Todo debe resolverse dentro del único archivo HTML.

═══════════════════════════════════════════════════
METODOLOGÍA — EJECUTA LOS 10 PASOS EN ORDEN
═══════════════════════════════════════════════════

──────────────────────────────────────────────────
PASO 1 — AUDITORÍA COMPLETA DE PERFORMANCE
──────────────────────────────────────────────────

Antes de modificar nada, analiza el código completo e identifica todos
los problemas de rendimiento existentes. Clasifícalos en tres niveles:

CRÍTICO: Bloquea la carga inicial. Ejemplos: fuentes externas sin
font-display, imágenes above-the-fold sin preload, JavaScript síncrono
en el <head>, CSS externo bloqueante.

ALTO: Retrasa el Time to Interactive. Ejemplos: imágenes sin lazy load,
JS monolítico sin defer, recursos de terceros sin dns-prefetch,
background-attachment:fixed en móvil, will-change mal aplicado.

MEDIO: Genera layout shift o consume recursos innecesarios. Ejemplos:
imágenes sin width/height explícitos, animaciones CSS always-on,
requestAnimationFrame loops activos en dispositivos táctiles,
CSS con comentarios y espacios sin minificar.

Presenta esta auditoría como tabla antes de entregar el código.

──────────────────────────────────────────────────
PASO 2 — OPTIMIZACIÓN DEL <head> Y RESOURCE HINTS
──────────────────────────────────────────────────

Reconstruye el bloque <head> en este orden exacto y con estas reglas:

1. <meta charset="UTF-8"> — siempre primero.
2. <meta name="viewport" content="width=device-width, initial-scale=1.0">
3. <meta name="theme-color"> con el color dominante del diseño.
4. <title> y <meta name="description"> — conserva los originales.
5. <meta name="robots" content="index, follow">
6. Open Graph: agrega og:title, og:description, og:image (usa la URL
   de la imagen principal del producto si existe), og:type, og:url.
7. Resource hints en este orden de prioridad:
   a. <link rel="preconnect"> para todos los dominios externos usados
      (fonts.googleapis.com, fonts.gstatic.com, cdn.shopify.com y
      cualquier otro dominio presente en el código).
   b. <link rel="dns-prefetch"> para dominios de pago o terceros
      (hotmart, stripe, mercadopago, paypal, o el que corresponda).
   c. <link rel="preload" as="image"> únicamente para la imagen hero
      principal (la primera imagen visible above-the-fold).
   d. <link rel="preload" as="font"> para la fuente tipográfica más
      usada, con crossorigin="anonymous".
8. Carga de fuentes optimizada — ver Paso 3.
9. CSS crítico inline — ver Paso 4.
10. <link rel="canonical"> con la URL de la página si está definida.

──────────────────────────────────────────────────
PASO 3 — FUENTES TIPOGRÁFICAS SIN BLOQUEO
──────────────────────────────────────────────────

Las fuentes de Google Fonts bloquean el render. Aplica esta estrategia:

A. Elimina todos los <link href="https://fonts.googleapis.com/css2...">
   que estén en el <head> de forma síncrona.

B. Reemplázalos por carga asíncrona usando este patrón exacto:

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style"
  href="[URL_ORIGINAL_DE_GOOGLE_FONTS]"
  onload="this.onload=null;this.rel='stylesheet'">
<noscript>
  <link rel="stylesheet" href="[URL_ORIGINAL_DE_GOOGLE_FONTS]">
</noscript>

C. En el CSS, agrega font-display:swap a todas las declaraciones
   @font-face que encuentres o que estén implícitas via Google Fonts.
   Si la URL de Google Fonts no incluye &display=swap, agrégalo.

D. Define un font-stack de sistema como fallback para cada familia
   tipográfica usada, de modo que el texto sea legible instantáneamente
   mientras carga la fuente real:
   - Sans-serif: system-ui, -apple-system, BlinkMacSystemFont,
     'Segoe UI', Arial, sans-serif
   - Condensed: Impact, 'Arial Narrow', Arial Narrow, sans-serif

──────────────────────────────────────────────────
PASO 4 — CSS CRÍTICO INLINE (ABOVE THE FOLD)
──────────────────────────────────────────────────

A. Identifica el CSS que afecta los primeros 600-700px de pantalla
   en móvil (viewport inicial). Esto incluye: variables CSS (:root),
   reset básico, estilos del body, header/trust bar si lo hay,
   hero section, tipografía base, y el botón CTA principal.

B. Coloca ese CSS crítico en un bloque <style> inline dentro del <head>.
   Debe ser suficiente para que la página se vea correctamente antes
   de que cargue el resto del CSS.

C. El CSS no crítico (estilos de secciones below-the-fold) cárgalo
   de forma asíncrona con este patrón:
   <link rel="preload" as="style" href="styles.css"
     onload="this.onload=null;this.rel='stylesheet'">

   NOTA: Si el código es un único archivo HTML (sin CSS externo),
   mantén todo el CSS inline pero aplica el Paso 7 para minificarlo.
   En ese caso, no es necesario separar en archivo externo.

D. Elimina cualquier @import dentro de bloques <style> — los @import
   en CSS son síncronos y bloquean el render.

──────────────────────────────────────────────────
PASO 5 — OPTIMIZACIÓN COMPLETA DE IMÁGENES
──────────────────────────────────────────────────

Revisa cada imagen del código y aplica estas reglas:

A. IMAGEN HERO (primera imagen visible, above-the-fold):
   - Debe tener loading="eager" (nunca lazy en la imagen principal).
   - Agrega fetchpriority="high".
   - Agrega decoding="sync".
   - Debe tener un <link rel="preload" as="image"> en el <head>.
   - Si la URL de Shopify CDN no incluye parámetros de optimización,
     agrégalos: ?width=800&quality=85&format=webp
     (Shopify soporta estos parámetros nativamente).

B. TODAS LAS DEMÁS IMÁGENES:
   - loading="lazy" en todas sin excepción.
   - decoding="async" en todas.
   - Agrega width y height explícitos si no los tienen.
     Usa las dimensiones reales o estimadas de cada imagen
     para eliminar Cumulative Layout Shift (CLS).
   - Si son imágenes de Shopify CDN, agrega parámetros de optimización:
     ?width=[ancho_apropiado]&quality=80&format=webp

C. IMÁGENES DE FONDO CSS (background-image):
   - Si alguna sección usa background-image con URL externa
     (Unsplash, imágenes no-CDN), agrégala como resource hint:
     <link rel="preload" as="image" href="[URL]">
   - Elimina background-attachment:fixed en todos los elementos.
     En dispositivos móviles, fixed backgrounds deshabilitan la
     composición en GPU y causan repaint en cada scroll.
     Reemplaza por background-attachment:scroll.
   - Si la imagen de fondo es decorativa y no crítica, agrégale
     una clase que la cargue solo después del primer paint usando
     IntersectionObserver (ver Paso 6).

D. CARRUSELES Y GALERÍAS:
   - En carruseles con múltiples slides, aplica lazy load a todas
     las imágenes excepto la primera slide visible.
   - Si el carrusel duplica imágenes para efecto de loop infinito CSS,
     las imágenes del set duplicado deben tener loading="lazy".

──────────────────────────────────────────────────
PASO 6 — JAVASCRIPT: DIFERIDO, MODULAR Y EFICIENTE
──────────────────────────────────────────────────

A. DIFERIMIENTO:
   - Todo el JavaScript que no sea crítico para el primer render
     debe ejecutarse después de que la página sea visible.
   - Si el JS está en un bloque <script> inline al final del body,
     envuelve todo su contenido en:
     document.addEventListener('DOMContentLoaded', function() { ... });
   - Si hay scripts externos (<script src="...">), agrégales defer
     o async según corresponda.

B. CURSOR PERSONALIZADO:
   - Si el código incluye un cursor custom con requestAnimationFrame
     loop continuo, agrega esta detección obligatoria al inicio:
     if (navigator.maxTouchPoints > 0 ||
         !window.matchMedia('(hover: hover)').matches) {
       // Saltar toda la lógica del cursor en dispositivos táctiles
       document.getElementById('cursor')?.remove();
       document.getElementById('cursor-ring')?.remove();
       return; // o usar return para salir del bloque
     }
   - En móvil, un rAF loop de cursor consume entre 8-15% de CPU
     de forma constante. Esto es crítico en paid traffic móvil.

C. INICIALIZACIÓN DIFERIDA DE FUNCIONES NO CRÍTICAS:
   Las siguientes funcionalidades deben inicializarse usando
   requestIdleCallback (con fallback a setTimeout 200ms) porque
   no son necesarias para el primer paint ni la primera interacción:
   - Contadores animados de estadísticas (counters con data-target).
   - Parallax del hero.
   - Animaciones de scroll reveal que estén below-the-fold.
   - Timers y countdowns de urgencia (el usuario no los ve
     hasta hacer scroll).

   Patrón a usar:
   var idle = window.requestIdleCallback ||
     function(cb){ setTimeout(cb, 200); };
   idle(function() {
     // inicializar funciones no críticas aquí
   });

D. INTERSECTION OBSERVER:
   - Todos los IntersectionObserver deben crearse una sola vez
     y reutilizarse. Evita crear un observer por elemento.
   - Agrega rootMargin: '0px 0px -40px 0px' y threshold: 0.1
     como valores base para los scroll reveal observers.

E. EVENT LISTENERS:
   - Todos los listeners de scroll deben tener {passive: true}.
   - Todos los listeners de touchstart/touchend deben tener
     {passive: true}.
   - Si hay mousemove listeners para efectos parallax o cursor,
     agrega una verificación: solo en dispositivos con hover real.

F. TIMER Y COUNTDOWN:
   - Si hay un countdown de urgencia, inicialízalo dentro del
     requestIdleCallback para que no bloquee el critical path.

──────────────────────────────────────────────────
PASO 7 — MINIFICACIÓN Y LIMPIEZA DE CSS
──────────────────────────────────────────────────

A. Elimina todos los comentarios CSS (/* ... */) del código final.
B. Elimina líneas en blanco y espacios innecesarios entre reglas.
C. Conserva la funcionalidad de cada regla exactamente igual.
D. Audita todos los will-change del código:
   - will-change:transform → mantener solo si tiene una animación
     CSS o JS activa asociada.
   - will-change en elementos estáticos → eliminar.
     El will-change mal aplicado consume memoria GPU innecesariamente.
E. Revisa si hay propiedades que fuercen nuevas capas de composición
   sin necesidad: transform:translateZ(0), backface-visibility:hidden,
   perspective en elementos que no tienen animación 3D real.
   Elimínalas si no son funcionales.
F. Si hay animaciones CSS de tipo @keyframes que corren always-on
   (infinite), verifica que estén protegidas con:
   @media (prefers-reduced-motion: reduce) {
     *, *::before, *::after {
       animation-duration: 0.01ms !important;
       animation-iteration-count: 1 !important;
     }
   }
   Si ya existe este bloque, confirma que esté completo.

──────────────────────────────────────────────────
PASO 8 — ELIMINACIÓN DE LAYOUT SHIFT (CLS)
──────────────────────────────────────────────────

El Cumulative Layout Shift es una de las principales causas de
rebote en paid traffic. Aplica estas correcciones:

A. Todas las imágenes sin width y height explícitos generan layout
   shift. Agrega dimensiones a todas las imágenes del código.
   Si no conoces las dimensiones exactas, usa aspect-ratio en CSS:
   img { aspect-ratio: [ancho] / [alto]; width: 100%; height: auto; }

B. Si hay fuentes con font-display:swap, puede haber un flash de
   texto con fuente de sistema. Para reducirlo:
   - Usa font-display:optional para fuentes decorativas no críticas.
   - Usa font-display:swap solo para fuentes de texto principal.

C. Si hay elementos que aparecen dinámicamente (mobile CTA que
   aparece al hacer scroll, banners, pop-ups), deben estar en el DOM
   desde el inicio pero con visibility:hidden o translateY(110%)
   en lugar de display:none, para que el browser reserve su espacio.

D. Si hay carruseles, el contenedor debe tener una altura mínima
   definida (min-height) para evitar que la página "salte" cuando
   cargan las imágenes del primer slide.

──────────────────────────────────────────────────
PASO 9 — OPTIMIZACIONES ESPECÍFICAS PARA SHOPIFY
──────────────────────────────────────────────────

A. PARÁMETROS CDN DE SHOPIFY:
   Shopify CDN soporta transformación de imágenes on-the-fly.
   Para cada imagen de cdn.shopify.com, optimiza la URL agregando:
   - &width=[ancho_máximo_en_que_se_muestra]
     (no pedir 1200px si se muestra en 400px)
   - &quality=80 para imágenes generales
   - &quality=85 para imagen hero/producto principal
   - &format=webp (Shopify lo soporta y es 30-50% más liviano)

   Ejemplo de transformación:
   ANTES: cdn.shopify.com/s/files/.../imagen.jpg?v=123456
   DESPUÉS: cdn.shopify.com/s/files/.../imagen.jpg?v=123456&width=480&quality=80&format=webp

B. IMÁGENES RESPONSIVAS:
   Para imágenes que se muestran a diferente tamaño en móvil y
   desktop, agrega el atributo srcset con dos versiones:
   srcset="[url]&width=480&format=webp 480w,
           [url]&width=960&format=webp 960w"
   sizes="(max-width: 640px) 100vw, 50vw"

C. Si el código tiene un header o trust bar fijo (sticky/fixed),
   asegúrate de que tenga will-change:transform para que el browser
   lo eleve a su propia capa GPU y no cause repaint en cada scroll.

──────────────────────────────────────────────────
PASO 10 — VALIDACIÓN FINAL
──────────────────────────────────────────────────

Antes de entregar el código, confirma internamente que:

[ ] El <head> tiene preconnect a todos los dominios externos.
[ ] La imagen hero tiene preload + fetchpriority="high" + loading="eager".
[ ] Todas las demás imágenes tienen loading="lazy" + decoding="async".
[ ] Google Fonts carga de forma asíncrona con display=swap.
[ ] El JS no bloquea el parsing del HTML.
[ ] El cursor custom está desactivado en dispositivos táctiles.
[ ] No hay background-attachment:fixed en ningún elemento.
[ ] Todos los event listeners de scroll tienen {passive:true}.
[ ] Los will-change innecesarios fueron eliminados.
[ ] Las imágenes de Shopify CDN tienen parámetros de optimización.
[ ] El CSS no tiene comentarios ni espacios innecesarios.
[ ] No hay ninguna sección, texto, color ni función modificada.

═══════════════════════════════════════════════════
RESTRICCIONES FINALES
═══════════════════════════════════════════════════

- No uses librerías externas adicionales (no jQuery, no lodash,
  no frameworks).
- No uses Service Workers ni técnicas que requieran configuración
  de servidor.
- No cambies la estructura de ninguna sección HTML visible.
- No elimines ni modifiques ningún ID o clase que esté siendo
  referenciada por el JavaScript existente.
- El resultado debe ser un único archivo HTML, completo y funcional.

═══════════════════════════════════════════════════
FORMATO DE ENTREGA — EN ESTE ORDEN EXACTO
═══════════════════════════════════════════════════

1. TABLA DE AUDITORÍA
   Formato: | Problema encontrado | Nivel | Solución aplicada |
   Lista todos los problemas detectados en el Paso 1.

2. RESUMEN DE CAMBIOS TÉCNICOS
   Lista en formato de viñetas los cambios realizados, agrupados
   por categoría: Fuentes / Imágenes / JavaScript / CSS / Head.

3. CÓDIGO HTML COMPLETO OPTIMIZADO
   El archivo completo, listo para pegar en Shopify, en un único
   bloque de código.

4. CHECKLIST DE VERIFICACIÓN VISUAL
   Lista de los elementos clave que el usuario debe revisar para
   confirmar que nada visual cambió: secciones, colores,
   funcionalidades, textos.

5. ESTIMACIÓN DE MEJORA
   Tabla con: Métrica | Antes (estimado) | Después (estimado)
   Incluir: LCP, FID/INP, CLS, tasa de carga estimada en Meta Ads.
