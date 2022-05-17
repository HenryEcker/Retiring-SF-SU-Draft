import re
from dataclasses import dataclass
from pathlib import Path
from pprint import pprint
from typing import Tuple

import markdown
from html2image import Html2Image
from jinja2 import Template


@dataclass
class RenderConfig:
    html_template: Path
    rendered_html: Path
    output_img_size: Tuple[int, int]


def build_and_validate_reasons() -> dict:
    reason = 'Not a practical, answerable problem unique to software development'
    topic = 'This question does not appear to be about [a specific programming problem, a software algorithm, or software tools commonly used by programmers](/help/on-topic)'
    another_site = '[another Stack Exchange site](https://stackexchange.com/sites)'

    reasons = {
        'Brief Description': reason,
        'Usage guidance': f'{topic}.',
        'Post notice close description': f'**Closed.** This question is [{reason.lower()}](/help/closed-questions). It is not currently accepting answers.',
        'Post owner guidance': f'{topic}. You can edit the question so it’s [on-topic](/help/on-topic) or see if it can be answered on {another_site}, but be sure to read the on-topic page for the site you choose before posting.',
        'Privileged user guidance': f'{topic}. If you believe the question is on-topic on {another_site} you can leave a comment to explain where the question may be able to be answered.'
    }

    # Ensure reasons are correct length
    assert len(reasons['Brief Description']) <= 100
    assert len(reasons['Usage guidance']) <= 500
    assert len(reasons['Post notice close description']) <= 500
    assert len(reasons['Post owner guidance']) <= 500
    assert len(reasons['Privileged user guidance']) <= 500
    return reasons


def render_html(
        reasons: dict,
        configs: dict[str, RenderConfig]
) -> None:
    reasons = {
        k: re.sub(
            # Remove paragraph wrapper in favour of text
            r'^<p>|</p>$',
            '',
            markdown.markdown(
                v
                    # Replace relative routes with absolute routes
                    .replace(r'](/', r'](https://stackoverflow.com/')
                    # Replace $SiteName with Stack Overflow
                    .replace('$SiteName', 'Stack Overflow')
            ),
        )
        for k, v in reasons.items()
    }

    for _, config in configs.items():
        with open(config.html_template, encoding='UTF-8') as f:
            t = Template(f.read())

        with open(config.rendered_html, 'w', encoding='UTF-8') as f:
            f.write(t.render(reasons=reasons))


def render_img(
        hti: Html2Image,
        configs: dict[str, RenderConfig]
):
    for _, config in configs.items():
        hti.screenshot(
            html_file=str(config.rendered_html),
            save_as=str(config.rendered_html.with_suffix('.png').name),
            size=config.output_img_size
        )


def build_markdown_table(reasons: dict, output_path: str) -> None:
    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(
            '\n'.join([
                '| Field | (Rendered) Markdown | Markdown Length |',
                '|:---|:---|:---|',
                *(f'| {k} | {v} | {len(v)} |' for k, v in reasons.items())
            ])
        )


def main() -> None:
    reasons = build_and_validate_reasons()
    pprint(reasons)

    # Make Folders
    templates_folder = Path('./templates')
    templates_folder.mkdir(exist_ok=True)
    html_output_folder = Path('./html-output')
    html_output_folder.mkdir(exist_ok=True)
    md_output_folder = Path('./md-output')
    md_output_folder.mkdir(exist_ok=True)

    # Render Config
    pbm_px = 16 + 1 + 1
    configs = {
        'close_dialogue': RenderConfig(
            html_template=templates_folder / 'mock-close-dialogue.html',
            rendered_html=(
                    html_output_folder / 'mock-close-dialogue-rendered.html'
            ),
            output_img_size=(766 + (pbm_px * 2), 533 + (pbm_px * 2))
        ),

        'private_banner': RenderConfig(
            html_template=templates_folder / 'mock-private-banner.html',
            rendered_html=(
                    html_output_folder / 'mock-private-banner-rendered.html'
            ),
            output_img_size=(694 + (pbm_px * 2), 223 + (pbm_px * 2))
        ),
        'privileged_banner': RenderConfig(
            html_template=templates_folder / 'mock-privileged-banner.html',
            rendered_html=(
                    html_output_folder / 'mock-privileged-banner-rendered.html'
            ),
            output_img_size=(694 + (pbm_px * 2), 223 + (pbm_px * 2))
        ),
        'public_banner': RenderConfig(
            html_template=templates_folder / 'mock-public-banner.html',
            rendered_html=(
                    html_output_folder / 'mock-public-banner-rendered.html'
            ),
            output_img_size=(694 + (pbm_px * 2), 169 + (pbm_px * 2))
        )
    }
    # Render Templates
    render_html(reasons, configs=configs)

    # Render Rendered HTML as imgs
    render_img(
        hti=Html2Image(output_path=Path('./img_output/'), size=(3840, 2160)),
        configs=configs
    )

    # Build Markdown Table
    build_markdown_table(reasons, output_path='md-output/table.md')


if __name__ == '__main__':
    main()
