#!/usr/bin/env python3
"""Generate a deliberately broken SEO fashion website with 100 pages — v2 with real design."""

import os, random, datetime

DOMAIN = "https://pierregaudard.github.io/seo-disaster-mode"
BASE = os.path.dirname(os.path.abspath(__file__))
P = "/seo-disaster-mode/"  # Base path prefix for GitHub Pages
random.seed(42)

# ═══════════════════════════════════════════════════════
# DATA
# ═══════════════════════════════════════════════════════

# Image mapping (real downloaded images)
IMG = {
    "hero": "images/hero-fashion.jpg",
    "robe": "images/robe-elegante.jpg",
    "mannequin": "images/mannequin-studio.jpg",
    "defile": "images/defile-mode.jpg",
    "boutique": "images/boutique-luxe.jpg",
    "shopping": "images/shopping-mode.jpg",
    "rack": "images/vetements-rack.jpg",
    "rue": "images/mannequin-rue.jpg",
    "blanche": "images/robe-blanche.jpg",
    "coloree": "images/mannequin-coloree.jpg",
    "accessoires": "images/accessoires-luxe.jpg",
    "bijoux": "images/bijoux-or.jpg",
    "chaussures": "images/chaussures-sport.jpg",
    "sneakers": "images/sneakers-rouge.jpg",
    "baskets": "images/baskets-running.jpg",
    "sac": "images/sac-main-luxe.jpg",
    "tshirt": "images/tshirt-streetwear.jpg",
    "maquillage": "images/maquillage-pro.jpg",
    "lunettes": "images/lunettes-soleil.jpg",
    "parfum": "images/parfum-luxe.jpg",
    "hiver": "images/mannequin-hiver.jpg",
    "soiree": "images/mannequin-soiree.jpg",
    "lingerie": "images/lingerie-fine.jpg",
    "naturel": "images/maquillage-naturel.jpg",
    "ete": "images/robe-ete.jpg",
    "homme": "images/homme-costume.jpg",
    "interieur": "images/interieur-boutique.jpg",
    "runway": "images/defile-runway.jpg",
    "femme": "images/accessoires-femme.jpg",
    "vintage": "images/mode-vintage.jpg",
}

# Broken image paths (404)
BROKEN_IMG = [
    "images/robe_supprimee_404.jpg",
    "images/photo-manquante.png",
    "img/produit-ancien.jpg",
    "assets/visuel-erreur.webp",
    "media/image-corrompue.jpg",
    "uploads/old-collection.png",
    "static/img/broken-photo.jpg",
    "images/collection/archive-2023.jpg",
]

CATEGORIES = [
    ("robes", "Robes", "robe", "Découvrez notre collection exclusive de robes pour toutes les occasions."),
    ("chaussures", "Chaussures", "chaussures", "Les plus belles chaussures des créateurs parisiens et internationaux."),
    ("accessoires", "Accessoires", "accessoires", "Complétez votre look avec nos accessoires soigneusement sélectionnés."),
    ("sacs-a-main", "Sacs à Main", "sac", "Sacs à main de luxe, pochettes et cabas pour sublimer votre style."),
    ("bijoux", "Bijoux", "bijoux", "Bijoux fins et précieux pour toutes les femmes élégantes."),
    ("maquillage", "Maquillage", "maquillage", "Sublimez votre beauté avec notre sélection maquillage premium."),
    ("tendances", "Tendances", "runway", "Les tendances mode du moment décryptées par nos stylistes."),
    ("designers", "Designers", "defile", "Les grands noms de la mode française et internationale."),
    ("vetements-homme", "Vêtements Homme", "homme", "Mode masculine élégante et contemporaine."),
    ("lingerie", "Lingerie", "lingerie", "Lingerie fine et confortable pour se sentir belle au quotidien."),
]

