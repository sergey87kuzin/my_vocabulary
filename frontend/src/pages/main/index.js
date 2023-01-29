import React from "react"
import { WordCard, MainContainer, Pagination } from "../../components"
import api from "../../api"

const Main = () => {
    const [words, setWords] = React.useState()
    const [wordsCount, setWordsCount] = React.useState()
    const [wordsPage, setWordsPage] = React.useState()

    const getWords = ({ page = 2 }) => {
        api
          .getWords({ page })
          .then(res => {
            const { results, count } = res
            setWords(results)
            setWordsCount(count)
          })
      }
    
    React.useEffect(_ => {
        getWords({ page: wordsPage })
      }, [wordsPage])

    console.log(words)

    const WordCards = words ? words.map((word) => {
        return <WordCard key={word.id} {...word} />
    }) : ""
    return (
        <MainContainer>
        <Pagination
            count={wordsCount}
            limit={50}
            onPageChange={page => setWordsPage(page)}
        />
        {WordCards}
        </MainContainer>
    )
}

export default Main
