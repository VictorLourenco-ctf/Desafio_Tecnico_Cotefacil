def login(user, password):
    return {
        "usuario": user,
        "senha": password,
    }

def products(page, user_id, user_external_id):
    return {
                "filtro": "",
                "pagina": page,
                "registrosPorPagina": 25,
                "ordenarDecrescente": False,
                "colunaOrdenacao": "nenhuma",
                "clienteId": user_external_id,
                "tipoVendaId": 1,
                "pIIdFiltro": 0,
                "cestaPPFiltro": False,
                "codigoExterno": 0,
                "codigoUsuario": user_id,
                "promocaoSelecionada": "",
                "indicadorTipoUsuario": "CLI",
                "kindUser": 0,
                "xlsx": [],
                "principioAtivo": "",
                "master": False,
                "kindSeller": 0,
                "grupoEconomico": "",
                "users": [user_external_id],
                "list": True
            }