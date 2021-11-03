from parse import parse

nomeArquivoBase = "ChannelFlow.sim"
nomeNovoArquivo = "html_Channel.txt"

indiceLinhaAtual = 0

arq = open("tooltips.txt", 'rt')
dict_tooltips = {}
linha = arq.readline()
while( linha ):
	resultado = parse("{} = {}", linha)
	if( resultado ):
		dict_tooltips[resultado[0]] = resultado[1]
	linha = arq.readline()

def tooltipString(texto, tooltip):
	return "<span class='codetooltip' data-toggle='tooltip' data-placement='top' data-animation='false' title='%s'>%s</span>" % (tooltip, texto)

def formataLinha(linha):
	global indiceLinhaAtual
	linha = linha.replace("\n", "")

	if( indiceLinhaAtual==0 ):
		# OUTPUT vtk=[0 2000] backup=532 print=100 pasta=pastaOutput
		stringParse = "OUTPUT vtk=[{} {}] backup={} print={} pasta={}"
		resultado = parse(stringParse, linha)
		input_fields = resultado[0]
		input_interface = resultado[1]
		input_backup = resultado[2]
		input_print = resultado[3]
		input_folder = resultado[4]

		output_fields = tooltipString(input_fields, dict_tooltips['output_fields'])
		output_interface = tooltipString(input_interface, dict_tooltips['output_interface'])
		output_backup = tooltipString(input_backup, dict_tooltips['output_backup'])
		output_print = tooltipString(input_print, dict_tooltips['output_print'])
		output_folder = tooltipString(input_folder, dict_tooltips['output_folder'])
		
		output_total = stringParse.format(output_fields, output_interface, output_backup, output_print, output_folder)
	elif( indiceLinhaAtual==1 ):
		# CARTESIANO

		output_total = tooltipString(linha, dict_tooltips['coordinate_system'])
	elif( indiceLinhaAtual==2 ):
		# Nt 1000000
		stringParse = "Nt {}"
		resultado = parse(stringParse, linha)
		Nt = resultado[0]

		Nt = tooltipString(Nt, dict_tooltips['Nt'])
		output_total = stringParse.format(Nt)
	elif( indiceLinhaAtual==3 ):
		# xMin -5.0
		stringParse = "xMin {}"
		resultado = parse(stringParse, linha)
		resultado = resultado[0]

		resultado = tooltipString(resultado, dict_tooltips['xMin'])
		output_total = stringParse.format(resultado)
	elif( indiceLinhaAtual==4 ):
		# xMax -5.0
		stringParse = "xMax {}"
		resultado = parse(stringParse, linha)
		resultado = resultado[0]

		resultado = tooltipString(resultado, dict_tooltips['xMax'])
		output_total = stringParse.format(resultado)
	elif( indiceLinhaAtual==5 ):
		# yMin -5.0
		stringParse = "yMin {}"
		resultado = parse(stringParse, linha)
		resultado = resultado[0]

		resultado = tooltipString(resultado, dict_tooltips['yMin'])
		output_total = stringParse.format(resultado)
	elif( indiceLinhaAtual==6 ):
		# yMax -5.0
		stringParse = "yMax {}"
		resultado = parse(stringParse, linha)
		resultado = resultado[0]

		resultado = tooltipString(resultado, dict_tooltips['yMax'])
		output_total = stringParse.format(resultado)
	elif( indiceLinhaAtual==7 ):
		# tMax 50
		stringParse = "tMax {}"
		resultado = parse(stringParse, linha)
		resultado = resultado[0]

		resultado = tooltipString(resultado, dict_tooltips['tMax'])
		output_total = stringParse.format(resultado)
	elif( indiceLinhaAtual==8 ):
		# Re 87.45012176
		stringParse = "Re {}"
		resultado = parse(stringParse, linha)
		resultado = resultado[0]

		resultado = tooltipString(resultado, dict_tooltips['Re'])
		output_total = stringParse.format(resultado)
	elif( indiceLinhaAtual==9 ):
		# Fr 1 grav=[0 0]
		stringParse = "Fr {} grav=[{} {}]"
		resultado = parse(stringParse, linha)
		froude = resultado[0]
		gravx = resultado[1]
		gravy = resultado[2]

		froude = tooltipString(froude, dict_tooltips['Fr'])
		gravx = tooltipString(gravx, dict_tooltips['gravx'])
		gravy = tooltipString(gravy, dict_tooltips['gravy'])
		
		output_total = stringParse.format(froude, gravx, gravy)
	elif( indiceLinhaAtual==10 ):
		# param_visco Wi=3 beta=0.111111 alpha=0 epsilon=0.25
		stringParse = "param_visco Wi={} beta={} alpha={} epsilon={}"
		resultado = parse(stringParse, linha)

		Wi = tooltipString(resultado[0], dict_tooltips['Wi'])
		beta = tooltipString(resultado[1], dict_tooltips['beta'])
		alpha = tooltipString(resultado[2], dict_tooltips['alpha'])
		epsilon = tooltipString(resultado[3], dict_tooltips['epsilon'])
		
		output_total = stringParse.format(Wi, beta, alpha, epsilon)
	elif( indiceLinhaAtual==11 ):
		# FORMULACAO_VISCO CSF
		stringParse = "formulacao_visco {}"
		resultado = parse(stringParse, linha)

		formulacao_visco = tooltipString(resultado[0], dict_tooltips['formulacao_visco'])
		
		output_total = stringParse.format(formulacao_visco)
	elif( indiceLinhaAtual==12 ):
		# tolNSF 1e-6 0.0 1		
		stringParse = "tolNSF {} {} {}"
		resultado = parse(stringParse, linha)

		tolNSF_0 = tooltipString(resultado[0], dict_tooltips['tolNSF_0'])
		tolNSF_1 = tooltipString(resultado[1], dict_tooltips['tolNSF_1'])
		tolNSF_2 = tooltipString(resultado[2], dict_tooltips['tolNSF_2'])
		
		output_total = stringParse.format(tolNSF_0, tolNSF_1, tolNSF_2)
	elif( indiceLinhaAtual==13 ):
		# tensao_superficial ligado=sim Weber=30 tsur=1
		stringParse = "tensao_superficial ligado={} Weber={} tsur={}"
		resultado = parse(stringParse, linha)

		tensao_ligado = tooltipString(resultado[0], dict_tooltips['tensao_ligado'])
		Weber = tooltipString(resultado[1], dict_tooltips['Weber'])
		tsur = tooltipString(resultado[2], dict_tooltips['tsur'])
		
		output_total = stringParse.format(tensao_ligado, Weber, tsur)
	elif( indiceLinhaAtual==14 ):
		# VEL_INICIAL [0.0 0.0]
		stringParse = "VEL_INICIAL [{} {}]"
		resultado = parse(stringParse, linha)

		vel_x = tooltipString(resultado[0], dict_tooltips['vel_x'])
		vel_y = tooltipString(resultado[1], dict_tooltips['vel_y'])
		
		output_total = stringParse.format(vel_x, vel_y)
	elif( indiceLinhaAtual==15 ):
		# MALHA_EIXO_X tipo=uniforme N=400
		stringParse = "MALHA_EIXO_X tipo={} N={}"
		resultado = parse(stringParse, linha)

		tipo = tooltipString(resultado[0], dict_tooltips['mesh_uniform'])
		Nx = tooltipString(resultado[1], dict_tooltips['mesh_uniform_Nx'])
		
		output_total = stringParse.format(tipo, Nx)
	elif( indiceLinhaAtual==16 ):
		# MALHA_EIXO_Y tipo=uniforme N=400
		stringParse = "MALHA_EIXO_Y tipo={} N={}"
		resultado = parse(stringParse, linha)

		tipo = tooltipString(resultado[0], dict_tooltips['mesh_uniform'])
		Ny = tooltipString(resultado[1], dict_tooltips['mesh_uniform_Ny'])
		
		output_total = stringParse.format(tipo, Ny)
	elif( indiceLinhaAtual==17 or indiceLinhaAtual==18 or indiceLinhaAtual==19 or indiceLinhaAtual==20 ):
		# BOUNDARY id=0 direcao=vertical posicao=0.0 inicio=0.0 fim=1.0 tipo=INFLOW perfil=parabolico valorDirichlet=1.5

		resultado = None
		if( not resultado ): # Tentativa inflow
			stringParse = "BOUNDARY id={} direcao={} posicao={} inicio={} fim={} tipo={} perfil={} valorDirichlet={}"
			resultado = parse(stringParse, linha)
		if( not resultado ): # Tentativa noslip
			stringParse = "BOUNDARY id={} direcao={} posicao={} inicio={} fim={} tipo={} movimento={}"
			resultado = parse(stringParse, linha)
		if( not resultado ): # Tentativa neumann
			stringParse = "BOUNDARY id={} direcao={} posicao={} inicio={} fim={} tipo={}"
			resultado = parse(stringParse, linha)
		
		if( not resultado ):
			print( "1. problema! nao encontrou o tipo certo da boundary" )
			exit()
		else:
			tipo_boundary = resultado[5]

		boundary_id = tooltipString(resultado[0], dict_tooltips['boundary_id'])
		direction = tooltipString(resultado[1], dict_tooltips['direction_%s' % (resultado[1])])
		posicao = tooltipString(resultado[2], dict_tooltips['position_%s' % (resultado[1])])
		inicio = tooltipString(resultado[3], dict_tooltips['inicio_%s' % (resultado[1])])
		fim = tooltipString(resultado[4], dict_tooltips['fim_%s' % (resultado[1])])
		tipo = tooltipString(resultado[5], dict_tooltips['tipo'])

		if( tipo_boundary=="INFLOW" ):
			perfil = tooltipString(resultado[6], dict_tooltips['perfil'])
			valorDirichlet = tooltipString(resultado[7], dict_tooltips['valorDirichlet'])
			output_total = stringParse.format(boundary_id, direction, posicao, inicio, fim, tipo, perfil, valorDirichlet)
		elif( tipo_boundary=="NOSLIP" ):
			movimento = tooltipString(resultado[6], dict_tooltips['movimento_noslip'])
			output_total = stringParse.format(boundary_id, direction, posicao, inicio, fim, tipo, movimento)
		elif( tipo_boundary=="NEUMANN" ):
			output_total = stringParse.format(boundary_id, direction, posicao, inicio, fim, tipo)
		else:
			print( "2. problema! nao encontrou o tipo certo da boundary" )
			exit()

	elif( indiceLinhaAtual==21 ):
		# REGIAO tipo=FULL numFaces=4 faces=0 1 2 3
		stringParse = "REGIAO tipo={} numFaces={} faces={} {} {} {}"
		resultado = parse(stringParse, linha)

		tipo = tooltipString(resultado[0], dict_tooltips['regiao_tipo'])
		numfaces = tooltipString(resultado[1], dict_tooltips['regiao_numfaces'])
		face_0 = tooltipString(resultado[2], dict_tooltips['regiao_idface'])
		face_1 = tooltipString(resultado[3], dict_tooltips['regiao_idface'])
		face_2 = tooltipString(resultado[4], dict_tooltips['regiao_idface'])
		face_3 = tooltipString(resultado[5], dict_tooltips['regiao_idface'])
		
		output_total = stringParse.format(tipo, numfaces, face_0, face_1, face_2, face_3)
	else:
		output_total = linha


	

