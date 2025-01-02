import streamlit as st
from PhiModel import PhiModel
from LlamaModel import LlamaModel
from TranslationHandler import TranslationHandler

class FeedbackHandler:
    def __init__(self, phi_model_endpoint, phi_api_key, llama_endpoint, llama_token, llama_model_name, translator):
        self.phi_model = PhiModel(phi_model_endpoint, phi_api_key)
        self.llama_model = LlamaModel(llama_endpoint, llama_token, llama_model_name)
        self.translator = translator

    def generate_feedback(self, prompt_1, prompt_2, language):
        # Phi 모델 피드백 생성
        phi_feedback_1 = self.phi_model.generate_feedback_text(prompt_1)
        phi_feedback_2 = self.phi_model.generate_feedback_text(prompt_2)
        
        # Llama 모델 피드백 생성
        llama_feedback_1 = self.llama_model.generate_feedback_text(prompt_1)
        llama_feedback_2 = self.llama_model.generate_feedback_text(prompt_2)
        
        # 모든 피드백 결합
        combined_feedback = "\n\n".join([phi_feedback_1, phi_feedback_2, llama_feedback_1, llama_feedback_2])
        
        # 번역하여 반환
        return self.translator.translate_text(combined_feedback, language)
    
    def display_feedback(self, feedback, language):
        expander_title = self.translator.translate_text("🔍 Combined Model Feedback", language)
        info_title = self.translator.translate_text("**Combined Model Feedback**", language)
        
        with st.expander(expander_title, expanded=True):
            st.info(info_title, icon="💡")
            st.write(feedback)

