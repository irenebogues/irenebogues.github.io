from pathlib import Path
from textwrap import dedent


NAME = "Irene Bogues"
TITLE = "Creative operator, project builder, and Python learner"
INTRO = "I help ideas become organized, polished, and ready to share."
GITHUB_URL = "https://github.com/irenebogues"
INSTAGRAM_URL = "https://www.instagram.com/ireneluvsrain/"
LINKEDIN_URL = "https://www.linkedin.com/in/irenebogues/"
CALENDLY_URL = "https://calendly.com/irenebogues/"

ABOUT = (
    "I bring together operations, web projects, creative coordination, and a "
    "growing Python practice. This site collects the work I have supported, "
    "the projects I am learning from, and the next things I want to build."
)

PROJECTS = [
    {
        "name": "Mingma Sherpa Landscaping",
        "type": "Current project",
        "url": "https://www.mingmasherpalandscaping.com/",
        "description": "A service-focused website for landscaping work and customer inquiries.",
    },
    {
        "name": "Arkadiy Barber Shop",
        "type": "Past project",
        "url": "https://arkadiybarbershop.com/",
        "description": "A polished web presence for a local barber shop and its clients.",
    },
    {
        "name": "LS Therapeutic Touch",
        "type": "Current project",
        "url": "https://lstherapeutictouch.com/",
        "description": "A calm, wellness-centered website for therapeutic services.",
    },
    {
        "name": "Gotham Life Coach",
        "type": "Past project",
        "url": "https://gothamlifecoach.com/",
        "description": "A coaching website built around trust, clarity, and client connection.",
    },
    {
        "name": "Heat &amp; Stir",
        "type": "Past project",
        "url": "https://heatandstir.com/",
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
        "file": "assets/hero-workspace.png",
        "alt": "A bright desk workspace with a laptop, notebook, plants, and coffee.",
        "caption": "Workspace energy",
    },
    {
        "file": "assets/learning-notes.png",
        "alt": "A notebook with project notes beside a laptop and coffee mug.",
        "caption": "Notes, ideas, next steps",
    },
    {
        "file": "assets/project-workspace.png",
        "alt": "A laptop workspace showing an abstract project screen with plants and notebooks.",
        "caption": "Project days",
    },
]


def build_projects():
    html = ""

    for project in PROJECTS:
        html += f"""
        <article class="project-card">
            <p class="project-type">{project["type"]}</p>
            <h3>{project["name"]}</h3>
            <p>{project["description"]}</p>
            <a class="project-link" href="{project["url"]}" target="_blank" rel="noreferrer">Visit project</a>
        </article>
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
        <a class="photo-link" href="{INSTAGRAM_URL}" target="_blank" rel="noreferrer">
            <figure class="photo-card">
                <img src="{photo["file"]}" alt="{photo["alt"]}">
                <figcaption>{photo["caption"]}</figcaption>
            </figure>
        </a>
        """

    return html


