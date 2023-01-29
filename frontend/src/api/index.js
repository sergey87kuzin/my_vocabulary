
class Api {
    constructor (url, headers) {
      this._url = url
      this._headers = headers
    }
  
    checkResponse (res) {
      console.log(res)
      return new Promise((resolve, reject) => {
        if (res.status === 204) {
          return resolve(res)
        }
        const func = res.status < 400 ? resolve : reject
        res.json().then(data => func(data))
      })
    }
  
    getWords ({page, limit=50}) {
      console.log('getting words')
      return fetch(
        `/api/v1/all_words?page=${page}&limit=${limit}`,
        {
          method: 'GET',
          headers: {
            ...this._headers,
          }
        }
      ).then(this.checkResponse)
    }

    getNewWords ({ page, limit=50 }) {
      return fetch(
        `/api/v1/new_words?page=${page}&limit=${limit}`,
        {
          method: 'GET',
          headers: {
            ...this._headers,
          }
        }
      ).then(this.checkResponse)
    }

    getFamiliarWords ({ page, limit=50 }) {
      return fetch(
        `/api/v1/familiar_words?page=${page}&limit=${limit}`,
        {
          method: 'GET',
          headers: {
            ...this._headers,
          }
        }
      ).then(this.checkResponse)
    }

    getKnownWords ({ page, limit=50 }) {
      return fetch(
        `/api/v1/known_words?page=${page}&limit=${limit}`,
        {
          method: 'GET',
          headers: {
            ...this._headers,
          }
        }
      ).then(this.checkResponse)
    }

    setNewWordStatus({id, field}) {
      console.log(`triing change word status, id = ${id}, field = ${field}`)
      let body = {
        is_new: false,
        is_well_known: false,
        is_known: false
      }
      body[`${field}`] = true

      return fetch(
        `api/v1/all_words/${id}/`,
        {
          method: 'PATCH',
          headers: {
            ...this._headers,
          },
          body: JSON.stringify(body)
        }
      )
    }

    getWord() {
    //   var word
    //   fetch(
    //     "api/v1/get_word/",
    //     {
    //       method: "GET",
    //       headers: {
    //         ...this._headers,
    //       },
    //     }
    //   ).then(res => {
    //     res.json()
    //     console.log(res)
    //   }).then(data => {
    //     word = data;
    //     }).then(() =>{
    //       console.log("got word from api: " + word)
    //       var question
    //       if({shuffle}) {
    //         question = shuffled(word[{from}].split(' ')[0])
    //       } else { question = word[{from}] }
    //       var answer = word[{to}]
    //       return {
    //         id: word.id,
    //         question: question,
    //         answer: answer
    //       }
    //     })
    // }
      return fetch(
        "api/v1/get_word/",
        {
          method: "GET",
          headers: {
            ...this._headers,
          },
        }
      ).then(this.checkResponse)
    }

    checkAnswer({body}) {
      console.log('making api request', body)
      return fetch(
        "api/v1/check_answer/",
        {
          method: "POST",
          headers: {
            ...this._headers,
          },
          body: JSON.stringify(body)
        }
      ).then(this.checkResponse)
    }
}

export default new Api('', { 'content-type': 'application/json' })