PRODUCTS = {
    "robes": [
        ("robe-soiree-noire", "Robe de Soirée Noire", "MAISON ÉLÉGANCE", 289, "robe"),
        ("robe-ete-fleurie", "Robe Été Fleurie", "JARDIN PARISIEN", 159, "ete"),
        ("robe-cocktail-rouge", "Robe Cocktail Rouge", "ATELIER ROUGE", 349, "coloree"),
        ("robe-maxi-boheme", "Robe Maxi Bohème", "LIBRE & BELLE", 199, "blanche"),
        ("robe-courte-blanche", "Robe Courte Blanche", "MAISON PURE", 129, "blanche"),
        ("robe-dentelle-ivoire", "Robe Dentelle Ivoire", "HÉRITAGE PARIS", 459, "robe"),
    ],
    "chaussures": [
        ("escarpins-noirs", "Escarpins Noirs Classiques", "TALONS PARIS", 189, "chaussures"),
        ("baskets-blanches", "Baskets Blanches Minimalistes", "URBAN WALK", 129, "sneakers"),
        ("sandales-ete", "Sandales Été Dorées", "SOLEIL D'OR", 99, "baskets"),
        ("bottes-cuir", "Bottes en Cuir Italien", "BOTTEGA STILE", 349, "chaussures"),
        ("mocassins-velours", "Mocassins Velours Bordeaux", "VELVET STEP", 159, "baskets"),
        ("talons-aiguilles-rouges", "Talons Aiguilles Rouges", "ATELIER ROUGE", 229, "chaussures"),
    ],
    "accessoires": [
        ("lunettes-soleil-aviateur", "Lunettes Aviateur Or", "VISION LUXE", 199, "lunettes"),
        ("echarpe-cachemire", "Écharpe Cachemire Gris", "DOUCEUR PARIS", 149, "accessoires"),
        ("ceinture-cuir-italien", "Ceinture Cuir Italien", "BOTTEGA STILE", 89, "accessoires"),
        ("chapeau-fedora", "Chapeau Fedora Noir", "CHAPELIER PARISIEN", 119, "vintage"),
        ("gants-soie", "Gants en Soie Ivoire", "HÉRITAGE PARIS", 79, "femme"),
    ],
    "sacs-a-main": [
        ("sac-cuir-noir", "Sac Cuir Noir Intemporel", "MAISON ÉLÉGANCE", 489, "sac"),
        ("pochette-soiree", "Pochette de Soirée Dorée", "SOLEIL D'OR", 199, "sac"),
        ("sac-bandouliere", "Sac Bandoulière Camel", "URBAN WALK", 259, "sac"),
        ("cabas-plage", "Cabas de Plage Naturel", "LIBRE & BELLE", 79, "sac"),
        ("sac-voyage-luxe", "Sac de Voyage en Cuir", "BOTTEGA STILE", 599, "sac"),
    ],
    "bijoux": [
        ("collier-or-18k", "Collier Or 18 Carats", "JOAILLERIE ÉTOILE", 899, "bijoux"),
        ("boucles-oreilles-perles", "Boucles d'Oreilles Perles", "PERLES DU SUD", 249, "bijoux"),
        ("bracelet-argent", "Bracelet Argent Massif", "ARGENT NOBLE", 159, "bijoux"),
        ("bague-diamant", "Bague Diamant Solitaire", "JOAILLERIE ÉTOILE", 1299, "bijoux"),
    ],
    "maquillage": [
        ("rouge-levres-mat", "Rouge à Lèvres Mat Velours", "BEAUTÉ PARISIENNE", 39, "maquillage"),
        ("fond-teint-naturel", "Fond de Teint Naturel", "PEAU DOUCE", 49, "naturel"),
        ("mascara-volume", "Mascara Volume Extrême", "REGARD INTENSE", 29, "maquillage"),
        ("palette-fards", "Palette Fards à Paupières", "BEAUTÉ PARISIENNE", 59, "maquillage"),
    ],
    "tendances": [
        ("tendances-printemps-2025", "Tendances Printemps 2025", "MODESTYLE", 0, "runway"),
        ("tendances-automne-hiver", "Tendances Automne-Hiver", "MODESTYLE", 0, "hiver"),
        ("couleurs-saison", "Les Couleurs de la Saison", "MODESTYLE", 0, "coloree"),
        ("mode-durable", "Mode Durable et Écoresponsable", "MODESTYLE", 0, "vintage"),
    ],
    "designers": [
        ("jean-paul-gaultier", "Jean-Paul Gaultier", "JPG", 0, "defile"),
        ("coco-chanel-heritage", "Coco Chanel : L'Héritage", "CHANEL", 0, "boutique"),
        ("alexander-mcqueen", "Alexander McQueen", "MCQUEEN", 0, "runway"),
        ("yves-saint-laurent", "Yves Saint Laurent", "YSL", 0, "mannequin"),
    ],
    "vetements-homme": [
        ("costume-italien", "Costume Italien Coupe Slim", "SARTORIA ROMA", 599, "homme"),
        ("chemise-lin", "Chemise en Lin Blanc", "MAISON PURE", 89, "homme"),
        ("jean-slim-brut", "Jean Slim Brut Japonais", "DENIM CRAFT", 149, "tshirt"),
        ("veste-cuir-vintage", "Veste Cuir Vintage", "HERITAGE LEATHER", 399, "vintage"),
        ("polo-coton-bio", "Polo Coton Bio", "ÉCOMODE", 59, "tshirt"),
    ],
    "lingerie": [
        ("ensemble-dentelle", "Ensemble Dentelle Française", "INTIME PARIS", 129, "lingerie"),
        ("nuisette-soie", "Nuisette en Soie Rose", "DOUCEUR DE NUIT", 89, "soiree"),
        ("body-sculptant", "Body Sculptant Seconde Peau", "SILHOUETTE", 69, "lingerie"),
        ("pyjama-satin", "Pyjama Satin Champagne", "DOUCEUR DE NUIT", 109, "soiree"),
    ],
}

