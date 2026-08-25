# DESIGN.md — ShineLee's AI Lab

## 1. Brand Identity & Register
- **Register**: `Experience` (Digital AI Research Lab & Portal)
- **Mood**: Cinematic, sleek, minimalist, dark luxury, physics-based liquid glass.
- **Anti-References**: Avoid generic light dashboard cards, cartoon gradients, neon cyan glare, and standard Bootstrap-like rounded buttons.

## 2. Color Palette
- **Background Deep Ramp**:
  - Center: `#1a1a2e` (Deep Midnight Indigo)
  - Middle: `#0d0d14` (Obsidian Base)
  - Edge: `#050507` (Pitch Dark)
- **Glass Surfaces**:
  - Base: `rgba(13, 13, 20, 0.45)` (Tinted dark glass)
  - Hover: `rgba(25, 25, 38, 0.6)` (Subtle luminous reaction)
  - Auth Modal: `rgba(18, 18, 28, 0.7)`
- **Text & Foreground**:
  - Primary: `#ffffff` (Pure White, 100%)
  - Secondary: `rgba(255, 255, 255, 0.82)` (WCAG AA pass on glass)
  - Tertiary/Muted: `rgba(255, 255, 255, 0.65)`
  - Error: `#f87171` (Red-400)

## 3. Typography
- **Headings & Display**: `'Instrument Serif', Georgia, serif` (Editorial elegance, italic accents)
- **Body & Controls**: `ui-sans-serif, system-ui, -apple-system, "Segoe UI", "PingFang SC", sans-serif`
- **Scale**:
  - Display Hero: `clamp(2.2rem, 6vw, 3.8rem)` / `line-height: 1.05`
  - Page Title: `clamp(2.5rem, 6vw, 4rem)`
  - Card Title: `1.45rem` (Italic serif)
  - Body / Sub: `0.9rem` - `1rem`
  - Captions: `0.85rem`

## 4. Materials & Physics
- **Liquid Glass**:
  - `backdrop-filter: blur(10px)`
  - Dual masked gradient border: `rgba(255, 255, 255, 0.45)` to transparent.
  - Inset specular highlight: `inset 0 1px 1px rgba(255, 255, 255, 0.12)`
- **Transitions**:
  - Natural easing: `cubic-bezier(0.16, 1, 0.3, 1)`
  - Standard duration: `200ms` - `300ms`

## 5. Accessibility (A11y)
- Must respect `prefers-reduced-motion: reduce` by suppressing autoplay video and heavy translation transforms.
- All interactive elements must declare `:focus-visible` outline rings.
