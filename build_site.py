from pathlib import Path
import json
from textwrap import dedent, indent


NAME = "Irene Bogues"
SITE_URL = "https://irenebogues.github.io"
SITE_TITLE = "Irene Bogues | Executive Assistant, Creative Operator and Project Builder"
TITLE = "Executive assistant, creative operator, project builder, and Python learner"
INTRO = "I help ideas become organized, polished, and ready to share."
SEO_DESCRIPTION = (
    "Irene Bogues is an Executive Assistant to the Chairman of Chelsea Piers, "
    "a creative operator, project builder, and Python learner based in New York. "
    "Explore her projects, photography, writing, and contact links."
)
SEO_KEYWORDS = (
    "Irene Bogues, Irene Zanoria, Executive Assistant, Chelsea Piers, "
    "creative operator, project builder, Python learner, New York, Cebu City"
)
GOOGLE_SITE_VERIFICATION = "93SpTpZzzP8xeXHlKrow4UxxrvBSD7tYQ7vtGSar7Fs"
OG_IMAGE = f"{SITE_URL}/assets/hero-workspace.png"
GITHUB_URL = "https://github.com/irenebogues"
INSTAGRAM_URL = "https://www.instagram.com/ireneluvsrain/"
LINKEDIN_URL = "https://www.linkedin.com/in/irenebogues/"
CALENDLY_URL = "https://calendly.com/irenebogues/meeting-with-irene"
LAST_UPDATED = "2026-06-13"

SOCIAL_LINKS = [
    {
        "name": "GitHub",
        "url": GITHUB_URL,
        "domain": "github.com",
    },
    {
        "name": "Instagram",
        "url": INSTAGRAM_URL,
        "domain": "instagram.com",
    },
    {
        "name": "LinkedIn",
        "url": LINKEDIN_URL,
        "domain": "linkedin.com",
    },
    {
        "name": "Calendly",
        "url": CALENDLY_URL,
        "domain": "calendly.com",
    },
]

ABOUT = (
    "Hi, I’m Irene — Executive Assistant to the Chairman of Chelsea Piers. "
    "Originally from Cebu City and now based in New York, I bring a global "
    "perspective, a sharp eye for detail, and a deep love of storytelling to "
    "everything I do. My work lives at the intersection of strategy, creativity, "
    "and execution — building systems, organizing complex projects, solving "
    "problems, and helping ideas become real. I’m passionate about adventure, "
    "photography, writing with heart, and creating work that feels both useful "
    "and deeply human. I’m drawn to the beautiful, the brave, and the practical "
    "— the things that move people forward."
)

PROJECTS = [
    {
        "name": "Mingma Sherpa Landscaping",
        "url": "https://www.mingmasherpalandscaping.com/",
        "image": "assets/project-mingma.png",
        "alt": "Screenshot of the Mingma Sherpa Landscaping website.",
        "description": "A service-focused website for landscaping work and customer inquiries.",
    },
    {
        "name": "Arkadiy Barber Shop",
        "url": "https://arkadiybarbershop.com/",
        "image": "assets/project-arkadiy.png",
        "alt": "Screenshot of the Arkadiy Barber Shop website.",
        "description": "A polished web presence for a local barber shop and its clients.",
    },
    {
        "name": "LS Therapeutic Touch",
        "url": "https://lstherapeutictouch.com/",
        "image": "assets/project-ls-therapeutic.png",
        "alt": "Screenshot of the LS Therapeutic Touch website.",
        "description": "A calm, wellness-centered website for therapeutic services.",
    },
    {
        "name": "Gotham Life Coach",
        "url": "https://gothamlifecoach.com/",
        "image": "assets/project-gotham.png",
        "alt": "Screenshot of the Gotham Life Coach website.",
        "description": "A coaching website built around trust, clarity, and client connection.",
    },
    {
        "name": "Heat &amp; Stir",
        "url": "https://heatandstir.com/",
        "image": "assets/project-heat-stir.png",
        "alt": "Screenshot of the Heat and Stir website.",
        "description": "A food and lifestyle project with a warm, memorable web presence.",
    },
]

