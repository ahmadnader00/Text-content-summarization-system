"# Text-content-summarization-system" 
The main goal of building an automatic text summarization system is to improve the efficiency and effectiveness of using available data and information. For example, in the case of summarizing a newspaper article, creating a short summary makes the article more effective and easy to read, and helps save time and effort in addition to improving understanding and recall. Moreover, automatic summarization helps extract essential and important information from long and complex texts, which reduces the time and effort required to read and understand these texts. Automatic summarization enables people to access essential information faster and more effectively, and helps them make faster and better decisions. Finally, the automatic summarization system allows access to knowledge and information in a more comprehensive way, which enables individuals to use it in research, studies, and daily life processes.
Automatic Summarization Stages:

Data Source: 1.4.3
The system takes input documents either by adding text or file or online from any site containing documents

structured or article format where every piece of information related to the research topic is almost always relevant, complete and in
organized form.

Preprocessing: 2.4.3
Sentence segmentation, punctuation removal, stopword filtering, and derivation (reducing root words) are used in advance during the preprocessing stage. Before common summarization (and other important techniques for processing incoming text documents), the initial source document is cleaned and converted into a data format, several preprocessing steps are taken:
• url_fetch: This is a method used to fetch the content of a web page from a specific link.
• Stop word removal: Stop words are removed either before or after text analysis, depending on the context. They must be
identified and removed from the text.
• Stemming: Strips a set of words designated as initial or root forms from their inflections and derived forms.
Text segmentation changes the words to account for multiple words.
• Tokenization: By dividing text streams into symbols that can be words, phrases, symbols, or
other meaningful units, it examines the words in the document.
12
• Capitalization: It is necessary to change every letter in the document to lowercase (but this depends on the nature of
languages) because different capital letters in different papers can be a problem. This technique then
unifies all the words of the text The document in one feature.
• Removal Noise: Punctuation marks and special characters are among the many extra characters found in most text materials.




Main interface:
 This interface contains the name of the service provided by the system (summarizaton Text) and a simple definition of the functions it provides
order. When clicking on (text summarizing to go), the user will be taken to the summary interface by adding the user
Plain text. When clicking on (link summarizing to go), the user will be taken to the summary interface by adding
The user sent a link to a website containing an article. When clicking on “file summarizing to go,” the user will be taken to the interface
Summarization by adding the user to a PDF file.


![Capture](https://github.com/user-attachments/assets/41fd7767-cd2e-4629-8fe3-35b95a34d334)


Summary interface by adding a link:
 In this interface, the user can add a link to a website that contains an article, and specify the level of summary he wants
Then click on “summary” to be taken to the summary result interface.

![Capture](https://github.com/user-attachments/assets/62108892-2a33-42a9-ab27-615ca6b12ec5)

Summary interface by adding text:
 In this interface, the user can add plain text, specify the level of summary he wants, and then click on
summary to move it to the summary result interface


![Capture](https://github.com/user-attachments/assets/dd88a423-8d4a-4d7f-b0e7-04f52191af22)


Summary interface by adding a file:
 In this interface, the user can add a pdf file, specify the level of summary he wants, and then click
on (summary) to move it to the summary result interface

![Capture](https://github.com/user-attachments/assets/0362ddb9-0d4e-49f6-b6ad-32e03c196ed5)

Summarization result interface:
 In this interface, the summary result using the third algorithm is displayed when you click on the algorithm name
The summary result is displayed to the user, and the user can copy the result.

![Capture](https://github.com/user-attachments/assets/eca69359-e5b2-43de-8429-8a7c13352577)


