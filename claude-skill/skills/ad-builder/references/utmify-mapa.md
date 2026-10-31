# UTMify — mapa de dashboards y cómo leer los números

Fuente de verdad de resultados. La regla de arquitectura es **un dashboard, un pixel, una tienda, un
producto** (`WIKI/tracking-y-atribucion.md`), así que el dashboard es la unidad de análisis.

Si un dashboard nuevo no está acá, correr `get_dashboards` y agregarlo.

---

## 1. Los dashboards

Completá esta tabla con tus propios dashboards. Pedile a Claude que corra `get_dashboards` en UTMify
y la llene.

| Dashboard | ID | TZ | Cuenta habilitada | Qué corre |
|---|---|---|---|---|
| | | | | |

Todos en **USD**, `viewType: Normal` (facturación líquida).

⚠️ **Ojo con el timezone de cada dashboard.** Las fechas de las consultas se arman con el timezone
del dashboard, no con el de la máquina. Un día mal armado corre los números de la tanda.

---

## 2. Consultas

### Resultados de una tanda, a nivel anuncio

```
get_meta_ad_objects
  dashboardId: <ID>
  level: "ad"
  dateRange: { from: "<YYYY-MM-DD>T00:00:00-03:00", to: "<YYYY-MM-DD>T23:59:59-03:00" }
```

`nameContains` filtra por texto del nombre del anuncio: con la nomenclatura puesta, `nameContains:
"ECO-"` trae todos los creativos de un ángulo, y `"_UGC_"` todos los de un formato. **Esa es la razón
de ser de la nomenclatura.**

`adObjectStatuses` acepta `ACTIVE`, `PAUSED`, `DELETED`, `ARCHIVED`, `DISAPPROVED`. Para cerrar una
tanda hay que consultar **sin filtrar por ACTIVE**: los creativos cortados ya están en pausa y son
justamente los que hay que anotar.

`DISAPPROVED` merece revisión aparte — es señal de compliance, no de performance.

### Otros niveles

`level: "campaign"` para leer las CBO por concepto · `level: "adset"` para los conjuntos ABO ·
`level: "account"` para el consolidado de la cuenta.

### AOV real y contexto del día

`get_dashboard_summary` con el mismo `dashboardId` y rango: da órdenes aprobadas, facturación,
desglose por producto (`byProductName`) y por país. **De ahí sale el AOV real** — no del precio de
lista.

Costos de producto y comisiones: `get_extra_fees_product_costs` y
`get_extra_fees_taxes_and_fees`. Sin eso el profit del panel es bruto y engaña.

---

## 3. Campos que importan

⚠️ **Los valores monetarios vienen en centavos.** `spend: 1250` = 12,50 USD. Convertir antes de
escribir el historial.

| Campo | Uso |
|---|---|
| `name` | El ID del creativo. Se parsea con el regex de `nomenclatura.md` |
| `spend` | Gasto. Contra el CPA medio decide el corte |
| `approvedOrdersCount` | Ventas aprobadas — la métrica de verdad |
| `pendingOrdersCount` | Pendientes. Ojo antes de matar algo: puede estar por aprobar |
| `cpa` | Costo por adquisición |
| `revenue` / `grossRevenue` | Facturación neta / bruta |
| `profit`, `profitMargin`, `roas`, `roi` | Rentabilidad real ya con costos si están cargados |
| `arpu` | Ticket promedio del anuncio — el AOV real |
| `inlineLinkClickCtr`, `costPerInlineLinkClick`, `cpm` | CTR, CPC, CPM. El trío que detecta fatiga |
| `landingPageViews`, `costPerLandingPageView` | Brecha entre clic y visita = problema de velocidad de landing |
| `initiateCheckout`, `checkoutConversion` | Dónde se cae el funnel |
| `hook`, `hookPlayRate` | **Video: hook rate.** Diagnostica los primeros 3 segundos |
| `retention`, `holdRate`, `bodyRetention`, `video75Watched` | Video: dónde abandona |
| `frequency` | Saturación del segmento |
| `effectiveStatus` | `DISAPPROVED` = compliance, no performance |
| `untrackedCount` (raíz) | Órdenes sin atribuir. Si crece, revisar tracking antes de culpar al creativo |

---

## 4. Cómo se decide el veredicto con estos números

Con `ticket` = precio del front y `CPA_medio = ticket ÷ 2`, `CPA_be` = break-even después de
comisiones:

| Condición | Veredicto |
|---|---|
| `approvedOrdersCount >= 5` y `cpa < CPA_be` | ✅ Validado |
| `approvedOrdersCount >= 1` y `cpa < CPA_be` | 🟢 Vende |
| `spend < CPA_medio` y sin ventas | ⏳ En testeo |
| `spend >= CPA_medio` y `approvedOrdersCount == 0` y `pendingOrdersCount == 0` | ❌ Descartar (el **anuncio**) |
| Fue ✅/🟢 y ahora `cpm ↑`, `costPerInlineLinkClick ↑`, `inlineLinkClickCtr ↓` | 🔁 Fatigado → renovar hook |
| Se apagó con `spend < CPA_medio`, o corrió en pre-testeo a 1,50–2 USD | ⚠️ Inconcluso |

**El ángulo solo se marca ❌ cuando ≥3 creativos distintos de ese ángulo acumulan gasto ≥ CPA_be sin
una sola venta.** Un anuncio muerto no mata un ángulo.

Diagnóstico rápido cuando algo no vende:

- **CTR bajo** → el problema es el hook / la imagen. No la oferta.
- **CTR bien, `landingPageViews` muy por debajo de los clics** → velocidad de la landing.
- **Visitas bien, `initiateCheckout` bajo** → la landing o la oferta, no el creativo.
- **`initiateCheckout` bien, ventas bajas** → checkout o precio.
- **`untrackedCount` alto** → tracking. Verificar antes de tocar creativos.
