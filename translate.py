import config
 #  Translate text into English
def translate_to_english(detected_language,text):
        try:
            translation = config.translator.translate(text, src=detected_language,dest="en")
            return translation.text
        except Exception as e:
            return f" Error in translation: {str(e)}"

#  Detect user language
def detect_and_translate(user_input):
        try:
            detected = config.translator.detect(user_input)
            detected_language = detected.lang
            if detected_language != "en":
                translated_text = translate_to_english(detected_language,user_input)
                return translated_text
            else:    
                return user_input  # If input is already in English, return the same input
        except Exception as e:
            return f"⚠️ Error detecting language: {str(e)}"