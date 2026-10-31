---
tema: Quiz funnel
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/quiz-funnel.md, RAW/formacion/lecciones/creando-una-web-con-magic-patterns.md]
---

# Quiz funnel

Alternativa a la página de ventas directa: antes de ver la oferta, el visitante pasa por **~16 preguntas**. Quien llega al final llega **muy calificado**.

## Los números que lo justifican

| Métrica | Valor |
|---|---|
| Conversión de quien completa el quiz | **25–30%** |
| CPC tolerable | Hasta **1 USD** |

Ese CPC de 1 USD es la clave, y contrasta con el resto del sistema: en un funnel normal, 1 USD de CPC es descarte inmediato porque exigiría un 7% de conversión ([[metricas-y-kpis]]). Aquí es viable **porque la conversión del tramo final es 10 veces mayor**.

Es, en la práctica, otra forma de resolver la misma ecuación de siempre: costo por visita vs. revenue por visita. Si no puedes bajar el costo, subes brutalmente la conversión.

## Estructura

```
Anuncio → Quiz (~16 preguntas) → Oferta + testimonios
                                       ↓
                        Página de ventas (con mini VSL) → Checkout
```

Al final del quiz se presenta oferta y testimonios, y se redirige a una página de ventas externa. Esa página puede ser una landing normal; en el ejemplo lleva un **mini VSL**.

## Plataforma

**InLead**. Se construye por bloques, «como WordPress». También se puede hacer con código HTML.

### Configuración técnica

En *Configuración → Píxeles y scripts*:

| Dónde | Qué |
|---|---|
| **Head** | Script del cloaker ([[funnel-hacking]]) |
| **Body** | Capturador de UTMs de UTMify ([[tracking-y-atribucion]]) |
| — | ID del pixel de Meta |

Y un **subdominio**, igual que con Magic Patterns.

## La analítica etapa por etapa

Es la ventaja operativa del formato: se ve **dónde se fugan los leads**, paso a paso.

> Etapa 1: 100% · Etapa 2: 95% · 92% · 88% …

Con esos números se **eliminan o añaden secciones**. Es un nivel de diagnóstico que una landing plana no da: en vez de saber que el comprate es bajo, sabes en qué pregunta concreta se cae la gente.

## Todos los formatos funcionan

Contra la tentación de buscar el formato «correcto». Casos reales de alumnos, todos al mismo tiempo:

| Formato | Resultado |
|---|---|
| **Quiz sin VSL** | ~1.000 USD de profit por día |
| TCL, ticket 27 | escalando |
| TCL, ticket 19 | 25.000 USD de profit |
| Quiz + VSL | escalando |

> «Todo anda, hermano. O sea, **es lanzar**.»

El formato no es la variable que decide. Ver [[pagina-de-ventas]] y [[validacion-de-oferta]].

## De dónde salen los quiz

La misma lógica que el resto: **modelar quiz de Brasil**, acortarlos y mejorarlos. Se estudian en la Biblioteca de Anuncios. Ver [[funnel-hacking]].

## Nota sobre escalado (de la misma sesión)

Cómo se escalaba en ese momento:

- **Todo aislada**: pre-testeo → campaña aislada
- Subir **+50% cada 2 horas** si mete venta; **duplicar** si el ROAS viene bueno
- Una **BidCap CBO** con el bid **en el precio del break-even** y 3 anuncios por conjunto

Con una advertencia importante:

> «Si no tenés backend, no le pongas el precio [como bid], porque te la va a consumir.»

Ver [[escalado-en-meta-ads]] · [[aumento-de-aov]].

## Complementos prácticos

- **Compras ÷ landing page views ≈ 5%** en quiz funnels, contado sobre todos los que entran al quiz. El 25–30% se refiere a quien llega a la última página contra la primera.

Relacionado: [[pagina-de-ventas]] · [[metricas-y-kpis]] · [[tracking-y-atribucion]] · [[funnel-hacking]]
