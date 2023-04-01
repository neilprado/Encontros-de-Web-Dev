# Git para iniciantes

### O que é Git?
Em 2005, Linus Torvalds (o homem conhecido por criar o núcleo, ou kernel, do SO Linux) desenvolveu o GIT, que desde então tem sido ativamente mantido por Junio ​​Hamano, um engenheiro de software japonês. Atualmente, o GIT é um dos mais famosos sistemas de controle de versão de código aberto e milhões de projetos no mundo inteiro o utilizam para seu controle de versão (incluindo projetos comerciais e de código aberto).

### Características
1. Um sistema de controle de versão distribuído, o GIT segue uma abordagem peer to peer, contrário de outros como o Subversion (SVN) que segue um modelo baseado em cliente-servidor.
2. GIT permite aos desenvolvedores ter uma infinidade de ramos de código completamente independente. Criação, exclusão e fusão desses ramos é simples e não leva tempo.
3. No GIT, todas as operações são atômicas. Isso significa que uma ação pode ter sucesso ou falhar (sem fazer nenhuma alteração). Isso é importante porque em alguns sistemas de controle de versão (como o CVS) onde as operações não são atômicas, se uma operação de repositório é suspensa, ela pode deixar o repositório em um estado instável.
4. No GIT, tudo é armazenado dentro da pasta .git. Isso não é o mesmo em outros VCS como SVN e CVS onde os metadadados de arquivos são armazenados em pastas ocultas (por exemplo, .cvs, .svn, etc.)
5. GIT usa um modelo de dados que ajuda a garantir a integridade criptográfica de qualquer coisa presente dentro de um repositório. Cada vez que um arquivo é adicionado ou um commit é feito, suas somas de verificação são geradas. Da mesma forma, eles são recuperados através de suas somas de verificação também.
6. Outra característica presente no GIT é sua área de teste ou índice. Na área de preparação, os desenvolvedores podem formatar commits e receber feedback ​​antes de aplicá-los.

O GIT é consideravelmente simples de usar. Para começar, você pode criar um repositório ou conferir um já existente. Após a instalação, um simples *git-init* irá deixar tudo pronto. Da mesma maneira, o comando *git clone* pode criar uma cópia de um repositório local para um usuário.

### Instalação
**Windows**

1. Acesse o [site oficial](https://gitforwindows.org) e faça o download do instalador do GIT para Windows.
2. Depois de baixado, clique duas vezes no arquivo para iniciar o assistente de instalação. Basta seguir as instruções na tela, clicando em Next. Ao término, clique em Finish para concluir com êxito a instalação.

**Linux**

Se você é um usuário Linux, então deve estar acostumado com instalar programas e pacotes em seu computador usando comandos de instalação *apt-get* ou *yum*. Instalar o GIT não é diferente

1. Abra o terminal e execute os seguintes comandos:
```bash
sudo apt-get update 
sudo apt-get install git
```
2. Verifique se a instalação ocorreu com sucesso usando *git --version*.

### Comandos básicos do git

1. *git init*: Cria um novo repositório Git no diretório atual.
Exemplo: 
```bash
git init
```
2. *git clone*: Clona um repositório Git existente em um novo diretório.
Exemplo: 
```bash
git clone https://github.com/user/repo.git
```
3. *git add*: Adiciona um arquivo ao índice (também conhecido como staging area) para ser commitado.
Exemplo:
```bash
git add arquivo.txt
```
4. *git commit*: Grava as mudanças feitas nos arquivos em um novo commit no repositório.
Exemplo:
```bash
git commit -m "Adicionei um novo arquivo"
```
5. *git status*: Mostra o estado atual do repositório, incluindo arquivos modificados, adicionados e excluídos.
Exemplo:
```bash
git status
```
6. *git push*: Envia as mudanças locais para o repositório remoto.
Exemplo:
```bash
git push origin main
```
7. *git pull*: Obtém as mudanças mais recentes do repositório remoto e mescla-as com o repositório local
Exemplo:
```bash
git pull origin main
```
8. *git branch*: Cria, lista ou exclui branches
Exemplo:
```bash
git branch minha-nova-branch
```
9. *git checkout*: Muda para outra branch ou restaura arquivos do commit especificado.
Exemplo:
```bash
git checkout minha-nova-branch
```
10. *git merge*: Mescla as mudanças de uma branch para outra.
Exemplo:
```bash
git merge minha-nova-branch
```



