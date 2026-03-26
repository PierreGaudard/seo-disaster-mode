#!/usr/bin/env python3
"""Generate a deliberately broken SEO fashion website with 100 pages."""

import os
import random
import datetime

DOMAIN = "https://www.modestyle-paris.fr"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── Fashion content data ───────────────────────────────────────────

CATEGORIES = [
    ("robes", "Robes"),
    ("chaussures", "Chaussures"),
    ("accessoires", "Accessoires"),
    ("sacs-a-main", "Sacs à Main"),
    ("bijoux", "Bijoux"),
    ("maquillage", "Maquillage"),
    ("tendances", "Tendances"),
    ("designers", "Designers"),
    ("vetements-homme", "Vêtements Homme"),
    ("lingerie", "Lingerie"),
]

PRODUCTS = {
    "robes": [
        ("robe-soiree-noire", "Robe de Soirée Noire"),
        ("robe-ete-fleurie", "Robe Été Fleurie"),
        ("robe-cocktail-rouge", "Robe Cocktail Rouge"),
        ("robe-maxi-boheme", "Robe Maxi Bohème"),
        ("robe-courte-blanche", "Robe Courte Blanche"),
        ("robe-dentelle-ivoire", "Robe Dentelle Ivoire"),
    ],
    "chaussures": [
        ("escarpins-noirs", "Escarpins Noirs"),
        ("baskets-blanches", "Baskets Blanches"),
        ("sandales-ete", "Sandales Été"),
        ("bottes-cuir", "Bottes en Cuir"),
        ("mocassins-velours", "Mocassins Velours"),
        ("talons-aiguilles-rouges", "Talons Aiguilles Rouges"),
    ],
    "accessoires": [
        ("lunettes-soleil-aviateur", "Lunettes de Soleil Aviateur"),
        ("echarpe-cachemire", "Écharpe en Cachemire"),
        ("ceinture-cuir-italien", "Ceinture Cuir Italien"),
        ("chapeau-fedora", "Chapeau Fedora"),
        ("gants-soie", "Gants en Soie"),
    ],
    "sacs-a-main": [
        ("sac-cuir-noir", "Sac en Cuir Noir"),
        ("pochette-soiree", "Pochette de Soirée"),
        ("sac-bandouliere", "Sac Bandoulière"),
        ("cabas-plage", "Cabas de Plage"),
        ("sac-voyage-luxe", "Sac de Voyage Luxe"),
    ],
    "bijoux": [
        ("collier-or-18k", "Collier Or 18K"),
        ("boucles-oreilles-perles", "Boucles d'Oreilles Perles"),
        ("bracelet-argent", "Bracelet Argent"),
        ("bague-diamant", "Bague Diamant"),
    ],
    "maquillage": [
        ("rouge-levres-mat", "Rouge à Lèvres Mat"),
        ("fond-teint-naturel", "Fond de Teint Naturel"),
        ("mascara-volume", "Mascara Volume"),
        ("palette-fards", "Palette de Fards"),
    ],
    "tendances": [
        ("tendances-printemps-2025", "Tendances Printemps 2025"),
        ("tendances-automne-hiver", "Tendances Automne-Hiver"),
        ("couleurs-saison", "Les Couleurs de la Saison"),
        ("mode-durable", "Mode Durable et Écoresponsable"),
    ],
    "designers": [
        ("jean-paul-gaultier", "Jean-Paul Gaultier"),
        ("coco-chanel-heritage", "Coco Chanel : L'Héritage"),
        ("alexander-mcqueen", "Alexander McQueen"),
        ("yves-saint-laurent", "Yves Saint Laurent"),
    ],
    "vetements-homme": [
        ("costume-italien", "Costume Italien"),
        ("chemise-lin", "Chemise en Lin"),
        ("jean-slim-brut", "Jean Slim Brut"),
        ("veste-cuir-vintage", "Veste Cuir Vintage"),
        ("polo-coton-bio", "Polo Coton Bio"),
    ],
    "lingerie": [
        ("ensemble-dentelle", "Ensemble Dentelle"),
        ("nuisette-soie", "Nuisette en Soie"),
        ("body-sculptant", "Body Sculptant"),
        ("pyjama-satin", "Pyjama Satin"),
    ],
}

