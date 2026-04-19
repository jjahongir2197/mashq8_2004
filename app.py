@app.route('/result4', methods=['GET', 'POST'])
def result4():
    res = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        birthdate = request.form.get('birthdate', '').strip()

        if len(name) > 2 and birthdate:
            res = [name, birthdate]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result4.html', res=res)
