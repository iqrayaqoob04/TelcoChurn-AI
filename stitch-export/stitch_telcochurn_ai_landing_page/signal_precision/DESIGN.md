---
name: Signal Precision
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#444933'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#747a60'
  outline-variant: '#c4c9ac'
  surface-tint: '#506600'
  primary: '#506600'
  on-primary: '#ffffff'
  primary-container: '#ccff00'
  on-primary-container: '#5b7300'
  inverse-primary: '#abd600'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#505f76'
  on-tertiary: '#ffffff'
  tertiary-container: '#e3edff'
  on-tertiary-container: '#5c6c82'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c3f400'
  primary-fixed-dim: '#abd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for a high-performance telecom analytics environment where data density must coexist with visual clarity. The brand personality is authoritative yet unobtrusive, positioning the tool as a precise instrument rather than a decorative interface.

The design style follows a **Modern Tech-Minimalism** approach. It prioritizes functional aesthetics through generous whitespace, a restricted color palette, and a focus on "Data-as-UI." The interface utilizes subtle borders and high-contrast typography to create clear information hierarchies without the clutter of excessive shadows or decorative gradients. The result is a professional, tech-forward environment that reduces cognitive load during intensive data analysis.

## Colors

The palette is anchored by a high-contrast foundation to ensure absolute legibility of technical metrics.

- **Primary (Vibrant Lime):** Used exclusively for high-priority actions, active states, and critical data highlights. It serves as a visual beacon against the neutral backdrop.
- **Secondary (Dark Navy):** Applied to primary text, headings, and navigation backgrounds to provide a grounded, professional structure.
- **Neutral/Background:** A tiered system of White (#FFFFFF) for primary content cards and Off-White (#F8FAFC) for the application canvas.
- **Supportive Greys:** Used for secondary labels and subtle borders to maintain a clean, airy feel.

## Typography

This design system utilizes a dual-font strategy to balance character with utility.

- **Plus Jakarta Sans** is used for headlines. Its modern, slightly wide proportions provide a tech-forward feel and clear section anchoring.
- **Inter** is the workhorse for all body text, data tables, and UI labels. It was selected for its exceptional legibility at small sizes and its neutral, systematic character.
- **Data Clarity:** Numeric values in tables and dashboards should use `data-mono` (Inter with tabular lining figures enabled) to ensure vertical alignment in lists of metrics.

## Layout & Spacing

The layout utilizes a **12-column fluid grid** system optimized for data-heavy dashboards.

- **Spacing Rhythm:** Based on a 4px baseline shift. Most components use 8px, 16px, or 24px increments to maintain a rigorous mathematical harmony.
- **Dashboard Structure:** A fixed left navigation sidebar (240px) with a fluid content area.
- **Padding:** High whitespace is a functional requirement. Cards and containers should use a minimum of 24px internal padding to separate distinct data clusters.
- **Responsive Behavior:** On mobile, the 12-column grid collapses to a single column, and margins reduce to 16px. Tablet views utilize a 6-column grid.

## Elevation & Depth

This design system avoids heavy shadows to maintain a "flat-plus" aesthetic. Depth is communicated primarily through **Tonal Layering** and **Subtle Outlines**.

- **Level 0 (Canvas):** The off-white background (#F8FAFC).
- **Level 1 (Cards/Content):** Pure white surfaces (#FFFFFF) with a 1px solid border (#E2E8F0). No shadow.
- **Level 2 (Dropdowns/Modals):** Pure white surfaces with a very soft, diffused ambient shadow (0px 10px 15px -3px rgba(0, 0, 0, 0.05)) to indicate temporary interaction layers.
- **Active States:** Subtle 2px "focus rings" using the primary lime green with 20% opacity.

## Shapes

The shape language is "Soft-Technical." Elements use a **0.25rem (4px) base radius** to provide a hint of approachability while maintaining the precise, structured look of a professional tool.

- **Buttons & Inputs:** Use the standard 4px radius.
- **Cards:** Use the `rounded-lg` (8px) radius to softly frame large data sets.
- **Data Visualizations:** Bar charts and status indicators should remain sharp or use minimal 2px rounding to maintain the integrity of the data points.

## Components

- **Buttons:** Primary buttons use the vibrant lime green background with dark navy text for maximum contrast. Secondary buttons use a white background with a thin navy border.
- **Input Fields:** Minimalist design with a 1px border. On focus, the border transitions to a dark navy with a subtle lime green outer glow.
- **Data Cards:** Essential to the dashboard. They must include a `headline-sm` title, a clear metric value, and a 1px bottom-border separator for header/content split.
- **Status Chips:** Small, pill-shaped indicators. "Healthy" states use a subtle green tint, while "Warning" or "Error" states use muted ambers and reds—never competing with the primary lime green accent.
- **Analytics Tables:** High-density, borderless rows. Use subtle zebra-striping or a 1px bottom border (#F1F5F9). Headers are in `label-md` for clear categorization.
- **Metric Widgets:** Large-format numbers using `headline-lg` to ensure the most critical KPIs are immediately visible upon page load.