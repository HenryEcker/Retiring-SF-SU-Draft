import json
import re
from pprint import pprint

import markdown
from jinja2 import Template


def load_and_validate_reasons(file_path: str) -> dict:
    with open(file_path, encoding='UTF-8') as f:
        reasons = json.loads(f.read())

    # Ensure reasons are correct length
    assert len(reasons['Brief Description']) <= 100
    assert len(reasons['Usage guidance']) <= 500
    assert len(reasons['Post notice close description']) <= 500
    assert len(reasons['Post owner guidance']) <= 500
    assert len(reasons['Privileged user guidance']) <= 500
    return reasons


def render_template(
        reasons: dict, template_path: str, output_path: str
) -> None:
    reasons = {
        k: re.sub(
            # Remove paragraph wrapper in favour of text
            r'^<p>|</p>$',
            '',
            markdown.markdown(
                # Replace relative routes with absolute routes before rendering
                v.replace(r'](/', r'](https://stackoverflow.com/')
            ),
        )
        for k, v in reasons.items()
    }
    with open(template_path, encoding='UTF-8') as f:
        t = Template(f.read())

    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(t.render(reasons=reasons))


def build_markdown_table(reasons: dict, output_path: str) -> None:
    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(
            '\n'.join([
                '| Field | Text | Markdown Length |',
                '|:---|:---|:---|',
                *(f'| {k} | {v} | {len(v)} |' for k, v in reasons.items())
            ])
        )


def main() -> None:
    reasons = load_and_validate_reasons('./reasons.json')
    pprint(reasons)
    render_template(
        reasons,
        template_path='templates/mocks-template.html',
        output_path='output/new-html-mocks.html'
    )

    build_markdown_table(reasons, output_path='output/table.md')


if __name__ == '__main__':
    main()