# BOUNDARY id=1 direcao=vertical posicao=5.0 inicio=0.0 fim=1.0 tipo=NEUMANN
# BOUNDARY id=2 direcao=horizontal posicao=0 inicio=0.0 fim=5 tipo=NOSLIP movimento=SEM_MOVIMENTO
# BOUNDARY id=3 direcao=horizontal posicao=1 inicio=0.0 fim=5 tipo=NOSLIP movimento=SEM_MOVIMENTO
# REGIAO tipo=FULL numFaces=4 faces=0 1 2 3




	indiceLinhaAtual += 1
	return "<code>%s</code>\n" % (output_total)






# Lendo o arquivo que sera usado como base
arq = open(nomeArquivoBase, 'rt')
linha_output = arq.readline() # Linha OUTPUT
linha_cartesiano = arq.readline() # Linha CARTESIANO OU AXI_SIMETRICO
linha_Nt = arq.readline()
linha_xMin = arq.readline()
linha_xMax = arq.readline()
linha_yMin = arq.readline()
linha_yMax = arq.readline()
linha_tMax = arq.readline()
linha_Re = arq.readline()
linha_Fr = arq.readline()
linha_visco = arq.readline()
linha_formVisco = arq.readline()
linha_tolNSF = arq.readline()
linha_tensaoSup = arq.readline()
linha_velInicial = arq.readline()
linha_malhaX = arq.readline()
linha_malhaY = arq.readline()