def build_html():
    return dedent(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{NAME} | Personal Website</title>
            <link rel="stylesheet" href="styles.css">
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
                    <aside class="hero-panel" aria-label="Highlights">
                        <p>Portfolio focus</p>
                        <strong>Web projects, creative systems, and practical tools.</strong>
                        <span>Currently learning Python and building a growing project library.</span>
                    </aside>
                </section>

                <section class="section two-column" id="about">
                    <div>
                        <p class="eyebrow">About</p>
                        <h2>Organized, creative, and always building.</h2>
                    </div>
                    <p>{ABOUT}</p>
                </section>

                <section class="section" id="projects">
                    <div class="section-heading">
                        <p class="eyebrow">Projects</p>
                        <h2>Past and current projects</h2>
                        <p>Selected live sites and projects I have supported or continue to shape.</p>
                    </div>
                    <div class="project-grid">
                        {build_projects()}
                    </div>
                </section>

                <section class="section photos" id="photos">
                    <div class="photos-header">
                        <div>
                            <p class="eyebrow">Photos</p>
                            <h2>Follow the visual diary.</h2>
                            <p>For fresh photos, food moments, city details, and day-to-day project life, follow me on Instagram.</p>
                        </div>
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
                    <p class="eyebrow">Contact</p>
                    <h2>Let's connect.</h2>
                    <p>Have a project, idea, or collaboration in mind? Schedule a meeting and we can talk through the next step.</p>
                    <a class="button primary contact-button" href="{CALENDLY_URL}" target="_blank" rel="noreferrer">Schedule a meeting</a>
                    <p>GitHub: <a href="{GITHUB_URL}">{GITHUB_URL}</a></p>
                    <p>Instagram: <a href="{INSTAGRAM_URL}">{INSTAGRAM_URL}</a></p>
                    <p>LinkedIn: <a href="{LINKEDIN_URL}">{LINKEDIN_URL}</a></p>
                    <p>Calendly: <a href="{CALENDLY_URL}">{CALENDLY_URL}</a></p>
                </section>
            </main>

            <footer>
                <p>Made with Python by {NAME}.</p>
            </footer>
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
            background: #f7f8f4;
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
            color: #16353c;
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
            color: #31424d;
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
                    rgba(247, 248, 244, 0.98) 0%,
                    rgba(247, 248, 244, 0.9) 36%,
                    rgba(247, 248, 244, 0.45) 68%,
                    rgba(247, 248, 244, 0.14) 100%
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
            padding: 24px;
            color: #ffffff;
            background: rgba(23, 33, 43, 0.88);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 8px;
            box-shadow: 0 24px 70px rgba(23, 33, 43, 0.22);
        }

        .hero-panel p {
            margin-bottom: 8px;
            color: #9ce7dc;
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
            color: #dbe7e5;
        }

        .eyebrow {
            margin: 0 0 12px;
            color: #0f766e;
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
            color: #31424d;
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
            box-shadow: 0 14px 30px rgba(23, 33, 43, 0.16);
        }

        .primary {
            color: #ffffff;
            background: #0f766e;
        }

        .secondary {
            color: #17212b;
            background: #ffffff;
            border: 1px solid rgba(23, 33, 43, 0.18);
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
            color: #52616b;
            font-size: 1.05rem;
        }

        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 18px;
        }

        .project-card {
            min-height: 240px;
            display: flex;
            flex-direction: column;
            padding: 24px;
            background: linear-gradient(180deg, #ffffff 0%, #f8fbfa 100%);
            border: 1px solid rgba(23, 33, 43, 0.12);
            border-radius: 8px;
            box-shadow: 0 18px 50px rgba(23, 33, 43, 0.08);
        }

        .project-card p {
            margin-bottom: 18px;
        }

        .project-type {
            width: fit-content;
            padding: 4px 10px;
            color: #7a321e;
            background: #ffe3d4;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        .project-link {
            margin-top: auto;
            color: #0f766e;
            font-weight: 700;
            text-decoration: none;
        }

        .photos {
            background: #173c43;
            color: #ffffff;
        }

        .photos .eyebrow {
            color: #9ce7dc;
        }

        .photos-header {
            display: flex;
            align-items: end;
            justify-content: space-between;
            gap: 28px;
            margin-bottom: 30px;
        }

        .photos-header p {
            max-width: 680px;
            color: #dbe7e5;
            font-size: 1.06rem;
        }

        .instagram-button {
            flex: 0 0 auto;
            color: #17212b;
            background: #ffd3bf;
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
            aspect-ratio: 4 / 3;
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
            color: #0f766e;
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
                linear-gradient(135deg, rgba(15, 118, 110, 0.96), rgba(23, 33, 43, 0.98));
        }

        .contact a {
            color: #ffe3d4;
            font-weight: 700;
            overflow-wrap: anywhere;
        }

        .contact p {
            max-width: 760px;
        }

        .contact-button {
            margin: 12px 0 26px;
            color: #17212b;
            background: #ffffff;
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
                        rgba(247, 248, 244, 0.98) 0%,
                        rgba(247, 248, 244, 0.9) 58%,
                        rgba(247, 248, 244, 0.5) 100%
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
            .photo-grid {
                grid-template-columns: 1fr;
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


def main():
    project_folder = Path(__file__).parent

    (project_folder / "index.html").write_text(build_html() + "\n", encoding="utf-8")
    (project_folder / "styles.css").write_text(build_css() + "\n", encoding="utf-8")

    print("Website built.")
    print("Open index.html in your browser to see it.")


main()
