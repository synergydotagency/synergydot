# Synergy Dot website

A fast, responsive static website. No dependencies, installation, external fonts, or build step required. Open `index.html` directly to view it, or run `node preview.cjs` for a local preview at http://127.0.0.1:4173.

## Publish on GitHub Pages

1. Create a GitHub repository and upload `index.html`, `styles.css`, `script.js`, `.nojekyll`, and the complete `assets` and `work` folders to its root. Upload the files inside the website folder, rather than an enclosing folder or ZIP.
2. In the repository's Settings → Pages, choose Deploy from a branch, select your main branch and `/ (root)`, then Save.
3. GitHub will display your website address when publishing finishes.

All links use relative paths, so the site also works at a GitHub project URL. No custom domain configuration is included.

## Add a project without installing anything

1. Duplicate `work/forma.html` with a new filename such as `new-project.html`.
2. Replace its page title, description, project heading, metadata, image, challenge, approach, scope and outcome. Add more image and text blocks as needed. Use only verified client results.
3. Put optimized images in `assets`. In project pages the path is `../assets/your-image.jpg`.
4. In `index.html`, duplicate one complete `<a class="project ...">...</a>` inside `project-grid`. Change the image, text and link to `work/new-project.html`. Update Next links on project pages as desired.

Alternatively, edit `projects.json` and run `node generate-pages.cjs` to recreate the homepage portfolio and case-study HTML. This optional tool uses `generate-portfolio.cjs` and overwrites generated portfolio sections and project pages. Add images to each project's `gallery` array for an expanded presentation. Projects with galleries appear as featured work; logo-only projects appear in the identity collection. Update the collection count text in the generator when adding logo projects.

## Content notes

The portfolio contains eight user-supplied projects: Chameleon Seasonings, Pixi, Hostera Group, Orlune, Dot Academy, Grow Academy, Nazi Fert and Street Myth. Chameleon and Pixi presentations use optimized images rendered from the supplied brand books. Logo-only projects are presented as logo design, without inventing broader deliverables or performance results. Project descriptions discuss visible design characteristics. Social media work can be added when supplied.

Email and WhatsApp links use the supplied contact details. There is no backend contact form, analytics, tracking or cookie dependency. Fonts are system fonts for fast, offline-capable loading. Reduced-motion preferences are respected.

Original supplied logo files are retained as `assets/logo.png` and `assets/logo-white.png`; the website uses the optimized `assets/brand-mark.png`.

## Social media selection
The social section features four supplied designs: two Orlune posts, one Pass NetZero post and one Nazi Fert post. Other supplied social designs were left out as an editorial selection. No campaign performance or account-management claims are made. The social project uses group: social in projects.json, keeping it separate from the identity collection. All displayed images preserve their complete composition.

