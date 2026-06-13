from pathlib import Path
from textwrap import dedent


NAME = "Irene Bogues"
TITLE = "Python learner and creative builder"
INTRO = "I am learning Python one small project at a time."
EMAIL = "hello@example.com"
GITHUB_URL = "https://github.com/irenebogues"
INSTAGRAM_URL = "https://www.instagram.com/ireneluvsrain/"
LINKEDIN_URL = "https://www.linkedin.com/in/irenebogues/"

ABOUT = (
    "I started with beginner Python projects and I am building my skills step by "
    "step. This website is a place to share what I make, what I learn, and what "
    "I want to try next."
)

PROJECTS = [
    {
        "name": "Number Guessing Game",
        "description": "A simple Python game that uses input, variables, loops, and if statements.",
    },
    {
        "name": "Personal Website",
        "description": "A website generated with Python and published with GitHub.",
    },
    {
        "name": "Future AI Agent",
        "description": "A growing assistant project that can remember notes and help with small tasks.",
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
        "caption": "My learning space",
    },
    {
        "file": "assets/learning-notes.png",
        "alt": "A notebook with project notes beside a laptop and coffee mug.",
        "caption": "Notes and ideas",
    },
    {
        "file": "assets/project-workspace.png",
        "alt": "A laptop workspace showing an abstract project screen with plants and notebooks.",
        "caption": "Projects in progress",
    },
]


def build_projects():
    html = ""

    for project in PROJECTS:
        html += f"""
        <article class="project-card">
            <h3>{project["name"]}</h3>
            <p>{project["description"]}</p>
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
        <figure class="photo-card">
            <img src="{photo["file"]}" alt="{photo["alt"]}">
            <figcaption>{photo["caption"]}</figcaption>
        </figure>
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
                            <a class="button secondary" href="{INSTAGRAM_URL}">Instagram</a>
                            <a class="button secondary" href="{LINKEDIN_URL}">LinkedIn</a>
                        </div>
                    </div>
                </section>

                <section class="section two-column" id="about">
                    <div>
                        <p class="eyebrow">About</p>
                        <h2>Building my skills with real projects.</h2>
                    </div>
                    <p>{ABOUT}</p>
                </section>

                <section class="section" id="projects">
                    <div class="section-heading">
                        <p class="eyebrow">Projects</p>
                        <h2>What I am working on</h2>
                    </div>
                    <div class="project-grid">
                        {build_projects()}
                    </div>
                </section>

                <section class="section photos" id="photos">
                    <div class="section-heading">
                        <p class="eyebrow">Photos</p>
                        <h2>A few project moments</h2>
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
                    <p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
                    <p>GitHub: <a href="{GITHUB_URL}">{GITHUB_URL}</a></p>
                    <p>Instagram: <a href="{INSTAGRAM_URL}">{INSTAGRAM_URL}</a></p>
                    <p>LinkedIn: <a href="{LINKEDIN_URL}">{LINKEDIN_URL}</a></p>
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
            background: #f6f3ee;
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
            background: rgba(255, 255, 255, 0.82);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(23, 33, 43, 0.12);
        }

        .logo {
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
            text-decoration: none;
        }

        .hero {
            min-height: 78vh;
            display: flex;
            align-items: center;
            padding: 120px 6vw 80px;
            background:
                linear-gradient(
                    90deg,
                    rgba(246, 243, 238, 0.98) 0%,
                    rgba(246, 243, 238, 0.88) 34%,
                    rgba(246, 243, 238, 0.42) 62%,
                    rgba(246, 243, 238, 0.12) 100%
                ),
                url("assets/hero-workspace.png");
            background-size: cover;
            background-position: center;
        }

        .hero-content {
            width: min(620px, 100%);
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
            font-size: clamp(3rem, 6vw, 5.8rem);
            line-height: 1;
            letter-spacing: 0;
        }

        h2 {
            margin-bottom: 18px;
            font-size: clamp(2rem, 4vw, 3.2rem);
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

        .project-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .project-card {
            min-height: 190px;
            padding: 24px;
            background: #ffffff;
            border: 1px solid rgba(23, 33, 43, 0.12);
            border-radius: 8px;
        }

        .project-card p {
            margin-bottom: 0;
        }

        .photos {
            background: #f6f3ee;
        }

        .photo-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 18px;
        }

        .photo-card {
            margin: 0;
            overflow: hidden;
            background: #ffffff;
            border: 1px solid rgba(23, 33, 43, 0.12);
            border-radius: 8px;
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
            color: #ffffff;
            background: #173c43;
        }

        .learning .eyebrow {
            color: #9ce7dc;
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
            background: #ffffff;
        }

        .contact a {
            color: #0f766e;
            font-weight: 700;
            overflow-wrap: anywhere;
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
                padding: 72px 5vw 56px;
                background:
                    linear-gradient(
                        180deg,
                        rgba(246, 243, 238, 0.98) 0%,
                        rgba(246, 243, 238, 0.9) 58%,
                        rgba(246, 243, 238, 0.5) 100%
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
            .photo-grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 3rem;
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
