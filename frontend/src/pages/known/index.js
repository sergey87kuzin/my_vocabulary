import React from "react"
import { WordCard, Pagination } from "../../components"
import api from "../../api"

const Known = () => {
    const [words, setWords] = React.useState()
    const [wordsCount, setWordsCount] = React.useState()
    const [wordsPage, setWordsPage] = React.useState()

    const getWords = ({ page = 1 }) => {
        api
          .getKnownWords({ page })
          .then(res => {
            const { results, count } = res
            setWords(results)
            setWordsCount(count)
          })
      }
    
    React.useEffect(_ => {
        getWords({ page: wordsPage })
      }, [wordsPage])

    const WordCards = words ? words.map((word) => {
        return <WordCard key={word.id} {...word} />
    }) : ""
    return (
        <div>
        <Pagination
            count={wordsCount}
            limit={50}
            onPageChange={page => setWordsPage(page)}
        />
        {WordCards}
        </div>
    )
}

export default Known