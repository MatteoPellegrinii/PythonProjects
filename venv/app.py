from flask import Flask, jsonify, request
from serie_tv import serie_tv_list, SerieTV, aggiungi_serie

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenuto nell'API delle Serie TV!"

@app.route('/serie_tv', methods=['GET'])
def elenca_serie_tv():
    return jsonify([str(serie) for serie in serie_tv_list])

@app.route('/aggiungi_serie', methods=['POST'])
def aggiungi_nuova_serie():
    try:
        data = request.json
        nuova_serie = SerieTV(**data)
        aggiungi_serie(nuova_serie)
        return f"Serie TV '{nuova_serie.titolo}' aggiunta con successo!", 201
    except Exception as e:
        return f"Errore durante l'aggiunta della serie TV: {str(e)}", 500
    
@app.route('/aggiorna_serie/<titolo>', methods=['PUT'])
def aggiorna_serie(titolo):
    try:
        data = request.json
        for serie in serie_tv_list:
            if serie.titolo == titolo:
                serie.titolo = data.get('titolo', serie.titolo)
                serie.genere = data.get('genere', serie.genere)
                serie.stagioni = data.get('stagioni', serie.stagioni)
                serie.episodi = data.get('episodi', serie.episodi)
                serie.anno = data.get('anno', serie.anno)
                return f"Serie TV '{titolo}' aggiornata con successo!", 200
        return f"Serie TV '{titolo}' non trovata", 404
    except Exception as e:
        return f"Errore durante l'aggiornamento della serie TV: {str(e)}", 500
    

@app.route('/elimina_serie/<titolo>', methods=['DELETE'])
def elimina_serie(titolo):
    try:
        for serie in serie_tv_list:
            if serie.titolo == titolo:
                serie_tv_list.remove(serie)
                return f"Serie TV '{titolo}' eliminata con successo!", 200
        return f"Serie TV '{titolo}' non trovata", 404
    except Exception as e:
        return f"Errore durante l'eliminazione della serie TV: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