BLOG_ARTICLES = [
    ("blog/comment-porter-le-velours", "Comment porter le velours cet hiver"),
    ("blog/top-10-sacs-iconiques", "Top 10 des Sacs Iconiques"),
    ("blog/guide-tailles-international", "Guide des Tailles International"),
    ("blog/entretien-cuir", "Comment Entretenir vos Articles en Cuir"),
    ("blog/histoire-haute-couture", "L'Histoire de la Haute Couture"),
    ("blog/mode-annees-90", "Le Retour de la Mode des Années 90"),
    ("blog/capsule-wardrobe", "Créer une Garde-Robe Capsule"),
    ("blog/fashion-week-recap", "Fashion Week : Le Récap Complet"),
    ("blog/mode-ethique-guide", "Guide Complet de la Mode Éthique"),
    ("blog/accessoiriser-tenue", "Comment Accessoiriser sa Tenue"),
]

# Pages that will NOT exist (404 targets)
GHOST_PAGES = [
    "soldes-hiver-2024",
    "collection-limitee-ete",
    "lookbook-printemps",
    "nouvelle-collection",
    "partenariat-exclusif",
    "vente-privee",
    "page-supprimee",
    "ancien-catalogue",
    "promo-flash",
    "collaboration-designer",
    "offre-speciale-noel",
    "black-friday-mode",
]

# Broken image URLs
BROKEN_IMAGES = [
    "images/robe_404.jpg",
    "images/chaussure_manquante.png",
    "img/produit-supprime.jpg",
    "assets/photo_inexistante.webp",
    "media/image-corrompue.jpg",
    "uploads/ancien-visuel.png",
    "static/img/404-fashion.jpg",
    "images/collection/old-photo.jpg",
]

# Real placeholder images (from picsum)
REAL_IMAGES = [
    "https://picsum.photos/seed/mode1/800/600",
    "https://picsum.photos/seed/mode2/800/600",
    "https://picsum.photos/seed/mode3/800/600",
    "https://picsum.photos/seed/fashion1/800/600",
    "https://picsum.photos/seed/fashion2/800/600",
]

# ─── SEO Problem Templates ─────────────────────────────────────────

DUPLICATE_TITLES = [
    "Mode & Style - Votre Boutique en Ligne",
    "Mode & Style - Votre Boutique en Ligne",
    "Découvrez nos Collections | ModeStyle Paris",
    "Découvrez nos Collections | ModeStyle Paris",
    "Achetez en Ligne - Mode Femme & Homme",
    "Achetez en Ligne - Mode Femme & Homme",
]

DUPLICATE_META_DESC = "Découvrez notre collection de mode tendance. Livraison gratuite dès 50€ d'achat. Retours sous 30 jours."

VERY_LONG_TITLE = "Découvrez Notre Incroyable Collection de Mode Printemps-Été 2025 avec des Réductions Exceptionnelles et une Livraison Gratuite pour Tous les Articles de Notre Catalogue en Ligne - ModeStyle Paris France Boutique Officielle"

# ─── Helper functions ───────────────────────────────────────────────

random.seed(42)

all_pages = []  # collect (path, title) for sitemap

def nav_html():
    return """
    <nav>
        <a href="/index.html">Accueil</a>
        <a href="/robes/index.html">Robes</a>
        <a href="/chaussures/index.html">Chaussures</a>
        <a href="/accessoires/index.html">Accessoires</a>
        <a href="/sacs-a-main/index.html">Sacs</a>
        <a href="/bijoux/index.html">Bijoux</a>
        <!-- BUG: lien en HTTP au lieu de HTTPS -->
        <a href="http://www.modestyle-paris.fr/maquillage/index.html">Maquillage</a>
        <a href="/tendances/index.html">Tendances</a>
        <!-- BUG: lien vers page inexistante -->
        <a href="/nouvelle-collection.html">Nouvelle Collection</a>
        <a href="/blog/index.html">Blog</a>
    </nav>"""

def footer_html():
    return f"""
    <footer>
        <p>&copy; 2025 ModeStyle Paris - Tous droits réservés</p>
        <!-- BUG: liens vers pages 404 -->
        <a href="/mentions-legales.html">Mentions Légales</a>
        <a href="/cgv.html">CGV</a>
        <a href="/{random.choice(GHOST_PAGES)}.html">Offres Spéciales</a>
        <a href="/plan-du-site.html">Plan du site</a>
        <!-- BUG: lien externe cassé -->
        <a href="https://www.fashion-federation-inexistante.org">Fédération de la Mode</a>
    </footer>"""