BLOG_ARTICLES = [
    ("blog/comment-porter-le-velours", "Comment Porter le Velours cet Hiver", "TENDANCES", "Le velours fait son grand retour sur les podiums. Découvrez comment intégrer cette matière noble dans vos tenues quotidiennes sans faux pas.", "hiver"),
    ("blog/top-10-sacs-iconiques", "Top 10 des Sacs les Plus Iconiques de l'Histoire", "CULTURE MODE", "Du Birkin d'Hermès au 2.55 de Chanel, retour sur les sacs qui ont marqué l'histoire de la mode.", "sac"),
    ("blog/guide-tailles-international", "Guide des Tailles International : Ne Vous Trompez Plus", "GUIDES", "Fini les erreurs de taille lors de vos achats en ligne. Notre guide complet pour convertir toutes les tailles.", "rack"),
    ("blog/entretien-cuir", "L'Art d'Entretenir vos Articles en Cuir", "ENTRETIEN", "Le cuir est un investissement. Apprenez les gestes essentiels pour préserver vos pièces en cuir pendant des années.", "sac"),
    ("blog/histoire-haute-couture", "L'Histoire Fascinante de la Haute Couture Française", "CULTURE MODE", "De Worth à aujourd'hui, plongez dans l'histoire de la haute couture qui a fait de Paris la capitale mondiale de la mode.", "defile"),
    ("blog/mode-annees-90", "Le Grand Retour de la Mode des Années 90", "TENDANCES", "Jeans taille haute, crop tops et plateformes : les années 90 n'ont jamais été aussi actuelles.", "vintage"),
    ("blog/capsule-wardrobe", "Créer sa Garde-Robe Capsule en 30 Pièces", "GUIDES", "Moins c'est plus. Découvrez comment composer une garde-robe minimaliste mais infiniment versatile.", "rack"),
    ("blog/fashion-week-recap", "Fashion Week Paris : Le Récap Complet des Défilés", "ÉVÉNEMENTS", "Toutes les tendances, les moments forts et les collections qui ont marqué cette Fashion Week parisienne.", "runway"),
    ("blog/mode-ethique-guide", "Mode Éthique : Le Guide Complet pour Consommer Responsable", "ÉCOMODE", "Comment concilier style et éthique ? Nos conseils pour une garde-robe responsable sans compromis sur le style.", "vintage"),
    ("blog/accessoiriser-tenue", "L'Art d'Accessoiriser : 10 Règles d'Or", "STYLE", "Les accessoires font la différence. Maîtrisez l'art de l'accessoirisation avec nos 10 commandements mode.", "femme"),
]

EXTRA_PAGES = [
    ("promo/ete-2025", "Promotions Été 2025", "shopping"),
    ("promo/hiver-2025", "Promotions Hiver 2025", "hiver"),
    ("promo/black-friday", "Black Friday Mode", "rack"),
    ("promo/soldes-finales", "Soldes Finales", "boutique"),
    ("guide/morphologie", "Guide Morphologie", "mannequin"),
    ("guide/couleurs-peau", "Quelles Couleurs pour Ma Peau", "maquillage"),
    ("guide/dress-code-bureau", "Dress Code Bureau", "homme"),
    ("guide/mode-grande-taille", "Mode Grande Taille", "rue"),
    ("guide/style-minimaliste", "Le Style Minimaliste", "blanche"),
    ("inspiration/look-casual", "Look Casual Chic", "rue"),
    ("inspiration/look-soiree", "Look Soirée Glamour", "soiree"),
    ("inspiration/look-bureau", "Look Bureau Tendance", "homme"),
    ("inspiration/look-weekend", "Look Weekend Décontracté", "ete"),
    ("inspiration/look-vacances", "Look Vacances Été", "ete"),
    ("marques/chanel", "Chanel — Nos Sélections", "boutique"),
    ("marques/dior", "Dior — Nos Sélections", "defile"),
    ("marques/louis-vuitton", "Louis Vuitton — Nos Sélections", "sac"),
    ("marques/hermes", "Hermès — Nos Sélections", "accessoires"),
    ("marques/prada", "Prada — Nos Sélections", "mannequin"),
    ("marques/gucci", "Gucci — Nos Sélections", "coloree"),
    ("marques/balenciaga", "Balenciaga — Nos Sélections", "sneakers"),
    ("marques/valentino", "Valentino — Nos Sélections", "robe"),
    ("collections/printemps-2025", "Collection Printemps 2025", "ete"),
    ("collections/ete-2025", "Collection Été 2025", "shopping"),
    ("collections/automne-2025", "Collection Automne 2025", "hiver"),
    ("collections/hiver-2025", "Collection Hiver 2025", "hiver"),
    ("guide/entretien-soie", "Entretien de la Soie", "lingerie"),
    ("guide/choisir-parfum", "Comment Choisir son Parfum", "parfum"),
    ("inspiration/look-festival", "Look Festival", "coloree"),
    ("inspiration/look-mariage", "Look Invitée Mariage", "blanche"),
]

GHOST_PAGES = [
    "soldes-hiver-2024", "collection-limitee-ete", "lookbook-printemps",
    "nouvelle-collection", "partenariat-exclusif", "vente-privee",
    "page-supprimee", "ancien-catalogue", "promo-flash",
    "collaboration-designer", "offre-speciale-noel", "black-friday-mode",
]

