from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(conexao, sessao):
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()

def test_listar_usuarios(conexao, sessao):
    sessao = conexao.gerar_sessao()
    usuarios = [
        Usuario(nome='Renzo', email='renzo@python.pro.br'),
        Usuario(nome='Luciano', email='renzo@python.pro.br'),
        Usuario(nome='Guilherme', email='guilhermedasilvapires1996@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()