def broken_img_tag():
    """Return an <img> with broken src and no alt."""
    src = random.choice(BROKEN_IMAGES)
    return f'<img src="/{src}">'


def img_no_alt():
    """Return an <img> with valid src but NO alt."""
    src = random.choice(REAL_IMAGES)
    return f'<img src="{src}">'


def img_ok(alt="Photo de mode"):
    src = random.choice(REAL_IMAGES)
    return f'<img src="{src}" alt="{alt}">'


def lorem_fashion():
    paragraphs = [
        "Explorez les dernières tendances de la mode parisienne. Notre sélection est soigneusement choisie par nos stylistes pour vous offrir le meilleur de la mode contemporaine.",
        "Chaque pièce de notre collection raconte une histoire. Du tissu à la couture, nous mettons l'accent sur la qualité et le savoir-faire artisanal français.",
        "La mode est un art de vivre. Chez ModeStyle Paris, nous croyons que chaque femme et chaque homme mérite de se sentir unique et élégant au quotidien.",
        "Nos créateurs s'inspirent des défilés parisiens et milanais pour vous proposer des pièces intemporelles qui traversent les saisons avec élégance.",
        "Découvrez une mode responsable et éthique. Nous travaillons avec des fournisseurs certifiés pour réduire notre impact environnemental tout en maintenant une qualité exceptionnelle.",
        "Le style n'a pas de prix. Retrouvez nos collections à des prix accessibles, sans compromis sur la qualité des matières et des finitions.",
    ]
    return "\n".join(f"<p>{p}</p>" for p in random.sample(paragraphs, k=random.randint(2, 4)))


def write_page(path, content):
    full_path = os.path.join(OUTPUT_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


def make_page(path, title, meta_desc, h1, body_content, canonical=None, extra_issues=None):
    """Generate an HTML page with optional SEO issues."""
    extra_issues = extra_issues or []

    # Title tag
    if "empty_title" in extra_issues:
        title_tag = "<title></title>"
    elif "long_title" in extra_issues:
        title_tag = f"<title>{VERY_LONG_TITLE}</title>"
    elif "duplicate_title" in extra_issues:
        title_tag = f"<title>{random.choice(DUPLICATE_TITLES)}</title>"
    else:
        title_tag = f"<title>{title}</title>"

    # Meta description
    if "no_meta_desc" in extra_issues:
        meta_tag = ""
    elif "duplicate_meta_desc" in extra_issues:
        meta_tag = f'<meta name="description" content="{DUPLICATE_META_DESC}">'
    else:
        meta_tag = f'<meta name="description" content="{meta_desc}">' if meta_desc else ""

    # Canonical
    if "wrong_canonical" in extra_issues:
        canon = f'<link rel="canonical" href="{DOMAIN}/{random.choice(GHOST_PAGES)}.html">'
    elif canonical:
        canon = f'<link rel="canonical" href="{DOMAIN}/{canonical}">'
    else:
        canon = f'<link rel="canonical" href="{DOMAIN}/{path}">'

    # H1
    if "no_h1" in extra_issues:
        h1_tag = ""
    elif "multiple_h1" in extra_issues:
        h1_tag = f"<h1>{h1}</h1>\n<h1>Bienvenue chez ModeStyle Paris</h1>"
    else:
        h1_tag = f"<h1>{h1}</h1>" if h1 else ""

    # Sprinkle broken images
    extra_images = ""
    if "broken_images" in extra_issues:
        extra_images += broken_img_tag() + "\n" + broken_img_tag() + "\n"
    if "no_alt_images" in extra_issues:
        extra_images += img_no_alt() + "\n" + img_no_alt() + "\n"

    # 404 links
    broken_links = ""
    if "broken_links" in extra_issues:
        ghosts = random.sample(GHOST_PAGES, k=random.randint(1, 3))
        broken_links = "\n".join(f'<a href="/{g}.html">Voir {g.replace("-", " ").title()}</a>' for g in ghosts)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title_tag}
    {meta_tag}
    {canon}
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    {nav_html()}
    <main>
        {h1_tag}
        {extra_images}
        {body_content}
        {broken_links}
    </main>
    {footer_html()}
