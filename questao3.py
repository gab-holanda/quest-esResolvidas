import xml.etree.ElementTree as ET
dados = ET.Element('dados')

def cria_xml() -> None:
    """
    Cria um arquivo XML contendo registros de faturamento diário para um mês específico.

    Esta função define um conjunto de dados de faturamento para cada dia do mês de setembro de 2024 e gera um arquivo XML com esses dados. Cada registro no arquivo XML inclui a data e o valor do faturamento correspondente.

    O XML gerado terá a seguinte estrutura:
    <dados>
        <registro>
            <dia>2024-09-01</dia>
            <faturamento>1600</faturamento>
        </registro>
        ...
    </dados>

    O arquivo é salvo como 'faturamento_mes.xml' com codificação UTF-8 e declaração XML.
    """
    
    faturamentos = {
        '2024-09-01': 1600,
        '2024-09-02': 2560,
        '2024-09-03': 0,
        '2024-09-04': 2006,
        '2024-09-05': 0,
        '2024-09-06': 3064,
        '2024-09-07': 0,
        '2024-09-08': 2550,
        '2024-09-09': 0,
        '2024-09-10': 10,
        '2024-09-11': 3500,
        '2024-09-12': 0,
        '2024-09-13': 4000,
        '2024-09-14': 0,
        '2024-09-15': 4780,
        '2024-09-16': 0,
        '2024-09-17': 0,
        '2024-09-18': 3890,
        '2024-09-19': 0,
        '2024-09-20': 5500,
        '2024-09-21': 0,
        '2024-09-22': 2020,
        '2024-09-23': 0,
        '2024-09-24': 0,
        '2024-09-25': 2510,
        '2024-09-26': 420,
        '2024-09-27': 2010,
        '2024-09-28': 3410,
        '2024-09-29': 7500,
        '2024-09-30': 0
    }

    for dia, faturamento in faturamentos.items():
        registro = ET.SubElement(dados, 'registro')  
        dia_elemento = ET.SubElement(registro, 'dia')  
        dia_elemento.text = dia  
        faturamento_elemento = ET.SubElement(registro, 'faturamento')  
        faturamento_elemento.text = str(faturamento)  

    tree = ET.ElementTree(dados)
    tree.write('faturamento_mes.xml', encoding='utf-8', xml_declaration=True)

    print("Arquivo 'faturamento_mes.xml' criado com sucesso!")


cria_xml()

# Criando na função acima
tree = ET.parse('faturamento_mes.xml')
root = tree.getroot()

# Variáveis para cálculos
faturamentos = []
for registro in root.findall('registro'):
    faturamento = int(registro.find('faturamento').text)
    if faturamento > 0:
        faturamentos.append(faturamento)

soma = 0
menor_faturamento = 0
maior_faturamento = 0

for i in range(len(faturamentos)):
    if i==0 or (faturamentos[i] < menor_faturamento and faturamentos[i] != 0):
        menor_faturamento = faturamentos[i]
    elif i==0 or (faturamentos[i] > maior_faturamento and faturamentos[i] != 0):
        maior_faturamento = faturamentos[i]

    soma += faturamentos[i]

media_mensal = (soma / len(faturamentos))

dias_acima_da_media = 0
for faturamento in faturamentos:
    if faturamento > media_mensal:
        dias_acima_da_media += 1

print("Menor valor de faturamento ocorrido em um dia do mês: {0}".format(menor_faturamento))
print("Maior valor de faturamento ocorrido em um dia do mês: {0}".format(maior_faturamento))
print("Número de dias no mês com faturamento acima da média mensal: {0}".format(dias_acima_da_media))