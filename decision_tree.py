import data

training_data = data.learning_data

header = ['color', 'shape', 'weight', 'size', 'name']


# funkcja która zwraca listę unikalnych wartości z każdej kolumny
def uniqie_vals(rows, col):
    return set([row[col] for row in rows])


# zliczamy liczbę wystąpień danego typu w zestawie danych
def class_counts(rows):
    counts = {}  # label -> count

    for row in rows:
        name = row[-1]
        if name not in counts:
            counts[name] = 0
        counts[name] += 1
    return counts


# funkcja do sprawdzania czy wartość jest wartością numeryczną
def is_numeric(val):
    return isinstance(val, int) or isinstance(val, float)


# klasa do zadawania pytań
class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        val = example[self.column]

        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        condition = '=='
        if is_numeric(self.value):
            condition = '>='
        return "Is %s %s %s?" % (header[self.column], condition, str(self.value))


def partition(rows, question):
    """ podział zbioru informacji
        dla każdego rzędu w zbiorze, sprawdź czy zgadza się z pytaniem, jeśli tak
        dodaj do 'true' inaczej dodaj do 'false' """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def gini(rows):
    """ Gini impurity to miara tego jak często losowo wybrany element zbioru byłby źle skategoryzowany, gdyby
    przypisać mu losową kategorię spośród wszystkich kategorii znajdujących się w danym zbiorze.  """

    counts = class_counts(rows)
    impurity = 0
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity += prob_of_lbl * (1 - prob_of_lbl)
    return impurity


def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


def find_best_split(rows):
    """ znajdź najlepsze możliwe pytanie do zadania, sprawdzając wszystkie
        właściwośći oraz licząc dla nich 'info_gain' """
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):
        values = set([row[col] for row in rows])

        for val in values:
            question = Question(col, val)

            true_rows, false_rows = partition(rows, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain > best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


class Leaf:
    def __init__(self, rows):
        self.predicions = class_counts(rows)


class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows):
    gain, question = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)

    true_branch = build_tree(true_rows)

    false_branch = build_tree(false_rows)

    return DecisionNode(question, true_branch, false_branch)


def print_tree(node, spacing=""):
    if isinstance(node, Leaf):
        print(spacing + "Predict", node.predicions)

    else:
        print(spacing + str(node.question))

        print(spacing + '--> True:')
        print_tree(node.true_branch, spacing + "  ")

        print(spacing + '--> False:')
        print_tree(node.false_branch, spacing + "  ")


def classify(row, node):
    if isinstance(node, Leaf):
        return node.predicions

    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


def print_leaf(counts):
    probs = []
    for lbl in counts.keys():
        probs.append(lbl)
    return probs


# my_tree = build_tree(training_data)
#
# print_tree(my_tree)
#
# testing_data = [
#     ['red', 'rectangle', 50, 'medium', 'Kit-kat'],
#     ['blue', 'rectangle', 115, 'big', 'Wedel'],
#     ['white', 'rectangle', 15, 'small', 'Krowka'],
# ]
#
# test =  ['white', 'rectangle', 15, 'small', 'Krowka']
#
# for row in testing_data:
#     print(print_leaf(classify(row, my_tree)))
#
# wynik = print_leaf(classify(test, my_tree))[0]
# print(wynik)
