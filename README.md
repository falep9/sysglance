sysglance é ferramenta leve de auditoria de sistema que exibe IP, hardware ID e processos ativos, compatível com Windows e Linux.

---

## O que faz? 

Ao executar, o `sysglance` coleta e exibe rapidamente:

- Sistema operacional detectado automaticamente
- Endereço IP local da máquina
- Hardware ID (UUID do produto / Serial BIOS)
- Processos ativos em execução no momento

---

## Como usar

Pré-requisito: Python 3.x instalado.

```bash
git clone https://github.com/falep9/sysglance.git
cd sysglance
python sysglance.py
```

Exemplo de saída:

```
OS: Linux | IP: 192.168.1.105
Hardware ID: 4c4c4544-1234-5610-8034-b8c04f575931
Processos:
systemd
kthreadd
bash
python3
...
```

---

# Compatibilidade

| Sistema | Suportado |
|---------|-----------|
| Linux   | ✅        |
| Windows | ✅        |
| macOS   | ⚠️ Não testado |

---

## Tecnologias

- Python 3
- `subprocess` — execução de comandos do sistema
- `socket` — detecção de IP
- `platform` — identificação do SO

---

## Autor

**falep9** — [github.com/falep9](https://github.com/falep9)