</body>
</html>"""

    write_page(path, html)
    all_pages.append(path)


# ─── Generate pages ─────────────────────────────────────────────────

# 1. Homepage - duplicate title, multiple H1, broken images
make_page(
    "index.html",
    "Mode & Style - Votre Boutique en Ligne",
    "Bienvenue sur ModeStyle Paris, votre destination mode en ligne.",
    "ModeStyle Paris - Mode Femme & Homme",
    f"""
    {img_no_alt()}
    {broken_img_tag()}
    <h2>Nos Collections</h2>
    {lorem_fashion()}
    <h2>Nouveautés</h2>
    {img_no_alt()}
    <p>Découvrez nos dernières arrivées :</p>
    <ul>
        <li><a href="/robes/robe-soiree-noire.html">Robe de Soirée Noire</a></li>
        <li><a href="/soldes-hiver-2024.html">Soldes d'Hiver</a></li>
        <li><a href="/chaussures/escarpins-noirs.html">Escarpins Noirs</a></li>
        <li><a href="/collection-limitee-ete.html">Collection Limitée Été</a></li>
        <li><a href="/lookbook-printemps.html">Lookbook Printemps</a></li>
    </ul>
    """,
    extra_issues=["duplicate_title", "multiple_h1", "broken_images", "no_alt_images"]
)

# 2. Category pages
for i, (cat_slug, cat_name) in enumerate(CATEGORIES):
    issues = []
    meta = f"Découvrez notre collection de {cat_name.lower()}. Les plus belles pièces de la mode parisienne."

    if i in [0, 3]:
        issues.append("duplicate_title")
    if i in [1, 5]:
        issues.append("no_h1")
    if i in [2, 7]:
        issues.append("no_meta_desc")
    if i in [4, 6]:
        issues.append("duplicate_meta_desc")
    if i in [0, 2, 5, 8]:
        issues.append("broken_images")
    if i in [1, 3, 6, 9]:
        issues.append("no_alt_images")
    if i in [0, 4, 7]:
        issues.append("broken_links")

    products_in_cat = PRODUCTS.get(cat_slug, [])
    product_links = "\n".join(
        f'<li><a href="/{cat_slug}/{slug}.html">{name}</a></li>'
        for slug, name in products_in_cat
    )
    # Add some broken product links
    product_links += f'\n<li><a href="/{cat_slug}/produit-supprime-ancien.html">Article en Rupture</a></li>'
    product_links += f'\n<li><a href="/{cat_slug}/collection-archivee.html">Collection Archivée</a></li>'

    make_page(
        f"{cat_slug}/index.html",
        f"{cat_name} - Collection ModeStyle Paris",
        meta,
        f"Collection {cat_name}",
        f"""
        {img_ok(f"Collection {cat_name}") if i % 3 == 0 else img_no_alt()}
        {lorem_fashion()}
        <h2>Nos {cat_name}</h2>
        <ul>{product_links}</ul>
        """,
        extra_issues=issues
    )

# 3. Product pages
page_count = 12  # already have index + 10 categories + 1
for cat_slug, cat_name in CATEGORIES:
    for j, (prod_slug, prod_name) in enumerate(PRODUCTS.get(cat_slug, [])):
        issues = []
        meta = f"{prod_name} - Achetez en ligne sur ModeStyle Paris. Livraison rapide."

        # Distribute SEO issues
        r = random.random()
        if r < 0.12:
            issues.append("empty_title")
        elif r < 0.22:
            issues.append("long_title")
        elif r < 0.35:
            issues.append("duplicate_title")

        if random.random() < 0.2:
            issues.append("no_h1")
        if random.random() < 0.15:
            issues.append("multiple_h1")
        if random.random() < 0.25:
            issues.append("no_meta_desc")
        if random.random() < 0.2:
            issues.append("duplicate_meta_desc")
        if random.random() < 0.3:
            issues.append("broken_images")
        if random.random() < 0.35:
            issues.append("no_alt_images")
        if random.random() < 0.25:
            issues.append("broken_links")
        if random.random() < 0.1:
            issues.append("wrong_canonical")

        # Related products with some 404s
        related = ""
        all_prods = [(cs, ps, pn) for cs, cn in CATEGORIES for ps, pn in PRODUCTS.get(cs, [])]
        sample_related = random.sample(all_prods, k=min(3, len(all_prods)))
        related_links = "\n".join(
            f'<li><a href="/{cs}/{ps}.html">{pn}</a></li>'
            for cs, ps, pn in sample_related
        )
        # Add a 404 related link
        related_links += f'\n<li><a href="/{cat_slug}/{random.choice(GHOST_PAGES)}.html">Voir aussi</a></li>'

        price = f"{random.randint(29, 499)},00 €"

        make_page(
            f"{cat_slug}/{prod_slug}.html",
            f"{prod_name} | ModeStyle Paris",
            meta,
            prod_name,
            f"""
            <div class="product">
                {broken_img_tag() if "broken_images" in issues else img_no_alt()}
                <p class="price">{price}</p>
                {lorem_fashion()}
                <h2>Produits Similaires</h2>
                <ul>{related_links}</ul>
            </div>
            """,
            extra_issues=issues
        )
        page_count += 1

# 4. Blog pages
os.makedirs(os.path.join(OUTPUT_DIR, "blog"), exist_ok=True)

# Blog index - no H1, duplicate meta
make_page(
    "blog/index.html",
    "Blog Mode - ModeStyle Paris",
    DUPLICATE_META_DESC,
    "Notre Blog Mode",
    f"""
    {img_no_alt()}
    <p>Retrouvez tous nos articles mode, conseils style et actualités fashion.</p>
    <ul>
    {"".join(f'<li><a href="/{slug}.html">{title}</a></li>' for slug, title in BLOG_ARTICLES)}
    <li><a href="/blog/article-supprime.html">Les Tendances Oubliées</a></li>
    <li><a href="/blog/guide-perdu.html">Guide Disparu</a></li>
    </ul>
    """,
    extra_issues=["duplicate_meta_desc", "no_alt_images"]
)
page_count += 1

for k, (blog_slug, blog_title) in enumerate(BLOG_ARTICLES):
    issues = []
    meta = f"{blog_title} - Conseils et inspirations mode sur le blog ModeStyle Paris."

    if k in [0, 4]:
        issues.append("duplicate_title")
    if k in [1, 6]:
        issues.append("no_h1")
    if k in [2, 8]:
        issues.append("empty_title")
    if k in [3]:
        issues.append("long_title")
    if k in [5, 9]:
        issues.append("multiple_h1")
    if k % 2 == 0:
        issues.append("broken_images")
        issues.append("no_alt_images")
    if k in [1, 3, 7]:
        issues.append("broken_links")
    if k in [2, 5]:
        issues.append("wrong_canonical")
    if k in [0, 4, 8]:
        issues.append("no_meta_desc")

    make_page(
        f"{blog_slug}.html",
        f"{blog_title} | Blog ModeStyle Paris",
        meta,
        blog_title,
        f"""
        <article>
            <p class="date">Publié le {random.randint(1,28)} {random.choice(['janvier','février','mars','avril','mai','juin'])} 2025</p>
            {img_ok(blog_title) if k % 3 == 0 else img_no_alt()}
            {lorem_fashion()}
            {lorem_fashion()}
            <h2>À lire aussi</h2>
            <ul>
                <li><a href="/{random.choice(GHOST_PAGES)}.html">Article connexe</a></li>
                <li><a href="/blog/{random.choice(GHOST_PAGES)}.html">Guide complémentaire</a></li>
            </ul>
        </article>
        """,
        extra_issues=issues
    )
    page_count += 1

# 5. Fill up to ~100 pages with extra "landing" pages
EXTRA_PAGES = [
    ("promo/ete-2025", "Promotions Été 2025"),
    ("promo/hiver-2025", "Promotions Hiver 2025"),
    ("promo/black-friday", "Black Friday Mode"),
    ("promo/soldes-finales", "Soldes Finales"),
    ("guide/morphologie", "Guide Morphologie"),
    ("guide/couleurs-peau", "Quelles Couleurs pour Ma Peau"),
    ("guide/dress-code-bureau", "Dress Code Bureau"),
    ("guide/mode-grande-taille", "Mode Grande Taille"),
    ("guide/style-minimaliste", "Le Style Minimaliste"),
    ("inspiration/look-casual", "Look Casual Chic"),
    ("inspiration/look-soiree", "Look Soirée Glamour"),
    ("inspiration/look-bureau", "Look Bureau Tendance"),
    ("inspiration/look-weekend", "Look Weekend Décontracté"),
    ("inspiration/look-vacances", "Look Vacances"),
    ("marques/chanel", "Chanel - Nos Sélections"),
    ("marques/dior", "Dior - Nos Sélections"),
    ("marques/louis-vuitton", "Louis Vuitton - Nos Sélections"),
    ("marques/hermes", "Hermès - Nos Sélections"),
    ("marques/prada", "Prada - Nos Sélections"),
    ("marques/gucci", "Gucci - Nos Sélections"),
    ("marques/balenciaga", "Balenciaga - Nos Sélections"),
    ("marques/valentino", "Valentino - Nos Sélections"),
    ("collections/printemps-2025", "Collection Printemps 2025"),
    ("collections/ete-2025", "Collection Été 2025"),
    ("collections/automne-2025", "Collection Automne 2025"),
    ("collections/hiver-2025", "Collection Hiver 2025"),
    ("guide/entretien-soie", "Entretien de la Soie"),
    ("guide/choisir-parfum", "Comment Choisir son Parfum"),
    ("inspiration/look-festival", "Look Festival"),
    ("inspiration/look-mariage", "Look Invitée Mariage"),
]

for m, (extra_slug, extra_title) in enumerate(EXTRA_PAGES):
    if page_count >= 100:
        break
    issues = []
    if m % 4 == 0:
        issues.append("duplicate_title")
    if m % 5 == 0:
        issues.append("no_h1")
    if m % 3 == 0:
        issues.append("broken_images")
    if m % 2 == 0:
        issues.append("no_alt_images")
    if m % 6 == 0:
        issues.append("wrong_canonical")
    if m % 4 == 1:
        issues.append("no_meta_desc")
    if m % 7 == 0:
        issues.append("broken_links")
    if m % 5 == 2:
        issues.append("multiple_h1")

    make_page(
        f"{extra_slug}.html",
        f"{extra_title} | ModeStyle Paris",
        f"{extra_title} - Découvrez nos sélections mode exclusives chez ModeStyle Paris.",
        extra_title,
        f"""
        {img_no_alt()}
        {lorem_fashion()}
        <h2>Nos Recommandations</h2>
        {lorem_fashion()}
        <a href="/{random.choice(GHOST_PAGES)}.html">Découvrir plus</a>
        """,
        extra_issues=issues
    )
    page_count += 1


# ─── robots.txt (GOOD) ─────────────────────────────────────────────

robots_txt = f"""User-agent: *
Allow: /

