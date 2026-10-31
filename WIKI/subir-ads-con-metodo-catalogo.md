---
tema: Subir ads con método catálogo
actualizado: 2026-09-23
fuentes: [RAW/youtube/firgon-tutorial-campana-de-catalogo.md]
---

# Subir ads con método catálogo

Forma estándar de montar los testeos de las ofertas nuevas desde el 2026-09-23 (decisión de
Santiago). Cada anuncio es un **anuncio de catálogo Advantage+ a nivel anuncio, en video único**,
dentro de la estructura V3 de siempre (ver [[escalado-en-meta-ads]] y [[setup-de-campanas]]).
El método viene del tutorial de Grupo Firgon.

## Para qué

Que la competencia no copie los creativos desde la Biblioteca de anuncios (ver [[funnel-hacking]]).
Protege solo en parte: los anuncios de catálogo aparecen igual en la Biblioteca, como plantilla o
"varias versiones", y la página y la cantidad de anuncios activos se siguen viendo.

## Regla fija

- **Productos con datos reales:** nombre del creativo u oferta, precio real del front, mockup real
  del producto, una línea que diga qué es y la landing de la campaña.
- **Nada de relleno:** ni descripción de un punto, ni imagen sacada de Google, ni precio inventado,
  aunque el tutorial lo haga así.
- **Nunca pasar por catálogo un creativo que Meta ya rechazó.** El tutorial lo vende como forma de
  aprobar creativos, y ese uso queda afuera. Si hay rechazos, se pide revisión o se diagnostica la
  cuenta (ver [[contingencia-de-cuentas]]).

## Paso a paso por tanda

1. **Pixel en la BM del catálogo.** El catálogo usa el mismo pixel que la campaña.
2. **Crear el catálogo** ("productos online") y conectar **solo** ese pixel. Uno por business: si
   ya existe, se le suman productos.
3. **Un producto por creativo**, con el link exacto del anuncio. Video de menos de 100 MB (si falla
   por muy chico, llevarlo a 70-90 MB) e imagen de al menos 500×500.
4. **Un conjunto de productos por creativo**, con el mismo nombre del anuncio.
5. **Campaña y conjunto V3.** El conjunto es normal: sitio web, pixel, evento Comprar, fechado con
   la tanda. Las renovaciones van como conjunto nuevo dentro de la campaña que ya corre.
6. **Anuncio, en Ads Manager:**
   - Activar el catálogo Advantage+ **a nivel anuncio**, nunca a nivel campaña (a nivel campaña mete
     todo en un carrusel).
   - Formato imagen o video único, con el catálogo y el conjunto de productos de ese creativo.
   - URL igual a la del producto.
   - "Priorizar video" ON, "mostrar como colección" OFF, "ocultar precio" ON.
   - CTA "Más información" y los parámetros de URL de siempre (ver [[tracking-y-atribucion]]).
7. **Verificar** el estado de campaña, conjunto y anuncios después de publicar.

## Qué se puede automatizar

- **Por el conector de Meta Ads (Claude):** catálogo, pixel, productos, conjuntos de productos,
  campaña y conjunto. Los videos se cargan con un feed CSV con la columna `video[0].url` apuntando
  al MP4 público.
- **Solo a mano en Ads Manager:** el anuncio. El conector solo crea catálogo en carrusel, sin video
  único, sin priorizar video y sin ocultar precio. Lo hacés vos, o Claude por Chrome con tu OK.

