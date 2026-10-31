---
tema: Contingencia de cuentas y BMs
actualizado: 2026-08-10
fuentes: [RAW/formacion/lecciones/contingencia-de-perfiles-y-bms.md, RAW/formacion/lecciones/escalar-en-otras-cuentas-publicitarias-testear-varias-cuentas-publicitarias-para-relojear-el-cpm.md, RAW/contexto-chatgpt.md]
---

# Contingencia de cuentas y BMs

Riesgo operativo real, no teórico: es habitual que se bloqueen **varias cuentas de Facebook al mismo tiempo**, con apelaciones que piden documento y escaneo facial. Y hay efectos colaterales: si Instagram estaba conectado a ManyChat mediante uno de esos perfiles, la integración se rompe.

> «Si solo dependés de un perfil, un Business Manager o dos o tres cuentas publicitarias, estás colgando de un hilo.»

## La arquitectura recomendada

```
2–3 PERFILES DE BACKUP  (nunca anuncian)
        │  propietarios / admin total
        ▼
   3+ BUSINESS MANAGERS
        │  3+ cuentas publicitarias cada uno
        ▼
   PERFIL ANUNCIANTE  ← recibe acceso desde el backup
                        es el que corre riesgo
```

### Perfiles de backup

- **2 o 3**, con **actividad mínima**: entrar cada 3–7 días y hacer un poco de scroll
- Se «calientan» durante **30 días** antes de usarlos
- **Nunca anuncian.** Su única función es ser **propietarios de los BMs** y otorgar o quitar accesos
- Son los que menos riesgo de bloqueo corren, precisamente porque no anuncian

### Regla central

> **El propietario del Business Manager nunca debe ser el perfil que anuncia.**

Si el anunciante crea el BM y lo bloquean, se cae todo. Si el BM pertenece a un perfil de backup, el anunciante es reemplazable.

### Mínimos

| Elemento | Cantidad mínima |
|---|---|
| Perfiles de backup | 2–3 |
| Business Managers | **3** |
| Cuentas publicitarias por BM | **3** |

## Higiene técnica

Aplica a **todos** los perfiles, backup y anunciantes:

- **Dirección IP única** por perfil
- **Huella digital (fingerprint) única** por perfil

La herramienta que usa para esto es **Multilogin**, un navegador antidetección que mantiene cada perfil aislado. Aparece también al conectar perfiles a UTMify ([[tracking-y-atribucion]]).

Y la regla que Santiago subraya:

> **Nunca abrir un perfil —y menos uno anunciante— desde tu propia IP.** No queremos que se manche tu dirección.

## Procedimiento ante un bloqueo

**Se bloquea el perfil anunciante:**
1. Desde un perfil de backup, eliminar su acceso
2. Dar acceso a otro perfil anunciante
3. Seguir corriendo en los mismos BMs

**Empiezan a caer cuentas publicitarias de un BM:**
El perfil de backup **renuncia y sale de ese BM**, para que no quede manchado por asociación.

## Múltiples cuentas como palanca de escala

La contingencia tiene un beneficio secundario: **más cuentas publicitarias es también más capacidad de escala**.

Hay lección dedicada a correr el mismo producto en varias cuentas para **«relojear» el CPM** — comparar qué cuenta entrega más barato y escalar por ahí. Se plantea a partir de los 100–300 USD/día de facturación.

Ver [[escalado-en-meta-ads]] · [[internacionalizacion]].

## Nota

Los Business Managers y los perfiles de backup **se pueden comprar**.

> Nota del bibliotecario: comprar perfiles y camuflar IP/fingerprint contraviene los términos de servicio de Meta. No está registrado en el material ningún análisis de ese riesgo — se presenta solo como práctica operativa.

Relacionado: [[escalado-en-meta-ads]] · [[setup-de-campanas]] · [[stack-de-herramientas]]