Disallow: /admin/
Disallow: /api/
Disallow: /tmp/
Disallow: /private/

# Crawl-delay
Crawl-delay: 1

# Sitemap
Sitemap: {DOMAIN}/sitemap.xml
"""
write_page("robots.txt", robots_txt)


# ─── sitemap.xml (GOOD) ────────────────────────────────────────────

today = datetime.date.today().isoformat()
sitemap_entries = []
for page_path in all_pages:
    priority = "1.0" if page_path == "index.html" else "0.8" if "/index.html" in page_path else "0.6"
    freq = "daily" if page_path == "index.html" else "weekly"
    sitemap_entries.append(f"""  <url>
    <loc>{DOMAIN}/{page_path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"".join(sitemap_entries)}
</urlset>"""
write_page("sitemap.xml", sitemap_xml)


# ─── Minimal CSS ────────────────────────────────────────────────────

css = """
body { font-family: Georgia, serif; max-width: 960px; margin: 0 auto; padding: 20px; color: #333; }
nav { background: #1a1a2e; padding: 15px; margin-bottom: 30px; }
nav a { color: #e94560; text-decoration: none; margin-right: 15px; font-size: 14px; }
nav a:hover { text-decoration: underline; }
h1 { color: #1a1a2e; border-bottom: 2px solid #e94560; padding-bottom: 10px; }
h2 { color: #16213e; }
.product { border: 1px solid #ddd; padding: 20px; margin: 20px 0; }
.price { font-size: 24px; color: #e94560; font-weight: bold; }
img { max-width: 100%; height: auto; margin: 10px 0; }
footer { margin-top: 50px; padding: 20px; background: #f5f5f5; text-align: center; font-size: 12px; }
footer a { color: #666; margin: 0 10px; }
ul { line-height: 2; }
article .date { color: #999; font-style: italic; }
"""
write_page("css/style.css", css)


# ─── Summary ────────────────────────────────────────────────────────

print(f"✅ Generated {page_count} pages + robots.txt + sitemap.xml + CSS")
print(f"   Total files: {len(all_pages) + 3}")
print(f"   Ghost pages (404 targets): {len(GHOST_PAGES)}")