LEARNING_GOALS = [
    "Write clearer Python code",
    "Use Git and GitHub with confidence",
    "Build small projects that grow over time",
]

PHOTOS = [
    {
        "file": "assets/instagram-latest-1.jpg",
        "alt": "Recent Instagram post thumbnail showing a nighttime city crowd.",
        "caption": "City night",
        "url": "https://www.instagram.com/reel/DZbl_uRtk97/",
    },
    {
        "file": "assets/instagram-latest-2.jpg",
        "alt": "Recent Instagram post thumbnail showing a South Africa travel view.",
        "caption": "South Africa travel",
        "url": "https://www.instagram.com/reel/DZSNytZCVXK/",
    },
    {
        "file": "assets/instagram-latest-3.jpg",
        "alt": "Recent Instagram post thumbnail showing a scenic travel moment.",
        "caption": "Traveler notes",
        "url": "https://www.instagram.com/reel/DZM54P2iENM/",
    },
    {
        "file": "assets/instagram-latest-4.jpg",
        "alt": "Recent Instagram post thumbnail showing a safari scene.",
        "caption": "Safari rules",
        "url": "https://www.instagram.com/reel/DZFa2mbiEqt/",
    },
    {
        "file": "assets/instagram-latest-5.jpg",
        "alt": "Recent Instagram post thumbnail showing a South Africa safari adventure.",
        "caption": "Epic safari",
        "url": "https://www.instagram.com/reel/DZDkEI3CrXO/",
    },
    {
        "file": "assets/instagram-latest-6.jpg",
        "alt": "Recent Instagram post thumbnail showing wild elephants.",
        "caption": "Elephant encounter",
        "url": "https://www.instagram.com/p/DZDj3EileLS/",
    },
]


def build_projects():
    html = ""

    for project in PROJECTS:
        html += f"""
        <a class="project-card" href="{project["url"]}" target="_blank" rel="noreferrer" aria-label="Visit {project["name"]}">
            <img src="{project["image"]}" alt="{project["alt"]}">
            <span class="project-overlay">
                <strong>{project["name"]}</strong>
            </span>
        </a>
        """

    return html


def build_goals():
    html = ""

    for goal in LEARNING_GOALS:
        html += f"<li>{goal}</li>"

    return html


def build_photos():
    html = ""

    for photo in PHOTOS:
        html += f"""
        <a class="photo-link" href="{photo["url"]}" target="_blank" rel="noreferrer">
            <figure class="photo-card">
                <img src="{photo["file"]}" alt="{photo["alt"]}">
                <figcaption>{photo["caption"]}</figcaption>
            </figure>
        </a>
        """

    return html


def build_social_links():
    html = ""

    for link in SOCIAL_LINKS:
        favicon_url = f"https://www.google.com/s2/favicons?sz=64&domain={link['domain']}"
        html += f"""
        <a class="social-link" href="{link["url"]}" target="_blank" rel="noreferrer" aria-label="Open {link["name"]}">
            <img src="{favicon_url}" alt="" aria-hidden="true">
            <span>{link["name"]}</span>
        </a>
        """

    return html


