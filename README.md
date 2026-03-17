# 🚀 Flutter Web Login Test Automation (Playwright)

Automação de testes end-to-end para um aplicativo web desenvolvido em Flutter (Dreamflow), utilizando Playwright com Python.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido para automatizar o fluxo de login de uma aplicação Flutter Web — um cenário desafiador devido à ausência de elementos HTML tradicionais no DOM.

Diferente de aplicações web comuns, o Flutter renderiza a interface via canvas, o que exige abordagens alternativas de automação.

---

## 🧠 Desafio técnico

- ❌ Não há inputs HTML (`<input>`, `<button>`, etc.)
- ❌ Selectors tradicionais (CSS/XPath) não funcionam
- ❌ Texto não está disponível no DOM
- ❌ Elementos são renderizados dinamicamente via canvas

---

## 💡 Solução adotada

Foi implementada uma estratégia baseada em:

- 🎯 Interação por coordenadas relativas ao centro da tela
- 🧠 Controle explícito de foco nos campos
- 🧹 Limpeza de input antes da digitação
- 🧪 Sincronização manual com renderização do Flutter

Essa abordagem garante estabilidade mesmo em um ambiente não convencional.

---

## 🔧 Tecnologias utilizadas

- Python 3.x
- Playwright
- Pytest

---

## 🧪 Funcionalidades do teste

- ✅ Automação completa do login
- ✅ Preenchimento de campos (WhatsApp e senha)
- ✅ Clique no botão de acesso
- ✅ Validação de sucesso
- ✅ Captura de evidências:
  - 📸 Screenshots
  - 🎥 Vídeos
  - 🔍 Trace (debug avançado)
- ✅ Logs estruturados

---

## 📁 Estrutura do projeto

```
tests/
└── test_login.py

artifacts/
├── screenshots/
├── videos/
├── traces/
└── logs/
```

---

## ▶️ Como executar

### 1. Instalar dependências

```
pip install playwright pytest
playwright install
```

---

### 2. Rodar o teste

```
pytest -v
```

---

## 📊 Evidências geradas

Após a execução, os artefatos ficam disponíveis em:

```
artifacts/
```

- Screenshots da execução
- Vídeo do teste
- Trace completo para análise
- Logs detalhados

---

## ⚠️ Observações importantes

Este projeto não utiliza seletores tradicionais devido à natureza do Flutter Web.

A estratégia adotada pode exigir ajustes finos de posicionamento (offset) caso o layout da aplicação seja alterado.

---

## 🚀 Possíveis melhorias

- Integração com CI/CD (GitHub Actions)
- Geração de relatórios (Allure)
- Detecção visual automatizada (sem uso de coordenadas fixas)
- Expansão para fluxos completos (login → navegação → logout)

---

## 📎 Aplicação testada

🔗 LR Coffe Company

---

## 👨‍💻 Autor

Desenvolvido por Felipe Venâncio

---

## ⭐ Destaque

Este projeto demonstra a capacidade de adaptar estratégias de automação para cenários fora do padrão, especialmente em aplicações modernas que não expõem elementos no DOM tradicional.
