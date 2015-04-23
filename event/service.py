def planning_parse(planning):
    plans = []
    for line in _x_format_lines(planning):
        if line.startswith('@'):
            plans.append({
                'title': line[1:].strip(),
                'lines': [],
            })
        elif plans:
            plans[-1]['lines'].append(line)

    data = []
    for plan in plans:
        data.append({
            'title': plan['title'],
            'paragraphs': list(_x_paragraphs(plan['lines'])),
        })

    return data


def text_parse(text):
    return list(_x_paragraphs(_x_format_lines(text)))




def _x_format_lines(text):
    prev = None
    for line in text.splitlines():
        trim = line.strip()
        if trim or prev:
            yield trim
        prev = trim

def _x_paragraphs(lines):
    parag = []
    prev = None
    for line in lines:
        if line:
            parag.append(line)
        elif prev:
            yield parag
            parag = []
        prev = line

    if parag:
        yield parag
