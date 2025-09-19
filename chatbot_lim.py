import streamlit as st
import json
import urllib.parse

# Carrega o JSON de FAQs
with open("faq_chatbot_lim.json", "r", encoding="utf-8") as f:
    faqs = json.load(f)

# E-mails responsáveis
emails_responsaveis = {
    "Comunicação Institucional": "comunicacao.lims@hc.fm.usp.br",
    "Diretoria Executiva": "diretoria.lims@hc.fm.usp.br",
    "Gerência Técnica": "gerenciarisco.lims@hc.fm.usp.br",
    "Gestão de Pesquisa e Inovação": "agip.lims@hc.fm.usp.br",
    "Gestão de Pessoas": "gestaopessoas.lims@hc.fm.usp.br",
    "Gestão de Projetos": "projetos.lims@hc.fm.usp.br",
    "Gestão Documental": "expediente.lims@hc.fm.br",
    "Gestão Econômica": "ceflim@hc.fm.usp.br",
    "Logística, Suprimentos e Infraestrutura": "alsi.lim@hc.fm.usp.br",
    "Rede PREMiUM",
    "Tecnologia de Informação": "eti.lims@hc.fm.usp.br"
}

st.title("Chatbot LIM")

# Seleção de área
area = st.selectbox("Selecione uma área:", [""] + list(faqs.keys()))

if area:
    assunto = st.selectbox("Selecione um assunto:", [""] + list(faqs[area].keys()))
    
    if assunto:
        perguntas = faqs[area][assunto]
        pergunta = st.selectbox(
            "Selecione uma pergunta:", 
            [""] + list(perguntas.keys()) + ["Não encontrou sua dúvida?"]
        )
        
        if pergunta and pergunta != "Não encontrou sua dúvida?":
            resposta = perguntas[pergunta]
            st.markdown(resposta, unsafe_allow_html=True)
        
        elif pergunta == "Não encontrou sua dúvida?":
            st.markdown("### Envie sua mensagem para a equipe responsável")
            with st.form("formulario_contato"):
                nome = st.text_input("Nome")
                email = st.text_input("E-mail")
                telefone = st.text_input("Telefone")
                mensagem = st.text_area("Mensagem")
                enviar = st.form_submit_button("Gerar e-mail")
                
                if enviar:
                    email_destino = emails_responsaveis.get(area)
                    if email_destino:
                        corpo = f"Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\nMensagem:\n{mensagem}"
                        corpo_url = urllib.parse.quote(corpo)
                        link_mailto = f"mailto:{email_destino}?subject=Dúvida do Chatbot LIM - {area}&body={corpo_url}"
                        st.markdown(f"[Clique aqui para enviar sua dúvida por e-mail]({link_mailto})")
                    else:
                        st.error("E-mail da área não configurado.")

