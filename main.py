from vagas import EdificioGaragem, EstacionamentoExterno, Adapter

objects = []

garagem = EdificioGaragem()
objects.append(Adapter(nome = garagem.NomeEG(), vagas = garagem.VagasEG(), valor = garagem.ValorEG()))

externa = EstacionamentoExterno()
objects.append(Adapter(nome = externa.NomeExt(), vagas = externa.VagasExt(), valor = externa.ValorExt()))

for i in objects:
  print(f'A {i.nome} possui {i.vagas} vagas e custa R$ {i.valor:.2f}')