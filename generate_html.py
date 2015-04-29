def generate_title(text):
    first_location = text.find('TITLE: ')
    end_location = text.find('DESCRIPTION: ')
    title = text[first_location+7 : end_location-1]
    return title

def generate_description(text):
    first_location = text.find('DESCRIPTION: ')
    description = text[first_location+13 :]
    return description



def html_get_concept(title, description):
    html_1 = '''
<div class="concept">
    <div class="title">
        ''' + title + '''</div>'''
    html_2 = '''
    <div class="description">
        ''' + description + '''</div>
</div>'''

    full_concept = html_1 + html_2
    return full_concept


def get_concept_by_number(text, number):
    counter = 0
    while counter < number:
        concept_start = text.find('TITLE:')
        next_concept_start = text.find('TITLE:', concept_start + 1)
        concept_by_number = text[concept_start:next_concept_start - 1]
        text = text[next_concept_start:]
        counter = counter + 1
    return concept_by_number

def get_all_html(text):
    counter = 1
    concept = get_concept_by_number(text, counter)
    all_html = ''
    while concept != '':
        title = generate_title(concept)
        description = generate_description(concept)
        html_concept = html_get_concept(title, description)
        all_html = all_html + html_concept
        counter = counter + 1
        concept = get_concept_by_number(text, counter)
    return all_html

example = '''TITLE: Variables
DESCRIPTION: In Python, a variable is an assigment statement (Name=Expression). We can us variables to create a name and use that name to reffer to a variable. Once we define a variable we can change the value, and when we use that name again, it reffers to the new value.
The equal (=) sign does not have the same meaning in Python that in arithmetic. In Python it's equivalent to an assigment.
TITLE: Strings
DESCRIPTION: A String is a sequence of characters sorrounded by quotes. ("This is a String"). If you dont use the quotes, python interprets it as a variable, so you're going to get error, because it's not a define variable.
TITLE: Functions
DESCRIPTION: A function is a block of organized, reusable code that is used to perform a single, related action. they are used to avoid repetition by grouping common operations.
Functions can be break down in inputs, defined by def, and ouputs, stablished by return.'''


print get_all_html(example)