DUPLICATE_TITLES = [
    "Mode &amp; Style — Votre Boutique en Ligne",
    "Découvrez nos Collections | ModeStyle Paris",
    "Achetez en Ligne — Mode Femme &amp; Homme",
]

DUPLICATE_META = "Découvrez notre collection de mode tendance. Livraison gratuite dès 50€. Retours sous 30 jours."
LONG_TITLE = "Découvrez Notre Incroyable Collection de Mode Printemps-Été 2025 avec des Réductions Exceptionnelles et une Livraison Gratuite pour Tous les Articles de Notre Catalogue en Ligne — ModeStyle Paris France Boutique Officielle"

all_pages = []

# ═══════════════════════════════════════════════════════
# COMPONENT TEMPLATES
# ═══════════════════════════════════════════════════════

def img_path(key):
    return IMG.get(key, IMG["hero"])

def broken_img():
    return f'<img src="{P}{random.choice(BROKEN_IMG)}">'

def img_no_alt(key="hero"):
    return f'<img src="{P}{img_path(key)}">'

def img_ok(key="hero", alt="Photo de mode"):
    return f'<img src="{P}{img_path(key)}" alt="{alt}">'

def top_bar():
    return '<div class="top-bar">Livraison offerte dès 100€ d\'achat — Retours gratuits sous 30 jours</div>'

def header_html():
    return f"""
    <header class="header">
        <div class="container">
            <a href="{P}index.html" class="logo">Mode<span>Style</span></a>
            <nav>
                <a href="{P}robes/index.html">Robes</a>
                <a href="{P}chaussures/index.html">Chaussures</a>
                <a href="{P}accessoires/index.html">Accessoires</a>
                <a href="{P}sacs-a-main/index.html">Sacs</a>
                <a href="{P}bijoux/index.html">Bijoux</a>
                <!-- BUG SEO: lien HTTP mixte -->
                <a href="http://www.modestyle-paris.fr/maquillage/index.html">Maquillage</a>
                <a href="{P}tendances/index.html">Tendances</a>
                <!-- BUG SEO: lien 404 -->
                <a href="{P}nouvelle-collection.html">Nouveau</a>
                <a href="{P}blog/index.html">Journal</a>
            </nav>
        </div>
    </header>"""

def footer_html():
    ghost = random.choice(GHOST_PAGES)
    return f"""
    <section class="newsletter">
        <div class="container">
            <h2>Restez Inspiré</h2>
            <p>Inscrivez-vous à notre newsletter et recevez en avant-première nos nouveautés et conseils style.</p>
            <form class="newsletter-form">
                <input type="email" placeholder="Votre adresse email">
                <button type="submit">S'inscrire</button>
            </form>
        </div>
    </section>
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h4>ModeStyle Paris</h4>
                    <p>Depuis 2018, ModeStyle Paris sélectionne les plus belles pièces de mode pour femmes et hommes exigeants. Notre passion : vous offrir le meilleur du style parisien.</p>
                </div>
                <div>
                    <h4>Boutique</h4>
                    <ul>
                        <li><a href="{P}robes/index.html">Robes</a></li>
                        <li><a href="{P}chaussures/index.html">Chaussures</a></li>
                        <li><a href="{P}sacs-a-main/index.html">Sacs à Main</a></li>
                        <li><a href="{P}bijoux/index.html">Bijoux</a></li>
                        <!-- BUG SEO: 404 -->
                        <li><a href="{P}{ghost}.html">Offres Spéciales</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Informations</h4>
                    <ul>
                        <!-- BUG SEO: plusieurs 404 -->
                        <li><a href="{P}mentions-legales.html">Mentions Légales</a></li>
                        <li><a href="{P}cgv.html">CGV</a></li>
                        <li><a href="{P}plan-du-site.html">Plan du Site</a></li>
                        <li><a href="{P}guide/morphologie.html">Guide Morphologie</a></li>
                    </ul>
                </div>
                <div>
                    <h4>Contact</h4>
                    <ul>
                        <li>12 Rue du Faubourg Saint-Honoré</li>
                        <li>75008 Paris, France</li>
                        <li>contact@modestyle-paris.fr</li>
                        <li>+33 1 42 68 00 00</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>&copy; 2025 ModeStyle Paris — Tous droits réservés</span>
                <!-- BUG SEO: lien externe cassé -->
                <a href="https://www.fashion-federation-inexistante.org">Fédération de la Mode</a>
            </div>
        </div>
    </footer>"""

PARAGRAPHS = [
    "Explorez les dernières tendances de la mode parisienne. Notre sélection est soigneusement choisie par nos stylistes pour vous offrir le meilleur de la mode contemporaine.",
    "Chaque pièce de notre collection raconte une histoire. Du tissu à la couture, nous mettons l'accent sur la qualité et le savoir-faire artisanal français qui fait la renommée de la mode parisienne dans le monde entier.",
    "La mode est un art de vivre. Chez ModeStyle Paris, nous croyons que chaque femme et chaque homme mérite de se sentir unique et élégant au quotidien, quelles que soient les circonstances.",
    "Nos créateurs s'inspirent des défilés parisiens et milanais pour vous proposer des pièces intemporelles qui traversent les saisons avec élégance et raffinement.",
    "Découvrez une mode responsable et éthique. Nous travaillons avec des fournisseurs certifiés pour réduire notre impact environnemental tout en maintenant une qualité exceptionnelle.",
    "Le style n'a pas de prix. Retrouvez nos collections à des prix accessibles, sans compromis sur la qualité des matières et des finitions haut de gamme.",
]

