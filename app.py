from flask import Flask, render_template, redirect, url_for, request, send_file

app = Flask(__name__)

#write file function
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

#class of card info
class card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

#given the text convert them into card types
def extractInfo(content):
    cards = content.split(';;')
    cards = cards[:-1]
    a_card = [] #contains one line cards
    my_cards = [] #contains cards of card type
    for line in cards:
        a_card = line.split('\t')
        print(line)
        if (len(a_card) != 2 or (not a_card[0]) or (not a_card[1])):
            print('this',end='')
            return 'ERROR'
        thiscard = card(a_card[0],a_card[1])
        my_cards.append(thiscard)
    return my_cards

#a way to seperate the bullets with <br> instead of \n
def addBullet(text):
    content = ''
    if len(text.split('\n')) < 2:
        return text
    for bullet in text.split('\n'):
        content+= bullet.strip() + '<br>'
    return content

#make basic cards
def basicCard(my_cards):
    content = ''
    for card in my_cards:
        content += card.front + '\t' 
        content += addBullet(card.back)
        content += '\n'
    return content


#make cards cloze
def clozeCard(my_cards):
    content = ''
    for card in my_cards:
        content += card.front + ' -> {{c1::' + addBullet(card.back) + '}} \n'
    return content

#make cards cloze
def clozeCardFlipped(my_cards):
    content = ''
    for card in my_cards:
        if card.front[-1] != '?':
            content += '{{c1:: ' + card.front + ' }}' + ' is '
            content += addBullet(card.back) + ' \n'
            content += card.front + ' is {{c1::' 
            content += addBullet(card.back)
            content += '}} \n'
        else:
            content += card.front + ' -> {{c1::' 
            content += addBullet(card.back)
            content += '}} \n'
    return content

#runs basic app
@app.route('/')
def home():
    return render_template('index.html', show_popup=False, download_popup=False)

#runs for when textbox is submitted
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_text'] #getting text from textbox
    if not user_input: #if text is empty just return page back with error pop up box
        return render_template('index.html', show_popup=True, download_popup=False)
    
    selected_card_type = request.form.get('cardType') #get cardType selected

    my_cards = extractInfo(user_input) #convert it to card type
    if isinstance(my_cards, str):
        return render_template('index.html', show_popup=True, download_popup=False)


    if(selected_card_type == "cloze"):
        user_input = clozeCard(my_cards)
    elif(selected_card_type == "clozeflipped"):
        user_input = clozeCardFlipped(my_cards)
    else:
        user_input = basicCard(my_cards)

    write_file("cards.txt",user_input) #write the cards in anki format to a .txt file

    return render_template('index.html', show_popup=False, download_popup=True) #return back home with download pop up box showing

#functions to download a file
@app.route('/download')
def download_file():
    return send_file('cards.txt', as_attachment=True)   

if __name__ == '__main__':
    app.run(debug=True)