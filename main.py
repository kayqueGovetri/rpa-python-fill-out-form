import rpa as r

r.init(visual_automation=True)
r.url('https://www.conube.com.br')
r.wait(3)
r.click('imagens/saiba_quanto_custa.png')

r.timeout(2)
r.snap('page', 'results.png')

# Insere as informações inicias do form;
r.type("imagens/nome.png", text_to_type="Teste do robo rpa python")
r.type("imagens/sobrenome.png", text_to_type="Conube teste")
r.type("imagens/telefone.png", text_to_type="1154876-7894")
r.type("imagens/email.png", text_to_type="teste@conube.com.br")
r.click("imagens/qual_sera_atividade.png")

r.timeout(1)

# Insere as informações sobre a empresa.
r.click("imagens/advocacia.png")
r.click("imagens/qual_segmento.png")
r.click("imagens/comercio.png")
r.click("imagens/formato_juridico.png")
r.click("imagens/empresario_individual.png")
r.type("imagens/cidade_estado.png", text_to_type="Taboao da Serra")
r.click("imagens/taboao_da_serra.png")
r.timeout(2)
r.click("imagens/calcular_plano.png")

r.timeout(2)
r.snap('page', 'results.png')
r.close()