linha_geometria = []
linha_geometria.append( arq.readline() )
linha_geometria.append( arq.readline() )
linha_geometria.append( arq.readline() )
linha_geometria.append( arq.readline() )

linha_regiao = arq.readline()
arq.close()


# Criando o novo arquivo com o codigo html
arq = open(nomeNovoArquivo, 'wt', newline='\n')
arq.write(formataLinha(linha_output))
arq.write(formataLinha(linha_cartesiano))
arq.write(formataLinha(linha_Nt))
arq.write(formataLinha(linha_xMin))
arq.write(formataLinha(linha_xMax))
arq.write(formataLinha(linha_yMin))
arq.write(formataLinha(linha_yMax))
arq.write(formataLinha(linha_tMax))
arq.write(formataLinha(linha_Re))
arq.write(formataLinha(linha_Fr))
arq.write(formataLinha(linha_visco))
arq.write(formataLinha(linha_formVisco))
arq.write(formataLinha(linha_tolNSF))
arq.write(formataLinha(linha_tensaoSup))
arq.write(formataLinha(linha_velInicial))
arq.write(formataLinha(linha_malhaX))
arq.write(formataLinha(linha_malhaY))
arq.write(formataLinha(linha_geometria[0]))
arq.write(formataLinha(linha_geometria[1]))
arq.write(formataLinha(linha_geometria[2]))
arq.write(formataLinha(linha_geometria[3]))
arq.write(formataLinha(linha_regiao))
arq.close()
