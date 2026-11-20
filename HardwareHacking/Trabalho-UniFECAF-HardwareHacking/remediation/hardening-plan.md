# Plano de Hardening

## Priorização
| ID | Achado | Ação de correção | Prioridade | Esforço | Responsável | Prazo | Status |
|---|---|---|---|---|---|---|---|
| R-001 | F-001 | | Alta | | | | Pendente |

## Controles recomendados
### Hardware
- [ ] Desabilitar/bloquear UART e JTAG em produção
- [ ] Ativar secure boot e verificação de assinatura
- [ ] Criptografar firmware / proteger leitura da flash
- [ ] Remover pads de debug ou adicionar proteção física

### Rede
- [ ] TLS 1.2+ com validação de certificado
- [ ] Remover credenciais padrão; exigir troca no primeiro uso
- [ ] Desativar serviços desnecessários
- [ ] Atualizações assinadas e com proteção contra rollback
- [ ] Segmentação de rede e firewall

## Validação (reteste)
| ID | Reteste realizado | Resultado | Data |
|---|---|---|---|
| R-001 | | | |