def lorem():
    return "\n".join(f"<p>{p}</p>" for p in random.sample(PARAGRAPHS, k=random.randint(2, 3)))

# ═══════════════════════════════════════════════════════
# PAGE GENERATOR
# ═══════════════════════════════════════════════════════

def write_file(path, content):
    fp = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

def seo_issues(index):
    """Return a set of SEO issues based on page index for variety."""
    issues = set()
    r = random.random()
    if r < 0.12: issues.add("empty_title")
    elif r < 0.25: issues.add("dup_title")
    elif r < 0.32: issues.add("long_title")
    if random.random() < 0.18: issues.add("no_h1")
    if random.random() < 0.12: issues.add("multi_h1")
    if random.random() < 0.22: issues.add("no_meta")
    if random.random() < 0.18: issues.add("dup_meta")
    if random.random() < 0.30: issues.add("broken_img")
    if random.random() < 0.35: issues.add("no_alt")
    if random.random() < 0.10: issues.add("bad_canonical")
    return issues

def title_tag(title, issues):
    if "empty_title" in issues: return "<title></title>"
    if "long_title" in issues: return f"<title>{LONG_TITLE}</title>"
    if "dup_title" in issues: return f"<title>{random.choice(DUPLICATE_TITLES)}</title>"
    return f"<title>{title}</title>"

def meta_tag(desc, issues):
    if "no_meta" in issues: return ""
    if "dup_meta" in issues: return f'<meta name="description" content="{DUPLICATE_META}">'
    return f'<meta name="description" content="{desc}">'

def canonical_tag(path, issues):
    if "bad_canonical" in issues:
        return f'<link rel="canonical" href="{DOMAIN}/{random.choice(GHOST_PAGES)}.html">'
    return f'<link rel="canonical" href="{DOMAIN}/{path}">'

def h1_tag(text, issues):
    if "no_h1" in issues: return ""
    if "multi_h1" in issues: return f"<h1>{text}</h1>\n<h1>Bienvenue chez ModeStyle Paris</h1>"
    return f"<h1>{text}</h1>"

def ghost_links(n=2):
    gs = random.sample(GHOST_PAGES, k=min(n, len(GHOST_PAGES)))
    return "\n".join(f'<a href="{P}{g}.html" class="btn btn-dark">{g.replace("-"," ").title()}</a>' for g in gs)

# ═══════════════════════════════════════════════════════
# PAGE BUILDERS
# ═══════════════════════════════════════════════════════

def build_page(path, title, desc, body, issues=None):
    issues = issues or set()
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {title_tag(title, issues)}
    {meta_tag(desc, issues)}
    {canonical_tag(path, issues)}
    <link rel="stylesheet" href="{P}css/style.css">
</head>
<body>
    {top_bar()}
    {header_html()}
    {body}
    {footer_html()}
