from langchain import PromptTemplate

STORY_MAKER_TEMPLATE = """saya memiliki seorang anak yang berjenis kelamin {gender}, ia berumur {age} tahun
buatkan sebuah cerita pendek atau dongen untuk saya bacakan ke anak saya sebelum ia tidur
{topic}
cerita pendek tersebut maksimal mengandung {n_sentence} kalimat

jangan buat cerita yang tidak layak untuk anak-anak, seperti kisah asmara, sex, dan pembunuhan

buatlah cerita dengan format paragraf, sehingga lebih mudah dibaca

tolong berikan pula judul untuk cerita tersebut

jawaban diawali 'judul: ' lalu  'cerita: '"""

PROMPT_STORY_MAKER = PromptTemplate(input_variables=["gender","age","topic","n_sentence"], template=STORY_MAKER_TEMPLATE)
