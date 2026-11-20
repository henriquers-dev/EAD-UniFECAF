# Análise de Protocolos de Rede

## 1. Superfície de rede
| Item | Valor |
|---|---|
| IP / MAC do dispositivo | |
| Interfaces (Wi-Fi, Ethernet, BLE…) | |
| Topologia do laboratório | |

## 2. Serviços expostos
| Porta | Protocolo | Serviço / versão | Autenticação | Criptografia | Observações |
|---|---|---|---|---|---|
| | | | | | |

## 3. Protocolos analisados
### Protocolo: `<nome>`
- **Finalidade:**
- **Direção / endpoints:**
- **Formato das mensagens:**
- **Autenticação e controle de sessão:**
- **Criptografia (TLS? versão? validação de certificado?):**
- **Proteção contra replay / integridade:**
- **Captura:** `evidence/<arquivo>.pcapng`

## 4. Verificações
- [ ] Credenciais em texto claro
- [ ] Versões de TLS/cifras fracas
- [ ] Validação de certificado
- [ ] Credenciais padrão / hardcoded
- [ ] Atualização de firmware (assinada? via HTTPS?)
- [ ] Serviços desnecessários expostos
- [ ] Tratamento de entradas malformadas (fuzzing controlado)

## 5. Pendências
-