</body>
</html>"""
    write_file(path, html)
    all_pages.append(path)

# ─── HOMEPAGE ──────────────────────────────────────────

def build_homepage():
    cat_cards = ""
    for slug, name, img_key, desc in CATEGORIES[:6]:
        cat_cards += f"""
        <a href="{P}{slug}/index.html" class="category-card">
            {img_no_alt(img_key)}
            <div class="overlay">
                <h3>{name}</h3>
                <span>Découvrir</span>
            </div>
        </a>"""

    # Product cards with mix of broken/missing alt
    prod_cards = ""
    sample_prods = []
    for cat_slug, _, _, _ in CATEGORIES[:5]:
        for p in PRODUCTS.get(cat_slug, [])[:2]:
            sample_prods.append((cat_slug, p))
    random.shuffle(sample_prods)
    for i, (cs, (ps, pn, brand, price, img_key)) in enumerate(sample_prods[:8]):
        if i == 2:
            img_tag = broken_img()  # BUG: image cassée
        elif i % 3 == 0:
            img_tag = img_no_alt(img_key)  # BUG: pas d'alt
        else:
            img_tag = img_ok(img_key, pn)
        badge = '<span class="badge">Nouveau</span>' if i < 2 else ""
        old = f'<span class="old-price">{price + random.randint(30,80)},00 €</span>' if price > 0 and random.random() > 0.6 else ""
        prod_cards += f"""
        <a href="{P}{cs}/{ps}.html" class="product-card">
            <div class="image-wrapper">
                {img_tag}
                {badge}
            </div>
            <div class="info">
                <div class="brand">{brand}</div>
                <h3>{pn}</h3>
                <div class="price">{price},00 €{old}</div>
            </div>
        </a>"""

    blog_cards = ""
    for slug, title, cat, excerpt, img_key in BLOG_ARTICLES[:3]:
        blog_cards += f"""
        <a href="{P}{slug}.html" class="blog-card">
            <div class="image-wrapper">
                {img_no_alt(img_key)}
            </div>
            <div class="content">
                <div class="meta">{cat}</div>
                <h3>{title}</h3>
                <p>{excerpt[:120]}...</p>
                <span class="read-more">Lire la suite</span>
            </div>
        </a>"""

    body = f"""
    <section class="hero">
        {img_no_alt("hero")}
        <img src="{P}{img_path('hero')}" class="hero-bg">
        <div class="hero-content">
            <h1>L'Élégance à la Parisienne</h1>
            <p>Découvrez notre nouvelle collection printemps-été 2025, inspirée par les rues de Paris.</p>
            <a href="{P}soldes-hiver-2024.html" class="btn">Découvrir la Collection</a>
        </div>
    </section>

    <section class="categories-section">
        <div class="container">
            <div class="section-title">
                <h2>Nos Univers</h2>
                <div class="divider"></div>
                <p>Explorez nos collections soigneusement sélectionnées par nos stylistes parisiens.</p>
            </div>
            <div class="categories-grid">
                {cat_cards}
            </div>
        </div>
    </section>

    <section class="featured-banner">
        {img_no_alt("defile")}
        <div class="content">
            <h2>Collection Exclusive Printemps 2025</h2>
            <p>Des pièces uniques créées en collaboration avec les plus grands designers français. Disponible en édition limitée.</p>
            <a href="{P}collection-limitee-ete.html" class="btn">Voir la Collection</a>
        </div>
    </section>

    <section class="products-section">
        <div class="container">
            <div class="section-title">
                <h2>Sélection du Moment</h2>
                <div class="divider"></div>
                <p>Les pièces incontournables choisies par notre équipe de stylistes.</p>
            </div>
            <div class="products-grid">
                {prod_cards}
            </div>
        </div>
    </section>

    <section class="featured-banner">
        {broken_img()}
        <div class="content">
            <h2>Mode Homme — Nouvelle Saison</h2>
            <p>Élégance et modernité pour l'homme contemporain. Découvrez notre sélection masculine.</p>
            <a href="{P}vetements-homme/index.html" class="btn">Explorer</a>
        </div>
    </section>

    <section class="blog-section">
        <div class="container">
            <div class="section-title">
                <h2>Le Journal Mode</h2>
                <div class="divider"></div>
                <p>Tendances, conseils et inspirations par nos experts mode.</p>
            </div>
            <div class="blog-grid">
                {blog_cards}
            </div>
        </div>
    </section>"""

    build_page("index.html", "Mode & Style — Votre Boutique en Ligne",
               "ModeStyle Paris — votre destination mode en ligne. Collections femme et homme, livraison gratuite.",
               body, {"dup_title", "multi_h1", "no_alt", "broken_img"})

# ─── CATEGORY PAGES ──────────────────────────────────

def build_category(idx, slug, name, img_key, desc):
    issues = set()
    if idx in [0, 3]: issues.add("dup_title")
    if idx in [1, 5]: issues.add("no_h1")
    if idx in [2, 7]: issues.add("no_meta")
    if idx in [4, 6]: issues.add("dup_meta")
    if idx in [0, 5, 8]: issues.add("broken_img")
    if idx in [1, 3, 6, 9]: issues.add("no_alt")
    if idx in [0, 4, 7]: issues.add("bad_canonical")

    prods = PRODUCTS.get(slug, [])
    cards = ""
    for j, (ps, pn, brand, price, pimg) in enumerate(prods):
        if j == 0 and "broken_img" in issues:
            img_t = broken_img()
        elif "no_alt" in issues:
            img_t = img_no_alt(pimg)
        else:
            img_t = img_ok(pimg, pn)
        badge = '<span class="badge">-30%</span>' if random.random() > 0.7 else ""
        old = f'<span class="old-price">{price + random.randint(30,100)},00 €</span>' if price > 0 and random.random() > 0.5 else ""
        cards += f"""
        <a href="{P}{slug}/{ps}.html" class="product-card">
            <div class="image-wrapper">{img_t}{badge}</div>
            <div class="info">
                <div class="brand">{brand}</div>
                <h3>{pn}</h3>
                <div class="price">{"" if price == 0 else f"{price},00 €"}{old}</div>
            </div>
        </a>"""

    # BUG: liens vers produits inexistants
    cards += f"""
    <a href="{P}{slug}/produit-supprime-ancien.html" class="product-card">
        <div class="image-wrapper">{broken_img()}</div>
        <div class="info"><div class="brand">ARCHIVE</div><h3>Article en Rupture</h3><div class="price">--,-- €</div></div>
    </a>
    <a href="{P}{slug}/collection-archivee.html" class="product-card">
        <div class="image-wrapper">{img_no_alt(img_key)}</div>
        <div class="info"><div class="brand">ARCHIVE</div><h3>Collection Archivée</h3><div class="price">--,-- €</div></div>
    </a>"""

    body = f"""
    <section class="page-header">
        {img_ok(img_key, f"Collection {name}") if idx % 2 == 0 else img_no_alt(img_key)}
        <div class="content">
            {h1_tag(f"Collection {name}", issues)}
            <p>{desc}</p>
        </div>
    </section>
    <div class="container">
        <div class="breadcrumb">
            <a href="{P}index.html">Accueil</a> <span>›</span> {name}
        </div>
    </div>
    <section class="products-section">
        <div class="container">
            <div class="products-grid">{cards}</div>
        </div>
    </section>"""

    build_page(f"{slug}/index.html", f"{name} — Collection ModeStyle Paris", desc, body, issues)

# ─── PRODUCT PAGES ─────────────────────────────────────

def build_product(cat_slug, cat_name, prod_slug, prod_name, brand, price, img_key, idx):
    issues = seo_issues(idx)

    # Related products
    all_prods = [(cs, ps, pn, br, pr, ik) for cs, _, _, _ in CATEGORIES for ps, pn, br, pr, ik in PRODUCTS.get(cs, [])]
    related = random.sample(all_prods, k=min(4, len(all_prods)))
    related_cards = ""
    for cs, ps, pn, br, pr, ik in related:
        related_cards += f"""
        <a href="{P}{cs}/{ps}.html" class="product-card">
            <div class="image-wrapper">{img_no_alt(ik)}</div>
            <div class="info"><div class="brand">{br}</div><h3>{pn}</h3><div class="price">{"" if pr == 0 else f"{pr},00 €"}</div></div>
        </a>"""
    # BUG: related 404
    related_cards += f"""
    <a href="{P}{cat_slug}/{random.choice(GHOST_PAGES)}.html" class="product-card">
        <div class="image-wrapper">{broken_img()}</div>
        <div class="info"><div class="brand">ARCHIVE</div><h3>Article Similaire</h3><div class="price">--,-- €</div></div>
    </a>"""

    main_img = broken_img() if "broken_img" in issues else (img_no_alt(img_key) if "no_alt" in issues else img_ok(img_key, prod_name))
    thumbs = "".join(img_no_alt(random.choice(list(IMG.keys()))) for _ in range(3))

    body = f"""
    <div class="container">
        <div class="breadcrumb">
            <a href="{P}index.html">Accueil</a> <span>›</span>
            <a href="{P}{cat_slug}/index.html">{cat_name}</a> <span>›</span> {prod_name}
        </div>
    </div>
    <section class="product-detail">
        <div class="container">
            <div class="product-detail-grid">
                <div class="product-gallery">
                    {main_img}
                    <div class="thumbnails">{thumbs}</div>
                </div>
                <div class="product-info">
                    {h1_tag(prod_name, issues)}
                    <div class="brand-name">{brand}</div>
                    <div class="price-block">{"Lire l'article" if price == 0 else f"{price},00 €"}</div>
                    <div class="description">{lorem()}</div>
                    {"" if price == 0 else '<a href="#" class="add-to-cart">Ajouter au Panier</a>'}
                </div>
            </div>
        </div>
    </section>
    <section class="related-products">
        <div class="container">
            <div class="section-title"><h2>Vous Aimerez Aussi</h2><div class="divider"></div></div>
            <div class="products-grid">{related_cards}</div>
        </div>
    </section>"""

    build_page(f"{cat_slug}/{prod_slug}.html", f"{prod_name} | ModeStyle Paris",
               f"{prod_name} — {brand}. Achetez en ligne sur ModeStyle Paris. Livraison gratuite dès 100€.",
               body, issues)

# ─── BLOG PAGES ────────────────────────────────────────

def build_blog_index():
    cards = ""
    for slug, title, cat, excerpt, img_key in BLOG_ARTICLES:
        cards += f"""
        <a href="{P}{slug}.html" class="blog-card">
            <div class="image-wrapper">{img_no_alt(img_key)}</div>
            <div class="content">
                <div class="meta">{cat}</div>
                <h3>{title}</h3>
                <p>{excerpt[:140]}...</p>
                <span class="read-more">Lire la suite</span>
            </div>
        </a>"""
    # 404 blog links
    cards += f"""
    <a href="{P}blog/article-supprime.html" class="blog-card">
        <div class="image-wrapper">{broken_img()}</div>
        <div class="content"><div class="meta">ARCHIVE</div><h3>Les Tendances Oubliées</h3><p>Cet article n'est plus disponible...</p></div>
    </a>"""

    body = f"""
    <section class="page-header">
        {img_no_alt("runway")}
        <div class="content"><h1>Le Journal Mode</h1><p>Tendances, guides et inspirations par nos experts</p></div>
    </section>
    <section class="blog-section">
        <div class="container">
            <div class="blog-grid">{cards}</div>
        </div>
    </section>"""

    build_page("blog/index.html", "Blog Mode — ModeStyle Paris", DUPLICATE_META, body, {"dup_meta", "no_alt"})


def build_blog_article(idx, slug, title, cat, excerpt, img_key):
    issues = set()
    if idx in [0, 4]: issues.add("dup_title")
    if idx in [1, 6]: issues.add("no_h1")
    if idx in [2, 8]: issues.add("empty_title")
    if idx == 3: issues.add("long_title")
    if idx in [5, 9]: issues.add("multi_h1")
    if idx % 2 == 0: issues.add("broken_img"); issues.add("no_alt")
    if idx in [1, 3, 7]: issues.add("bad_canonical")
    if idx in [0, 4, 8]: issues.add("no_meta")

    date = f"{random.randint(1,28)} {random.choice(['janvier','février','mars','avril','mai','juin'])} 2025"
    featured = broken_img() if "broken_img" in issues else img_ok(img_key, title)

    body = f"""
    <section class="article-page">
        <div class="container">
            <div class="article-header">
                <div class="meta">{cat} — {date}</div>
                {h1_tag(title, issues)}
                <p class="subtitle">{excerpt}</p>
            </div>
            {featured}
            <div class="article-content">
                {lorem()}
                <h2>L'Essentiel à Retenir</h2>
                {lorem()}
                <blockquote>« La mode se démode, le style jamais. » — Coco Chanel</blockquote>
                {lorem()}
                <h2>Nos Recommandations</h2>
                {lorem()}
                <p><a href="{P}{random.choice(GHOST_PAGES)}.html">Découvrir nos sélections associées</a></p>
                <p><a href="{P}blog/{random.choice(GHOST_PAGES)}.html">Lire notre guide complémentaire</a></p>
            </div>
        </div>
    </section>"""

    build_page(f"{slug}.html", f"{title} | Journal ModeStyle Paris",
               f"{title} — {excerpt[:100]}", body, issues)

# ─── EXTRA PAGES ────────────────────────────────────────

def build_extra(idx, slug, title, img_key):
    issues = set()
    if idx % 4 == 0: issues.add("dup_title")
    if idx % 5 == 0: issues.add("no_h1")
    if idx % 3 == 0: issues.add("broken_img")
    if idx % 2 == 0: issues.add("no_alt")
    if idx % 6 == 0: issues.add("bad_canonical")
    if idx % 4 == 1: issues.add("no_meta")
    if idx % 5 == 2: issues.add("multi_h1")

    header_img = broken_img() if "broken_img" in issues else (img_no_alt(img_key) if "no_alt" in issues else img_ok(img_key, title))

    body = f"""
    <section class="page-header">
        {header_img}
        <div class="content">
            {h1_tag(title, issues)}
            <p>Découvrez notre sélection exclusive chez ModeStyle Paris.</p>
        </div>
    </section>
    <div class="container">
        <div class="breadcrumb"><a href="{P}index.html">Accueil</a> <span>›</span> {title}</div>
    </div>
    <section class="products-section">
        <div class="container">
            {lorem()}
            {img_no_alt(img_key) if "no_alt" in issues else img_ok(img_key, title)}
            {lorem()}
            <p style="margin-top:32px">{ghost_links(2)}</p>
        </div>
    </section>"""

    build_page(f"{slug}.html", f"{title} | ModeStyle Paris",
               f"{title} — Découvrez nos sélections mode exclusives chez ModeStyle Paris.",
               body, issues)

# ═══════════════════════════════════════════════════════
# MAIN BUILD
# ═══════════════════════════════════════════════════════

print("🔨 Building ModeStyle Paris...")

# Homepage
build_homepage()

# Categories
for i, (slug, name, img_key, desc) in enumerate(CATEGORIES):
    build_category(i, slug, name, img_key, desc)

# Products
page_idx = 11
for cat_slug, cat_name, _, _ in CATEGORIES:
    for prod_slug, prod_name, brand, price, img_key in PRODUCTS.get(cat_slug, []):
        build_product(cat_slug, cat_name, prod_slug, prod_name, brand, price, img_key, page_idx)
        page_idx += 1

# Blog
build_blog_index()
page_idx += 1
for i, (slug, title, cat, excerpt, img_key) in enumerate(BLOG_ARTICLES):
    build_blog_article(i, slug, title, cat, excerpt, img_key)
    page_idx += 1

# Extra pages
for i, (slug, title, img_key) in enumerate(EXTRA_PAGES):
    if page_idx > 110:
        break
    build_extra(i, slug, title, img_key)
    page_idx += 1

# ═══════════════════════════════════════════════════════
# ROBOTS.TXT & SITEMAP.XML
# ═══════════════════════════════════════════════════════

write_file("robots.txt", f"""User-agent: *
Allow: /

Disallow: /admin/
Disallow: /api/
Disallow: /tmp/
Disallow: /private/
Disallow: /checkout/
Disallow: /cart/

Sitemap: {DOMAIN}/sitemap.xml
""")

today = datetime.date.today().isoformat()
entries = []
for p in all_pages:
    prio = "1.0" if p == "index.html" else "0.8" if p.endswith("/index.html") else "0.6"
    freq = "daily" if p == "index.html" else "weekly"
    entries.append(f"""  <url>
    <loc>{DOMAIN}/{p}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

write_file("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"".join(entries)}
</urlset>""")

print(f"✅ {page_idx} pages + robots.txt + sitemap.xml")
print(f"   Total HTML files: {len(all_pages)}")
print(f"   Ghost pages (404): {len(GHOST_PAGES)}")
