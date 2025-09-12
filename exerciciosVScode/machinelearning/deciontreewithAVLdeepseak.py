import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# Definindo a estrutura de um nó da AVL
class AVLNode:
    def __init__(self, company, job, degree, salary_more_than_100k):
        self.company = company
        self.job = job
        self.degree = degree
        self.salary_more_than_100k = salary_more_than_100k
        self.left = None
        self.right = None
        self.height = 1

# Definindo a árvore AVL
class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, root, company, job, degree, salary_more_than_100k):
        if not root:
            return AVLNode(company, job, degree, salary_more_than_100k)
        
        # Inserção simples (não balanceada para este exemplo)
        if company < root.company:
            root.left = self.insert(root.left, company, job, degree, salary_more_than_100k)
        else:
            root.right = self.insert(root.right, company, job, degree, salary_more_than_100k)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return root
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def in_order_traversal(self, root, data_list):
        if root:
            self.in_order_traversal(root.left, data_list)
            data_list.append({
                'company': root.company,
                'job': root.job,
                'degree': root.degree,
                'salary_more_then_100k': root.salary_more_than_100k
            })
            self.in_order_traversal(root.right, data_list)

# Criando e populando a árvore AVL com dados
avl_tree = AVLTree()
root = None

# Inserindo dados na árvore (em vez de ler de um CSV)
data_to_insert = [
    ('google', 'sales executive', 'bachelors', 0),
    ('google', 'sales executive', 'masters', 1),
    ('google', 'business manager', 'bachelors', 0),
    ('google', 'business manager', 'masters', 1),
    ('google', 'computer programmer', 'bachelors', 1),
    ('google', 'computer programmer', 'masters', 1),
    ('abc pharma', 'sales executive', 'bachelors', 0),
    ('abc pharma', 'sales executive', 'masters', 0),
    ('abc pharma', 'business manager', 'bachelors', 0),
    ('abc pharma', 'business manager', 'masters', 1),
    ('abc pharma', 'computer programmer', 'bachelors', 0),
    ('abc pharma', 'computer programmer', 'masters', 1),
    ('facebook', 'sales executive', 'bachelors', 0),
    ('facebook', 'sales executive', 'masters', 1),
    ('facebook', 'business manager', 'bachelors', 1),
    ('facebook', 'business manager', 'masters', 1),
    ('facebook', 'computer programmer', 'bachelors', 1),
    ('facebook', 'computer programmer', 'masters', 1),
]

for company, job, degree, salary in data_to_insert:
    root = avl_tree.insert(root, company, job, degree, salary)

# Coletando dados da árvore para criar um DataFrame
data_list = []
avl_tree.in_order_traversal(root, data_list)
df = pd.DataFrame(data_list)

# A partir daqui, o processo é similar ao original
inputs = df.drop('salary_more_then_100k', axis='columns')
target = df['salary_more_then_100k']

# Codificação de variáveis categóricas
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')

print("Dados da Árvore AVL:")
print(df)
print("\nDados Codificados:")
print(inputs_n)

# Treinamento do modelo
model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)
accuracy = model.score(inputs_n, target)
print(f"\nAcurácia do modelo: {accuracy:.2f}")

# Função para fazer previsões baseadas em entradas textuais
def predict_salary(company, job, degree):
    # Transforma os valores textuais em numéricos usando os encoders já treinados
    try:
        company_n = le_company.transform([company])[0]
        job_n = le_job.transform([job])[0]
        degree_n = le_degree.transform([degree])[0]
        
        prediction = model.predict([[company_n, job_n, degree_n]])
        
        if prediction[0] == 1:
            return "Ganha mais de 100k"
        else:
            return "Não ganha mais de 100k"
    except ValueError as e:
        return f"Erro: {e}. Verifique se os valores estão presentes nos dados de treinamento."

# Exemplos de uso
print("\nPrevisões:")
print(f"Google, Computer Programmer, Masters: {predict_salary('google', 'computer programmer', 'masters')}")
print(f"ABC Pharma, Sales Executive, Bachelors: {predict_salary('abc pharma', 'sales executive', 'bachelors')}")
print(f"Facebook, Business Manager, Masters: {predict_salary('facebook', 'business manager', 'masters')}")