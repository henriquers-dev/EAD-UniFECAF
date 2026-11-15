# Mapa de interfaces e reconhecimento de hardware

## 1. Reconhecimento do dispositivo (Etapa 1)
| Item | Identificação | Como foi identificado |
|------|---------------|-----------------------|
| Microcontrolador | | (marcação do chip, datasheet, `esptool chip_id`) |
| Memória (flash/RAM) | | |
| Sensores | | |
| Interfaces de comunicação (Wi-Fi, BLE, Zigbee...) | | |
| Interfaces físicas (USB, pinos, conectores) | | |
| Alimentação | | |
| Armazenamento | | |
| Comunicação com outros sistemas | | |

## 2. Interfaces físicas observadas (Etapa 4)
| Interface | Presente? | Localização / pinos | Como foi verificada | Evidência (arquivo em `evidence/`) |
|-----------|-----------|---------------------|---------------------|------------------------------------|
| UART | | | | |
| JTAG | | | | |
| SPI | | | | |
| I²C | | | | |
| Interface de programação | | | | |
| Pontos de teste | | | | |

## 3. Análise por interface
Repita este bloco para cada interface encontrada.

### Interface: <nome>
- **O que ela permite fazer:** 
- **Informação que fornece (ex.: log de boot, console, leitura de memória):** 
- **Proteções existentes (senha, bloqueio, desativação):** 
- **Contexto (acesso físico necessário? invasivo?):** 
- **Risco se permanecer acessível em um produto comercial:** 
- **Classificação:** (não é vulnerabilidade / exposição de baixo risco / vulnerabilidade) e justificativa:

> Evite concluir "a interface existe, logo o dispositivo é inseguro". Descreva o que ela fornece, o que falta de proteção e o impacto para um atacante com acesso físico.

## 4. Evidências
Arquivos guardados em `hardware/evidence/` (fotos, logs de UART, saídas de comandos):
- 

> Não inclua senhas, tokens ou chaves reais. Use `[REDACTED]`.
