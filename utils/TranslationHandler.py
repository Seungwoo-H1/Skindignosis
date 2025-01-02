import deepl

class TranslationHandler:
    def __init__(self, api_key):
        self.translator = deepl.Translator(api_key)

    def translate_text(self, text, target_language):
        try:
            result = self.translator.translate_text(text, target_lang=target_language)
            return result.text
        except deepl.DeepLException as e:
            return text  # 번역 실패 시 원문 반환
