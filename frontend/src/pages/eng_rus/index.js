import styles from "./style.module.css"
import {shuffled} from "../../utils"
import React from "react"
import api from "../../api"
import {MainContainer, InputCard} from "../../components"
// import MetaTags from 'react-meta-tags'

const EngRus = ({shuffle, from, to}) => {

    const [eng, setEnglish] = React.useState()
    const [rus, setRussian] = React.useState()
    const [word_id, setId] = React.useState()
    const url = window.location.pathname.split('/').pop();

    const props = () => {
        api.getWord()
        .then(res => {
            const {id, english, russian} = res
            let answer = to === "english" ? english : russian
            let word = from === "english" ? english : russian
            let addition = from === "english" ? russian : english
            let question = shuffle ? addition + "   " + shuffled(word.split(" ")[0]) : word
            setEnglish(question)
            setId(id)
            setRussian(answer)
        })
    }

    React.useEffect(_ => {
        props()
      }, [url])
    

    return (
        <MainContainer>
            {/* <MetaTags>
                <title>Перевод на русский</title>
                <meta name="description" content="Перевод предложенного английского слова на русский" />
                <meta property="og:title" content="Перевод на русский" />
            </MetaTags> */}
        <InputCard 
            question={eng}
            ans={rus}
            id={word_id}
        />
        </MainContainer>
    )
}

export default EngRus