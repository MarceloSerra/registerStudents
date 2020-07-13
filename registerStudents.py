alunoContador = 0
alunoAprovado = 0
alunoReprovado = 0
alunoExame = 0
alunoMasculinoAprovado = 0;
alunoMasculinoReprovado = 0;
alunoMasculinoExame = 0;
alunoFemininoAprovado = 0;
alunoFemininoReprovado = 0;
alunoFemininoExame = 0;

#SUB-ROTINA COM RELATÓRIO FINAL A SER EXIBIDO
def relatorioAluno():
 print('****************************************************************************************')
 print('Total de alunos: '+str(alunoContador))
 print(str((alunoAprovado/alunoContador)*100)+'% Aprovados | '+str((alunoExame/alunoContador)*100)+' % de Exame | '+str((alunoReprovado/alunoContador)*100)+'% Reprovados')
 print('Alunos masculinos aprovados:  '+str(alunoMasculinoAprovado)+' | de Exame: '+str(alunoMasculinoExame)+' | e Reprovados: '+str(alunoMasculinoReprovado))
 print('Alunas femininas aprovadas:  '+str(alunoFemininoAprovado)+' | de Exame: '+str(alunoFemininoExame)+' | e Reprovadas: '+str(alunoFemininoReprovado))
 print('****************************************************************************************')
 input('Programa Finalizado...')

#QUESTIONA SE O USUÁRIO QUER CADASTRAR E CRIA UM LOOP CASO A OPÇÃO SEJA INVÁLIDA
cadastra = input('Gostaria de Cadastrar? 1=SIM  |  2=NÃO  | 3=Exibir Relatório  ')
if cadastra != '1' and cadastra != '2'and cadastra != '3':
 while cadastra != '1' and cadastra != '2' and cadastra != '3':
  print('Valor incorreto, tente novamente:  ')
  cadastra = input('Gostaria de Cadastrar? 1=SIM  |  2=NÃO  | 3=Exibir Relatório  ')
elif cadastra == '2':
  input('Programa finalizado...')
elif cadastra== '3':
  if alunoContador > 0:
   relatorioAluno()
  else:
   input('Não há relatório válido, cadastre algum aluno antes. Programa finalizado...')
elif cadastra=='1':
 while cadastra == '1':
#CADASTRA OS DADOS DO ALUNO E JÁ CALCULA A MÉDIA
  alunoNome = input('Digite o nome do aluno: ')
  alunoSexo = input('Digite seu sexo:  M=Masculino  |  F=Feminino  ')
  if alunoSexo != 'M' and alunoSexo != 'F':
   while alunoSexo != 'M' and alunoSexo != 'F' and alunoSexo != 'm' and alunoSexo != 'f':
    print('Valor incorreto, tente novamente:  ')
    alunoSexo = input('Digite seu sexo:  M=Masculino  |  F=Feminino  ')

  alunoNota1 = int(input('Digite a nota 1 do aluno:  '))
  if alunoNota1 > 10 or alunoNota1 < 0:
   while alunoNota1 > 10 or alunoNota1 < 0:
    print('Valor incorreto, tente novamente:  ')
    alunoNota1 = int(input('Digite a nota 1 do aluno:  '))

  alunoNota2 = int(input('Digite a nota 2 do aluno:  '))
  if alunoNota2 > 10 or alunoNota2 < 0:
   while alunoNota2 > 10 or alunoNota2 < 0:
    print('Valor incorreto, tente novamente:  ')
    alunoNota2 = int(input('Digite a nota 2 do aluno:  '))

  alunoNota3 = int(input('Digite a nota 3 do aluno:  '))
  if alunoNota3 > 10 or alunoNota3 < 0:
   while alunoNota3 > 10 or alunoNota3 < 0:
    print('Valor incorreto, tente novamente:  ')
    alunoNota3 = int(input('Digite a nota 3 do aluno:  '))

  alunoMedia = ((alunoNota1+alunoNota2+alunoNota3)/3)


#FILTRAGEM DE MÉDIA GERAL E POR SEXO
  if alunoMedia >= 7:
    if alunoSexo == 'M' or alunoSexo == 'm':
     alunoMasculinoAprovado += 1
     alunoAprovado += 1
    else:
     alunoFemininoAprovado += 1
     alunoAprovado += 1
  elif alunoMedia < 7 and alunoMedia >= 4:
     if alunoSexo == 'M' or alunoSexo == 'm':
      alunoMasculinoExame += 1
      alunoExame += 1
     else:
      alunoFemininoExame += 1
      alunoExame += 1
  else:
      if alunoSexo == 'M' or alunoSexo == 'm':
       alunoMasculinoReprovado += 1
       alunoReprovado += 1
      else:
       alunoFemininoReprovado += 1
       alunoFemininoReprovado += 1



  print('A média do '+alunoNome+' é '+str(alunoMedia))

#CONTADOR TOTAL DE ALUNOS
  alunoContador += 1

  cadastra = input('Gostaria de Cadastrar? 1=SIM  |  2=NÃO  | 3=Exibir Relatório  ')
  if cadastra != '1' and cadastra != '2'and cadastra != '3':
   while cadastra != '1' and cadastra != '2' and cadastra != '3':
    print('Valor incorreto, tente novamente:  ')
    cadastra = input('Gostaria de Cadastrar? 1=SIM  |  2=NÃO  | 3=Exibir Relatório  ')
  elif cadastra == '2':
    input('Programa finalizado...')
  elif cadastra == '3':
    if alunoContador > 0:
        relatorioAluno()
    else:
        input('Não há relatório válido, cadastre algum aluno antes. Programa finalizado...')