def build_structured_data():
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Person",
                "@id": f"{SITE_URL}/#person",
                "name": NAME,
                "alternateName": "Irene Zanoria",
                "url": f"{SITE_URL}/",
                "image": OG_IMAGE,
                "jobTitle": "Executive Assistant to the Chairman",
                "worksFor": {
                    "@type": "Organization",
                    "name": "Chelsea Piers",
                },
                "homeLocation": {
                    "@type": "Place",
                    "name": "New York, NY",
                },
                "birthPlace": {
                    "@type": "Place",
                    "name": "Cebu City, Philippines",
                },
                "sameAs": [GITHUB_URL, INSTAGRAM_URL, LINKEDIN_URL],
                "knowsAbout": [
                    "Executive assistance",
                    "Project coordination",
                    "Creative operations",
                    "Photography",
                    "Writing",
                    "Python",
                ],
                "description": SEO_DESCRIPTION,
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": f"{SITE_URL}/",
                "name": NAME,
                "description": SEO_DESCRIPTION,
                "publisher": {
                    "@id": f"{SITE_URL}/#person",
                },
            },
        ],
    }

    return indent(json.dumps(data, ensure_ascii=False, indent=4), " " * 12)


def build_html():
    return dedent(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{SITE_TITLE}</title>
            <meta name="description" content="{SEO_DESCRIPTION}">
            <meta name="keywords" content="{SEO_KEYWORDS}">
            <meta name="author" content="{NAME}">
            <meta name="robots" content="index, follow">
            <meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">
            <link rel="canonical" href="{SITE_URL}/">
            <meta property="og:type" content="website">
            <meta property="og:title" content="{SITE_TITLE}">
            <meta property="og:description" content="{SEO_DESCRIPTION}">
            <meta property="og:url" content="{SITE_URL}/">
            <meta property="og:site_name" content="{NAME}">
            <meta property="og:image" content="{OG_IMAGE}">
            <meta name="twitter:card" content="summary_large_image">
            <meta name="twitter:title" content="{SITE_TITLE}">
            <meta name="twitter:description" content="{SEO_DESCRIPTION}">
            <meta name="twitter:image" content="{OG_IMAGE}">
            <link rel="stylesheet" href="styles.css">
            <script type="application/ld+json">
{build_structured_data()}
            </script>
        </head>
        <body>
            <header class="site-header">
                <a class="logo" href="#top">{NAME}</a>
                <nav>
                    <a href="#about">About</a>
                    <a href="#projects">Projects</a>
                    <a href="#photos">Photos</a>
                    <a href="#contact">Contact</a>
                </nav>
            </header>

            <main id="top">
                <section class="hero">
                    <div class="hero-content">
                        <p class="eyebrow">{TITLE}</p>
                        <h1>{NAME}</h1>
                        <p class="intro">{INTRO}</p>
                        <div class="hero-actions">
                            <a class="button primary" href="#projects">View projects</a>
                            <a class="button secondary" href="{CALENDLY_URL}">Schedule a meeting</a>
                            <a class="button secondary" href="{LINKEDIN_URL}">LinkedIn</a>
                        </div>
                    </div>
                    <a class="hero-panel" href="{GITHUB_URL}" target="_blank" rel="noreferrer" aria-label="Open Irene's GitHub portfolio">
                        <p>Portfolio focus</p>
                        <strong>Web projects, creative systems, and practical tools.</strong>
                        <span>Currently learning Python and building a growing project library.</span>
                    </a>
                </section>

                <section class="section two-column" id="about">
                    <div>
                        <p class="eyebrow">About</p>
                        <h2>AI Native, EA to Ultra High Net Worth Individual and always building, traveling.</h2>
                    </div>
                    <p>{ABOUT}</p>
                </section>

                <section class="section" id="projects">
                    <div class="section-heading">
                        <p class="eyebrow">Projects</p>
                        <h2>Here are a few things I've done recently</h2>
                    </div>
                    <div class="project-grid">
                        {build_projects()}
                    </div>
                </section>

                <section class="section photos" id="photos">
                    <div class="photos-header">
                        <p class="eyebrow">Photos</p>
                        <a class="button instagram-button" href="{INSTAGRAM_URL}" target="_blank" rel="noreferrer">Open @ireneluvsrain</a>
                    </div>
                    <div class="photo-grid">
                        {build_photos()}
                    </div>
                </section>

                <section class="section learning">
                    <div>
                        <p class="eyebrow">Learning Goals</p>
                        <h2>What I want to get better at</h2>
                    </div>
                    <ul>
                        {build_goals()}
                    </ul>
                </section>

                <section class="section contact" id="contact">
                    <div class="contact-layout">
                        <div class="contact-copy">
                            <p class="eyebrow">Contact</p>
                            <h2>Let's plan the next step.</h2>
                            <p>Have a project, idea, or collaboration in mind? Pick a time and we can talk through what you need, what is already working, and what should happen next.</p>
                            <a class="button primary contact-button" href="{CALENDLY_URL}" target="_blank" rel="noreferrer">Schedule a meeting</a>
                            <div class="social-links" aria-label="Social links">
                                {build_social_links()}
                            </div>
                        </div>
                        <div class="calendly-card">
                            <p class="eyebrow">Book Time</p>
                            <h3>Meeting with Irene</h3>
                            <!-- Calendly inline widget begin -->
                            <div class="calendly-inline-widget" data-url="{CALENDLY_URL}" style="min-width:320px;height:520px;"></div>
                            <!-- Calendly inline widget end -->
                        </div>
                    </div>
                </section>
            </main>

            <footer>
                <p>Made with Python by {NAME}.</p>
            </footer>
            <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
        </body>
        </html>
        """
    ).strip()


def build_css():
    return dedent(
        """
        * {
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            color: #17212b;
            background: #f4f6ef;
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
        }

        a {
            color: inherit;
        }

        .site-header {
            position: fixed;
            top: 0;
            left: 0;
            z-index: 10;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            padding: 18px 6vw;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(23, 33, 43, 0.12);
        }

        .logo {
            color: #26351f;
            font-weight: 700;
            text-decoration: none;
        }

        nav {
            display: flex;
            gap: 18px;
            flex-wrap: wrap;
            font-size: 0.95rem;
        }

        nav a {
            color: #36442b;
            text-decoration: none;
        }

        .hero {
            min-height: 84vh;
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(260px, 360px);
            align-items: center;
            gap: 36px;
            padding: 120px 6vw 80px;
            background:
                linear-gradient(
                    90deg,
                    rgba(244, 246, 239, 0.98) 0%,
                    rgba(244, 246, 239, 0.9) 36%,
                    rgba(244, 246, 239, 0.46) 68%,
                    rgba(244, 246, 239, 0.16) 100%
                ),
                url("assets/hero-workspace.png");
            background-size: cover;
            background-position: center;
        }

        .hero-content {
            width: min(620px, 100%);
        }

        .hero-panel {
            align-self: end;
            display: block;
            padding: 24px;
            color: #ffffff;
            background: rgba(38, 53, 31, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 8px;
            box-shadow: 0 24px 70px rgba(23, 33, 43, 0.22);
            text-decoration: none;
            transition: transform 160ms ease, box-shadow 160ms ease;
        }

        .hero-panel:hover {
            transform: translateY(-2px);
            box-shadow: 0 28px 76px rgba(23, 33, 43, 0.28);
        }

        .hero-panel p {
            margin-bottom: 8px;
            color: #d6e6b6;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        .hero-panel strong {
            display: block;
            margin-bottom: 10px;
            font-size: 1.25rem;
            line-height: 1.25;
        }

        .hero-panel span {
            color: #edf3df;
        }

        .eyebrow {
            margin: 0 0 12px;
            color: #596a3d;
            font-size: 0.92rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        h1,
        h2,
        h3,
        p {
            margin-top: 0;
        }

        h1 {
            margin-bottom: 18px;
            font-size: 5.2rem;
            line-height: 1;
            letter-spacing: 0;
        }

        h2 {
            margin-bottom: 18px;
            font-size: 3rem;
            line-height: 1.1;
            letter-spacing: 0;
        }

        h3 {
            margin-bottom: 10px;
            font-size: 1.2rem;
            letter-spacing: 0;
        }

        .intro {
            max-width: 520px;
            color: #36442b;
            font-size: 1.25rem;
        }

        .hero-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 28px;
        }

        .button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 44px;
            padding: 10px 18px;
            border-radius: 8px;
            font-weight: 700;
            text-decoration: none;
            transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
        }

        .button:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 30px rgba(38, 53, 31, 0.18);
        }

        .primary {
            color: #ffffff;
            background: #596a3d;
        }

        .secondary {
            color: #17212b;
            background: #ffffff;
            border: 1px solid rgba(89, 106, 61, 0.28);
        }

        .section {
            padding: 76px 6vw;
        }

        .two-column {
            display: grid;
            grid-template-columns: minmax(0, 0.9fr) minmax(280px, 1.1fr);
            gap: 48px;
            background: #ffffff;
        }

        .two-column p,
        .contact p {
            font-size: 1.08rem;
        }

        .section-heading {
            max-width: 720px;
            margin-bottom: 28px;
        }

        .section-heading p {
            max-width: 680px;
            color: #526049;
            font-size: 1.05rem;
        }

        .project-grid {
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: 16px;
        }

        .project-card {
            position: relative;
            grid-column: span 3;
            min-height: 340px;
            display: block;
            overflow: hidden;
            color: #ffffff;
            background: #26351f;
            border: 1px solid rgba(89, 106, 61, 0.18);
            border-radius: 8px;
            box-shadow: 0 18px 50px rgba(38, 53, 31, 0.09);
            text-decoration: none;
            isolation: isolate;
        }

        .project-card:first-child {
            grid-column: span 6;
            min-height: 430px;
        }

        .project-card img {
            display: block;
            width: 100%;
            height: 100%;
            min-height: inherit;
            object-fit: cover;
            transition: transform 500ms ease;
        }

        .project-card:hover img {
            transform: scale(1.04);
        }

        .project-overlay {
            position: absolute;
            inset: auto 0 0;
            z-index: 1;
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;
            padding: 22px;
            background: linear-gradient(180deg, rgba(38, 53, 31, 0), rgba(38, 53, 31, 0.9));
        }

        .project-overlay strong {
            font-size: 1.35rem;
            line-height: 1.15;
            text-align: left;
        }

        .photos {
            background: #26351f;
            color: #ffffff;
        }

        .photos .eyebrow {
            color: #d6e6b6;
        }

        .photos-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 28px;
            margin-bottom: 30px;
        }

        .photos-header .eyebrow {
            margin-bottom: 0;
        }

        .instagram-button {
            flex: 0 0 auto;
            color: #17212b;
            background: #e5b76c;
        }

        .photo-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .photo-link {
            color: inherit;
            text-decoration: none;
        }

        .photo-card {
            margin: 0;
            overflow: hidden;
            background: #ffffff;
            color: #17212b;
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 8px;
            box-shadow: 0 22px 60px rgba(0, 0, 0, 0.18);
        }

        .photo-card img {
            display: block;
            width: 100%;
            aspect-ratio: 1 / 1;
            object-fit: cover;
        }

        .photo-card figcaption {
            padding: 14px 16px 16px;
            font-weight: 700;
        }

        .learning {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(280px, 1fr);
            gap: 48px;
            color: #17212b;
            background: #ffffff;
        }

        .learning .eyebrow {
            color: #596a3d;
        }

        .learning ul {
            margin: 0;
            padding-left: 24px;
            font-size: 1.08rem;
        }

        .learning li + li {
            margin-top: 12px;
        }

        .contact {
            color: #ffffff;
            background:
                linear-gradient(135deg, rgba(89, 106, 61, 0.98), rgba(38, 53, 31, 0.98));
        }

        .contact a {
            color: #f1d48b;
            font-weight: 700;
            overflow-wrap: anywhere;
        }

        .contact-layout {
            display: grid;
            grid-template-columns: minmax(0, 0.85fr) minmax(320px, 1.15fr);
            gap: 36px;
            align-items: start;
        }

        .contact-copy p {
            max-width: 760px;
        }

        .social-links {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 18px;
        }

        .social-link {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            min-height: 42px;
            padding: 9px 13px;
            color: #17212b;
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(241, 212, 139, 0.38);
            border-radius: 8px;
            font-weight: 700;
            text-decoration: none;
            transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
        }

        .social-link:hover {
            transform: translateY(-2px);
            background: #ffffff;
            box-shadow: 0 14px 30px rgba(23, 33, 43, 0.18);
        }

        .social-link img {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }

        .contact-button {
            margin: 12px 0 26px;
            color: #17212b;
            background: #ffffff;
        }

        .calendly-card {
            min-width: 0;
            padding: 18px;
            color: #17212b;
            background: #f8fbf2;
            border: 1px solid rgba(255, 255, 255, 0.28);
            border-radius: 8px;
            box-shadow: 0 24px 80px rgba(23, 33, 43, 0.26);
        }

        .calendly-card .eyebrow {
            color: #596a3d;
        }

        .calendly-card h3 {
            color: #26351f;
        }

        .calendly-inline-widget {
            width: 100%;
            overflow: hidden;
            background: #ffffff;
            border-radius: 8px;
        }

        footer {
            padding: 24px 6vw;
            color: #ffffff;
            background: #17212b;
        }

        footer p {
            margin: 0;
        }

        @media (max-width: 760px) {
            .site-header {
                position: static;
                align-items: flex-start;
                flex-direction: column;
                padding: 16px 5vw;
            }

            .hero {
                min-height: 70vh;
                grid-template-columns: 1fr;
                padding: 72px 5vw 56px;
                background:
                    linear-gradient(
                        180deg,
                        rgba(244, 246, 239, 0.98) 0%,
                        rgba(244, 246, 239, 0.9) 58%,
                        rgba(244, 246, 239, 0.5) 100%
                    ),
                    url("assets/hero-workspace.png");
                background-size: cover;
                background-position: center right;
            }

            .section {
                padding: 56px 5vw;
            }

            .two-column,
            .learning,
            .project-grid,
            .photo-grid,
            .contact-layout {
                grid-template-columns: 1fr;
            }

            .project-card,
            .project-card:first-child {
                grid-column: auto;
                min-height: 280px;
            }

            .project-overlay {
                align-items: flex-start;
                flex-direction: column;
            }

            .project-overlay strong {
                text-align: left;
            }

            .calendly-inline-widget {
                min-width: 0 !important;
                height: 460px !important;
            }

            .photos-header {
                align-items: flex-start;
                flex-direction: column;
            }

            h1 {
                font-size: 3rem;
            }

            h2 {
                font-size: 2rem;
            }
        }
        """
    ).strip()


def build_robots_txt():
    return dedent(
        f"""
        User-agent: *
        Allow: /

        Sitemap: {SITE_URL}/sitemap.xml
        """
    ).strip()


def build_sitemap_xml():
    return dedent(
        f"""\
        <?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url>
                <loc>{SITE_URL}/</loc>
                <lastmod>{LAST_UPDATED}</lastmod>
                <changefreq>monthly</changefreq>
                <priority>1.0</priority>
            </url>
        </urlset>
        """
    ).strip()


def main():
    project_folder = Path(__file__).parent

    (project_folder / "index.html").write_text(build_html() + "\n", encoding="utf-8")
    (project_folder / "styles.css").write_text(build_css() + "\n", encoding="utf-8")
    (project_folder / "robots.txt").write_text(build_robots_txt() + "\n", encoding="utf-8")
    (project_folder / "sitemap.xml").write_text(build_sitemap_xml() + "\n", encoding="utf-8")

    print("Website built.")
    print("Open index.html in your browser to see it.")


main()
