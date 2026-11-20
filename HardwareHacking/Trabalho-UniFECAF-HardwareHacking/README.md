# Avaliação de Segurança — Simulação

> **Status:** [Em andamento | Concluída] · **Versão do documento:** 1.0 · **Data:** [2026-11-20]
> **Nome:** Henrique Ribeiro Siqueira
> **Classificação:** [Confidencial]

---

## Sumário

1. [Objetivo da avaliação](#1-objetivo-da-avaliação)
2. [Dispositivo analisado](#2-dispositivo-analisado)
3. [Limites e escopo dos testes](#3-limites-e-escopo-dos-testes)
4. [Arquitetura](#4-arquitetura)
5. [Ferramentas utilizadas](#5-ferramentas-utilizadas)
6. [Organização das evidências](#6-organização-das-evidências)
7. [Resumo da análise de firmware](#7-resumo-da-análise-de-firmware)
8. [Resumo da análise de hardware](#8-resumo-da-análise-de-hardware)
9. [Resumo da análise dos protocolos](#9-resumo-da-análise-dos-protocolos)
10. [Principais achados](#10-principais-achados)
11. [Recomendações](#11-recomendações)
12. [Reprodução dos testes no ambiente autorizado](#12-reprodução-dos-testes-no-ambiente-autorizado)
13. [Referências](#13-referências)

---

## 1. Objetivo da avaliação

**Objetivo geral:** avaliar a postura de segurança do dispositivo **[NOME/MODELO]**, identificando vulnerabilidades em firmware, hardware e protocolos de comunicação, e propor medidas de mitigação.

**Objetivos específicos:**

- Identificar falhas de configuração, credenciais embutidas e componentes desatualizados no firmware.
- Verificar a exposição de interfaces físicas de depuração e a proteção contra extração de dados.
- Analisar a segurança dos protocolos de comunicação (autenticação, cifragem e integridade).
- Classificar os achados por severidade e priorizar a correção.
- Documentar evidências e procedimentos de forma reproduzível.

**Metodologia de referência:** [ex.: OWASP IoT Security Testing Guide / OWASP FSTM / ETSI EN 303 645 / NIST SP 800-115].

---

## 2. Dispositivo analisado

| Item | Descrição |
|---|---|
| Fabricante | [ ] |
| Modelo | [ ] |
| Número de série / ID | [ ] |
| Versão de hardware (revisão da PCB) | [ ] |
| Versão de firmware | [ ] |
| SoC / MCU | [ ] |
| Memória (Flash / RAM) | [ ] |
| Sistema operacional embarcado | [ ] (ex.: Linux embarcado, FreeRTOS, bare-metal) |
| Interfaces de comunicação | [ ] (ex.: Wi-Fi, BLE, Ethernet, Zigbee, MQTT) |
| Interfaces físicas | [ ] (ex.: UART, JTAG/SWD, SPI, USB) |
| Aplicativo / nuvem associados | [ ] |
| Origem da amostra | [ ] (ex.: cedida pelo cliente) |

**Fotos do dispositivo:** `evidencias/hardware/fotos/`

---

## 3. Limites e escopo dos testes

### 3.1 Dentro do escopo

- [ ] Análise estática e dinâmica do firmware.
- [ ] Inspeção física da placa e identificação de componentes.
- [ ] Análise das interfaces de depuração (UART/JTAG/SWD).
- [ ] Captura e análise de tráfego de rede e sem fio entre dispositivo, aplicativo e nuvem.
- [ ] Testes de autenticação, autorização e gerenciamento de sessão nas interfaces do dispositivo.
- [ ] Processo de atualização de firmware.

### 3.2 Fora do escopo

- [ ] Infraestrutura de nuvem e servidores do fabricante (exceto se autorizado).
- [ ] Testes de negação de serviço (DoS) contra redes de produção.
- [ ] Engenharia social e ataques a pessoas.
- [ ] Testes destrutivos que inutilizem a unidade (exceto unidade designada para isso).
- [ ] Dispositivos e redes de terceiros.

### 3.3 Premissas e restrições

- Ambiente: rede isolada de laboratório, sem acesso à internet de produção.
- Período de testes: [data inicial] a [data final].
- Autorização formal: [referência ao documento / contrato / e-mail] — `docs/autorizacao/`.
- Limitações: [ex.: acesso a apenas uma unidade, sem código-fonte, sem credenciais de nuvem].

---

## 4. Arquitetura

### 4.1 Visão geral

```
┌──────────────┐   BLE / Wi-Fi    ┌────────────────┐    HTTPS / MQTT    ┌──────────────┐
│  App móvel   │◄────────────────►│  Dispositivo   │◄──────────────────►│  Nuvem do    │
│  (cliente)   │                  │  [MODELO]      │                    │  fabricante  │
└──────────────┘                  └───────┬────────┘                    └──────────────┘
                                          │
                              UART / JTAG / SPI Flash
                                          │
                                  ┌───────┴────────┐
                                  │ Bancada de     │
                                  │ testes (lab)   │
                                  └────────────────┘
```

> Substitua o diagrama acima pela arquitetura real do dispositivo (pode ser inserida como imagem em `docs/imagens/arquitetura.png`).

### 4.2 Componentes principais

| Componente | Função | Observações |
|---|---|---|
| [SoC/MCU] | Processamento principal | [ ] |
| [Flash SPI/NOR/NAND] | Armazenamento de firmware e dados | [ ] |
| [Módulo de rádio] | Comunicação sem fio | [ ] |
| [Elemento seguro / TPM] | Armazenamento de chaves | [Presente / Ausente] |

### 4.3 Topologia do ambiente de testes

- Rede de laboratório isolada: `[faixa de IP/VLAN]`
- Dispositivo sob teste (DUT): `[IP/MAC]`
- Estação de análise: `[SO / versão]`
- Ponto de acesso controlado / proxy de interceptação: `[IP]`

---

## 5. Ferramentas utilizadas

| Categoria | Ferramenta | Versão | Finalidade |
|---|---|---|---|
| Firmware | `binwalk` | [ ] | Identificação e extração de componentes da imagem |
| Firmware | `strings`, `hexdump`, `xxd` | [ ] | Inspeção básica de binários |
| Firmware | `Ghidra` / `radare2` | [ ] | Engenharia reversa e análise estática |
| Firmware | `QEMU` / `Firmadyne` / `FirmAE` | [ ] | Emulação do firmware |
| Firmware | `Trivy` / `Syft` / `cve-bin-tool` | [ ] | Identificação de componentes e CVEs conhecidas |
| Hardware | Multímetro / osciloscópio | [ ] | Identificação de pinos e níveis lógicos |
| Hardware | Analisador lógico (ex.: Saleae) | [ ] | Captura de sinais UART/SPI/I²C |
| Hardware | Adaptador USB-serial (3,3 V) | [ ] | Acesso ao console UART |
| Hardware | Leitor de flash (ex.: CH341A) / `flashrom` | [ ] | Leitura da memória flash (com autorização) |
| Hardware | OpenOCD / adaptador JTAG/SWD | [ ] | Verificação de depuração em hardware |
| Rede | `Wireshark` / `tcpdump` | [ ] | Captura e análise de tráfego |
| Rede | `nmap` | [ ] | Descoberta de portas e serviços |
| Rede | `mitmproxy` / `Burp Suite` | [ ] | Análise de tráfego HTTP(S) em ambiente controlado |
| Sem fio | `nRF Connect` / `bettercap` / Ubertooth | [ ] | Análise de BLE |
| Sem fio | `testssl.sh` | [ ] | Avaliação de configuração TLS |
| Apoio | `Git`, `sha256sum`, `script` | [ ] | Controle de versão e integridade das evidências |

---

## 6. Organização das evidências

### 6.1 Estrutura de diretórios

```
.
├── README.md
├── docs/
│   ├── autorizacao/            # Termo de autorização e escopo assinado
│   ├── imagens/                # Diagramas e figuras do relatório
│   └── relatorio-final.pdf
├── evidencias/
│   ├── firmware/
│   │   ├── originais/          # Imagens de firmware obtidas (somente leitura)
│   │   ├── extraido/           # Sistema de arquivos extraído
│   │   ├── analise-estatica/   # Saídas do binwalk, strings, Ghidra
│   │   └── emulacao/           # Logs e configurações de emulação
│   ├── hardware/
│   │   ├── fotos/              # Fotos da PCB, componentes e pontos de teste
│   │   ├── capturas-logicas/   # Arquivos do analisador lógico
│   │   └── logs-uart/          # Logs de console serial
│   ├── protocolos/
│   │   ├── pcap/               # Capturas de tráfego
│   │   ├── ble/                # Capturas e dumps BLE
│   │   └── tls/                # Relatórios de configuração TLS
│   └── achados/
│       └── ACH-001/ ...        # Uma pasta por achado, com evidências e passos
├── scripts/                    # Scripts de apoio à análise e reprodução
└── hashes.sha256               # Hashes de integridade de todas as evidências
```

### 6.2 Convenções

- **Nomenclatura:** `AAAA-MM-DD_componente_descricao.ext` (ex.: `2026-11-20_uart_boot-log.txt`).
- **Identificação de achados:** `ACH-001`, `ACH-002`, ... com referência cruzada à tabela da [seção 10](#10-principais-achados).
- **Integridade:** hash SHA-256 de cada arquivo registrado em `hashes.sha256`.
  ```bash
  find evidencias -type f -exec sha256sum {} \; > hashes.sha256
  ```
- **Originais imutáveis:** arquivos em `firmware/originais/` são mantidos como somente leitura; análises são feitas em cópias.
- **Dados sensíveis:** credenciais e chaves encontradas devem ser mascaradas nos relatórios e armazenadas com acesso restrito.

---

## 7. Resumo da análise de firmware

### 7.1 Obtenção

- **Método:** [download do site do fabricante | extração via UART/flash | captura da atualização OTA].
- **Arquivo:** `[nome]` · **SHA-256:** `[hash]` · **Tamanho:** [ ]

### 7.2 Análise estática

| Verificação | Resultado |
|---|---|
| Formato e estrutura da imagem | [ ] (ex.: SquashFS + kernel Linux, bootloader U-Boot) |
| Imagem criptografada/assinada? | [Sim / Não] |
| Credenciais ou chaves embutidas | [ ] |
| Certificados e chaves privadas no sistema de arquivos | [ ] |
| Serviços habilitados por padrão (telnet, ssh, http) | [ ] |
| Componentes de terceiros e versões | [ ] |
| CVEs conhecidas identificadas | [ ] |
| Funções inseguras / binários sem proteções (NX, PIE, RELRO, canary) | [ ] |

### 7.3 Análise dinâmica

- Emulação: [bem-sucedida / parcial / não realizada] — ferramenta: [ ].
- Serviços observados em execução: [ ].
- Observações: [ ].

### 7.4 Atualização de firmware

- Mecanismo: [OTA / USB / manual].
- Verificação de assinatura e integridade: [Sim / Não].
- Proteção contra *rollback*: [Sim / Não].
- Canal de download: [HTTPS / HTTP].

---

## 8. Resumo da análise de hardware

### 8.1 Inspeção física

- Componentes identificados (SoC, flash, rádio, reguladores): [ ].
- Pontos de teste e conectores expostos: [ ].
- Presença de proteções físicas (resina, blindagem, *tamper switch*): [ ].

### 8.2 Interfaces de depuração

| Interface | Encontrada? | Acesso obtido? | Observações |
|---|---|---|---|
| UART | [ ] | [ ] | Baud rate: [ ] · Console com login? [ ] |
| JTAG / SWD | [ ] | [ ] | Proteção de leitura (RDP/fuses): [ ] |
| SPI Flash | [ ] | [ ] | Dump realizado? [ ] · Dados em texto claro? [ ] |
| USB | [ ] | [ ] | Modo DFU/bootloader: [ ] |

### 8.3 Proteções de dados

- Dados sensíveis armazenados em flash sem criptografia: [ ].
- Secure boot habilitado: [Sim / Não].
- Elemento seguro / armazenamento protegido de chaves: [ ].

---

## 9. Resumo da análise dos protocolos

### 9.1 Inventário de comunicações

| Protocolo | Porta / Canal | Direção | Cifrado? | Autenticado? |
|---|---|---|---|---|
| [HTTP/HTTPS] | [ ] | [ ] | [ ] | [ ] |
| [MQTT/MQTTS] | [ ] | [ ] | [ ] | [ ] |
| [BLE GATT] | [ ] | [ ] | [ ] | [ ] |
| [Outro] | [ ] | [ ] | [ ] | [ ] |

### 9.2 Resultados

- **Descoberta de serviços (nmap):** [portas e serviços expostos].
- **TLS:** versões e *cipher suites* suportadas, validação de certificado pelo dispositivo, uso de certificados autoassinados — [ ].
- **Autenticação e autorização:** [credenciais padrão, tokens previsíveis, ausência de controle de acesso].
- **BLE:** [modo de pareamento, *bonding*, exposição de características sem autenticação].
- **Integridade e *replay*:** [proteção contra reenvio de mensagens].
- **Dados em trânsito:** [informações sensíveis em texto claro].

---

## 10. Principais achados

> Classificação de severidade baseada em **CVSS v3.1/v4.0**: Crítica (9.0–10.0) · Alta (7.0–8.9) · Média (4.0–6.9) · Baixa (0.1–3.9) · Informativa.

| ID | Título | Área | Severidade | CVSS | Status |
|---|---|---|---|---|---|
| ACH-001 | [Ex.: Credenciais padrão em serviço de administração] | Firmware | [ ] | [ ] | Aberto |
| ACH-002 | [Ex.: Console UART com acesso root sem autenticação] | Hardware | [ ] | [ ] | Aberto |
| ACH-003 | [Ex.: Comunicação sem cifragem entre dispositivo e nuvem] | Protocolo | [ ] | [ ] | Aberto |
| ACH-004 | [Ex.: Atualização de firmware sem verificação de assinatura] | Firmware | [ ] | [ ] | Aberto |

### Modelo de detalhamento (um por achado)

```
ID:            ACH-00X
Título:        [ ]
Severidade:    [ ] (CVSS: [vetor])
Componente:    [ ]
Descrição:     [O que foi encontrado e por quê é um risco]
Impacto:       [Consequência para confidencialidade, integridade, disponibilidade]
Evidências:    evidencias/achados/ACH-00X/
Passos:        [Resumo dos passos para reprodução]
Recomendação:  [Correção sugerida]
Referências:   [CWE, CVE, OWASP]
```

---

## 11. Recomendações

### Prioridade alta (curto prazo)

1. Remover credenciais padrão e embutidas; exigir credenciais únicas por dispositivo.
2. Desabilitar serviços desnecessários (telnet, depuração remota) e portas não utilizadas.
3. Impor TLS 1.2+ com validação de certificado em todas as comunicações.
4. Assinar digitalmente os firmwares e verificar a assinatura antes da instalação.

### Prioridade média (médio prazo)

5. Desabilitar ou proteger UART/JTAG/SWD em produção (fuses, senha, remoção de *headers*).
6. Habilitar *secure boot* e criptografia da flash, com chaves em elemento seguro.
7. Atualizar componentes de terceiros com CVEs conhecidas e manter inventário (SBOM).
8. Implementar controle de acesso e limitação de tentativas nas interfaces de gerenciamento.

### Prioridade baixa / melhoria contínua

9. Adotar ciclo de desenvolvimento seguro e testes de segurança automatizados no pipeline.
10. Publicar política de divulgação de vulnerabilidades e canal de contato.
11. Implementar proteção contra *rollback* e *replay*.
12. Alinhar o produto a normas como **ETSI EN 303 645** e **OWASP ISVS**.

---

## 12. Reprodução dos testes no ambiente autorizado

> ⚠️ Execute apenas com autorização formal, em laboratório isolado e sobre a unidade designada.

### 12.1 Pré-requisitos

- Estação de análise com Linux (ex.: Ubuntu 22.04/24.04) e acesso `sudo`.
- Dispositivo(s) sob teste, fonte de alimentação adequada e cabos.
- Equipamentos: adaptador USB-serial 3,3 V, analisador lógico, leitor de flash/adaptador JTAG (conforme seção 5).
- Rede de laboratório isolada, sem rota para produção.
- Documento de autorização arquivado em `docs/autorizacao/`.

### 12.2 Preparação do ambiente

```bash
# Dependências básicas (ajuste conforme necessário)
sudo apt update
sudo apt install -y binwalk squashfs-tools nmap wireshark tcpdump \
                    flashrom openocd minicom python3-pip git qemu-system

# Clonar o repositório de evidências e scripts
git clone [URL_DO_REPOSITORIO] avaliacao && cd avaliacao
```

### 12.3 Firmware

```bash
# 1. Verificar integridade do arquivo original
sha256sum evidencias/firmware/originais/[firmware.bin]

# 2. Identificar componentes da imagem
binwalk evidencias/firmware/originais/[firmware.bin]

# 3. Extrair o conteúdo (em cópia, nunca no original)
cp evidencias/firmware/originais/[firmware.bin] /tmp/fw.bin
binwalk -e /tmp/fw.bin -C evidencias/firmware/extraido/

# 4. Busca de segredos e configurações
grep -riE "password|passwd|secret|api[_-]?key|BEGIN (RSA|EC) PRIVATE" \
     evidencias/firmware/extraido/ > evidencias/firmware/analise-estatica/segredos.txt

# 5. Inventário de componentes e CVEs
syft dir:evidencias/firmware/extraido/ -o json > evidencias/firmware/analise-estatica/sbom.json
```

Para a análise de binários, abra os executáveis relevantes no **Ghidra** e registre as conclusões em `evidencias/firmware/analise-estatica/`.

### 12.4 Hardware

1. Fotografar a placa (frente e verso) e registrar em `evidencias/hardware/fotos/`.
2. Identificar pontos de teste candidatos a UART (GND, TX, RX, VCC) com multímetro, **medindo níveis lógicos antes de conectar** (confirme 3,3 V ou 1,8 V).
3. Conectar o adaptador USB-serial (GND → GND, TX ↔ RX) e capturar o *boot*:
   ```bash
   script -a evidencias/hardware/logs-uart/boot-log.txt
   minicom -D /dev/ttyUSB0 -b [BAUD_RATE]
   ```
4. Verificar a presença de console/login e registrar o comportamento.
5. Para JTAG/SWD, usar o OpenOCD com a configuração do alvo e verificar se há proteção de leitura:
   ```bash
   openocd -f interface/[adaptador].cfg -f target/[alvo].cfg
   ```
6. Se autorizado, ler a flash SPI e registrar o hash:
   ```bash
   flashrom -p ch341a_spi -r evidencias/firmware/originais/dump-flash.bin
   sha256sum evidencias/firmware/originais/dump-flash.bin >> hashes.sha256
   ```

### 12.5 Protocolos

```bash
# 1. Descoberta de portas e serviços do DUT (somente no laboratório)
nmap -sV -sC -p- [IP_DO_DISPOSITIVO] -oA evidencias/protocolos/nmap-dut

# 2. Captura de tráfego do dispositivo
sudo tcpdump -i [INTERFACE] host [IP_DO_DISPOSITIVO] \
     -w evidencias/protocolos/pcap/dut-$(date +%F).pcap

# 3. Avaliação de TLS (endpoints do dispositivo, se aplicável)
testssl.sh [IP_DO_DISPOSITIVO]:[PORTA] | tee evidencias/protocolos/tls/testssl.txt
```

- **HTTP(S)/MQTT:** analisar os arquivos `.pcap` no Wireshark; usar `mitmproxy` apenas se o dispositivo estiver configurado para o proxy de teste.
- **BLE:** usar `nRF Connect` ou ferramenta equivalente para enumerar serviços/características e verificar quais exigem pareamento/autenticação.

### 12.6 Registro e encerramento

1. Documentar cada achado em `evidencias/achados/ACH-XXX/` com passos, capturas e logs.
2. Atualizar `hashes.sha256`:
   ```bash
   find evidencias -type f -exec sha256sum {} \; > hashes.sha256
   ```
3. Restaurar o dispositivo ao estado original (quando aplicável) e devolver os equipamentos.
4. Consolidar o relatório final em `docs/relatorio-final.pdf`.

---

## 13. Referências

- OWASP — Internet of Things Project e Firmware Security Testing Methodology (FSTM)
- ETSI EN 303 645 — Cyber Security for Consumer Internet of Things
- NIST SP 800-115 — Technical Guide to Information Security Testing and Assessment
- CVSS — Common Vulnerability Scoring System (FIRST)
- CWE / CVE — MITRE
- [Documentação do fabricante e datasheets dos componentes]

---

## Contato

| Função | Nome | E-mail |
|---|---|---|
| Responsável técnico | [ ] | [ ] |
| Contato do cliente | [ ] | [ ] |
