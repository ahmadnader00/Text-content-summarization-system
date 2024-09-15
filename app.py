
# استيراد المكتبات اللازمة
from flask import Flask, render_template, request
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from langdetect import detect
from werkzeug.utils import secure_filename
import os
import PyPDF2
# إنشاء تطبيق Flask
app = Flask(__name__)


# تعيين المجلد الذي ستتم فيه عملية تحميل الملفات
app.config['UPLOAD_FOLDER'] = ''
# دالة لتحليل النص من خلال الرابط الإلكتروني
def parserurl(url):
    parser = HtmlParser.from_url(url, Tokenizer('english'))
    parser1 = HtmlParser.from_url(url, Tokenizer('arabic'))

    # استخدام مكتبة LangDetect للتحقق من لغة النص
    if detect(str(parser.significant_words)) == 'en':
        print('en')
        return parser
    if detect(str(parser1.significant_words)) == 'ar':
        print('ar')
        return parser1

# دالة لتحليل النص من خلال النص المدخل يدويًا
def parsertext(text):
    # استخدام مكتبة LangDetect للتحقق من لغة النص
    if detect(text) == 'en':
        parser = PlaintextParser.from_string(text, Tokenizer('english'))
        print('en')
        return parser
    if detect(text) == 'ar':
        parser1 = PlaintextParser.from_string(text, Tokenizer('arabic'))
        print('ar')
        return parser1

# دالة لتحليل النص من ملف PDF
def parserpdf(filename):
    with open(filename, 'rb') as file:
        # استخدام PyPDF2 لقراءة ملف PDF واستخلاص النص منه
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text ()

    # استخدام مكتبة LangDetect للتحقق من لغة النص
    if detect(text) == 'en':
        parser = PlaintextParser.from_string(text, Tokenizer('english'))
        print('en')
        return parser
    if detect(text) == 'ar':
        parser1 = PlaintextParser.from_string(text, Tokenizer('arabic'))
        print('ar')
        return parser1

# دالة لاستخلاص الملخصات من النص المحلل باستخدام TextRankSummarizer أو LsaSummarizer أو LuhnSummarizer
def get_text_summaries(parser, range, summarizer):
    summary = summarizer(parser.document, range)
    result = []
    for sentence in summary:
        result.append(str(sentence))
    return result

# دوال للحصول على أفضل 10 جمل ملخصة باستخدام TextRankSummarizer أو LsaSummarizer أو LuhnSummarizer
def top_10_lsa_url(url, range):
    parser = parserurl(url)
    summarizer_2 = LsaSummarizer()
    return get_text_summaries(parser, range, summarizer_2)

def top_10_lsa_text(text, range):
    parser = parsertext(text)
    summarizer_2 = LsaSummarizer()
    return get_text_summaries(parser, range, summarizer_2)

def top10_textrank_text(text, range):
    parser = parsertext(text)
    summarizer_3 = TextRankSummarizer()
    return get_text_summaries(parser, range, summarizer_3)

def top10_textrank_url(url, range):
    parser= parserurl(url)
    summarizer_3 = TextRankSummarizer()
    return get_text_summaries(parser, range, summarizer_3)

def top10_luhn_url(url, range):
    parser = parserurl(url)
    summarizer_1 = LuhnSummarizer()
    return get_text_summaries(parser, range, summarizer_1)

def top10_luhn_text(text, range):
    parser = parsertext(text)
    summarizer_1 = LuhnSummarizer()
    return get_text_summaries(parser, range, summarizer_1)

# دالة للحصول على الملخصات من ملف PDF باستخدام 
def top10_lsa_pdf(pdf_file_path, range):
    parser = parserpdf(pdf_file_path)
    summarizer_2 = LsaSummarizer()
    return get_text_summaries(parser, range, summarizer_2)
def top10_luhn_pdf(pdf_file_path, range):
    parser = parserpdf(pdf_file_path)
    summarizer_1 = LuhnSummarizer()
    return get_text_summaries(parser, range, summarizer_1)
def top10_textrank_pdf(pdf_file_path, range):
    parser = parserpdf(pdf_file_path)
    summarizer_3 = TextRankSummarizer()
    return get_text_summaries(parser, range, summarizer_3)


# الصفحة الرئيسية للتطبيق، تحتوي على نموذج لإدخال النص أو رابط الإلكتروني أو ملف PDF واختيار الملخص المرغوب باستخدام إحدى الدوال المعرفة سابقًا
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try :
            if "url" in request.form:
                range = int(request.form.get("rangeurl"))
                url = request.form.get("url")
                lsa_text = top_10_lsa_url(url, range)
                textrank_text = top10_textrank_url(url, range)
                text_luhn = top10_luhn_url(url , range)

                # إرجاع الملخصات إلى الصفحة HTML
                return render_template('index.html', summer=text_luhn, summer_lsa=lsa_text, summer_textrank=textrank_text)

            elif "textforsummer" in request.form:
                range = int(request.form.get("rangetext"))
                text = request.form.get("textforsummer")
                text_for_fre = top10_luhn_text(text, range)
                text_for_lsa = top_10_lsa_text(text, range)
                text_for_rank = top10_textrank_text(text, range)
                # إرجاع الملخصات إلى الصفحة HTML
                success_msg = "Your message has been sent successfully"
                return render_template("index.html", summertext=text_for_fre, summertext_lsa=text_for_lsa, summertext_textrank=text_for_rank, success=success_msg)

            elif "pdfforsummer" in request.form:
              range = int(request.form.get("rangepdf"))
              file = request.files["pdfforsummer"]
              filename = secure_filename(file.filename)
              filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
              file.save(filepath)
              pdf_text_for_lsa = top10_lsa_pdf(filepath, range)
              pdf_text_for_luhn = top10_luhn_pdf(filepath, range)
              pdf_text_for_textrank = top10_textrank_pdf(filepath, range)



              # إرجاع الملخصات إلى الصفحة HTML
              success_msg = "Your message has been sent successfully"
              print('ok')
              return render_template("index.html",summertext=pdf_text_for_luhn, summertext_lsa=pdf_text_for_lsa,summer_textrank=pdf_text_for_textrank, success=success_msg)
        except Exception as e:
            error_msg = "An error occurred while processing your request. Please try again."

            # إذا حدث خطأ، إرجاع رسالة الخطأ إلى الصفحة HTML
            return render_template("index.html", error=error_msg)

    else:
     return render_template('index.html')

# تشغيل التطبيق
if __name__ == "__main__":
    app.run(debug=True)
    render_template